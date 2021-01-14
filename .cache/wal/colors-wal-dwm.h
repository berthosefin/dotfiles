static const char norm_fg[] = "#c8d5e3";
static const char norm_bg[] = "#111f25";
static const char norm_border[] = "#8c959e";

static const char sel_fg[] = "#c8d5e3";
static const char sel_bg[] = "#104FBD";
static const char sel_border[] = "#c8d5e3";

static const char urg_fg[] = "#c8d5e3";
static const char urg_bg[] = "#124AB2";
static const char urg_border[] = "#124AB2";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
