#!/usr/bin/env python3
"""terms.html, Sheet 2, STUDENT facing.

Every term carries two videos: one that TEACHES it, one that shows it working inside a text
this class has already watched. Renders from session4.py. No channel notes and no instructor
flags on this page; those live on rundown.html."""
import html as H
from _kit import KIT, NAV
import session4 as S


def card(term, defn, tkey, why, ckey, look, n):
    tid, tname, tchan, trt = S.TEACH[tkey]
    cid, cname = S.CANON_CLIP[ckey]
    turl = "https://www.youtube.com/watch?v=" + tid
    curl = "https://www.youtube.com/watch?v=" + cid
    return f'''<article class="term">
  <div class="n">{n:02d}</div>
  <div class="body">
    <h2>{H.escape(term)}</h2>
    <p class="def">{H.escape(defn)}</p>
    <div class="pair">
      <div class="slot teach">
        <span class="lbl">Teaches it</span>
        <p class="vid"><a href="{turl}" target="_blank" rel="noopener">{H.escape(tname)}</a></p>
        <p class="chan">{H.escape(tchan)} <span class="rt">{trt}</span></p>
        <p class="look">{H.escape(why)}</p>
        <p class="url"><a href="{turl}" target="_blank" rel="noopener">{turl}</a></p>
      </div>
      <div class="slot seen">
        <span class="lbl">See it in something we watched</span>
        <p class="vid"><a href="{curl}" target="_blank" rel="noopener">{H.escape(cname)}</a></p>
        <p class="look">{H.escape(look)}</p>
        <p class="url"><a href="{curl}" target="_blank" rel="noopener">{curl}</a></p>
      </div>
    </div>
  </div>
</article>'''


n = 0
glos_html = []
for t, d, tk, why, ck, look in S.GLOSSARY:
    n += 1
    glos_html.append(card(t, d, tk, why, ck, look, n))
unp_html = []
for t, d, tk, why, ck, look in S.UNPACKED:
    n += 1
    unp_html.append(card(t, d, tk, why, ck, look, n))
fwd = "".join(
  f'<article class="fwd"><h3>{H.escape(t)}</h3><p class="def">{H.escape(d)}</p>'
  f'<p class="when2"><span class="lbl">{H.escape(s)}</span> {H.escape(note)}</p></article>'
  for t, d, s, note in S.FORWARD)

req, allt = S.REQUIRED_REWATCH, S.ALL_TEACH

page = f'''{KIT}
<title>Session 4 Key Terms</title>
<style>
h2.sec{{margin:52px 0 0;font-size:15px;font-family:"IBM Plex Mono",monospace;letter-spacing:.22em;
 text-transform:uppercase;font-weight:600;border-bottom:3px solid var(--ink);padding-bottom:11px}}
h2.sec span{{float:right;letter-spacing:.06em;color:var(--ink2);font-weight:400;text-transform:none}}
.term{{display:grid;grid-template-columns:96px 1fr;gap:26px;padding:28px 0;
 border-bottom:1px solid var(--rule);align-items:start}}
.n{{font-family:"IBM Plex Mono",monospace;font-size:40px;font-weight:600;line-height:1;
 color:var(--green);font-variant-numeric:tabular-nums}}
.term h2{{margin:0 0 10px;font-size:40px;line-height:1.04;font-weight:700;letter-spacing:-.035em}}
.def{{margin:0 0 16px;font-size:23px;line-height:1.4;max-width:56ch}}
.pair{{display:grid;grid-template-columns:1fr 1fr;gap:2px;background:var(--rule);
 border:1px solid var(--rule)}}
.slot{{background:var(--fill);padding:15px 19px 17px}}
.slot.teach{{background:#EDF3F8}}
.vid{{margin:7px 0 3px;font-size:20px;font-weight:700;letter-spacing:-.015em;line-height:1.2}}
.vid a{{color:var(--ink);text-decoration:none;border-bottom:3px solid var(--green)}}
.slot.teach .vid a{{border-bottom-color:var(--blue)}}
.vid a:hover,.vid a:focus-visible{{color:var(--blue)}}
.chan{{margin:0 0 9px;font-family:"IBM Plex Mono",monospace;font-size:12.5px;
 letter-spacing:.05em;color:var(--ink2)}}
.chan .rt{{color:var(--ink);font-weight:600;margin-left:8px}}
.look{{margin:0 0 9px;font-size:17px;line-height:1.5;color:var(--ink2)}}
.url{{margin:0;font-family:"IBM Plex Mono",monospace;font-size:12px;word-break:break-all}}
.fwds{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:0;
 border-top:1px solid var(--rule)}}
.fwd{{padding:22px 26px 22px 0;border-right:1px solid var(--rule)}}
.fwd:last-child{{border-right:0}}
.fwd h3{{margin:0 0 8px;font-size:25px;font-weight:700;letter-spacing:-.02em}}
.fwd .def{{font-size:17.5px;line-height:1.5;color:var(--ink2)}}
.when2{{margin:0;font-size:16px}}
@media (max-width:820px){{.pair{{grid-template-columns:1fr}}}}
</style>
<div class="wrap">
<header class="mast">
 <div><span class="lbl">CTIN 290 &middot; Session 4 &middot; {S.TITLE} &middot; {S.UNIT}</span>
  <h1>The words for<br>what you are<br>looking at</h1></div>
 <div class="rt"><span class="lbl">Sheet 2 of 2</span></div>
</header>
<div class="sub">
 <div><span class="lbl">Terms</span><b>{len(S.GLOSSARY) + len(S.UNPACKED)}</b></div>
 <div><span class="lbl">On the syllabus</span><b>{len(S.GLOSSARY)}</b></div>
 <div><span class="lbl">Also covered</span><b>{len(S.UNPACKED)}</b></div>
 <div><span class="lbl">Required rewatch</span><b>{req // 60}:{req % 60:02d}</b></div>
</div>
{NAV.format(i='', m='', t=' class="here"')}
<main>
<div class="note" style="margin:26px 0 0">
 <p><b>Every term here carries two videos.</b> One <b>teaches</b> the term: it defines it and
 demonstrates it, usually by changing one thing at a time so you can watch what that one thing
 does. One shows the term <b>working inside something we have watched together</b>, so the word
 attaches to a film you already know rather than to a stranger's footage. Read them in that
 order. Learn it, then go find it.</p>
 <p><b>The first four terms are your required rewatch, {req // 60} minutes {req % 60} seconds
 in total.</b> The six below them are here because they came up in class and you will want them
 later; they are reference, not homework. Nobody is being asked to watch all
 {allt // 60} minutes in one week.</p>
</div>
<h2 class="sec">On the syllabus for today <span>These four are in the course glossary</span></h2>
{chr(10).join(glos_html)}
<h2 class="sec">Also covered today <span>Came up in the opening and in the annotation activity</span></h2>
{chr(10).join(unp_html)}
<h2 class="sec">Coming up <span>Named today, taught properly in another session</span></h2>
<div class="fwds">{fwd}</div>
</main>
<div class="note">
 <p><b>The definitions in the first block are the course glossary's own wording</b>, so what you
 learn here matches what you are assessed on. The glossary is the permanent reference and it
 lives beyond this session; these sheets are the week-by-week version of it.</p>
 <p><b>Where a timestamp is given, it is worth trusting.</b> Where one is not, the note tells
 you what to look at instead, which is more useful than a minute mark for a technique that runs
 through a whole clip.</p>
</div>
<div class="foot">
 <p>Every link on this sheet was checked on 1 Sep 2026. Runtimes are read off the videos.</p>
 <p>Bring one term you learned and one thing you are still unsure of to the exit ticket.</p>
</div>
</div>'''
open("terms.html", "w").write(page)
print("terms.html", len(page), "bytes; required", f"{req//60}:{req%60:02d}")
