#pragma warning disable CA2255 // 不应在库中使用 “ModuleInitializer” 属性
using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.IO;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
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

    static IntPtr DllImportResolver(string libraryName, Assembly assembly, DllImportSearchPath? searchPath)
    {
        var path = "native/";
        var extension = "";
        string name;

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

        path += name + extension;

        return NativeLibrary.Load(Path.Combine(AppContext.BaseDirectory, path), assembly, searchPath);
    }
}