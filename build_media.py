#!/usr/bin/env python3
"""media.html, Sheet 1, STUDENT facing. What plays in Session 4 and what each item teaches.
Renders from session4.py. The instructor note on each item is deliberately not rendered here;
build_rundown.py shows it."""
import html as H
from _kit import KIT, NAV
import session4 as S

ORDER = ["spidey", "sinners", "gta1", "imax", "extended"]
SCREENED = ["spidey", "sinners", "gta1", "imax"]   # item 05 is not screened; see note
in_class = sum(S.mmss(S.MEDIA[k][3]) for k in SCREENED)

rows = []
for i, k in enumerate(ORDER, 1):
    vid, title, chan, rt, cue, teaches, watch, moves, inote = S.MEDIA[k]
    url = "https://www.youtube.com/watch?v=" + vid
    opt = "" if k in SCREENED else " opt"
    chips = "".join(f"<i>{H.escape(m)}</i>" for m in moves)
    rows.append(f'''<article class="item{opt}">
  <div class="n">{i:02d}</div>
  <div class="body">
    <h2><a href="{url}" target="_blank" rel="noopener">{H.escape(title)}</a></h2>
    <p class="meta"><span class="lbl">{H.escape(chan)}</span> <span class="rt">{rt}</span> <span class="when">{cue}</span></p>
    <p class="teach">{teaches}</p>
    <p class="watch">{watch}</p>
    <div class="moves"><span class="sgn">Moves to spot</span><span class="chips">{chips}</span></div>
    <p class="url"><a href="{url}" target="_blank" rel="noopener">{url}</a></p>
  </div>
</article>''')

page = f'''{KIT}
<title>Session 4 Media</title>
<style>
.item{{display:grid;grid-template-columns:96px 1fr;gap:26px;padding:30px 0;
 border-bottom:1px solid var(--rule);align-items:start}}
.item:first-of-type{{border-top:1px solid var(--rule)}}
.n{{font-family:"IBM Plex Mono",monospace;font-size:44px;font-weight:600;line-height:1;
 color:var(--blue);font-variant-numeric:tabular-nums}}
.item.opt .n{{color:var(--silver)}}
.item h2{{margin:0 0 8px;font-size:38px;line-height:1.06;font-weight:700;letter-spacing:-.03em;
 text-wrap:balance}}
.item h2 a{{color:var(--ink);text-decoration:none;border-bottom:3px solid var(--blue)}}
.item h2 a:hover,.item h2 a:focus-visible{{color:var(--blue)}}
.meta{{margin:0 0 14px;display:flex;gap:16px;align-items:baseline;flex-wrap:wrap}}
.rt{{font-family:"IBM Plex Mono",monospace;font-size:15px;font-weight:600;
 font-variant-numeric:tabular-nums}}
.when{{font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.16em;
 text-transform:uppercase;background:var(--ink);color:var(--paper);padding:4px 11px}}
.item.opt .when{{background:var(--silver);color:var(--ink)}}
.teach{{margin:0 0 10px;font-size:25px;line-height:1.28;font-weight:600;letter-spacing:-.015em;
 color:var(--ink);max-width:34ch}}
.watch{{margin:0 0 16px;font-size:19px;line-height:1.55;color:var(--ink2);max-width:66ch}}
.moves{{display:flex;flex-direction:column;gap:6px;margin:0 0 12px}}
.sgn{{font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.2em;
 text-transform:uppercase;color:var(--ink2)}}
.chips{{display:flex;gap:6px;flex-wrap:wrap}}
.chips i{{font-style:normal;font-family:"IBM Plex Mono",monospace;font-size:13px;
 letter-spacing:.06em;border:2px solid var(--ink);padding:5px 12px;background:var(--paper)}}
.item.opt .chips i{{border-color:var(--silver);color:var(--ink2)}}
.url{{margin:0;font-family:"IBM Plex Mono",monospace;font-size:13px;word-break:break-all}}
</style>
<div class="wrap">
<header class="mast">
 <div><span class="lbl">CTIN 290 &middot; Session 4 &middot; {S.MEET}</span>
  <h1>What we are<br>watching, and<br>what it teaches</h1></div>
 <div class="rt"><span class="lbl">Sheet 1 of 2</span></div>
</header>
<div class="sub">
 <div><span class="lbl">Items</span><b>{len(ORDER)}</b></div>
 <div><span class="lbl">Screened in class</span><b>{in_class // 60}:{in_class % 60:02d}</b></div>
 <div><span class="lbl">Topic</span><b>{S.TITLE}</b></div>
 <div><span class="lbl">Unit</span><b>1 &middot; Seeing</b></div>
</div>
{NAV.format(i='', m=' class="here"', t='')}
<main style="margin-top:30px">
{chr(10).join(rows)}
</main>
<div class="note">
 <p><b>Eight minutes of video across a session that runs 170, and that is on purpose.</b>
 Color reads in a single frame. Movement does not: it only reads when you stop, rewind, and
 play the same thirty seconds three times. Most of today is spent stopping.</p>
 <p><b>The clip you annotate is GTA VI Trailer 1</b>, ninety seconds, item 03. It is short
 enough that you can mark every move in it, which is the whole reason it was chosen.</p>
 <p><b>Item 05 is not being screened, because you have already seen all of it.</b> We watched
 the full twenty-seven minutes in Session 3 and asked what the color was doing. Today the same
 footage is on the table with a different question, which is the third time this course has
 asked you to look at something twice and see a different thing. Bring what you remember.</p>
</div>
<div class="foot">
 <p>Every link on this sheet was checked on 1 Sep 2026. Runtimes are read off the videos.</p>
 <p>Class meets 10:00 AM to 12:50 PM, Mondays and Wednesdays, SCI L104.</p>
</div>
</div>'''
open("media.html", "w").write(page)
print("media.html", len(page), "bytes")
