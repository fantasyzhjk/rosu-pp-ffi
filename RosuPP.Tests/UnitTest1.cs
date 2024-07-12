using System.Diagnostics;
using System.Reflection;
using Microsoft.VisualStudio.TestPlatform.ObjectModel.Engine.ClientProtocol;
using Xunit.Abstractions;
using System.Text.Json;

namespace RosuPP.Tests;

public class UnitTest1
{
    private readonly ITestOutputHelper output;

    public UnitTest1(ITestOutputHelper output)
    {
        this.output = output;
    }

    [Fact]
    public void TestDiff()
    {
        var d = Assembly.GetExecutingAssembly().Location;
        var beatmap = Beatmap.FromPath("../../../resources/2785319.osu");
        beatmap.Convert(Mode.Taiko);
        var difficulty = Difficulty.New();
        var attr = difficulty.Calculate(beatmap.Context);
        output.WriteLine("{0}", attr);
        Assert.Equal(5.247857660585606, attr.taiko.ToNullable()!.Value.stars);
    }

    [Fact]
    public void TestPerf()
    {
        var d = Assembly.GetExecutingAssembly().Location;
        var beatmap = Beatmap.FromPath("../../../resources/2785319.osu");
        var performance = Performance.New();
        performance.Mods((uint)Utils.Mods.Hidden);
        var attr = performance.Calculate(beatmap);
        output.WriteLine("{0}", attr);
        Assert.Equal(281.28736211196446, attr.osu.ToNullable()!.Value.pp);
    }

    [Fact]
    public void TestDiffPerf()
    {
        var d = Assembly.GetExecutingAssembly().Location;
        var beatmap = Beatmap.FromPath("../../../resources/1028484.osu");
        var difficulty = Difficulty.New();
        var diff_attr = difficulty.Calculate(beatmap);
        var performance = Performance.New();
        var perf_attr = performance.CalculateFromDifficulty(diff_attr);
        output.WriteLine("{0}", perf_attr);
        Assert.Equal(46.11642717726248, perf_attr.taiko.ToNullable()!.Value.pp_acc);
    }
}