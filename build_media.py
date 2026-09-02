#!/usr/bin/env python3
"""Sheet 1: what plays in Session 4, in play order, and what each one teaches.
Every link and every runtime was confirmed against YouTube before this file was written.
Session 3 used color swatches. This session is movement, so the chips name the moves to
spot instead of the colors to point at."""
import html as H
from _kit import KIT, NAV

# id, title, channel, official?, runtime, when it plays, what it teaches, what to watch for, moves
ITEMS = [
 ("g4Hbz2jLxvQ", "Spider-Man: Into the Spider-Verse, Official Trailer",
  "Sony Pictures Entertainment", True, "2:40",
  "10:12 &middot; Case Study &middot; play 1:00 to 1:30, then again whole",
  "Movement as energy, and as the thing that tells you where to look.",
  "Pause constantly. This is the anchor text and it is only two minutes forty, so you can "
  "afford to stop on every move. For each one, name the move and then say what it is chasing. "
  "The film swaps camera language when it swaps who the frame belongs to, which is the point "
  "you are setting up for the annotation activity.",
  ["Pan", "Dolly", "Whip", "Parallax"]),

 ("bKGxHflevuk", "Sinners, Official Trailer", "Warner Bros.", True, "2:00",
  "10:12 &middot; Case Study",
  "Weight. A camera that costs something to move.",
  "Coogler shot this on large format. Deep-focus wide compositions, and a frame used top to "
  "bottom rather than center-weighted. The most purely cinematic thing in the canon, which is "
  "exactly why it is useful to a room building in engines: every move here had a price, and "
  "yours do not. Sit it next to Spider-Verse and ask which camera is freer, and what that "
  "freedom costs in meaning.",
  ["Crane", "Dolly", "Locked-off"]),

 ("QdBZY2fkU-0", "Grand Theft Auto VI, Trailer 1", "Rockstar Games", True, "1:30",
  "10:48 &middot; Activity &middot; the clip students annotate",
  "The assigned clip. Ninety seconds, every move countable.",
  "This is the clip for the movement annotation and it is named here so nobody has to ask. "
  "Ninety seconds is the whole argument for using it: short enough that a student can mark "
  "every move in the block, dense enough that there are plenty to mark. One sentence per move "
  "saying what it is chasing. Any move without a sentence is decoration, and finding those is "
  "the exercise.",
  ["Pan", "Tilt", "Dolly", "Crane"]),

 ("okvFCZi5B0k", "Sinners, Ryan Coogler on Shooting With IMAX Film Cameras",
  "IMAX", True, "2:02",
  "11:16 &middot; Second Text &middot; play it, then talk for the rest of the block",
  "What a real camera costs, and why that changes a choice.",
  "Two minutes of video holding a thirty-minute block, so the video is the prompt and the "
  "discussion is the work. Coogler on why aspect ratio changes what a shot means, with the "
  "cameras and the film stock on screen. Ask the room what changes about a director's choices "
  "when the camera is heavy: weight, setup time, a magazine that runs out. Then turn it "
  "around, because that is the point of the block. Your engine camera weighs nothing, so what "
  "stops you from moving it constantly, and what is lost when nothing does.",
  ["Aspect ratio", "Format", "Constraint"]),

 ("tJbzMqJGH4k", "Grand Theft Auto VI: An Extended Look", "Rockstar Games", True, "26:48",
  "Optional &middot; not placed in a block",
  "Twenty-seven minutes of camera, if the room is ahead.",
  "The Session 3 sheet promised this one a second home and this is it: Session 3 played six "
  "minutes of it for color, and the other twenty are camera. Rockstar never writes Trailer 3 "
  "on the video, so search the title, not the number. Nothing in the session depends on it. "
  "Reach for it only if the annotation activity finishes early, and if you do, play from 6:00 "
  "where Session 3 stopped rather than starting over.",
  ["Follow", "Dolly", "Handheld"]),
]

rows = []
for i, (vid, title, chan, official, rt, when, teaches, watch, moves) in enumerate(ITEMS, 1):
    url = "https://www.youtube.com/watch?v=" + vid
    opt = " opt" if "Optional" in when else ""
    badge = "" if official else '<span class="unoff">not an official channel</span>'
    chips = "".join('<i>{}</i>'.format(H.escape(m)) for m in moves)
    rows.append(f'''<article class="item{opt}">
  <div class="n">{i:02d}</div>
  <div class="body">
    <h2><a href="{url}" target="_blank" rel="noopener">{H.escape(title)}</a></h2>
    <p class="meta"><span class="lbl">{H.escape(chan)}</span>{badge} <span class="rt">{rt}</span> <span class="when">{when}</span></p>
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
.unoff{{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.14em;
 text-transform:uppercase;background:var(--orange);color:#fff;padding:4px 10px}}
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
 <div><span class="lbl">CTIN 290 &middot; Session 4 &middot; Wed 2 Sep &middot; SCI L104</span>
  <h1>What we are<br>watching, and<br>what it teaches</h1></div>
 <div class="rt"><span class="lbl">Sheet 1 of 2</span></div>
</header>
<div class="sub">
 <div><span class="lbl">Items</span><b>5</b></div>
 <div><span class="lbl">In class</span><b>8:12</b></div>
 <div><span class="lbl">In a block</span><b>4</b></div>
 <div><span class="lbl">Links checked</span><b>5 of 5</b></div>
 <div><span class="lbl">Unit</span><b>1 &middot; Seeing</b></div>
</div>
{NAV.format(m=' class="here"', t='')}
<main style="margin-top:30px">
{chr(10).join(rows)}
</main>
<div class="note">
 <p><b>Eight minutes of video across a 170-minute session, and that is deliberate.</b> Session 3
 ran eighteen minutes of footage because color reads in a single frame. Movement does not: it
 only reads when you stop, rewind and play the same thirty seconds three times. Budget the time
 for stopping, not for playing.</p>
 <p><b>The assigned clip is named on this sheet.</b> It is GTA VI Trailer 1, ninety seconds. The
 phrase &ldquo;an assigned clip&rdquo; had been sitting in the session plan with no clip behind
 it, the same gap Theresa caught on the Curriculum Summary. It has a name now.</p>
 <p><b>The Coogler piece is two minutes carrying a thirty-minute block.</b> That is the right
 shape for it, but only if the discussion questions are ready before you press play. They are on
 the rundown, on that block.</p>
</div>
<div class="foot">
 <p>Every link on this sheet was confirmed against the YouTube oEmbed endpoint on 1 Sep 2026, and
 every runtime was read off the video itself. The returned titles and channels are what you see
 printed above. All five are official channel uploads.</p>
 <p>Class meets 10:00 AM to 12:50 PM, Mon and Wed. 170 minutes.</p>
</div>
</div>'''
open("media.html", "w").write(page)
print("media.html", len(page), "bytes")
