using System.Collections.Generic;
using System.Collections.Immutable;
using System.Runtime.InteropServices;
using System.Text.Json.Serialization;
using SBRosuPP;

#nullable enable

namespace SBRosuPP;

public static class Utils
{
    public enum Mods : uint
    {
        None = 1 >> 1,
        NoFail = 1 << 0,
        Easy = 1 << 1,
        TouchDevice = 1 << 2,
        Hidden = 1 << 3,
        HardRock = 1 << 4,
        SuddenDeath = 1 << 5,
        DoubleTime = 1 << 6,
        Relax = 1 << 7,
        HalfTime = 1 << 8,
        Nightcore = 1 << 9 | DoubleTime, // Only set along with DoubleTime. i.e: NC only gives 576
        Flashlight = 1 << 10,
        Autoplay = 1 << 11,
        SpunOut = 1 << 12,
        Relax2 = 1 << 13, // Autopilot
        Perfect = 1 << 14 | SuddenDeath, // Only set along with SuddenDeath. i.e: PF only gives 16416
        Key4 = 1 << 15,
        Key5 = 1 << 16,
        Key6 = 1 << 17,
        Key7 = 1 << 18,
        Key8 = 1 << 19,
        FadeIn = 1 << 20,
        Random = 1 << 21,
        Cinema = 1 << 22,
        Target = 1 << 23,
        Key9 = 1 << 24,
        KeyCoop = 1 << 25,
        Key1 = 1 << 26,
        Key3 = 1 << 27,
        Key2 = 1 << 28,
        ScoreV2 = 1 << 29,
        Mirror = 1 << 30,
        KeyMod = Key1 | Key2 | Key3 | Key4 | Key5 | Key6 | Key7 | Key8 | Key9 | KeyCoop,
        FreeModAllowed =
            NoFail
            | Easy
            | Hidden
            | HardRock
            | SuddenDeath
            | Flashlight
            | FadeIn
            | Relax
            | Relax2
            | SpunOut
            | KeyMod,
        ScoreIncreaseMods = Hidden | HardRock | DoubleTime | Flashlight | FadeIn
    };
}

public partial struct ScoreState
{
    public uint TotalHits(Mode mode)
    {
        var amount = n300 + n100 + misses;

        if (mode is not Mode.Taiko)
        {
            amount += n50;

            if (mode is not Mode.Osu)
            {
                amount += n_katu;
                amount += mode is Mode.Catch ? n_geki : 0;
            }
        }

        return amount;
    }
}

public partial struct OsuDifficultyAttributes
{
    public readonly uint n_objects => n_circles + n_sliders + n_spinners;
}

public partial struct OsuPerformanceAttributes
{
    public readonly double stars => difficulty.stars;
    public readonly uint max_combo => difficulty.max_combo;
    public readonly uint n_objects => difficulty.n_objects;
}

public partial struct ManiaPerformanceAttributes
{
    public readonly double stars => difficulty.stars;
    public readonly uint max_combo => difficulty.max_combo;
    public readonly uint n_objects => difficulty.n_objects;
    public readonly bool is_convert => difficulty.is_convert;
}

public partial struct CatchDifficultyAttributes
{
    public readonly uint max_combo => n_droplets + n_fruits;
}

public partial struct CatchPerformanceAttributes
{
    public readonly double stars => difficulty.stars;
    public readonly uint max_combo => difficulty.max_combo;
    public readonly bool is_convert => difficulty.is_convert;
}

public partial struct TaikoPerformanceAttributes
{
    public readonly double stars => difficulty.stars;
    public readonly uint max_combo => difficulty.max_combo;
    public readonly bool is_convert => difficulty.is_convert;
}

public partial struct DifficultyAttributes
{
    public override string ToString()
    {
        var str = OwnedString.Empty();
        SBRosu.debug_difficylty_attributes(ref this, str.Context);
        return str.ToString();
    }
}

public partial struct PerformanceAttributes
{
    public override string ToString()
    {
        var str = OwnedString.Empty();
        SBRosu.debug_performance_attributes(ref this, str.Context);
        return str.ToString();
    }
}

public partial class Difficulty
{
    public DifficultyAttributes Calculate(Beatmap beatmap)
    {
        return Calculate(beatmap.Context);
    }

    public void Mods(uint mods)
    {
        IMods(mods);
    }

    public void Mods(string mods)
    {
        SMods(mods);
    }

    public void Mods(string[] mods)
    {
        SMods(string.Concat(mods));
    }

    public void Mods(Mods mods)
    {
        PMods(mods.Context);
    }
}

public partial class Performance
{
    public PerformanceAttributes Calculate(Beatmap beatmap)
    {
        return Calculate(beatmap.Context);
    }
    
    public ScoreState GenerateState(Beatmap beatmap)
    {
        return GenerateState(beatmap.Context);
    }

    public void Mods(uint mods)
    {
        IMods(mods);
    }

    public void Mods(string mods)
    {
        SMods(mods);
    }

    public void Mods(string[] mods)
    {
        SMods(string.Concat(mods));
    }

    public void Mods(Mods mods)
    {
        PMods(mods.Context);
    }
}

public partial class BeatmapAttributesBuilder
{
    public BeatmapAttributes Build(Beatmap beatmap)
    {
        return Build(beatmap.Context);
    }

    public void Mods(uint mods)
    {
        IMods(mods);
    }

    public void Mods(string mods)
    {
        SMods(mods);
    }

    public void Mods(string[] mods)
    {
        SMods(string.Concat(mods));
    }

    public void Mods(Mods mods)
    {
        PMods(mods.Context);
    }
}

public partial class OwnedString
{
    public override string ToString()
    {
        return ToCstr();
    }
}

public partial class Beatmap
{
    public static Beatmap FromBytes(byte[] data)
    {
        // 手动处理内存
        var handle = GCHandle.Alloc(data, GCHandleType.Pinned);
        var self = FromBytes(new Sliceu8(handle, (ulong)data.Length));
        handle.Free();
        return self;
    }
}
public partial class Mods
{
    public void Json(ref OwnedString str) {
        this.Json(str.Context);
    }
}
