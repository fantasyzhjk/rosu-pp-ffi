using System;
using RosuPP;

#nullable enable

namespace RosuPP;

public static class Extensions
{
    public static string DebugString(this DifficultyAttributes attributes)
    {
        return Interop.debug_difficulty_attributes(ref attributes).IntoString();
    }

    public static string DebugString(this PerformanceAttributes attributes)
    {
        return Interop.debug_performance_attributes(ref attributes).IntoString();
    }

    public static string DebugString(this ScoreState state)
    {
        return Interop.debug_score_state(ref state).IntoString();
    }

    public static double Acc(
        ref this ScoreState state,
        ref DifficultyAttributes attr,
        OsuScoreOrigin origin
    )
    {
        return Interop.calculate_accuacy(ref state, ref attr, origin);
    }

    public static double Acc(ref this ScoreState state, ref DifficultyAttributes attr)
    {
        return Interop.calculate_accuacy(ref state, ref attr, OsuScoreOrigin.WithSliderAcc);
    }
}

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
    [System.Diagnostics.CodeAnalysis.SetsRequiredMembers]
    public ScoreState()
    {
        this = default;
    }

    public uint TotalHits(Mode mode)
    {
        var amount = n300 + n100 + misses;

        if (!mode.IsTaiko)
        {
            amount += n50;

            if (!mode.IsOsu)
            {
                amount += n_katu;
                amount += !mode.IsCatch ? n_geki : 0;
            }
        }

        return amount;
    }
}

public partial struct Mode : IEquatable<Mode>
{
    public bool Equals(Mode other) => _variant == other._variant;

    public override bool Equals(object? obj) => obj is Mode other && Equals(other);

    public override int GetHashCode() => _variant.GetHashCode();

    public static bool operator ==(Mode left, Mode right) => left.Equals(right);

    public static bool operator !=(Mode left, Mode right) => !left.Equals(right);

    public static explicit operator int(Mode mode) => (int)mode._variant;

    public static explicit operator uint(Mode mode) => mode._variant;
}

public partial struct OsuDifficultyAttributes
{
    public readonly uint n_objects => n_circles + n_sliders + n_spinners;
    public readonly double od => (80.0 - great_hit_window) / 6.0;
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

public partial struct OptionDifficultyAttributes
{
    public DifficultyAttributes? ToNullable() => IsSome ? AsSome() : null;
}

public partial struct OptionPerformanceAttributes
{
    public PerformanceAttributes? ToNullable() => IsSome ? AsSome() : null;

}

public partial struct OptionTooSuspicious
{
    public TooSuspicious? ToNullable() => IsSome ? AsSome() : null;

}

public partial struct OptionDouble
{
    public double? ToNullable() => IsSome ? AsSome() : null;
}

public partial struct OptionUint
{
    public uint? ToNullable() => IsSome ? AsSome() : null;
}

public partial class Difficulty
{
    public void Mods(uint mods)
    {
        IMods(mods);
    }

    public void Mods(string mods)
    {
        using var value = Utf8String.From(mods);
        SMods(value);
    }

    public void Mods(string[] mods)
    {
        Mods(string.Concat(mods));
    }

    public void Mods(Mods mods)
    {
        PMods(mods);
    }
}

public partial class Performance
{
    public void Mods(uint mods)
    {
        IMods(mods);
    }

    public void Mods(string mods)
    {
        using var value = Utf8String.From(mods);
        SMods(value);
    }

    public void Mods(string[] mods)
    {
        Mods(string.Concat(mods));
    }

    public void Mods(Mods mods)
    {
        PMods(mods);
    }
}

public partial class BeatmapAttributesBuilder
{
    public void Mods(uint mods)
    {
        IMods(mods);
    }

    public void Mods(string mods)
    {
        using var value = Utf8String.From(mods);
        SMods(value);
    }

    public void Mods(string[] mods)
    {
        Mods(string.Concat(mods));
    }

    public void Mods(Mods mods)
    {
        PMods(mods);
    }
}

public partial class Beatmap
{
    public static Beatmap FromPath(string path)
    {
        using var value = Utf8String.From(path);
        return FromPath(value);
    }

    public static Beatmap FromBytes(byte[] data)
    {
        using var slice = SliceByte.From(data);
        return FromBytes(slice);
    }

    /// Convert a Beatmap to the specified mode
    public bool Convert(Mode mode)
    {
        using var mods = Mods.Create(mode);
        return Convert(mode, mods);
    }
}

public partial class LegacyBeatmap
{
    public static LegacyBeatmap FromBytes(byte[] data)
    {
        using var slice = SliceByte.From(data);
        return FromBytes(slice);
    }
}

public partial class Mods
{
    public static Mods FromAcronyms(string str, Mode mode)
    {
        using var value = Utf8String.From(str);
        return FromAcronyms(value, mode);
    }

    public static Mods FromJson(string str, Mode mode)
    {
        return FromJson(str, mode, false);
    }

    public static Mods FromJson(string str, Mode mode, bool denyUnknownFields)
    {
        using var value = Utf8String.From(str);
        return FromJson(value, mode, denyUnknownFields);
    }

    public bool InsertJson(string str)
    {
        return InsertJson(str, false);
    }

    public bool InsertJson(string str, bool denyUnknownFields)
    {
        using var value = Utf8String.From(str);
        return InsertJson(value, denyUnknownFields);
    }

    public void Insert(string str)
    {
        using var value = Utf8String.From(str);
        Insert(value);
    }

    public bool Contains(string str)
    {
        using var value = Utf8String.From(str);
        return Contains(value);
    }
}
