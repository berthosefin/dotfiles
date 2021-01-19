static const char norm_fg[] = "#c4bbcc";
static const char norm_bg[] = "#101115";
static const char norm_border[] = "#89828e";

static const char sel_fg[] = "#c4bbcc";
static const char sel_bg[] = "#5B7294";
static const char sel_border[] = "#c4bbcc";

static const char urg_fg[] = "#c4bbcc";
static const char urg_bg[] = "#83687E";
static const char urg_border[] = "#83687E";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
