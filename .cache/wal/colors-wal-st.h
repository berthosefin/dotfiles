const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#101115", /* black   */
  [1] = "#83687E", /* red     */
  [2] = "#5B7294", /* green   */
  [3] = "#8C7795", /* yellow  */
  [4] = "#658CAA", /* blue    */
  [5] = "#688BB1", /* magenta */
  [6] = "#79A9C4", /* cyan    */
  [7] = "#c4bbcc", /* white   */

  /* 8 bright colors */
  [8]  = "#89828e",  /* black   */
  [9]  = "#83687E",  /* red     */
  [10] = "#5B7294", /* green   */
  [11] = "#8C7795", /* yellow  */
  [12] = "#658CAA", /* blue    */
  [13] = "#688BB1", /* magenta */
  [14] = "#79A9C4", /* cyan    */
  [15] = "#c4bbcc", /* white   */

  /* special colors */
  [256] = "#101115", /* background */
  [257] = "#c4bbcc", /* foreground */
  [258] = "#c4bbcc",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
