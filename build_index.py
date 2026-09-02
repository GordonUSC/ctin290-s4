#!/usr/bin/env python3
"""index.html, the STUDENT rundown. Renders only the `student` field of each block.
Instructor direction lives in the same source file and is rendered only by
build_rundown.py, so nothing was lost when this version was made."""
import html as H
from _kit import KIT, NAV
import session4 as S

rows = []
for start, end, clock, title, student, note, media in S.BLOCKS:
    mins = end - start
    quiet = " quiet" if title in ("Break",) else ""
    clips = ""
    if media:
        items = []
        for k in media:
            vid, vt, chan, rt, cue, teaches, watch, moves, inote = S.MEDIA[k]
            url = "https://www.youtube.com/watch?v=" + vid
            items.append(
              f'<li><a href="{url}" target="_blank" rel="noopener">{H.escape(vt)}</a>'
              f'<span class="rt">{rt}</span></li>')
        clips = '<ul class="clips">' + "".join(items) + "</ul>"
    rows.append(f'''<article class="blk{quiet}" data-start="{start}" data-end="{end}">
  <div class="t"><b>{clock}</b><span>{mins} min</span></div>
  <div class="b">
    <h2>{title}</h2>
    <p>{student}</p>
    {clips}
  </div>
</article>''')

terms = "".join(
  f'<li><b>{H.escape(t)}</b> {H.escape(d)}</li>' for t, d, *_ in S.GLOSSARY)

page = f'''{KIT}
<title>Session 4 Rundown</title>
<style>
.blk{{display:grid;grid-template-columns:112px 1fr;gap:24px;padding:26px 0;
 border-bottom:1px solid var(--rule);align-items:start}}
.blk:first-of-type{{border-top:1px solid var(--rule)}}
.t b{{display:block;font-family:"IBM Plex Mono",monospace;font-size:30px;font-weight:600;
 line-height:1;color:var(--blue);font-variant-numeric:tabular-nums;letter-spacing:-.02em}}
.t span{{display:block;margin-top:6px;font-family:"IBM Plex Mono",monospace;font-size:12px;
 letter-spacing:.14em;text-transform:uppercase;color:var(--ink2)}}
.blk.quiet .t b{{color:var(--silver)}}
.blk h2{{margin:0 0 9px;font-size:31px;line-height:1.1;font-weight:700;letter-spacing:-.028em;
 text-wrap:balance}}
.blk p{{margin:0 0 12px;font-size:19.5px;line-height:1.5;color:var(--ink2);max-width:62ch}}
.clips{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}}
.clips li{{background:var(--fill);padding:9px 14px;display:flex;justify-content:space-between;
 gap:16px;align-items:baseline;flex-wrap:wrap}}
.clips a{{font-weight:600;font-size:18px;text-decoration:none;color:var(--ink);
 border-bottom:2px solid var(--blue)}}
.clips a:hover,.clips a:focus-visible{{color:var(--blue)}}
.clips .rt{{font-family:"IBM Plex Mono",monospace;font-size:14px;font-weight:600;
 color:var(--ink2);font-variant-numeric:tabular-nums}}
.tlist{{list-style:none;margin:0;padding:0;display:grid;
 grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}}
.tlist li{{border-top:2px solid var(--ink);padding-top:10px;font-size:17px;line-height:1.45;
 color:var(--ink2)}}
.tlist b{{display:block;font-size:21px;color:var(--ink);letter-spacing:-.02em;margin-bottom:4px}}
h2.sec{{margin:52px 0 18px;font-size:15px;font-family:"IBM Plex Mono",monospace;
 letter-spacing:.22em;text-transform:uppercase;font-weight:600;
 border-bottom:3px solid var(--ink);padding-bottom:11px}}
@media (max-width:640px){{
 .blk{{grid-template-columns:1fr;gap:8px}}
 .t{{display:flex;gap:12px;align-items:baseline}}
 .t b{{font-size:26px}} .t span{{margin-top:0}}
}}
</style>
<div class="wrap">
<header class="mast">
 <div><span class="lbl">CTIN 290 &middot; {S.MEET}</span>
  <h1>Session 4<br>{S.TITLE}</h1></div>
 <div class="rt"><span class="lbl">{S.UNIT}</span></div>
</header>
<div class="sub">
 <div><span class="lbl">Today</span><b>{S.AIM.split(",")[0].strip().capitalize()}</b></div>
 <div><span class="lbl">Blocks</span><b>{len(S.BLOCKS)}</b></div>
 <div><span class="lbl">Runs</span><b>170 min</b></div>
 <div><span class="lbl">Next class</span><b>{S.NEXT_MEETING[0]}</b></div>
</div>
{NAV.format(i=' class="here"', m='', t='')}
<main style="margin-top:30px">
{chr(10).join(rows)}
</main>

<h2 class="sec">Terms introduced today</h2>
<ul class="tlist">{terms}</ul>

<div class="note">
 <p><b>Homework.</b> Find a camera movement in a clip of your own choosing, from outside the
 course canon. Write the one sentence saying what that move is chasing, and bring both.</p>
 <p><b>Then rewatch the four teaching clips on Sheet 2</b>, {S.REQUIRED_REWATCH // 60} minutes
 {S.REQUIRED_REWATCH % 60} seconds in total. Every term on that sheet carries a video that
 teaches it and a video that shows it working in something we have watched together. That is
 the required viewing; everything else on the sheet is reference.</p>
 <p><b>Next class is {S.NEXT_MEETING[0]}.</b> {S.NEXT_MEETING[1]}</p>
</div>
<div class="foot">
 <p>This class meets 10:00 AM to 12:50 PM, Mondays and Wednesdays, SCI L104.</p>
 <p>Questions go in the class Discord so the answer reaches everyone.</p>
</div>
</div>'''
open("index.html", "w").write(page)
print("index.html", len(page), "bytes")
