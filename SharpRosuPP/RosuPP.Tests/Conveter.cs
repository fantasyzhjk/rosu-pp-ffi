namespace RosuPP.Tests;

public static class Extensions
{
    public static OsuPP.Calculater LoadState(this OsuPP.Calculater c, ScoreState state, DifficultyAttributes dattr, bool is_cl = false, bool is_lazer = false) {
        uint sliderTickMiss = 0;
        if (dattr.IsOsu) {
            var dattrosu = dattr.AsOsu();
            if (is_lazer) {
                if (is_cl) {
                    sliderTickMiss = dattrosu.n_large_ticks - state.osu_large_tick_hits;
                } else {
                    sliderTickMiss = dattrosu.n_large_ticks + dattrosu.n_sliders - state.osu_large_tick_hits;
                }
            }
        }
        
        c.combo ??= state.max_combo;
        c.SliderTickMiss ??= sliderTickMiss;
        c.SliderTailHit ??= state.slider_end_hits;
        c.NGeki ??= state.n_geki;
        c.NKatu ??= state.n_katu;
        c.N300 ??= state.n300;
        c.N100 ??= state.n100;
        c.N50 ??= state.n50;
        c.NMiss ??= state.misses;
        return c;
    }

    public static OsuPP.Calculater Mods(this OsuPP.Calculater c, Mods mods) {
        c.Mods(mods.Json().IntoString());
        return c;
    }

    public static OsuPP.Calculater Acc(this OsuPP.Calculater c, double acc) {
        c.accuracy = acc;
        return c;
    }
}