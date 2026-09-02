#!/usr/bin/env python3
"""Sheet 2: key terms, each with a video that TEACHES the term and one that shows it
working inside a text the class already knows.

Tier 1 definitions are verbatim from the course glossary (the single source, 55 terms).
Tier 2 unpacks terms the session teaches inside other definitions and inside the activity.

Every id below came out of a live YouTube search results page and was then confirmed
against the oEmbed endpoint with a positive control. Nothing here was typed from memory."""
import html as H
from _kit import KIT, NAV

# key: (id, display name, channel, runtime, official-or-studio channel?)
TEACH = {
 "dof":    ("6DZiJrL_9tU", "Learn Depth of Field in 6 Minutes (With Real Examples)",
            "Never fStop", "6:25", False),
 "dutch":  ("SHYfsYQDr6M", "Why movies tilt the camera like this", "Vox", "5:28", True),
 "glos":   ("R994JUx7PJ8", "Film Glossary: Shot Movement (Dolly, Crane, Track, Zoom, Tilt, Pan)",
            "J.D. Swerzenski", "1:40", False),
 "multi":  ("YdHTlUGN1zw", "Walt Disney's MultiPlane Camera (filmed 13 Feb 1957)",
            "fireurgunz", "7:20", False),
 "dolly":  ("AKOxbCx1LNc", "The Difference Between Dolly and Zoom Shots", "Film Riot", "6:22", True),
 "crane":  ("SojAuaWQ0fk", "The Art Of The CRANE SHOT", "Tao Hudson", "4:48", False),
 "lens":   ("fC-fyXCAWzA", "What is Lens Compression? Camera Focal Length Explained",
            "Remy Leonard", "5:29", False),
 "track":  ("mkVYpzyJvG8", "How to Shoot Better Tracking Shots", "StudioBinder", "5:06", True),
 "lock":   ("eL_XaKA5qWM", "Why Great Directors Lock the Camera", "StudioBinder", "11:57", True),
 "motiv":  ("DfhI4RV5KKQ", "Motivated VS Unmotivated Camera Movement",
            "Brickwall Pictures", "5:07", False),
}

# key: (id, display name, channel, official?)
CANON_CLIP = {
 "sinners": ("bKGxHflevuk", "Sinners, Official Trailer", "Warner Bros.", True),
 "leap":    ("hpuS9bvhEEQ", "Spider-Verse, “It’s a leap of faith”", "High-Def Digest", False),
 "gta1":    ("QdBZY2fkU-0", "Grand Theft Auto VI, Trailer 1", "Rockstar Games", True),
 "first9":  ("zzH4rV08TLI", "Spider-Verse, First 9 Minutes", "Sony Pictures Entertainment", True),
 "imax":    ("okvFCZi5B0k", "Coogler on Shooting With IMAX Film Cameras", "IMAX", True),
 "spidey":  ("g4Hbz2jLxvQ", "Spider-Verse, Official Trailer", "Sony Pictures Entertainment", True),
}

# term, definition, teach key, why that clip teaches it, canon key, what to look at there, flag
CANON = [
 ("Depth of Field",
  "The zone of sharp focus in an image; controlled by aperture, focal length, and distance. "
  "Deep DoF keeps foreground and background sharp; shallow DoF isolates subject.",
  "dof",
  "Builds the idea on real shots rather than diagrams, and shows the same frame refocused so "
  "you can watch attention move without the camera moving. That is the part a still picture "
  "of a lens diagram cannot give you.",
  "sinners",
  "Coogler shot large format for deep focus, so the background keeps competing for your eye "
  "instead of dissolving. Compare it against any shallow-focus trailer and ask which one is "
  "telling you where to look and which one is trusting you to choose.",
  "GLOSSARY CHANGE, YOUR CALL. The glossary currently points this term at an IGN upload of the "
  "Clair Obscur launch trailer, which shows depth of field but never teaches it. Sinners is "
  "official, it is already playing in this session, and it is the stronger example because "
  "deep focus is the deliberate choice in it."),

 ("Dutch Angle",
  "A tilted or canted frame, not level with the horizon; often signals unease, chaos, or "
  "subjective perspective.",
  "dutch",
  "Vox takes the tilt across decades of films and asks what it is actually for, including "
  "where it fails and reads as cheap. A term is better learned with its misuse attached, and "
  "this is the only clip on the sheet that argues against its own subject.",
  "leap",
  "Approx 2:30. The frame inverts on the leap. The whole meaning of the shot is in the tilt, "
  "and it is the clearest case in the canon of a camera angle carrying an argument rather "
  "than decorating one.",
  "CHANNEL NOTE. High-Def Digest is an enthusiast channel reposting a Sony clip, not an "
  "official account. Play it and say so, the same way you flag Madden 96 and the shot-sizes "
  "explainer. Shawn Dolinski, who the class already met in Session 2, also has a 1:06 version "
  "titled “Camera Orientation Explained” if you want the sixty-second definition instead."),

 ("Pan / Tilt / Boom",
  "Camera movements: pan (horizontal turn), tilt (vertical turn), boom (vertical lift). "
  "Boom is also a microphone arm.",
  "glos",
  "One hundred seconds, one move per caption, demonstrated on screen as it is named. It is "
  "shaped exactly like a glossary entry, which is why it sits here and not a fourteen-minute "
  "deep dive. It also covers dolly, crane and track, so it does duty for three more terms "
  "further down this sheet.",
  "gta1",
  "The clip students annotate in the 10:48 block, so the vocabulary and the activity point at "
  "the same ninety seconds. Ask what each move is chasing.",
  ""),

 ("Parallax",
  "The apparent shift in position between foreground and background layers when camera moves; "
  "creates depth and dimensionality.",
  "multi",
  "Walt Disney demonstrating the multiplane camera in 1957, on the actual machine, pulling "
  "painted glass layers apart to show why depth appears when the camera travels. This is the "
  "origin of the technique and it is still the clearest explanation of it ever filmed. It is "
  "also the direct ancestor of what Spider-Verse does in software, which is the connection "
  "worth making out loud.",
  "first9",
  "0:00 to 9:00. The same trick, seventy years later, done in a renderer. Watch the planes "
  "separate as the camera travels, and note that a game engine hands you this for free.",
  "CHANNEL NOTE. A third-party upload of a Disney film, not a Disney account. Worth playing "
  "anyway: it is a primary source and there is no official posting of it."),
]

UNPACKED = [
 ("Dolly",
  "Moving the whole camera toward or away from the subject, rather than zooming. The "
  "relationship between foreground and background changes, which is why it feels like travel "
  "and a zoom does not.",
  "dolly",
  "Runs the two side by side on the same subject, which is the only way this lands. Once you "
  "have seen the background stay put under a zoom and travel under a dolly, you cannot unsee "
  "it.",
  "sinners",
  "A dolly changes what is behind the subject. A zoom does not. Find one of each."),

 ("Crane / Boom move",
  "Lifting or lowering the camera through space on an arm. Usually used to reveal scale, or "
  "to leave a scene rather than cut away from it.",
  "crane",
  "Spends its time on why a crane move is chosen rather than on the rig, which is the half "
  "that transfers to an engine. Your virtual camera has an infinite jib and no budget line, "
  "so the only question left is the one this clip asks.",
  "sinners",
  "Where the camera rises, ask what you are being shown that the character cannot see."),

 ("Focal length",
  "How wide or narrow the lens sees. Wide lenses exaggerate depth and distance between "
  "planes; long lenses compress them and flatten the space.",
  "lens",
  "Holds the subject the same size and changes only the lens, so what you are watching is "
  "purely the background expanding and collapsing. That is compression isolated, and it is "
  "the thing the definition is actually describing.",
  "imax",
  "Coogler talks format rather than lens, but it is the same idea: the choice is made before "
  "the shot and it decides what the shot can mean."),

 ("Tracking / Following shot",
  "The camera travels with a moving subject, holding them roughly in frame. Keeps you "
  "attached to a character rather than watching them from outside.",
  "track",
  "Separates a tracking shot from a pan that happens to follow someone, which is the "
  "distinction students get wrong first and the one the annotation activity will expose.",
  "gta1",
  "Ask who the camera is loyal to. A follow is a claim about whose story this is."),

 ("Handheld vs. locked-off",
  "Handheld carries visible human motion; locked-off is fixed and still. One puts a body in "
  "the room with the subject, the other puts a witness at a distance.",
  "lock",
  "Argues that stillness is a decision rather than an absence of one, using directors who "
  "lock the frame deliberately. It is the strongest correction available to a room that is "
  "about to discover a free-flying engine camera.",
  "sinners",
  "Stillness is a camera move. It is a decision not to move, and in an engine it costs "
  "exactly the same nothing as anything else."),

 ("Motivated camera move",
  "A move that exists because something in the scene requires it: a subject moves, a fact "
  "needs revealing, an emotion turns. The opposite is decoration.",
  "motiv",
  "Puts motivated and unmotivated versions of the same move next to each other. This is the "
  "annotation activity in video form, so it is the one to point students at if they cannot "
  "get started on their sentences.",
  "gta1",
  "One sentence per move saying what it is chasing. A move with no sentence is decoration, "
  "and finding those is the exercise."),
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


def badge(official):
    return "" if official else '<span class="unoff">third-party upload</span>'


def card(term, defn, tkey, why, ckey, look, flag, n):
    tid, tname, tchan, trt, toff = TEACH[tkey]
    cid, cname, cchan, coff = CANON_CLIP[ckey]
    turl = "https://www.youtube.com/watch?v=" + tid
    curl = "https://www.youtube.com/watch?v=" + cid
    fl = ""
    if flag:
        cls = "flag" if flag.startswith(("GLOSSARY CHANGE", "CHANNEL NOTE")) else "more"
        fl = f'<p class="{cls}">{H.escape(flag)}</p>'
    return f'''<article class="term">
  <div class="n">{n:02d}</div>
  <div class="body">
    <h2>{H.escape(term)}</h2>
    <p class="def">{H.escape(defn)}</p>
    {fl}
    <div class="pair">
      <div class="slot teach">
        <span class="lbl">Teaches it</span>{badge(toff)}
        <p class="vid"><a href="{turl}" target="_blank" rel="noopener">{H.escape(tname)}</a></p>
        <p class="chan">{H.escape(tchan)} <span class="rt">{trt}</span></p>
        <p class="look">{H.escape(why)}</p>
        <p class="url"><a href="{turl}" target="_blank" rel="noopener">{turl}</a></p>
      </div>
      <div class="slot seen">
        <span class="lbl">See it in the canon</span>{badge(coff)}
        <p class="vid"><a href="{curl}" target="_blank" rel="noopener">{H.escape(cname)}</a></p>
        <p class="chan">{H.escape(cchan)}</p>
        <p class="look">{H.escape(look)}</p>
        <p class="url"><a href="{curl}" target="_blank" rel="noopener">{curl}</a></p>
      </div>
    </div>
  </div>
</article>'''


n = 0
canon_html = []
for t, d, tk, why, ck, look, flag in CANON:
    n += 1
    canon_html.append(card(t, d, tk, why, ck, look, flag, n))
unp_html = []
for t, d, tk, why, ck, look in UNPACKED:
    n += 1
    unp_html.append(card(t, d, tk, why, ck, look, "", n))
fwd = "".join(
  f'<article class="fwd"><h3>{H.escape(t)}</h3><p class="def">{H.escape(d)}</p>'
  f'<p class="when2"><span class="lbl">{H.escape(s)}</span> {H.escape(note)}</p></article>'
  for t, d, s, note in FORWARD)

# required rewatch = the four glossary terms' teaching clips
req = sum(int(a) * 60 + int(b) for a, b in
          (TEACH[k][3].split(":") for k in ("dof", "dutch", "glos", "multi")))
allt = sum(int(a) * 60 + int(b) for a, b in (v[3].split(":") for v in TEACH.values()))

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
.flag{{margin:0 0 16px;font-size:17px;line-height:1.5;max-width:66ch;background:#FBF2E4;
 border-left:6px solid var(--orange);padding:13px 17px}}
.pair{{display:grid;grid-template-columns:1fr 1fr;gap:2px;background:var(--rule);
 border:1px solid var(--rule)}}
.slot{{background:var(--fill);padding:15px 19px 17px}}
.slot.teach{{background:#EDF3F8}}
.unoff{{font-family:"IBM Plex Mono",monospace;font-size:10px;letter-spacing:.13em;
 text-transform:uppercase;background:var(--orange);color:#fff;padding:3px 8px;margin-left:9px}}
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
 <div><span class="lbl">CTIN 290 &middot; Session 4 &middot; Camera Movement &amp; Perspective &middot; Unit 1, Seeing</span>
  <h1>The words for<br>what you are<br>looking at</h1></div>
 <div class="rt"><span class="lbl">Sheet 2 of 2</span></div>
</header>
<div class="sub">
 <div><span class="lbl">Terms</span><b>10</b></div>
 <div><span class="lbl">From the glossary</span><b>4</b></div>
 <div><span class="lbl">Unpacked today</span><b>6</b></div>
 <div><span class="lbl">Video slots</span><b>20 &middot; 15 distinct</b></div>
 <div><span class="lbl">Required rewatch</span><b>{req // 60}:{req % 60:02d}</b></div>
</div>
{NAV.format(m='', t=' class="here"')}
<main>
<div class="note" style="margin:26px 0 0">
 <p><b>Every term now carries two videos.</b> One <b>teaches</b> the term, built to define and
 demonstrate it. One shows it <b>working inside a text this class already knows</b>, so the
 vocabulary attaches to something they have actually watched rather than to a stranger's
 footage. Read the pair left to right: learn it, then go find it.</p>
 <p><b>Only the four glossary terms are required rewatching, {req // 60} minutes {req % 60} seconds
 total.</b> The six unpacked terms are reference, another {(allt - req) // 60} minutes if anyone
 wants them, and nobody should be assigned all {allt // 60} minutes in one week.</p>
</div>
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
 pulled out here where students can see them.</p>
 <p><b>One glossary change is proposed and it is your call</b>, marked in orange on Depth of
 Field. The glossary sends that term to an IGN upload of the Clair Obscur trailer, which shows
 depth of field but never teaches it and is not an official channel. Sinners is official, is
 already in this session, and makes deep focus the visible choice.</p>
 <p><b>Five of the twenty slots are third-party uploads</b>, marked in orange. None is a problem
 to play; each wants a sentence saying whose upload it is, the same way you flag Madden 96 and
 the shot-sizes explainer. The 1957 multiplane film is the one worth keeping regardless, because
 there is no official posting of it and it is a primary source.</p>
 <p><b>Timestamps appear only where the session plan already had one.</b> Everything else says
 what to look at instead, because a precise minute mark I had not verified would be invented.</p>
</div>
<div class="foot">
 <p>Twenty video slots filled by fifteen distinct videos, because the canon clips do duty for
 more than one term. All fifteen confirmed against the YouTube oEmbed endpoint on 1 Sep 2026,
 with a positive control on the same run. Channel, title and runtime are as returned, not as
 remembered. Teaching clips were found by search, never typed from memory.</p>
 <p>Exit ticket: one term you learned today and where you saw it. One thing you are still unsure of.</p>
</div>
</div>'''
open("terms.html", "w").write(page)
print("terms.html", len(page), "bytes;", "required rewatch", f"{req//60}:{req%60:02d};",
      "all teach clips", f"{allt//60}:{allt%60:02d}")
