static const char norm_fg[] = "#cbdee3";
static const char norm_bg[] = "#1b1e25";
static const char norm_border[] = "#8e9b9e";

static const char sel_fg[] = "#cbdee3";
static const char sel_bg[] = "#6D92A9";
static const char sel_border[] = "#cbdee3";

static const char urg_fg[] = "#cbdee3";
static const char urg_bg[] = "#5C758D";
static const char urg_border[] = "#5C758D";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
