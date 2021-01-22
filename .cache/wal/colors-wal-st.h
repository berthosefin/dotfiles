const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#1b1e25", /* black   */
  [1] = "#5C758D", /* red     */
  [2] = "#6D92A9", /* green   */
  [3] = "#78B4C8", /* yellow  */
  [4] = "#9BADA1", /* blue    */
  [5] = "#87ADC6", /* magenta */
  [6] = "#8BC1D1", /* cyan    */
  [7] = "#cbdee3", /* white   */

  /* 8 bright colors */
  [8]  = "#8e9b9e",  /* black   */
  [9]  = "#5C758D",  /* red     */
  [10] = "#6D92A9", /* green   */
  [11] = "#78B4C8", /* yellow  */
  [12] = "#9BADA1", /* blue    */
  [13] = "#87ADC6", /* magenta */
  [14] = "#8BC1D1", /* cyan    */
  [15] = "#cbdee3", /* white   */

  /* special colors */
  [256] = "#1b1e25", /* background */
  [257] = "#cbdee3", /* foreground */
  [258] = "#cbdee3",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
