#!/usr/bin/env python3
"""rundown.html, the INSTRUCTOR rundown. Phone first, and step by step.

Every timed slot breaks into sub-steps, and each sub-step says exactly what to SAY (verbatim,
read aloud), what to DO, what to SHOW, and which TERMS get introduced there with both of their
videos attached. This is the page held in one hand at the podium.

Renders from session4.py, the same source the three student pages use, so the two audiences
cannot drift. Works with JavaScript off: the clock and auto-highlight are enhancements."""
import html as H
import session4 as S


def clock(m):
    return f"{m // 60}:{m % 60:02d}"


def media_card(key):
    vid, title, chan, rt, cue, teaches, watch, moves, inote = S.MEDIA[key]
    url = "https://www.youtube.com/watch?v=" + vid
    warn = " warn" if inote.startswith("PREVIEW") else ""
    return f'''<a class="show{warn}" href="{url}" target="_blank" rel="noopener">
   <span class="tag">Show</span>
   <span class="st">{H.escape(title)}</span>
   <span class="sm">{H.escape(chan)} &middot; {rt} &middot; {cue}</span>
   <span class="sn">{H.escape(inote)}</span>
  </a>'''


def term_card(name):
    tkey, ckey = S.TERM_VIDEOS[name]
    tid, tname, tchan, trt = S.TEACH[tkey]
    cid, cname = S.CANON_CLIP[ckey]
    turl = "https://www.youtube.com/watch?v=" + tid
    curl = "https://www.youtube.com/watch?v=" + cid
    star = " key" if name in S.GLOSSARY_NAMES else ""
    badge = "On the syllabus" if name in S.GLOSSARY_NAMES else "Also covered"
    return f'''<div class="term{star}">
   <span class="tag">Term &middot; {badge}</span>
   <b class="tn">{H.escape(name)}</b>
   <span class="td">{H.escape(S.TERM_DEF[name])}</span>
   <a class="tv teach" href="{turl}" target="_blank" rel="noopener">
     <span class="tl">Teaches it</span>{H.escape(tname)}
     <span class="tm">{H.escape(tchan)} &middot; {trt}</span></a>
   <a class="tv canon" href="{curl}" target="_blank" rel="noopener">
     <span class="tl">Seen in</span>{H.escape(cname)}</a>
  </div>'''


sections = []
for start, end, clk, title, student, note, media in S.BLOCKS:
    steps_html = []
    for a, b, label, says, dos, show, terms in S.STEPS[start]:
        say_html = "".join(f'<p class="say">{H.escape(x)}</p>' for x in says)
        if say_html:
            say_html = f'<div class="saybox"><span class="tag">Say</span>{say_html}</div>'
        do_html = "".join(f"<li>{H.escape(x)}</li>" for x in dos)
        if do_html:
            do_html = f'<div class="dobox"><span class="tag">Do</span><ul>{do_html}</ul></div>'
        show_html = media_card(show) if show else ""
        term_html = "".join(term_card(t) for t in terms)
        steps_html.append(f'''<div class="step">
   <div class="sh"><span class="sc">{clock(a)}</span><span class="sd">{b - a} min</span>
     <span class="sl">{H.escape(label)}</span></div>
   {say_html}{do_html}{show_html}{term_html}
  </div>''')
    sections.append(f'''<section class="blk" data-start="{start}" data-end="{end}" id="b{start}">
  <div class="hd"><span class="clk">{clk}</span><span class="len">{end - start}<i>min</i></span></div>
  <h2>{title}</h2>
  {"".join(steps_html)}
</section>''')

# every term, gathered once at the end
all_terms = "".join(term_card(n) for n in
                    S.GLOSSARY_NAMES + [t[0] for t in S.UNPACKED])

ovid, otitle, ochan, ort, *_rest = S.MEDIA["extended"]
onote = S.MEDIA["extended"][8]
ourl = "https://www.youtube.com/watch?v=" + ovid
avid, atitle, achan, art = S.MEDIA["up_alt"][:4]
aurl = "https://www.youtube.com/watch?v=" + avid

page = f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#0E1116">
<title>S4 Rundown &middot; instructor</title>
<style>
:root{{
  --bg:#0E1116; --card:#171C23; --card2:#1E2530; --line:#2A3340;
  --ink:#F2F5F9; --ink2:#A8B4C4; --ink3:#6E7C8D;
  --live:#FFB000; --say:#7FC4FF; --do:#FFD98A; --term:#7FE0A8; --warn:#FF7A59;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:18px;line-height:1.5;
  padding:0 max(13px,env(safe-area-inset-left)) calc(64px + env(safe-area-inset-bottom));
  overflow-x:hidden}}
.top{{position:sticky;top:0;z-index:10;background:rgba(14,17,22,.95);
  backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
  border-bottom:1px solid var(--line);
  padding:calc(9px + env(safe-area-inset-top)) 2px 9px;
  display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}}
.top h1{{margin:0;font-size:20px;letter-spacing:-.02em;font-weight:800}}
.top .meta{{font-family:var(--mono);font-size:10.5px;letter-spacing:.08em;color:var(--ink2);
  text-transform:uppercase}}
.top .now{{margin-left:auto;font-family:var(--mono);font-size:19px;font-weight:700;
  color:var(--live);font-variant-numeric:tabular-nums}}
.aim{{margin:15px 2px 2px;font-size:16.5px;color:var(--ink2);line-height:1.45}}
.jump{{display:flex;gap:6px;overflow-x:auto;padding:11px 2px 13px;margin:0 -2px;
  -webkit-overflow-scrolling:touch;scrollbar-width:none}}
.jump::-webkit-scrollbar{{display:none}}
.jump a{{flex:0 0 auto;font-family:var(--mono);font-size:14px;font-weight:600;
  padding:11px 14px;min-height:44px;display:flex;align-items:center;
  background:var(--card);border:1px solid var(--line);border-radius:11px;
  color:var(--ink2);text-decoration:none;font-variant-numeric:tabular-nums}}
.jump a.on{{background:var(--live);border-color:var(--live);color:#12161B}}
.blk{{background:var(--card);border:1px solid var(--line);border-radius:15px;
  padding:14px 13px 15px;margin:0 0 12px;scroll-margin-top:70px}}
.blk.now{{border-color:var(--live);box-shadow:0 0 0 2px rgba(255,176,0,.26)}}
.hd{{display:flex;align-items:baseline;gap:10px;margin-bottom:5px}}
.clk{{font-family:var(--mono);font-size:27px;font-weight:700;color:var(--live);
  font-variant-numeric:tabular-nums;letter-spacing:-.02em;line-height:1}}
.len{{font-family:var(--mono);font-size:12.5px;color:var(--ink3);font-weight:600}}
.len i{{font-style:normal;margin-left:2px}}
.blk h2{{margin:0 0 13px;font-size:23px;line-height:1.16;letter-spacing:-.022em;
  font-weight:750;text-wrap:balance}}
.step{{border-top:1px solid var(--line);padding:12px 0 3px}}
.sh{{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:9px}}
.sc{{font-family:var(--mono);font-size:17px;font-weight:700;color:var(--ink);
  font-variant-numeric:tabular-nums}}
.sd{{font-family:var(--mono);font-size:11px;color:var(--ink3);font-weight:600}}
.sl{{font-size:16px;font-weight:700;color:var(--ink2);letter-spacing:-.01em}}
.tag{{display:inline-block;font-family:var(--mono);font-size:9.5px;letter-spacing:.16em;
  text-transform:uppercase;font-weight:700;padding:2px 7px;border-radius:3px;margin-bottom:7px}}
.saybox{{background:rgba(127,196,255,.09);border-left:3px solid var(--say);
  padding:10px 12px;border-radius:0 9px 9px 0;margin:0 0 9px}}
.saybox .tag{{background:var(--say);color:#0B1B28}}
.say{{margin:0 0 8px;font-size:18.5px;line-height:1.45;color:#DCEBFA}}
.say:last-child{{margin:0}}
.say::before{{content:"\\201C"}} .say::after{{content:"\\201D"}}
.dobox{{background:rgba(255,217,138,.07);border-left:3px solid var(--do);
  padding:10px 12px;border-radius:0 9px 9px 0;margin:0 0 9px}}
.dobox .tag{{background:var(--do);color:#2B1F05}}
.dobox ul{{margin:0;padding-left:17px}}
.dobox li{{font-size:16.5px;line-height:1.45;color:var(--do);margin:0 0 5px}}
.dobox li:last-child{{margin:0}}
.show{{display:block;background:var(--card2);border:1px solid var(--line);border-radius:11px;
  padding:11px 12px;margin:0 0 9px;text-decoration:none;min-height:44px}}
.show .tag{{background:var(--live);color:#12161B}}
.show.warn{{border-color:var(--warn)}}
.show.warn .tag{{background:var(--warn);color:#2B0E06}}
.st{{display:block;font-size:17px;font-weight:700;color:var(--live);line-height:1.25}}
.show.warn .st{{color:var(--warn)}}
.sm{{display:block;font-family:var(--mono);font-size:11px;color:var(--ink3);
  letter-spacing:.04em;margin:3px 0 6px}}
.sn{{display:block;font-size:15.5px;color:var(--ink2);line-height:1.45}}
.term{{background:var(--card2);border:1px solid var(--line);border-left:3px solid var(--term);
  border-radius:0 11px 11px 0;padding:11px 12px;margin:0 0 9px}}
.term .tag{{background:var(--line);color:var(--ink2)}}
.term.key .tag{{background:var(--term);color:#062015}}
.tn{{display:block;font-size:19px;font-weight:800;color:var(--term);letter-spacing:-.02em}}
.td{{display:block;font-size:15.5px;color:var(--ink2);line-height:1.45;margin:4px 0 9px}}
.tv{{display:block;background:rgba(255,255,255,.04);border:1px solid var(--line);
  border-radius:9px;padding:9px 11px;margin:0 0 6px;text-decoration:none;
  font-size:16px;font-weight:650;color:var(--ink);line-height:1.3;min-height:44px}}
.tv:last-child{{margin:0}}
.tl{{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--ink3);margin-bottom:3px}}
.tv.teach{{border-left:3px solid var(--say)}}
.tv.canon{{border-left:3px solid var(--live)}}
.tm{{display:block;font-family:var(--mono);font-size:11px;color:var(--ink3);margin-top:3px}}
h3.sec{{font-family:var(--mono);font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--ink3);margin:30px 2px 12px;padding-top:16px;border-top:1px solid var(--line)}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:15px;padding:14px;
  margin:0 0 12px}}
.card p{{margin:0 0 10px;font-size:16.5px;line-height:1.5;color:var(--ink2)}}
.card p:last-child{{margin:0}}
.card b{{color:var(--ink)}}
.card a{{color:var(--live);word-break:break-all}}
.foot{{margin-top:24px;padding:15px 2px 0;border-top:1px solid var(--line);
  font-size:14px;color:var(--ink3);line-height:1.5}}
.foot a{{color:var(--say)}}
a:focus-visible{{outline:3px solid var(--live);outline-offset:3px}}
@media (min-width:760px){{
  body{{font-size:19px;max-width:820px;margin:0 auto;padding-left:22px;padding-right:22px}}
  .blk h2{{font-size:27px}} .clk{{font-size:31px}}
}}
</style>

<div class="top">
  <h1>S4 Rundown</h1>
  <span class="meta">Wed 2 Sep &middot; SCI L104 &middot; yours only</span>
  <span class="now" id="now"></span>
</div>

<p class="aim"><b>Today:</b> {S.AIM}</p>

<nav class="jump" id="jump">
{chr(10).join(f'<a href="#b{b[0]}">{b[2]}</a>' for b in S.BLOCKS)}
</nav>

{chr(10).join(sections)}

<h3 class="sec">Before class, two minutes</h3>
<div class="card">
  <p><b>Preview the Up clip.</b> Pixar's official upload is titled &ldquo;Side by Side&rdquo;,
  a series that pairs finished animation against storyboards. If it opens split-screen it is
  wrong for a diagramming exercise. Ten seconds of previewing settles it.</p>
  <p><b>Fallback if it is split-screen:</b> {H.escape(atitle)}, {H.escape(achan)}, {art}.
  <a href="{aurl}" target="_blank" rel="noopener">{aurl}</a></p>
  <p><b>Put the Sheet 2 link in Discord</b> so the rewatch homework is one tap for them.</p>
</div>

<h3 class="sec">If you are ahead</h3>
<div class="card">
  <p><b>{H.escape(otitle)}</b> &middot; {H.escape(ochan)} &middot; {ort}</p>
  <p>{H.escape(onote)}</p>
  <p><a href="{ourl}" target="_blank" rel="noopener">{ourl}</a></p>
</div>

<h3 class="sec">All ten terms, both videos each</h3>
{all_terms}

<div class="foot">
  <p><b>Instructor copy, not linked from anything students see.</b> Their pages are the
  <a href="index.html">rundown</a>, <a href="media.html">Sheet 1, media</a> and
  <a href="terms.html">Sheet 2, terms</a>.</p>
  <p>Blue is what you say out loud. Amber is what you do. Green is a term landing, with the
  clip that teaches it and the clip they have already seen it in. All of it renders from one
  source file, so this page and theirs cannot drift.</p>
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
print("rundown.html", len(page), "bytes;",
      sum(len(v) for v in S.STEPS.values()), "steps;",
      len(S.TERM_VIDEOS), "terms with both videos")
