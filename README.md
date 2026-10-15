# Lu-Xing Yang 杨橹星

Source of my academic homepage: **https://lyang910920.github.io**

The site is a single bilingual page, `index.html`, with self-hosted fonts in `assets/fonts/` and no external scripts.

## Updating the page

- **News:** in the *Recent news* section, copy one `<li>` to the top of the list and set its `datetime`. Items from the last 90 days get a "New" tag automatically; the first five are shown until a visitor presses "Show all".
- **Publications:** copy one `<li class="pub">` block into the right year. `data-topics` takes one or more of `apt malware info learning platform`; update the counts on the filter chips and the venue bars in the side column.
- **English and Chinese:** every piece of text has an `<span class="en">` and a `<span class="zh" lang="zh-Hans">` version.
- **New Chinese characters:** the Chinese font is a subset. After adding Chinese text, run `pip install fonttools brotli` and then `python3 tools/subset_cjk_font.py`; characters outside the subset otherwise fall back to the visitor's system font.
- **Portrait:** save a photo as `assets/photo.jpg` (portrait orientation, about 720 × 900 px) and uncomment the `<img class="portrait">` line in the About section.
