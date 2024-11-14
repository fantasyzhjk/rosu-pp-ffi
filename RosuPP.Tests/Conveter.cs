namespace RosuPP.Tests;

public static class Extensions
{
    public static OsuPP.Calculater LoadState(this OsuPP.Calculater c, RosuPP.ScoreState state) {
        c.combo ??= state.max_combo;
        c.SliderTickMiss ??= state.slider_tick_misses;
        c.SliderTailHit ??= state.slider_end_hits;
        c.NGeki ??= state.n_geki;
        c.NKatu ??= state.n_katu;
        c.N300 ??= state.n300;
        c.N100 ??= state.n100;
        c.N50 ??= state.n50;
        c.NMiss ??= state.misses;
        return c;
    }

    public static OsuPP.Calculater Mods(this OsuPP.Calculater c, RosuPP.Mods mods) {
        var s = OwnedString.Empty();
        mods.Json(ref s);
        c.Mods(s.ToCstr());
        return c;
    }

    public static OsuPP.Calculater Acc(this OsuPP.Calculater c, double acc) {
        c.accuracy = acc;
        return c;
    }
}