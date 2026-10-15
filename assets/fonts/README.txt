Fonts used on this site (all under the SIL Open Font License 1.1; licence texts in this folder):

  serif-roman.woff2, serif-italic.woff2  Source Serif 4 (Adobe), subset to Latin and renamed "LXY Serif"
  sans.woff2                             Source Sans 3 (Adobe), subset to Latin and renamed "LXY Sans"
  serif-sc.woff2                         Noto Serif SC (Adobe/Google), subset to the Chinese characters
                                         used on the page and renamed "LXY Serif SC"
  serif-sc-name.woff2                    the same font cut down to 杨橹星, so English pages that show the
                                         name do not download the full Chinese subset

The files were subset and renamed because the licence reserves the original names for unmodified fonts.
Chinese characters that are not in serif-sc.woff2 are drawn with the visitor's system serif font.
After adding Chinese text, run tools/subset_cjk_font.py so that serif-sc.woff2 covers every character on the page.
