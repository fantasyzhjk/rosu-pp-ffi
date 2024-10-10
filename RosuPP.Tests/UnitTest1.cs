using System.Diagnostics;
using System.Reflection;
using Microsoft.VisualStudio.TestPlatform.ObjectModel.Engine.ClientProtocol;
using Xunit.Abstractions;
using System.Text.Json;
using System.Text.Json.Nodes;

namespace RosuPP.Tests;

public class UnitTest1
{
    private readonly ITestOutputHelper output;

    public UnitTest1(ITestOutputHelper output)
    {
        this.output = output;
    }


    [Fact]
    public void TestPPNext()
    {
        var d = Assembly.GetExecutingAssembly().Location;
        var beatmap = Beatmap.FromPath("../../../resources/657916.osu");
        var performance = Performance.New();
        performance.Mods(["HDCL"]);
        performance.N100(66);
        performance.N50(1);
        performance.Misses(1);
        performance.Combo(1786);

        var attr = performance.Calculate(beatmap);
        output.WriteLine("{0}", attr);
        Assert.Equal(281.28736211196446, attr.osu.ToNullable()!.Value.pp);
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
        Assert.Equal(5.6601490215152728, attr.taiko.ToNullable()!.Value.stars);
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
        Assert.Equal(281.18902663807626, attr.osu.ToNullable()!.Value.pp);
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
        Assert.Equal(45.722317618639458, perf_attr.taiko.ToNullable()!.Value.pp_acc);
    }

    [Fact]
    public void TestBeatmapAttr()
    {
        var beatmap = Beatmap.FromPath("../../../resources/2785319.osu");
        var builder = BeatmapAttributesBuilder.New();
        builder.Mods("DT");

        var bmattr = builder.Build(beatmap);
        output.WriteLine("cs: {0}", bmattr.cs);
        output.WriteLine("od: {0}", bmattr.od);
        output.WriteLine("hp: {0}", bmattr.hp);
        output.WriteLine("ar: {0}", bmattr.ar);
        output.WriteLine("cr: {0}", bmattr.clock_rate);
        var difficulty = Difficulty.New();
        var diff_attr = difficulty.Calculate(beatmap);
        var performance = Performance.New();
        var perf_attr = performance.CalculateFromDifficulty(diff_attr);
        output.WriteLine("{0}", perf_attr);

        Assert.Equal(79.84500076626814, perf_attr.osu.ToNullable()!.Value.pp_acc);

      
    }

    [Fact]
    public void ModsTest()
    {
        var s = OwnedString.Empty();
        var j = """
                        [
                            { "acronym": "HD" },
                            { "acronym": "CL" },
                            { "acronym": "DT", "settings": { "speed_change": 1.5 } }
                        ]
                        """;

        var mods = Mods.FromJson(j, Mode.Taiko);
        Assert.Equal((uint)3, mods.Len());
        Assert.True(mods.Contains("DT"));

        Assert.Equal((double?)1.5, mods.ClockRate().ToNullable());

        mods.Json(ref s);
        var res = s.ToString();
        output.WriteLine(res);

        var parsed_json = JsonSerializer.Deserialize<JsonArray>(res);
        Assert.NotNull(parsed_json);
        Assert.Equal(3, parsed_json!.Count);
        var dt_node = parsed_json.First(x => x?["acronym"]?.ToString() == "DT");
        Assert.NotNull(dt_node);
        Assert.Equal(1.5, dt_node["settings"]?["speed_change"]?.GetValue<double>());
        
        mods.Insert("HR");
        Assert.Equal((uint)4, mods.Len());
    }
}