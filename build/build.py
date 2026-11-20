# -*- coding: utf-8 -*-
"""Emit page/index.html for The World in One Day — Friday 20 November 2026 (v4)."""
import html
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import data_v4 as D  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "page" / "index.html"

E = html.escape

CSS = """
  @page { size: 1024px 1024px; margin: 0; }
  * { margin:0; padding:0; box-sizing:border-box; }
  :root { --paper:#f4f0e7; --ink:#12141a; --red:#b3261e; --cool:#2f5d8a;
          --rule:#c9c1ae; --soft:#55524a; --green:#1f6b4a; }
  html,body { width:1024px; height:1024px; }
  body { background:var(--paper); color:var(--ink);
    font-family:"DejaVu Sans","Helvetica Neue",Arial,sans-serif;
    padding:5px 15px 3px; display:flex; flex-direction:column; gap:2px;
    -webkit-font-smoothing:antialiased; }
  header { border-bottom:3px solid var(--ink); padding-bottom:3px; }
  .kick { display:flex; justify-content:space-between; align-items:baseline;
          font-size:9.6px; letter-spacing:.14em; text-transform:uppercase; color:var(--soft); font-weight:700; }
  .kick b { color:var(--red); }
  h1 { font-family:"DejaVu Serif",Georgia,serif; font-size:36px; line-height:.94; letter-spacing:-.024em; }
  .strip { display:flex; gap:8px; align-items:center; margin-top:2px; font-size:10px;
           letter-spacing:.11em; text-transform:uppercase; }
  .strip span { color:var(--soft); }
  .strip em { font-style:normal; color:var(--red); font-weight:700; }
  .strip .sep { color:var(--rule); }
  .band { display:grid; grid-template-columns:repeat(6,1fr); border-top:1px solid var(--rule);
          border-bottom:2px solid var(--ink); }
  .num { padding:1px 7px 1px; border-right:1px solid var(--rule); }
  .num:last-child { border-right:none; }
  .num .big { font-family:"DejaVu Serif",Georgia,serif; font-size:21px; line-height:1;
              letter-spacing:-.02em; font-variant-numeric:tabular-nums; }
  .num:nth-child(2) .big, .num:nth-child(3) .big, .num:nth-child(5) .big { color:var(--red); }
  .num .cap { font-size:10.6px; color:var(--soft); line-height:1.1; }
  .grid { display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:3px; }
  .box { border:1px solid var(--rule); border-top:2px solid var(--ink); background:#f8f5ee;
         padding:2px 6px 3px; display:flex; flex-direction:column; border-left:3px solid var(--rule); }
  .box.r-ASIA { border-left-color:#c2542a; } .box.r-EUROPE { border-left-color:#2f5d8a; }
  .box.r-AMERICAS { border-left-color:#1f6b4a; } .box.r-AFRICA { border-left-color:#c08a1e; }
  .box.r-OCEANIA { border-left-color:#5d3a8a; } .box.r-MIDEAST { border-left-color:#0f7b7b; }
  .box.s3 { grid-column:span 3; }
  .tag { font-size:10.4px; letter-spacing:.08em; font-weight:700; color:var(--cool);
         display:flex; gap:5px; align-items:baseline; white-space:nowrap; }
  .tag .no { color:var(--red); }
  .tag.r-ASIA { color:#9c3b12; } .tag.r-EUROPE { color:#24507a; }
  .tag.r-AMERICAS { color:#1f6b4a; } .tag.r-AFRICA { color:#8a5a12; }
  .tag.r-OCEANIA { color:#5d3a8a; } .tag.r-MIDEAST { color:#0f6b6b; }
  .box h3 { font-family:"DejaVu Serif",Georgia,serif; font-size:13.8px; line-height:1.06;
            margin:0 0 2px; letter-spacing:-.005em; }
  .box p { font-size:10.7px; line-height:1.16; color:#23252b; flex:1; }
  .src { margin-top:2px; padding-top:2px; border-top:1px dotted var(--rule);
         font-size:10.3px; color:var(--soft); white-space:nowrap; overflow:hidden; }
  .mid { display:grid; grid-template-columns:1fr 392px; gap:6px; }
  .panel { border:1px solid var(--rule); padding:2px 6px 2px; background:#f8f5ee; }
  .ph { display:flex; justify-content:space-between; align-items:baseline;
        font-size:10px; letter-spacing:.08em; text-transform:uppercase; font-weight:700; margin-bottom:1px; }
  .ph i { font-style:normal; color:var(--soft); letter-spacing:.03em; font-weight:400; text-transform:none; }
  .world { width:100%; height:116px; display:block; }
  .dotn { font-size:16px; font-weight:700; fill:#fff; font-family:"DejaVu Sans",sans-serif; }
  ol.time { list-style:none; display:grid; grid-template-columns:1fr 1fr; gap:0 9px; }
  ol.time li { display:grid; grid-template-columns:38px 1fr; gap:5px; align-items:baseline;
               border-bottom:1px dotted var(--rule); padding:2px 0; }
  ol.time .t { font-size:10.8px; font-weight:700; font-variant-numeric:tabular-nums; color:var(--red); }
  ol.time .d { font-size:10.8px; line-height:1.16; }
  .mkt { display:grid; grid-template-columns:repeat(6,1fr); border-top:1px solid var(--rule);
         border-bottom:1px solid var(--rule); }
  .q { padding:1px 7px; border-right:1px solid var(--rule); }
  .q:last-child { border-right:none; }
  .q .nm { font-size:9.5px; letter-spacing:.09em; color:var(--soft); font-weight:700; }
  .q .vl { font-size:12px; font-variant-numeric:tabular-nums; line-height:1.05; }
  .q .pc { font-size:9.5px; font-weight:700; }
  .q .dn .pc, .q .pc.dn { color:var(--red); }
  .q .pc.up { color:var(--green); }
  .also { border-top:2px solid var(--ink); padding-top:2px; }
  .ah { display:flex; justify-content:space-between; align-items:baseline; margin-bottom:1px; }
  .ah h2 { font-family:"DejaVu Serif",Georgia,serif; font-size:14px; letter-spacing:.01em; }
  .ah span { font-size:10px; color:var(--soft); letter-spacing:.06em; text-transform:uppercase; }
  .briefs { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); }
  .bcol { min-width:0; display:flex; flex-direction:column; padding:0 6px; border-left:1px solid var(--rule); }
  .bcol:first-child { border-left:none; padding-left:0; }
  .bcol:last-child { padding-right:0; }
  ol.bl { list-style:none; }
  ol.bl li { font-size:10.4px; line-height:1.08; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  ol.bl b { color:var(--red); }
  ol.bl i { color:var(--soft); font-style:normal; }
  .dc { border:1.5px solid var(--ink); background:#efeade; padding:2px 7px 3px; }
  .dct { display:flex; gap:8px; align-items:baseline; }
  .dct h2 { font-family:"DejaVu Serif",Georgia,serif; font-size:12px; white-space:nowrap; }
  .dct h2 em { font-style:normal; color:var(--red); }
  .dct .sub { font-size:9.8px; color:var(--soft); }
  ul.dcl { list-style:none; column-count:5; column-gap:10px; margin-top:1px; }
  ul.dcl li { font-size:9.9px; line-height:1.1; break-inside:avoid; white-space:nowrap; }
  ul.dcl li::before { content:"— "; color:var(--red); }
  .foot2 { display:grid; grid-template-columns:1.3fr 1fr; gap:8px; border-top:1px solid var(--rule); padding-top:2px; }
  .meth { font-size:9.9px; line-height:1.12; color:#2a2c32; }
  .srcs { font-size:9.6px; line-height:1.12; color:var(--soft); }
  .srcs b { color:var(--ink); letter-spacing:.05em; text-transform:uppercase; }
  footer { display:flex; justify-content:space-between; align-items:baseline;
           border-top:1px solid var(--rule); padding-top:1px; font-size:10px; color:var(--soft);
           letter-spacing:.04em; text-transform:uppercase; }
"""

# --- world map: reuse the v3 silhouette, dots placed per story -----------------
MAP_SVG = (ROOT / "page" / "_mapdots.svg")
MAP_BASE = (ROOT / "page" / "_mapbase.svg")


def spread(items, cols):
    out = [[] for _ in range(cols)]
    for i, it in enumerate(items):
        out[i % cols].append(it)
    return out


def main():
    n_cards = len(D.CARDS)
    total = n_cards + len(D.BRIEFS)
    cards_html = []
    for no, region, kicker, head, body, src in D.CARDS:
        cards_html.append(
            f'<article class="box s3 r-{region}">\n'
            f'  <div class="tag r-{region}"><span class="no">{no}</span>{region} · {E(kicker)}</div>\n'
            f'  <h3>{E(head)}</h3>\n'
            f'  <p>{E(body)}</p>\n'
            f'  <div class="src">{E(src)}</div>\n'
            f'</article>')
    cols = spread(D.BRIEFS, 3)
    brief_cols = []
    for col in cols:
        rows = "\n".join(f'<li><b>{n_cards + 1 + k}</b> {E(txt)} <i>{E(src)}</i></li>' for k, (_, txt, src) in enumerate(col))
        brief_cols.append(f'<div class="bcol">\n<ol class="bl">\n{rows}\n</ol>\n</div>')
    tl = "\n".join(f'<li><span class="t">{t}</span><span class="d">{E(d)}</span></li>' for t, d in D.TIMELINE)
    mkt = "\n".join(
        f'<div class="q"><div class="nm">{E(n)}</div><div class="vl">{E(v)}</div>'
        f'<div class="pc {"up" if c == "up" else "dn"}">{E(p)}</div></div>'
        for n, v, p, c in D.MARKETS)
    nums = "\n".join(f'<div class="num"><div class="big">{E(b)}</div><div class="cap">{E(c)}</div></div>'
                     for b, c in D.NUMBERS)
    dcl = "\n".join(f'<li>{E(x)}</li>' for x in D.DATECHECK)
    map_svg = MAP_SVG.read_text() if MAP_SVG.exists() else ""

    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{D.DAY} — The World in One Day</title>
<style>{CSS}</style></head>
<body>
<header>
  <div class="kick"><span>The World in One Day · a news poster</span><span>No. 11,842 · <b>Friday</b> edition · one page</span></div>
  <h1>{D.DAY}</h1>
  <div class="strip">
    <em>THE WORLD IN ONE DAY</em><span class="sep">|</span>
    <span>{total} stories</span><span class="sep">·</span><span>6 regions</span><span class="sep">·</span>
    <span>{n_cards} main boxes, {len(D.BRIEFS)} briefs</span><span class="sep">·</span>
    <span>all first reported today</span>
  </div>
</header>
<section class="band">
{nums}
</section>
<section class="grid">
{chr(10).join(cards_html)}
</section>
<section class="mkt">
{mkt}
</section>
<section class="mid">
  <div class="panel">
    <div class="ph"><span>Where the day happened</span><i>numbers match the boxes</i></div>
    {map_svg}
  </div>
  <div class="panel">
    <div class="ph"><span>The day in UTC</span><i>six moments</i></div>
    <ol class="time">
{tl}
    </ol>
  </div>
</section>
<section class="also">
  <div class="ah"><h2>Also on Friday</h2><span>{len(D.BRIEFS)} more briefs · numbered on from {n_cards + 1}</span></div>
  <div class="briefs">
{chr(10).join(brief_cols)}
  </div>
</section>
<section class="dc">
  <div class="dct"><h2>Date check <em>— what we left out</em></h2><span class="sub">All of these broke on Thursday 19 November or earlier, so none is on the page.</span></div>
  <ul class="dcl">
{dcl}
  </ul>
</section>
<div class="foot2">
  <div class="meth"><b>Method.</b> Every story happened, or was first reported, on Friday 20 November 2026; disputed claims are attributed. Boxes 1–{n_cards} are the day's main lines, {n_cards + 1}–{total} the briefs; the block above lists what broke earlier. Figures are as the cited source gave them.</div>
  <div class="srcs"><b>Sources:</b> {E(D.SOURCES)}.</div>
</div>
<footer>
  <span>Compiled 20 November 2026 · all times UTC</span>
  <span>{total} stories checked · {len(D.DATECHECK)} kept out</span>
</footer>
</body></html>
"""
    OUT.write_text(doc)
    print(f"wrote {OUT} ({len(doc)} bytes) · {total} stories ({n_cards} boxes + {len(D.BRIEFS)} briefs)")


if __name__ == "__main__":
    main()
