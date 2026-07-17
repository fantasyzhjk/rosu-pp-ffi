using System.Diagnostics;
using System.Reflection;
using Microsoft.VisualStudio.TestPlatform.ObjectModel.Engine.ClientProtocol;
using Xunit.Abstractions;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using osu.Game.Rulesets.Taiko;

namespace RosuPP.Tests;

public class PPUnitTest(ITestOutputHelper output)
{
    private readonly ITestOutputHelper output = output;

    private void TestPP(string beatmapPath, string modstr, bool isLazer, Mode? mode = null, double compareRange = 0.00001) {
        var b = File.ReadAllBytes(beatmapPath);
        using var beatmap = Beatmap.FromBytes(b);

        if (mode is not null) {
            using var m = Mods.FromAcronyms(modstr, mode.Value);
            var convertSuccess = beatmap.Convert(mode.Value, m);
            Assert.True(convertSuccess, "convert failed");
        } else {
            mode = beatmap.Mode();
        }

        using var mods = Mods.FromAcronyms(modstr, beatmap.Mode());
        using var difficulty = Difficulty.Create();
        difficulty.Lazer(isLazer);
        difficulty.Mods(mods);
        var dattr = difficulty.Calculate(beatmap);

        using var performance = Performance.Create();
        performance.Lazer(isLazer);
        performance.Mods(mods);

        var state = performance.GenerateStateFromDifficulty(dattr);
        var attr = performance.CalculateFromDifficulty(dattr);
        var origin = OsuScoreOrigin.Stable;
        if (isLazer) {
            if (mods.Contains("CL")) {
                origin = OsuScoreOrigin.WithoutSliderAcc;
            } else {
                origin = OsuScoreOrigin.WithSliderAcc;
            }
        }
        var acc = state.Acc(ref dattr, origin) * 100;
        output.WriteLine("{0}", attr.DebugString());
        output.WriteLine("{0}", state.DebugString());
        
        var ruleset = OsuPP.Utils.ParseRuleset((int)beatmap.Mode())!;
        var osubm = OsuPP.Calculater.New(ruleset, new OsuPP.CalculatorWorkingBeatmap(b));
        osubm.Mods(mods);
        var attr2 = osubm.LoadState(state, dattr, mods.Contains("CL"), isLazer).Acc(acc).Calculate();

        var pp = (int)mode switch {
            0 => attr.AsOsu().pp,
            1 => attr.AsTaiko().pp,
            2 => attr.AsCatch().pp,
            3 => attr.AsMania().pp,
            _ => throw new ArgumentOutOfRangeException(nameof(mode), mode, null)
        };

        output.WriteLine("pp: {0}", attr2.Total);
        output.WriteLine("sr: {0}", osubm.difficultyAttributes.StarRating);
        Assert.InRange(pp, attr2.Total - compareRange, attr2.Total + compareRange);
    }

    [Fact]
    public void GradualTest() {
        var d = Assembly.GetExecutingAssembly().Location;
        var b = File.ReadAllBytes("../../../resources/657916.osu");
        using var beatmap = Beatmap.FromBytes(b);
        using var difficulty = Difficulty.Create();
        using var gradual = GradualPerformance.Create(difficulty, beatmap);

        var totalLen = gradual.Len();

        var calculated = 10;

        var state = new ScoreState();
        for (var i = 0; i < calculated; i++) {
            state.n300 += 1;
            state.max_combo += 1;
            var attrs = gradual.Next(state).AsSome();
            output.WriteLine("{0}", attrs);
            output.WriteLine("pp: {0}", attrs.AsOsu().pp);
        }

        var remainingObjects = gradual.Len();

        Assert.Equal(totalLen, remainingObjects + calculated);
    }

    [Fact]
    public void Convert() {
        TestPP(
            beatmapPath: "../../../resources/657916.osu",
            modstr: "",
            isLazer: false, 
            mode: Mode.Taiko
        );

        TestPP(
            beatmapPath: "../../../resources/657916.osu",
            modstr: "",
            isLazer: false, 
            mode: Mode.Catch
        );

        TestPP(
            beatmapPath: "../../../resources/657916.osu",
            modstr: "",
            isLazer: false, 
            mode: Mode.Mania
        );
    }


    [Fact]
    public void TestPPStable()
    {
        TestPP(
            beatmapPath: "../../../resources/657916.osu",
            modstr: "CL",
            isLazer: false
        );
        
        TestPP(
            beatmapPath: "../../../resources/1028484.osu",
            modstr: "CL",
            isLazer: false
        );

        TestPP(
            beatmapPath: "../../../resources/1638954.osu",
            modstr: "CL",
            isLazer: false
        );

        TestPP(
            beatmapPath: "../../../resources/2118524.osu",
            modstr: "CL",
            isLazer: false
        );

        TestPP(
            beatmapPath: "../../../resources/2785319.osu",
            modstr: "CL",
            isLazer: false
        );
    }

    [Fact]
    public void TestPPLazer()
    {
        TestPP(
            beatmapPath: "../../../resources/657916.osu",
            modstr: "",
            isLazer: true
        );

        TestPP(
            beatmapPath: "../../../resources/1028484.osu",
            modstr: "",
            isLazer: true
        );

        TestPP(
            beatmapPath: "../../../resources/1638954.osu",
            modstr: "",
            isLazer: true
        );

        TestPP(
            beatmapPath: "../../../resources/2118524.osu",
            modstr: "",
            isLazer: true
        );

        TestPP(
            beatmapPath: "../../../resources/2785319.osu",
            modstr: "",
            isLazer: true
        );

        TestPP(
            beatmapPath: "../../../resources/1256809.osu",
            modstr: "",
            isLazer: true
        );
    }

    [Fact]
    public void TestPPLazerWithCL()
    {
        TestPP(
            beatmapPath: "../../../resources/657916.osu",
            modstr: "CL",
            isLazer: true
        );

        TestPP(
            beatmapPath: "../../../resources/1028484.osu",
            modstr: "CL",
            isLazer: true
        );

        TestPP(
            beatmapPath: "../../../resources/1638954.osu",
            modstr: "CL",
            isLazer: true
        );

        TestPP(
            beatmapPath: "../../../resources/2118524.osu",
            modstr: "CL",
            isLazer: true
        );

        TestPP(
            beatmapPath: "../../../resources/2785319.osu",
            modstr: "CL",
            isLazer: true
        );
    }

    [Fact]
    public void TestState()
    {
        var d = Assembly.GetExecutingAssembly().Location;
        var b = File.ReadAllBytes("../../../resources/657916.osu");
        using var beatmap = Beatmap.FromBytes(b);
        using var difficulty = Difficulty.Create();
        var dattr = difficulty.Calculate(beatmap);

        using var performance = Performance.Create();
        performance.Accuracy(97.35);
        performance.Misses(1);

        var state = performance.GenerateStateFromDifficulty(dattr);
        var attr = performance.CalculateFromDifficulty(dattr);
        output.WriteLine("{0}", state);

        using var performance2 = Performance.Create();
        performance2.State(state);
        var attr2 = performance.CalculateFromDifficulty(dattr);

        Assert.Equal(attr2.AsOsu().pp, attr.AsOsu().pp);
    }

    [Fact]
    public void TestDiffTaiko()
    {
        var d = Assembly.GetExecutingAssembly().Location;
        var b = File.ReadAllBytes("../../../resources/2785319.osu");
        using var beatmap = Beatmap.FromBytes(b);
        beatmap.Convert(Mode.Taiko);

        using var difficulty = Difficulty.Create();
        var attr = difficulty.Calculate(beatmap);
        output.WriteLine("{0}", attr);

        var ruleset = OsuPP.Utils.ParseRuleset((int)beatmap.Mode())!;
        var osubm = OsuPP.Calculater.New(ruleset, new OsuPP.CalculatorWorkingBeatmap(b));
        var attr2 = osubm.CalculateDifficulty();

        output.WriteLine("{0}", JsonConvert.SerializeObject(attr2, Formatting.Indented));
        Assert.Equal(attr2.StarRating, attr.AsTaiko().stars);
    }

    [Fact]
    public void TestDiffFruit()
    {
        var d = Assembly.GetExecutingAssembly().Location;
        var b = File.ReadAllBytes("../../../resources/2785319.osu");
        using var beatmap = Beatmap.FromBytes(b);
        using var catchMods = Mods.Create(Mode.Catch);
        beatmap.Convert(Mode.Catch, catchMods);

        using var difficulty = Difficulty.Create();
        var attr = difficulty.Calculate(beatmap);
        output.WriteLine("{0}", attr);

        var ruleset = OsuPP.Utils.ParseRuleset((int)beatmap.Mode())!;
        var osubm = OsuPP.Calculater.New(ruleset, new OsuPP.CalculatorWorkingBeatmap(b));
        var attr2 = osubm.CalculateDifficulty();
        
        output.WriteLine("{0}", JsonConvert.SerializeObject(attr2, Formatting.Indented));
        Assert.Equal(attr2.StarRating, attr.AsCatch().stars);
    }

    [Fact]
    public void TestDiffMania()
    {
        var d = Assembly.GetExecutingAssembly().Location;
        var b = File.ReadAllBytes("../../../resources/2785319.osu");
        using var beatmap = Beatmap.FromBytes(b);
        beatmap.Convert(Mode.Mania);

        using var difficulty = Difficulty.Create();
        var attr = difficulty.Calculate(beatmap);
        output.WriteLine("{0}", attr);

        var ruleset = OsuPP.Utils.ParseRuleset((int)beatmap.Mode())!;
        var osubm = OsuPP.Calculater.New(ruleset, new OsuPP.CalculatorWorkingBeatmap(b));
        var attr2 = osubm.CalculateDifficulty();
        
        output.WriteLine("{0}", JsonConvert.SerializeObject(attr2, Formatting.Indented));
        Assert.Equal(attr2.StarRating, attr.AsMania().stars);
    }

    [Fact]
    public void TestBeatmapAttr()
    {
        using var beatmap = Beatmap.FromPath("../../../resources/2785319.osu");
        using var builder = BeatmapAttributesBuilder.Create();
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
        Assert.Equal(10.533333460489908, bmattr.ar);
        Assert.Equal(1.5, bmattr.clock_rate);
    }

    [Fact]
    public void ModsTest()
    {
        var j = """
                        [
                            { "acronym": "HD" },
                            { "acronym": "CL" },
                            { "acronym": "DT", "settings": { "speed_change": 1.5 } }
                        ]
                        """;

        using var mods = Mods.FromJson(j, Mode.Taiko);
        Assert.Equal((uint)3, mods.Len());
        Assert.True(mods.Contains("DT"));

        Assert.Equal((double?)1.5, mods.ClockRate().ToNullable());

        using var json = mods.Json();
        var res = json.String;
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

    [Fact]
    public void BeatmapInfoTest() {
        var d = Assembly.GetExecutingAssembly().Location;
        var b = File.ReadAllBytes("../../../resources/657916.osu");
        using var beatmap = Beatmap.FromBytes(b);
        using var hitobjects = beatmap.HitObjects();
        var objects = hitobjects.Unwire();
        var len = (uint)objects.Count;
        
        Assert.Equal((uint)1368, len);

        Assert.All(
            objects,
            obj => Assert.True(
                obj.data.IsCircle
                || obj.data.IsSlider
                || obj.data.IsSpinner
                || obj.data.IsHold
            )
        );
    }

    [Fact]
    public void UnicodePathTest()
    {
        var path = Path.Combine(Path.GetTempPath(), $"rosu-pp-ffi-测试-{Guid.NewGuid():N}.osu");
        File.Copy("../../../resources/657916.osu", path);

        try
        {
            using var beatmap = Beatmap.FromPath(path);
            Assert.Equal(Mode.Osu, beatmap.Mode());
        }
        finally
        {
            File.Delete(path);
        }
    }
}
