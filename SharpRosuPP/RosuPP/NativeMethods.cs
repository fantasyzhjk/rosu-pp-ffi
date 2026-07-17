#pragma warning disable CA2255 // 不应在库中使用 “ModuleInitializer” 属性
using System;
using System.IO;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

#nullable enable

namespace RosuPP;

internal static partial class NativeMethods
{
    [ModuleInitializer]
    internal static void Initialize()
    {
        NativeLibrary.SetDllImportResolver(typeof(NativeMethods).Assembly, DllImportResolver);
    }

    private static IntPtr DllImportResolver(
        string libraryName,
        Assembly assembly,
        DllImportSearchPath? searchPath
    )
    {
        if (libraryName != Interop.NativeLib)
        {
            return IntPtr.Zero;
        }

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

        var localPath = Path.Combine(
            AppContext.BaseDirectory,
            "runtimes",
            RuntimeInformation.RuntimeIdentifier,
            "native",
            name + extension
        );

        if (File.Exists(localPath))
        {
            return NativeLibrary.Load(localPath);
        }

        // NuGet runtime assets are selected through the application's .deps.json.
        // Returning zero delegates resolution back to the default .NET loader.
        return IntPtr.Zero;
    }
}
