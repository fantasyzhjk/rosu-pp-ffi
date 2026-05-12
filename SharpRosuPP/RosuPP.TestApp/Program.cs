using System;
using System.IO;
using SBRosuPP;

namespace RosuPP.TestApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // .osu 文件路径，可通过命令行参数传入
            string beatmapPath = args.Length > 0
                ? args[0]
                : Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "test.osu");

            if (!File.Exists(beatmapPath))
            {
                Console.WriteLine($"[!] 未找到 beatmap 文件: {beatmapPath}");
                Console.WriteLine("用法: RosuPP.TestApp.exe <path-to-.osu-file>");
                Console.WriteLine();
                Console.WriteLine("正在尝试使用内嵌测试模式（无 beatmap 文件时仅验证 DLL 加载）...");
                TestDllLoad();
                return;
            }

            TestWithBeatmap(beatmapPath);
        }

        /// <summary>
        /// 简单验证 DLL 能正常加载和调用
        /// </summary>
        static void TestDllLoad()
        {
            try
            {
                var mods = Mods.FromAcronyms("HDHR", Mode.Osu);
                Console.WriteLine($"[OK] Mods.FromAcronyms(\"HDHR\", Mode.Osu) 成功, bits = {mods.Bits()}");

                Console.WriteLine("[OK] 原生 DLL (sb_pp_ffi.dll) 加载成功!");
            }
            catch (DllNotFoundException ex)
            {
                Console.WriteLine($"[FAIL] 原生 DLL 加载失败: {ex.Message}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[FAIL] 发生异常: {ex.GetType().Name}: {ex.Message}");
            }
        }

        /// <summary>
        /// 加载 beatmap 并执行 Difficulty / Performance 计算
        /// </summary>
        static void TestWithBeatmap(string path)
        {
            Console.WriteLine($"加载 Beatmap: {path}");
            Console.WriteLine(new string('-', 60));

            try
            {
                // 1. 加载 Beatmap
                var beatmap = Beatmap.FromPath(path);
                Console.WriteLine("[OK] Beatmap 加载成功");
                Console.WriteLine($"     Mode: {beatmap.Mode()}");

                // 2. 计算 Difficulty
                var diff = Difficulty.New();
                var diffAttrs = diff.Calculate(beatmap);
                Console.WriteLine();
                Console.WriteLine("=== Difficulty Attributes ===");
                Console.WriteLine(diffAttrs);

                // 3. 计算 Performance (无 Mods)
                var perf = Performance.New();
                var perfAttrs = perf.Calculate(beatmap);
                Console.WriteLine();
                Console.WriteLine("=== Performance Attributes (NoMod) ===");
                Console.WriteLine(perfAttrs);

                // 4. 带 Mods 计算
                var perfHdHr = Performance.New();
                perfHdHr.Mods("HDHR");
                var perfAttrsHdHr = perfHdHr.Calculate(beatmap);
                Console.WriteLine();
                Console.WriteLine("=== Performance Attributes (HDHR) ===");
                Console.WriteLine(perfAttrsHdHr);

                // 5. 自定义参数计算
                var perfCustom = Performance.New();
                perfCustom.Accuracy(98.5);
                perfCustom.Combo(800);
                perfCustom.Misses(2);
                var perfAttrsCustom = perfCustom.Calculate(beatmap);
                Console.WriteLine();
                Console.WriteLine("=== Performance Attributes (98.5% Acc, 800x Combo, 2 Miss) ===");
                Console.WriteLine(perfAttrsCustom);

                Console.WriteLine();
                Console.WriteLine(new string('-', 60));
                Console.WriteLine("[OK] 所有测试完成!");
            }
            catch (DllNotFoundException ex)
            {
                Console.WriteLine($"[FAIL] 原生 DLL 未找到: {ex.Message}");
                Console.WriteLine("       请确保 sb_pp_ffi.dll 在输出目录中");
            }
            catch (InteropException<FFIError> ex)
            {
                Console.WriteLine($"[FAIL] FFI 调用错误: {ex.Error}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[FAIL] 异常: {ex.GetType().Name}: {ex.Message}");
                Console.WriteLine(ex.StackTrace);
            }
        }
    }
}
