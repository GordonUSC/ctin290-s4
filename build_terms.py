#!/usr/bin/env python3
"""Sheet 2: key terms with definitions, each pointing at a video that actually reinforces it.
Tier 1 definitions are verbatim from the course glossary (the single source, 55 terms).
Tier 2 unpacks terms the session teaches inside other definitions and inside the activity."""
import html as H
from _kit import KIT, NAV

# key: (id, display name, official channel?)
V = {
 "clair":  ("wWGIakhqr5g", "Clair Obscur: Expedition 33, Launch Trailer", False),
 "leap":   ("hpuS9bvhEEQ", "Spider-Verse, “It’s a leap of faith”", False),
 "gta1":   ("QdBZY2fkU-0", "Grand Theft Auto VI, Trailer 1", True),
 "first9": ("zzH4rV08TLI", "Spider-Verse, First 9 Minutes", True),
 "sinners":("bKGxHflevuk", "Sinners, Official Trailer", True),
 "imax":   ("okvFCZi5B0k", "Coogler on Shooting With IMAX Film Cameras", True),
}

# term, definition, video key, what to look at, extra note
CANON = [
 ("Depth of Field",
  "The zone of sharp focus in an image; controlled by aperture, focal length, and distance. "
  "Deep DoF keeps foreground and background sharp; shallow DoF isolates subject.", "clair",
  "Focus separating figure from ground, and what it forces you to look at.",
  "CHANNEL NOTE. This clip is an IGN upload, not the developer's own channel. It is the clip "
  "the glossary points at and it is fine to play, but say out loud that it is a third-party "
  "upload, the same way you flag Madden 96 and the shot-sizes explainer."),
 ("Dutch Angle",
  "A tilted or canted frame, not level with the horizon; often signals unease, chaos, or "
  "subjective perspective.", "leap",
  "Approx 2:30. The frame inverts on the leap. The tilt is the whole meaning of the shot, and "
  "it is the clearest single example of a camera move that is an argument.",
  "CHANNEL NOTE. High-Def Digest is an enthusiast channel reposting a Sony clip, not an "
  "official account. Play it and say so. If you would rather stay official, the same beat is "
  "inside the First 9 Minutes upload from Sony, which is already on this sheet for Parallax."),
 ("Pan / Tilt / Boom",
  "Camera movements: pan (horizontal turn), tilt (vertical turn), boom (vertical lift). "
  "Boom is also a microphone arm.", "gta1",
  "Motivated camera moves. Ask what each move is chasing. This is the clip students annotate "
  "in the 10:48 block, so the terms and the activity are pointed at the same ninety seconds.",
  ""),
 ("Parallax",
  "The apparent shift in position between foreground and background layers when camera moves; "
  "creates depth and dimensionality.", "first9",
  "0:00 to 9:00. Layered depth built out of a 2D-styled image. Watch the planes separate as "
  "the camera travels, and notice this is exactly the trick a game engine gives you for free.",
  ""),
]

UNPACKED = [
 ("Dolly",
  "Moving the whole camera toward or away from the subject, rather than zooming. The "
  "relationship between foreground and background changes, which is why it feels like travel "
  "and a zoom does not.", "sinners",
  "A dolly changes what is behind the subject. A zoom does not. Once you have seen it you "
  "cannot unsee it."),
 ("Crane / Boom move",
  "Lifting or lowering the camera through space on an arm. Usually used to reveal scale, or "
  "to leave a scene rather than cut away from it.", "sinners",
  "Where the camera rises, ask what you are being shown that the character cannot see."),
 ("Focal length",
  "How wide or narrow the lens sees. Wide lenses exaggerate depth and distance between "
  "planes; long lenses compress them and flatten the space.", "imax",
  "Coogler talks format rather than lens, but the same idea: the choice is made before the "
  "shot and it decides what the shot can mean."),
 ("Tracking / Following shot",
  "The camera travels with a moving subject, holding them roughly in frame. Keeps you "
  "attached to a character rather than watching them from outside.", "gta1",
  "Ask who the camera is loyal to. A follow is a choice about whose story it is."),
 ("Handheld vs. locked-off",
  "Handheld carries visible human motion; locked-off is fixed and still. One puts a body in "
  "the room with the subject, the other puts a witness at a distance.", "sinners",
  "Stillness is a camera move. It is a decision not to move, and it costs the same nothing "
  "in an engine as anything else."),
 ("Motivated camera move",
  "A move that exists because something in the scene requires it: a subject moves, a fact "
  "needs revealing, an emotion turns. The opposite is decoration.", "gta1",
  "This is the whole annotation activity in one term. One sentence per move saying what it "
  "is chasing. A move with no sentence is decoration, and finding those is the exercise."),
]

FORWARD = [
 ("Establishing Shot", "A wide shot that situates the audience in a place before the scene "
  "narrows to the people in it.", "Session 6",
  "Named today whenever a crane reveals a location. It belongs to composition."),
 ("Blocking", "The arrangement and movement of figures within the frame, and their "
  "relationship to the camera.", "Session 9",
  "Camera movement and figure movement are two halves of one problem. Today is the camera half."),
 ("Continuity", "Consistency of space, screen direction, and action across a cut, so that the "
  "audience keeps its bearings.", "Session 7",
  "The reason a move can be illegal. Today you only name it; editing owns it."),
]


def card(term, defn, vkey, look, extra, n):
    vid, vname, official = V[vkey]
    url = "https://www.youtube.com/watch?v=" + vid
    badge = "" if official else '<span class="unoff">not an official channel</span>'
    ex = ""
    if extra:
        cls = "flag" if extra.startswith("CHANNEL NOTE") else "more"
        ex = f'<p class="{cls}">{H.escape(extra)}</p>'
    return f'''<article class="term">
  <div class="n">{n:02d}</div>
  <div class="body">
    <h2>{H.escape(term)}</h2>
    <p class="def">{H.escape(defn)}</p>
    {ex}
    <div class="rein">
      <span class="lbl">Reinforced by</span>{badge}
      <p class="vid"><a href="{url}" target="_blank" rel="noopener">{H.escape(vname)}</a></p>
      <p class="look">{H.escape(look)}</p>
      <p class="url"><a href="{url}" target="_blank" rel="noopener">{url}</a></p>
    </div>
  </div>
</article>'''


n = 0
canon_html = []
for t, d, v, l, e in CANON:
    n += 1
    canon_html.append(card(t, d, v, l, e, n))
unp_html = []
for t, d, v, l in UNPACKED:
    n += 1
    unp_html.append(card(t, d, v, l, "", n))
fwd = "".join(
  f'<article class="fwd"><h3>{H.escape(t)}</h3><p class="def">{H.escape(d)}</p>'
  f'<p class="when2"><span class="lbl">{H.escape(s)}</span> {H.escape(note)}</p></article>'
  for t, d, s, note in FORWARD)

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
.def{{margin:0 0 14px;font-size:23px;line-height:1.4;max-width:56ch}}
.more{{margin:0 0 14px;font-size:18px;line-height:1.55;color:var(--ink2);max-width:64ch;
 border-left:3px solid var(--rule);padding-left:16px}}
.flag{{margin:0 0 14px;font-size:17px;line-height:1.5;max-width:64ch;background:#FBF2E4;
 border-left:6px solid var(--orange);padding:13px 17px}}
.rein{{background:var(--fill);padding:16px 20px;max-width:70ch}}
.unoff{{font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.14em;
 text-transform:uppercase;background:var(--orange);color:#fff;padding:3px 9px;margin-left:10px}}
.vid{{margin:6px 0 8px;font-size:22px;font-weight:600;letter-spacing:-.015em}}
.vid a{{color:var(--ink);text-decoration:none;border-bottom:3px solid var(--green)}}
.vid a:hover,.vid a:focus-visible{{color:var(--green)}}
.look{{margin:0 0 9px;font-size:18px;line-height:1.5;color:var(--ink2)}}
.url{{margin:0;font-family:"IBM Plex Mono",monospace;font-size:12.5px;word-break:break-all}}
.fwds{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:0;
 border-top:1px solid var(--rule)}}
.fwd{{padding:22px 26px 22px 0;border-right:1px solid var(--rule)}}
.fwd:last-child{{border-right:0}}
.fwd h3{{margin:0 0 8px;font-size:25px;font-weight:700;letter-spacing:-.02em}}
.fwd .def{{font-size:17.5px;line-height:1.5;color:var(--ink2)}}
.when2{{margin:0;font-size:16px}}
</style>
<div class="wrap">
<header class="mast">
 <div><span class="lbl">CTIN 290 &middot; Session 4 &middot; Camera Movement &amp; Perspective &middot; Unit 1, Seeing</span>
  <h1>The words for<br>what you are<br>looking at</h1></div>
 <div class="rt"><span class="lbl">Sheet 2 of 2</span></div>
</header>
<div class="sub">
 <div><span class="lbl">Terms</span><b>10</b></div>
 <div><span class="lbl">From the glossary</span><b>4</b></div>
 <div><span class="lbl">Unpacked today</span><b>6</b></div>
 <div><span class="lbl">Videos used</span><b>6</b></div>
 <div><span class="lbl">Links checked</span><b>all</b></div>
</div>
{NAV.format(m='', t=' class="here"')}
<main>
<h2 class="sec">In the course glossary <span>These are the four the syllabus already owns for Session 4</span></h2>
{chr(10).join(canon_html)}
<h2 class="sec">Taught today, not yet in the glossary <span>Unpacked from the opening and from the annotation activity</span></h2>
{chr(10).join(unp_html)}
<h2 class="sec">Next door <span>Named today, owned by another session</span></h2>
<div class="fwds">{fwd}</div>
</main>
<div class="note">
 <p><b>Every definition in the first block is verbatim from the course glossary</b>, the 55-term
 single source shared with the class. The second block is not in the glossary yet. All six are
 already taught inside the opening vocabulary and inside the annotation activity, so they are
 pulled out here where students can see them. Promote any of them and I will fold them into the
 glossary properly.</p>
 <p><b>Two of the four glossary clips are third-party uploads</b>, marked in orange above. Neither
 is a problem to play; both want a sentence saying whose upload it is, the same way you flag
 Madden 96 and the shot-sizes explainer. The Dutch Angle beat also exists inside Sony's own First
 9 Minutes upload if you would rather stay official all session.</p>
 <p><b>Timestamps are given only where the session plan already had one.</b> Everything else says
 what to look at instead, because a precise minute mark I had not verified would be invented.</p>
</div>
<div class="foot">
 <p>All six videos confirmed against the YouTube oEmbed endpoint on 1 Sep 2026, channel and title
 checked against the claim printed here.</p>
 <p>Exit ticket: one term you learned today and where you saw it. One thing you are still unsure of.</p>
</div>
</div>'''
open("terms.html", "w").write(page)
print("terms.html", len(page), "bytes")
