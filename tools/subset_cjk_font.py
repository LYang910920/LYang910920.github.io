"""Regenerate the Chinese font subset after adding Chinese text to index.html.

    pip install fonttools brotli
    python3 tools/subset_cjk_font.py

Downloads Noto Serif SC (weights 400-650) from Google Fonts, cut down to the CJK characters that
appear in index.html, renames it "LXY Serif SC" (as the OFL asks for modified fonts) and writes
assets/fonts/serif-sc.woff2 plus assets/fonts/serif-sc-name.woff2 (only 杨橹星, for English pages).
"""
import pathlib, re, ssl, urllib.parse, urllib.request
from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
RANGES = [(0x2E80, 0x2FDF), (0x3000, 0x303F), (0x3400, 0x4DBF), (0x4E00, 0x9FFF), (0xF900, 0xFAFF), (0xFE30, 0xFE4F), (0xFF00, 0xFFEF)]
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"


def fetch(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), context=ssl.create_default_context()).read()


html = (ROOT / "index.html").read_text(encoding="utf-8")
chars = "".join(sorted({c for c in html if any(a <= ord(c) <= b for a, b in RANGES)}))
css = fetch("https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400..650&text=" + urllib.parse.quote(chars)).decode()
(src,) = re.findall(r"url\((https://[^)]+)\) format\('woff2'\)", css)
tmp = FONTS / "_download.woff2"
tmp.write_bytes(fetch(src))
font = TTFont(tmp)
missing = [c for c in chars if ord(c) not in font.getBestCmap()]
assert not missing, missing
for rec in font["name"].names:
    s = rec.toUnicode()
    t = s.replace("Noto Serif SC", "LXY Serif SC").replace("NotoSerifSC", "LXYSerifSC")
    if t != s:
        rec.string = t
font = instancer.instantiateVariableFont(font, {"wght": (400, 650)})
font.flavor = "woff2"
font.save(FONTS / "serif-sc.woff2")
tmp.unlink()

name = TTFont(FONTS / "serif-sc.woff2")
opts = subset.Options()
opts.flavor, opts.layout_features, opts.name_IDs, opts.name_languages, opts.notdef_outline = "woff2", ["*"], ["*"], ["*"], True
sub = subset.Subsetter(opts)
sub.populate(text="杨橹星")
sub.subset(name)
name.save(FONTS / "serif-sc-name.woff2")
print(f"{len(chars)} characters -> serif-sc.woff2 ({(FONTS / 'serif-sc.woff2').stat().st_size // 1024} KB)")
