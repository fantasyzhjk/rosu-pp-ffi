using System.Diagnostics;
using System.Reflection;
using Microsoft.VisualStudio.TestPlatform.ObjectModel.Engine.ClientProtocol;
using Xunit.Abstractions;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using osu.Game.Rulesets.Taiko;

namespace RosuPP.Tests;

public class UnitTest1
{
    private readonly ITestOutputHelper output;

    public UnitTest1(ITestOutputHelper output)
    {
        this.output = output;
    }


    [Fact]
    public void TestPP()
    {
        var d = Assembly.GetExecutingAssembly().Location;
        var b = File.ReadAllBytes("../../../resources/657916.osu");
        var beatmap = Beatmap.FromBytes(b);
        var mods = Mods.FromAcronyms("HDCL", beatmap.Mode());
        var difficulty = Difficulty.New();
        difficulty.Mods(mods);
        var diff_attr = difficulty.Calculate(beatmap);

        var performance = Performance.New();
        performance.Lazer(Bool.True);
        performance.Mods(mods);
        performance.Accuracy(97.0);
        // performance.N100(66);
        // performance.N50(1);
        // performance.Misses(1);
        // performance.Combo(1786);

        var state = performance.GenerateState(beatmap);
        var attr = performance.CalculateFromDifficulty(diff_attr);
        output.WriteLine("{0}", state);
        output.WriteLine("{0}", attr);
        var acc = state.Acc(ref diff_attr, OsuScoreOrigin.WithSliderAcc) * 100;
        output.WriteLine("{0}", acc);
        
        var ruleset = OsuPP.Utils.ParseRuleset((int)beatmap.Mode())!;
        var osubm = OsuPP.Calculater.New(ruleset, new OsuPP.CalculatorWorkingBeatmap(b));
        var sliderTickMiss = diff_attr.osu.ToNullable()!.Value.n_large_ticks - state.osu_large_tick_hits;
        var attr2 = osubm.Mods(mods).LoadState(state, sliderTickMiss).Acc(acc).Calculate();

        Assert.Equal(attr2.Total, attr.osu.ToNullable()!.Value.pp);
    }

    [Fact]
    public void TestDiffTaiko()
    {
        var d = Assembly.GetExecutingAssembly().Location;
        var b = File.ReadAllBytes("../../../resources/2785319.osu");
        var beatmap = Beatmap.FromBytes(b);
        beatmap.Convert(Mode.Taiko);

        var difficulty = Difficulty.New();
        var attr = difficulty.Calculate(beatmap);
        output.WriteLine("{0}", attr);

        var ruleset = OsuPP.Utils.ParseRuleset((int)beatmap.Mode())!;
        var osubm = OsuPP.Calculater.New(ruleset, new OsuPP.CalculatorWorkingBeatmap(b));
        var attr2 = osubm.CalculateDifficulty();
        
        output.WriteLine("{0}", JsonConvert.SerializeObject(attr2, Formatting.Indented));
        Assert.Equal(attr2.StarRating, attr.taiko.ToNullable()!.Value.stars);
    }

    [Fact]
    public void TestDiffFruit()
    {
        var d = Assembly.GetExecutingAssembly().Location;
        var b = File.ReadAllBytes("../../../resources/2785319.osu");
        var beatmap = Beatmap.FromBytes(b);
        beatmap.Convert(Mode.Catch, Mods.New(Mode.Catch));

        var difficulty = Difficulty.New();
        var attr = difficulty.Calculate(beatmap);
        output.WriteLine("{0}", attr);

        var ruleset = OsuPP.Utils.ParseRuleset((int)beatmap.Mode())!;
        var osubm = OsuPP.Calculater.New(ruleset, new OsuPP.CalculatorWorkingBeatmap(b));
        var attr2 = osubm.CalculateDifficulty();
        
        output.WriteLine("{0}", JsonConvert.SerializeObject(attr2, Formatting.Indented));
        Assert.Equal(attr2.StarRating, attr.fruit.ToNullable()!.Value.stars);
    }

    [Fact]
    public void TestDiffMania()
    {
        var d = Assembly.GetExecutingAssembly().Location;
        var b = File.ReadAllBytes("../../../resources/2785319.osu");
        var beatmap = Beatmap.FromBytes(b);
        beatmap.Convert(Mode.Mania);

        var difficulty = Difficulty.New();
        var attr = difficulty.Calculate(beatmap);
        output.WriteLine("{0}", attr);

        var ruleset = OsuPP.Utils.ParseRuleset((int)beatmap.Mode())!;
        var osubm = OsuPP.Calculater.New(ruleset, new OsuPP.CalculatorWorkingBeatmap(b));
        var attr2 = osubm.CalculateDifficulty();
        
        output.WriteLine("{0}", JsonConvert.SerializeObject(attr2, Formatting.Indented));
        Assert.Equal(attr2.StarRating, attr.mania.ToNullable()!.Value.stars);
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

        Assert.Equal(4.5, bmattr.cs);
        Assert.Equal(10.311111238267687, bmattr.od);
        Assert.Equal(5, bmattr.hp);
        Assert.Equal(10.53333346048991, bmattr.ar);
        Assert.Equal(1.5, bmattr.clock_rate);
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
        Assert.True(mods.Contains("DT").Is);

        Assert.Equal((double?)1.5, mods.ClockRate().ToNullable());

        mods.Json(ref s);
        var res = s.ToString();
        output.WriteLine(res);

        var parsed_json = JsonConvert.DeserializeObject<JArray>(res);
        Assert.NotNull(parsed_json);
        Assert.Equal(3, parsed_json!.Count);
        var dt_node = parsed_json.First(x => x?["acronym"]?.ToString() == "DT");
        Assert.NotNull(dt_node);
        Assert.Equal(1.5, dt_node["settings"]?["speed_change"]?.ToObject<double>());
        
        mods.Insert("HR");
        Assert.Equal((uint)4, mods.Len());
    }
}