const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#111f25", /* black   */
  [1] = "#124AB2", /* red     */
  [2] = "#104FBD", /* green   */
  [3] = "#396BA7", /* yellow  */
  [4] = "#4573B1", /* blue    */
  [5] = "#4187D7", /* magenta */
  [6] = "#5391D9", /* cyan    */
  [7] = "#c8d5e3", /* white   */

  /* 8 bright colors */
  [8]  = "#8c959e",  /* black   */
  [9]  = "#124AB2",  /* red     */
  [10] = "#104FBD", /* green   */
  [11] = "#396BA7", /* yellow  */
  [12] = "#4573B1", /* blue    */
  [13] = "#4187D7", /* magenta */
  [14] = "#5391D9", /* cyan    */
  [15] = "#c8d5e3", /* white   */

  /* special colors */
  [256] = "#111f25", /* background */
  [257] = "#c8d5e3", /* foreground */
  [258] = "#c8d5e3",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
