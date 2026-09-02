#!/usr/bin/env python3
"""rundown.html, the INSTRUCTOR rundown. Phone first.

This is the page Gordon holds while teaching, so it is built for a phone in one hand in a
lit room: big wall-clock times, thumb-sized tap targets, high contrast, and no horizontal
scroll at any width. It carries BOTH the student text and every instructor note, which is
where all the direction removed from the student pages went. Nothing was deleted.

Works with JavaScript off: the clock and the auto-highlight are enhancements, and with JS
disabled the page is still a complete, ordered, readable run sheet."""
import html as H
from _kit import KIT  # noqa: F401  (kit imported for parity; this page uses its own CSS)
import session4 as S

blocks = []
for start, end, clock, title, student, note, media in S.BLOCKS:
    mins = end - start
    clips = ""
    if media:
        items = []
        for k in media:
            vid, vt, chan, rt, cue, teaches, watch, moves, inote = S.MEDIA[k]
            url = "https://www.youtube.com/watch?v=" + vid
            items.append(f'''<a class="clip" href="{url}" target="_blank" rel="noopener">
      <span class="ct">{H.escape(vt)}</span>
      <span class="cm">{H.escape(chan)} &middot; {rt} &middot; {cue}</span>
      <span class="cn">{H.escape(inote)}</span>
    </a>''')
        clips = '<div class="clips">' + "".join(items) + "</div>"
    blocks.append(f'''<section class="blk" data-start="{start}" data-end="{end}" id="b{start}">
  <div class="hd">
    <span class="clk">{clock}</span>
    <span class="len">{mins}<i>min</i></span>
  </div>
  <h2>{title}</h2>
  <p class="say">{student}</p>
  <p class="do"><b>You:</b> {note}</p>
  {clips}
</section>''')

# The optional item is not attached to a block; surface it once at the end.
ovid, otitle, ochan, ort, ocue, oteach, owatch, omoves, onote = S.MEDIA["extended"]
ourl = "https://www.youtube.com/watch?v=" + ovid

terms_rows = "".join(
  f'<tr><td><b>{H.escape(t)}</b></td><td>{H.escape(d)}</td></tr>'
  for t, d, *_ in S.GLOSSARY)

page = f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#0E1116">
<title>S4 Rundown &middot; instructor</title>
<style>
:root{{
  --bg:#0E1116; --card:#171C23; --card2:#1E2530; --line:#2A3340;
  --ink:#F2F5F9; --ink2:#A8B4C4; --ink3:#6E7C8D;
  --live:#FFB000; --say:#7FC4FF; --do:#FFD98A;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:18px;line-height:1.5;
  padding:0 max(14px,env(safe-area-inset-left)) calc(64px + env(safe-area-inset-bottom));
  overflow-x:hidden}}
.top{{position:sticky;top:0;z-index:10;background:rgba(14,17,22,.94);
  backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
  border-bottom:1px solid var(--line);
  padding:calc(10px + env(safe-area-inset-top)) 2px 10px;
  display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}}
.top h1{{margin:0;font-size:21px;letter-spacing:-.02em;font-weight:800}}
.top .meta{{font-family:var(--mono);font-size:11px;letter-spacing:.09em;color:var(--ink2);
  text-transform:uppercase}}
.top .now{{margin-left:auto;font-family:var(--mono);font-size:20px;font-weight:700;
  color:var(--live);font-variant-numeric:tabular-nums}}
.aim{{margin:16px 2px 4px;font-size:17px;color:var(--ink2);line-height:1.45}}
.jump{{display:flex;gap:7px;overflow-x:auto;padding:12px 2px 14px;margin:0 -2px;
  -webkit-overflow-scrolling:touch;scrollbar-width:none}}
.jump::-webkit-scrollbar{{display:none}}
.jump a{{flex:0 0 auto;font-family:var(--mono);font-size:15px;font-weight:600;
  padding:11px 15px;min-height:44px;display:flex;align-items:center;
  background:var(--card);border:1px solid var(--line);border-radius:11px;
  color:var(--ink2);text-decoration:none;font-variant-numeric:tabular-nums}}
.jump a.on{{background:var(--live);border-color:var(--live);color:#12161B}}
.blk{{background:var(--card);border:1px solid var(--line);border-radius:15px;
  padding:15px 15px 17px;margin:0 0 12px;scroll-margin-top:74px}}
.blk.now{{border-color:var(--live);box-shadow:0 0 0 2px rgba(255,176,0,.26)}}
.hd{{display:flex;align-items:baseline;gap:11px;margin-bottom:7px}}
.clk{{font-family:var(--mono);font-size:29px;font-weight:700;color:var(--live);
  font-variant-numeric:tabular-nums;letter-spacing:-.02em;line-height:1}}
.len{{font-family:var(--mono);font-size:13px;color:var(--ink3);font-weight:600}}
.len i{{font-style:normal;margin-left:2px}}
.blk h2{{margin:0 0 10px;font-size:24px;line-height:1.17;letter-spacing:-.022em;font-weight:750;
  text-wrap:balance}}
.say{{margin:0 0 11px;font-size:17px;line-height:1.5;color:var(--ink2);
  border-left:3px solid var(--say);padding-left:12px}}
.do{{margin:0;font-size:17.5px;line-height:1.52;color:var(--do);
  background:rgba(255,217,138,.07);border-left:3px solid var(--do);padding:10px 12px;
  border-radius:0 8px 8px 0}}
.do b{{color:#fff;letter-spacing:.02em}}
.clips{{margin-top:12px;display:flex;flex-direction:column;gap:8px}}
.clip{{display:block;background:var(--card2);border:1px solid var(--line);border-radius:11px;
  padding:12px 13px;text-decoration:none;min-height:44px}}
.clip:active{{background:#26303D}}
.ct{{display:block;font-size:17px;font-weight:700;color:var(--live);line-height:1.25;
  margin-bottom:3px}}
.cm{{display:block;font-family:var(--mono);font-size:11.5px;color:var(--ink3);
  letter-spacing:.04em;margin-bottom:6px}}
.cn{{display:block;font-size:15.5px;color:var(--ink2);line-height:1.45}}
h3.sec{{font-family:var(--mono);font-size:12px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--ink3);margin:30px 2px 12px;padding-top:16px;border-top:1px solid var(--line)}}
table{{width:100%;border-collapse:collapse;font-size:16px}}
td{{padding:11px 10px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink2)}}
td:first-child{{width:38%;color:var(--ink)}}
td b{{color:var(--live);font-weight:700}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:15px;padding:15px;
  margin:0 0 12px}}
.card p{{margin:0 0 10px;font-size:16.5px;line-height:1.5;color:var(--ink2)}}
.card p:last-child{{margin:0}}
.card b{{color:var(--ink)}}
.foot{{margin-top:26px;padding:16px 2px 0;border-top:1px solid var(--line);
  font-size:14px;color:var(--ink3);line-height:1.5}}
.foot a{{color:var(--say)}}
a:focus-visible{{outline:3px solid var(--live);outline-offset:3px}}
@media (min-width:760px){{
  body{{font-size:19px;max-width:800px;margin:0 auto;padding-left:22px;padding-right:22px}}
  .blk h2{{font-size:28px}} .clk{{font-size:33px}}
}}
</style>

<div class="top">
  <h1>S4 Rundown</h1>
  <span class="meta">Wed 2 Sep &middot; SCI L104</span>
  <span class="now" id="now"></span>
</div>

<p class="aim"><b>Today:</b> {S.AIM}</p>

<nav class="jump" id="jump">
{chr(10).join(f'<a href="#b{b[0]}">{b[2]}</a>' for b in S.BLOCKS)}
</nav>

{chr(10).join(blocks)}

<h3 class="sec">If you are ahead</h3>
<div class="card">
  <p><b>{H.escape(otitle)}</b> &middot; {H.escape(ochan)} &middot; {ort}</p>
  <p>{H.escape(onote)}</p>
  <p><a href="{ourl}" target="_blank" rel="noopener">{ourl}</a></p>
</div>

<h3 class="sec">Terms you are introducing</h3>
<div class="card" style="padding:4px 10px"><table>{terms_rows}</table></div>

<h3 class="sec">Before you leave the room</h3>
<div class="card">
  <p><b>Collect the exit tickets at the door.</b> Read them before Session 6 and open that
  class by answering the two most common ones by name.</p>
  <p><b>Say the next meeting out loud: {S.NEXT_MEETING[0]}.</b> {S.NEXT_MEETING[1]} The
  homework is easy to lose across a week and a holiday.</p>
</div>

<div class="foot">
  <p><b>Instructor copy.</b> The student pages are the
  <a href="index.html">rundown</a>, <a href="media.html">Sheet 1, media</a> and
  <a href="terms.html">Sheet 2, terms</a>. This page is not linked from any of them.</p>
  <p>Blue rule is what the class hears. Amber is yours. Both render from one source file, so
  the two versions cannot drift.</p>
</div>

<script>
(function(){{
  var blks=[].slice.call(document.querySelectorAll('.blk[data-start]')),
      jumps=[].slice.call(document.querySelectorAll('#jump a')),
      now=document.getElementById('now');
  function tick(){{
    var d=new Date(), m=d.getHours()*60+d.getMinutes(), hit=-1;
    now.textContent=String(d.getHours()).padStart(2,'0')+':'+String(d.getMinutes()).padStart(2,'0');
    blks.forEach(function(b,i){{
      var on = m>=+b.dataset.start && m<+b.dataset.end;
      b.classList.toggle('now',on);
      if(on) hit=i;
    }});
    jumps.forEach(function(a,i){{ a.classList.toggle('on', i===hit); }});
  }}
  tick(); setInterval(tick,15000);
}})();
</script>
'''
open("rundown.html", "w").write(page)
print("rundown.html", len(page), "bytes")
