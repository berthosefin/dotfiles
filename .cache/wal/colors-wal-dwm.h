static const char norm_fg[] = "#ECEFF4";
static const char norm_bg[] = "#3B4252";
static const char norm_border[] = "#4C566A";

static const char sel_fg[] = "#ECEFF4";
static const char sel_bg[] = "#A3BE8C";
static const char sel_border[] = "#ECEFF4";

static const char urg_fg[] = "#ECEFF4";
static const char urg_bg[] = "#BF616A";
static const char urg_border[] = "#BF616A";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
