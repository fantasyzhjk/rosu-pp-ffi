#pragma warning disable CA2255 // 不应在库中使用 “ModuleInitializer” 属性
using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text.Json.Serialization;
using RosuPP;

#nullable enable

namespace RosuPP;

internal static unsafe partial class NativeMethods
{
    // https://docs.microsoft.com/en-us/dotnet/standard/native-interop/cross-platform
    // Library path will search
    // win => __DllName, __DllName.dll
    // linux, osx => __DllName.so, __DllName.dylib

    [ModuleInitializer]
    internal static void Initialize()
    {
        NativeLibrary.SetDllImportResolver(typeof(NativeMethods).Assembly, DllImportResolver);
    }


    private static byte[] ComputeFileChecksum(string filePath)
    {
        using var md5 = MD5.Create();
        using var stream = File.OpenRead(filePath);
        return md5.ComputeHash(stream);
    }

    private static byte[] ComputeEmbeddedDllChecksum(Stream stream)
    {
        using var md5 = MD5.Create();
        return md5.ComputeHash(stream);
    }

    private static string ExtractDllToFile(string resourceName, string filePath)
    {
        var tempFile = Path.Combine(Path.GetTempPath(), filePath);

        using (var stream = Assembly.GetExecutingAssembly().GetManifestResourceStream(resourceName))
        {
            if (stream == null)
            {
                throw new FileNotFoundException($"Resource {resourceName} not found.");
            }

            if (File.Exists(tempFile))
            {
                var existingChecksum = ComputeFileChecksum(tempFile);
                var embeddedChecksum = ComputeEmbeddedDllChecksum(stream);

                if (existingChecksum.SequenceEqual(embeddedChecksum))
                {
                    return tempFile;
                }
            }

            using var fileStream = new FileStream(tempFile, FileMode.Create, FileAccess.Write);
            stream.CopyTo(fileStream);
        }

        return tempFile;
    }

    static IntPtr DllImportResolver(string libraryName, Assembly assembly, DllImportSearchPath? searchPath)
    {
        if (libraryName != RosuLibrary.NativeLib) { return IntPtr.Zero; }

        string name;
        string extension;

        if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
        {
            extension = ".dll";
            name = libraryName;
        }
        else if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
        {
            extension = ".dylib";
            name = "lib" + libraryName;
        }
        else
        {
            extension = ".so";
            name = "lib" + libraryName;
        }

        var filePath = name + extension;

        // 将库写入临时文件
        string resourceName = $"{assembly.GetName().Name}.{filePath}";
        string tempPath = ExtractDllToFile(resourceName, filePath);

        // 加载库
        return NativeLibrary.Load(tempPath, assembly, searchPath);
    }
}