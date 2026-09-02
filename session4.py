#!/usr/bin/env python3
"""Single source for Session 4. Student pages and the instructor rundown BOTH render
from this file, so the two can never drift.

Each block carries `student` (what the class sees) and `note` (instructor direction,
which appears ONLY on rundown.html). Nothing from the instructor version was deleted
when the student version was made; it moved here."""

MEET = "Wed 2 Sep 2026 &middot; 10:00 to 12:50 &middot; SCI L104"
TITLE = "Camera Movement &amp; Perspective"
UNIT = "Unit 1: Seeing"
AIM = ("Learn to name what the camera is doing, and to tell a move that means "
       "something from a move that is only decoration.")

# start-min, end-min, clock, title, student text, instructor note, [media keys]
BLOCKS = [
 (600, 612, "10:00", "Opening: The Four Moves",
  "Pan is a horizontal turn. Tilt is vertical. Dolly moves the whole camera toward or away "
  "from the subject. Crane lifts it through space. Four words. By the end of today you will "
  "spot all four and be able to say what each one is for.",
  "Introduce the vocabulary fast and resist over-explaining. They get the real definitions on "
  "Sheet 2 and the depth comes from the annotation activity, not from you talking. Twelve "
  "minutes is enough, and running long here is what wrecks the back half.",
  []),

 (612, 648, "10:12", "Camera Movement in Action",
  "We watch Spider-Verse and Sinners, and we stop constantly. Every time we stop: name the "
  "move, then say what it is chasing. These are two films with opposite relationships to the "
  "camera. In one it costs nothing to move. In the other every move was expensive.",
  "Pause constantly, this is the anchor block. Spider-Verse first, 1:00 to 1:30, then the "
  "whole trailer. Then Sinners. The question to land is which camera is freer and what that "
  "freedom costs in meaning. Do not let this run long; the annotation activity is where it "
  "actually lands.",
  ["spidey", "sinners"]),

 (648, 666, "10:48", "Activity: Movement Annotation",
  "GTA VI Trailer 1, ninety seconds, on a loop. Annotate every camera move. For each one, "
  "write the single sentence that says what that move is chasing. A move you cannot write a "
  "sentence for is decoration, and finding those is the point of the exercise.",
  "Loop the clip, do not play it once and move on. Ninety seconds means they can genuinely "
  "mark everything. Circulate. The students who finish fast are usually the ones writing "
  "“it looks cool” sentences; push those to name what the move reveals.",
  ["gta1"]),

 (666, 676, "11:06", "Break",
  "Ten minutes. Leave the room.",
  "The block is 170 minutes now, not 110. One five-minute break was right for a two-hour "
  "class and it is not right for this one. Take the full ten and leave the room yourself, "
  "because the back half is the half that has to land.",
  []),

 (676, 706, "11:16", "Second Text: What a Real Camera Costs",
  "Ryan Coogler on shooting Sinners with IMAX film cameras. Every move he describes has a "
  "price: weight, setup time, a magazine that runs out. Then the question turns around on "
  "you. Your engine camera weighs nothing. So what stops you from moving it constantly, and "
  "what is lost when nothing does?",
  "Two minutes of video holding a thirty-minute block. The video is the prompt; the "
  "discussion is the work, so have both questions ready before you press play. If the room "
  "goes quiet, ask them to name one move from the annotation activity they would cut first "
  "if it cost ten thousand dollars to shoot.",
  ["imax"]),

 (706, 731, "11:46", "Annotation Share-Back",
  "Compare your annotations in pairs. Where two of you marked the same move and wrote "
  "different sentences, that disagreement is the useful part, not a mistake. Then the harder "
  "question: which moves did nobody manage a sentence for?",
  "Keep a running list on the board with two columns: moves that survived a sentence, and "
  "moves that did not. The second column is the lesson. Do not resolve the disagreements for "
  "them, and do not let a confident student settle one by volume.",
  []),

 (731, 755, "12:11", "Movement Diagram: Up, &ldquo;Married Life&rdquo;",
  "Back to the four minutes you watched cold in Session 2 and annotated for shot scale. Third "
  "pass, new vocabulary. Diagram it on paper: what moves, when, and what the move does to the "
  "emotion.",
  "They know this sequence close to by heart, which is exactly why it works here. The point "
  "they should reach on their own is how little the camera moves and how much each move is "
  "carrying because of it. Ask why a sequence about an entire marriage holds so still, then "
  "wait. Do not give them the answer.",
  []),

 (755, 765, "12:35", "Homework and Close",
  "Find a camera movement in a clip of your own choosing, from outside the course canon. "
  "Write the one sentence saying what the move is chasing. Bring the clip and the sentence. "
  "Then rewatch the four teaching clips on Sheet 2, about twenty-one minutes total.",
  "Say the Session 6 date out loud and write it on the board. There is a week and a holiday "
  "between this class and the next one, and the homework is easy to lose in that gap.",
  []),

 (765, 770, "12:45", "Exit Ticket",
  "Two lines on paper before you leave. One term you learned today and where you saw it. One "
  "thing you are still unsure of.",
  "Collect them at the door. Five minutes, and it is the cheapest instrument you have for "
  "finding out what actually landed. The two things students are least likely to volunteer "
  "are which concept went past them and what they believe is expected of them, and this asks "
  "for both directly. Read them before Session 6 and open that class by answering the two "
  "most common ones by name.",
  []),
]

# key: id, title, channel, runtime, cue, what it teaches, what to watch for, moves, instructor note
MEDIA = {
 "spidey": ("g4Hbz2jLxvQ", "Spider-Man: Into the Spider-Verse, Official Trailer",
   "Sony Pictures Entertainment", "2:40", "10:12 &middot; play 1:00 to 1:30, then again whole",
   "Movement as energy, and as the thing that tells you where to look.",
   "The film swaps camera language when it swaps who the frame belongs to. Watch for the "
   "moment the camera stops behaving like a camera and starts behaving like the character.",
   ["Pan", "Dolly", "Whip", "Parallax"],
   "Only two minutes forty, so you can afford to stop on every move. This is the anchor text."),

 "sinners": ("bKGxHflevuk", "Sinners, Official Trailer", "Warner Bros.", "2:00",
   "10:12 &middot; play after Spider-Verse",
   "Weight. A camera that costs something to move.",
   "Coogler shot this on large format. Deep-focus wide compositions, and a frame used top to "
   "bottom rather than center-weighted. Every move here had a price, and yours do not.",
   ["Crane", "Dolly", "Locked-off"],
   "Sit it directly against Spider-Verse. The comparison is the block."),

 "gta1": ("QdBZY2fkU-0", "Grand Theft Auto VI, Trailer 1", "Rockstar Games", "1:30",
   "10:48 &middot; the assigned clip, played on a loop",
   "Ninety seconds, every move countable.",
   "Short enough to mark every move inside the block, dense enough that there are plenty to "
   "mark. One sentence per move saying what it is chasing.",
   ["Pan", "Tilt", "Dolly", "Crane"],
   "Loop it. Do not play it once. This is the clip the whole activity hangs on."),

 "imax": ("okvFCZi5B0k", "Sinners: Ryan Coogler on Shooting With IMAX Film Cameras",
   "IMAX", "2:02", "11:16 &middot; play whole, then discuss",
   "What a real camera costs, and why that changes a choice.",
   "Coogler on why aspect ratio changes what a shot means, with the cameras and the film "
   "stock on screen. Your engine equivalent is the render target and the framing.",
   ["Aspect ratio", "Format", "Constraint"],
   "Two minutes carrying thirty. Questions ready before you press play."),

 "extended": ("tJbzMqJGH4k", "Grand Theft Auto VI: An Extended Look", "Rockstar Games", "26:48",
   "Already watched &middot; nothing to screen",
   "Twenty-seven minutes of camera you have already seen.",
   "We watched all of this in Session 3, for color. Today it is the same footage and a "
   "different question, which is the third time this course has done that on purpose. You do "
   "not need to rewatch it. You need to remember it and now notice what the camera was doing "
   "while you were looking at the light.",
   ["Follow", "Dolly", "Handheld"],
   "No screening needed, they have seen every minute of it. That makes it your cheapest "
   "reference in the room: point at it from memory rather than playing it. It is also the "
   "obvious fallback for any student stuck on the homework, since the whole class already "
   "shares the text. Rockstar never writes Trailer 3 on it, so search the title."),
}

# teaching clips: id, title, channel, runtime
TEACH = {
 "dof":   ("6DZiJrL_9tU", "Learn Depth of Field in 6 Minutes (With Real Examples)", "Never fStop", "6:25"),
 "dutch": ("SHYfsYQDr6M", "Why movies tilt the camera like this", "Vox", "5:28"),
 "glos":  ("R994JUx7PJ8", "Film Glossary: Shot Movement (Dolly, Crane, Track, Zoom, Tilt, Pan)",
           "J.D. Swerzenski", "1:40"),
 "multi": ("YdHTlUGN1zw", "Walt Disney's MultiPlane Camera, filmed 13 Feb 1957",
           "Walt Disney Productions, 1957", "7:20"),
 "dolly": ("AKOxbCx1LNc", "The Difference Between Dolly and Zoom Shots", "Film Riot", "6:22"),
 "crane": ("SojAuaWQ0fk", "The Art Of The CRANE SHOT", "Tao Hudson", "4:48"),
 "lens":  ("fC-fyXCAWzA", "What is Lens Compression? Camera Focal Length Explained", "Remy Leonard", "5:29"),
 "track": ("mkVYpzyJvG8", "How to Shoot Better Tracking Shots", "StudioBinder", "5:06"),
 "lock":  ("eL_XaKA5qWM", "Why Great Directors Lock the Camera", "StudioBinder", "11:57"),
 "motiv": ("DfhI4RV5KKQ", "Motivated VS Unmotivated Camera Movement", "Brickwall Pictures", "5:07"),
}

CANON_CLIP = {
 "sinners": ("bKGxHflevuk", "Sinners, Official Trailer"),
 "leap":    ("hpuS9bvhEEQ", "Spider-Verse, “It’s a leap of faith”"),
 "gta1":    ("QdBZY2fkU-0", "Grand Theft Auto VI, Trailer 1"),
 "first9":  ("zzH4rV08TLI", "Spider-Verse, First 9 Minutes"),
 "imax":    ("okvFCZi5B0k", "Coogler on Shooting With IMAX Film Cameras"),
}

# term, definition, teach key, why it teaches, canon key, what to look at
GLOSSARY = [
 ("Depth of Field",
  "The zone of sharp focus in an image; controlled by aperture, focal length, and distance. "
  "Deep DoF keeps foreground and background sharp; shallow DoF isolates subject.",
  "dof",
  "Builds the idea on real shots rather than diagrams, and refocuses the same frame so you "
  "can watch attention move without the camera moving at all.",
  "sinners",
  "Coogler shot large format for deep focus, so the background keeps competing for your eye "
  "instead of dissolving away. Ask which is telling you where to look and which is trusting "
  "you to choose."),

 ("Dutch Angle",
  "A tilted or canted frame, not level with the horizon; often signals unease, chaos, or "
  "subjective perspective.",
  "dutch",
  "Takes the tilt across decades of films and asks what it is actually for, including where "
  "it fails and reads as cheap. A term is worth more with its misuse attached.",
  "leap",
  "Around 2:30. The frame inverts on the leap. The whole meaning of the shot is in the tilt."),

 ("Pan / Tilt / Boom",
  "Camera movements: pan (horizontal turn), tilt (vertical turn), boom (vertical lift). "
  "Boom is also a microphone arm.",
  "glos",
  "One hundred seconds, one move per caption, demonstrated on screen as it is named. It also "
  "covers dolly, crane and track, so it does duty for three more terms further down.",
  "gta1",
  "The clip you annotate in class, so the vocabulary and the activity point at the same "
  "ninety seconds."),

 ("Parallax",
  "The apparent shift in position between foreground and background layers when camera moves; "
  "creates depth and dimensionality.",
  "multi",
  "Walt Disney demonstrating the multiplane camera in 1957, on the actual machine, pulling "
  "painted glass layers apart to show why depth appears when the camera travels. It is the "
  "origin of the technique and still the clearest explanation of it ever filmed.",
  "first9",
  "0:00 to 9:00. The same trick seventy years later, done in a renderer. Watch the planes "
  "separate as the camera travels. A game engine hands you this for free."),
]

UNPACKED = [
 ("Dolly",
  "Moving the whole camera toward or away from the subject, rather than zooming. The "
  "relationship between foreground and background changes, which is why it feels like travel "
  "and a zoom does not.",
  "dolly",
  "Runs the two side by side on the same subject, which is the only way this lands.",
  "sinners", "A dolly changes what is behind the subject. A zoom does not. Find one of each."),

 ("Crane / Boom move",
  "Lifting or lowering the camera through space on an arm. Usually used to reveal scale, or "
  "to leave a scene rather than cut away from it.",
  "crane",
  "Spends its time on why a crane move is chosen rather than on the rig, which is the half "
  "that transfers to an engine. Your virtual camera has an infinite jib and no budget line.",
  "sinners", "Where the camera rises, ask what you are being shown that the character cannot see."),

 ("Focal length",
  "How wide or narrow the lens sees. Wide lenses exaggerate depth and distance between "
  "planes; long lenses compress them and flatten the space.",
  "lens",
  "Holds the subject the same size and changes only the lens, so what you are watching is "
  "purely the background expanding and collapsing. That is compression isolated.",
  "imax", "Coogler talks format rather than lens, but it is the same idea: the choice is made "
  "before the shot and it decides what the shot can mean."),

 ("Tracking / Following shot",
  "The camera travels with a moving subject, holding them roughly in frame. Keeps you "
  "attached to a character rather than watching them from outside.",
  "track",
  "Separates a tracking shot from a pan that happens to follow someone, which is the "
  "distinction most people get wrong first.",
  "gta1", "Ask who the camera is loyal to. A follow is a claim about whose story this is."),

 ("Handheld vs. locked-off",
  "Handheld carries visible human motion; locked-off is fixed and still. One puts a body in "
  "the room with the subject, the other puts a witness at a distance.",
  "lock",
  "Argues that stillness is a decision rather than an absence of one, using directors who "
  "lock the frame deliberately.",
  "sinners", "Stillness is a camera move. It is a decision not to move, and in an engine it "
  "costs exactly the same nothing as anything else."),

 ("Motivated camera move",
  "A move that exists because something in the scene requires it: a subject moves, a fact "
  "needs revealing, an emotion turns. The opposite is decoration.",
  "motiv",
  "Puts motivated and unmotivated versions of the same move next to each other. If you cannot "
  "get started on your sentences, start here.",
  "gta1", "One sentence per move saying what it is chasing. A move with no sentence is "
  "decoration, and finding those is the exercise."),
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

NEXT_MEETING = ("Session 6, Wed 9 Sep", "Session 5 is Labor Day, so there is no class on Mon 7 Sep.")


def mmss(t):
    a, b = t.split(":")
    return int(a) * 60 + int(b)


REQUIRED_REWATCH = sum(mmss(TEACH[k][3]) for k in ("dof", "dutch", "glos", "multi"))
ALL_TEACH = sum(mmss(v[3]) for v in TEACH.values())


# ---------------------------------------------------------------------------
# The Up sequence, used at 12:11. Session 2 screened it cold.
MEDIA["up"] = ("XoyZmu0IOKc", "Up, “Married Life”", "Pixar, official", "4:34",
   "12:11 &middot; play 0:00 to 4:00",
   "A whole marriage, and a camera that almost never moves.",
   "The sequence they saw cold in Session 2. Third pass, new vocabulary.",
   ["Locked-off", "Dolly", "Tilt"],
   "PREVIEW TEN SECONDS BEFORE CLASS. This is Pixar's official upload but the title says "
   "“Side by Side”, which is a series that pairs finished animation against storyboards. "
   "If it opens split-screen it is the wrong upload for a diagramming exercise and you should "
   "switch to the alternative below. This has been flagged since Session 2 and is still "
   "unconfirmed.")

MEDIA["up_alt"] = ("EHoHhdbEq1Y", "UP Married Life 1440p HD", "UP Pixar, a fan channel", "4:23",
   "12:11 &middot; fallback only",
   "The clean finished sequence, if the official upload is split-screen.",
   "Same four minutes with no storyboard comparison.",
   ["Locked-off", "Dolly", "Tilt"],
   "Fallback. Not an official channel, so say whose upload it is if you play it.")

# term name -> (teach key, canon key), built from the two term lists
TERM_VIDEOS = {t[0]: (t[2], t[4]) for t in GLOSSARY + UNPACKED}
TERM_DEF = {t[0]: t[1] for t in GLOSSARY + UNPACKED}
GLOSSARY_NAMES = [t[0] for t in GLOSSARY]

# block start -> [(from, to, label, [SAY lines], [DO lines], media key or None, [term names])]
STEPS = {
 600: [
  (600, 602, "Land the session", [
    "Monday we talked about color and light. Today we talk about the camera, and about the "
    "fact that it moves.",
    "By the time you leave you will be able to name what a camera is doing, and say whether "
    "it had a reason to do it."],
   ["Write four words on the board and leave them up: PAN, TILT, DOLLY, CRANE."], None, []),

  (602, 609, "The four moves, on your own body", [
    "Pan is my head turning. Tilt is my head nodding. Dolly is me walking toward you. Crane "
    "is me being lifted.",
    "That is the entire vocabulary for today and you already own all of it in your body."],
   ["Demonstrate each one physically. Turn, nod, walk toward the front row, then reach up.",
    "Make them do it with you. It takes thirty seconds and it is the reason they remember."],
   None, ["Pan / Tilt / Boom", "Dolly", "Crane / Boom move"]),

  (609, 612, "The question that runs all day", [
    "One question runs through everything today. Not what is the camera doing. What is the "
    "camera chasing.",
    "A move that is chasing something is motivated. A move that is chasing nothing is "
    "decoration. By 12:45 you will be able to tell them apart inside ninety seconds of footage."],
   ["Write WHAT IS IT CHASING? on the board. Leave it up for the whole session.",
    "Do not define motivated formally yet. They earn it at 10:48."],
   None, ["Motivated camera move"]),
 ],

 612: [
  (612, 620, "Spider-Verse, first pass, no talking", [
    "Watch it once. I am not going to say anything over it."],
   ["Play 1:00 to 1:30 twice, then run the whole trailer once.",
    "Say nothing during it. The silence is the point; they are building an impression you "
    "will take apart in a minute."], "spidey", []),

  (620, 632, "Spider-Verse, second pass, stop on every move", [
    "Freeze. What just happened to the frame?",
    "Good. Now the second half. What was it chasing?"],
   ["Pause constantly. Cold-call by name, alternate around the room.",
    "When the frame tilts, name Dutch angle. When the layers slide, name parallax.",
    "Watch for the moment the camera stops behaving like a camera and starts behaving like "
    "the character. That is the one to slow down on."],
   None, ["Parallax", "Dutch Angle"]),

  (632, 642, "Sinners, the opposite physics", [
    "Same exercise, different physics. Coogler shot this on large format film.",
    "Every move you are about to see cost money, and time, and somebody's back."],
   ["Play the trailer. Stop on the wide compositions.",
    "Name deep focus and ask what it does to where your eye goes.",
    "Name the locked-off shots. Stillness is a decision, not an absence of one."],
   "sinners", ["Depth of Field", "Handheld vs. locked-off"]),

  (642, 648, "The comparison, which is the block", [
    "Which of those two cameras is freer?",
    "Now the harder one. Which of those two cameras means more?",
    "I shipped football games at EA where the broadcast camera barely moved, and that was a "
    "design decision, not a limitation."],
   ["Let the second question sit. Do not answer it for them.",
    "SAY THE EA LINE. You consistently undersell this and it is the single thing in the room "
    "that makes the argument concrete: you have actually shipped a camera."],
   None, []),
 ],

 648: [
  (648, 651, "Set up the annotation", [
    "Two columns on your page. Left column, the move. Right column, one sentence saying what "
    "that move is chasing.",
    "If you cannot write the sentence, still write the move down. Those are the interesting ones."],
   ["Put the two column headings on the board: MOVE / WHAT IT IS CHASING.",
    "Ninety seconds of footage. Tell them it will loop and they do not need to rush."],
   "gta1", ["Tracking / Following shot"]),

  (651, 663, "Run the loop", [], [
    "Loop the clip continuously for the full twelve minutes. Do not play it once and stop.",
    "Circulate. Read over shoulders.",
    "The students who finish fast are usually writing “it looks cool”. Push those to name "
    "what the move reveals that a static frame would not."], None, []),

  (663, 666, "First read of the room", [
    "Hands up. How many moves did you mark?"],
   ["Write the range on the board, lowest to highest. Do not comment on it yet.",
    "That spread is the setup for the share-back at 11:46."], None, []),
 ],

 666: [
  (666, 676, "Break", ["Ten minutes. Go outside."],
   ["Take it yourself and leave the room. The back half is the half that has to land."],
   None, []),
 ],

 676: [
  (676, 679, "Frame the second text", [
    "You have spent an hour in worlds where moving the camera is free. A crane shot costs a "
    "keyframe.",
    "Now watch somebody talk about a camera you have to carry."],
   ["Do not preview the argument. Let Coogler make it."], None, []),

  (679, 682, "Play it", [], ["Play the whole two minutes. It is short."], "imax", []),

  (682, 694, "What changes when the camera is heavy", [
    "What changes about a director's choices when the camera weighs something?"],
   ["Draw out: weight, setup time, a magazine that runs out, a crew that has to be paid.",
    "Name focal length when aspect ratio comes up. Format and lens are the same kind of "
    "decision: made before the shot, and it decides what the shot can mean."],
   None, ["Focal length"]),

  (694, 706, "Turn it around, which is the point", [
    "Your engine camera weighs nothing. Nothing at all.",
    "So what stops you from moving it constantly? And what is lost when nothing does?"],
   ["This is the block. Give it the full twelve minutes.",
    "If the room goes quiet, ask them to name one move from the annotation they would cut "
    "first if it cost ten thousand dollars."], None, []),
 ],

 706: [
  (706, 709, "Pair up", [
    "Find someone who is not sitting next to you. Trade pages."], [], None, []),

  (709, 721, "Compare annotations", [
    "Where you both marked the same move and wrote different sentences, stop there. That "
    "disagreement is the useful part, not a mistake."],
   ["Circulate. Do not resolve the disagreements for them.",
    "Do not let a confident student settle one by volume. Ask the quieter one to say theirs "
    "again."], None, []),

  (721, 731, "Board the two columns", [
    "Which moves did nobody manage a sentence for?"],
   ["Two columns on the board: SURVIVED A SENTENCE / DID NOT.",
    "The second column is the whole lesson. Let it get long and do not rescue it."],
   None, ["Motivated camera move"]),
 ],

 731: [
  (731, 735, "Set it up, and remind them", [
    "You watched this cold in Session 2 with no vocabulary at all. Then you took it apart for "
    "shot scale.",
    "Third pass. Same four minutes. New words."],
   ["PREVIEW THIS CLIP BEFORE CLASS. See the note on the media card.",
    "Do not tell them what they are about to notice."], None, []),

  (735, 739, "Play 0:00 to 4:00", [], ["Play it clean, no commentary."], "up", []),

  (739, 751, "Diagram it", [
    "On paper. A line for the sequence. Mark every camera move on it, and under each mark, "
    "what that move does to the emotion."],
   ["Circulate. Most diagrams will be nearly empty, and that is correct.",
    "Do not tell them the camera barely moves. Let the empty page say it."],
   None, ["Handheld vs. locked-off"]),

  (751, 755, "The question", [
    "Why does a sequence about an entire marriage hold so still?"],
   ["Ask it, then wait. Wait longer than is comfortable.",
    "Do not give them the answer. This is the one they should carry out of the room."],
   None, []),
 ],

 755: [
  (755, 760, "Assign the homework", [
    "Find a camera movement in a clip of your own choosing, from outside anything we have "
    "watched together. Write the one sentence saying what that move is chasing. Bring both."],
   ["Anyone stuck can use the GTA VI Extended Look, since the whole room has seen all "
    "twenty-seven minutes of it.",
    "Say the next meeting out loud and write it on the board: Session 6, Wed 9 Sep. Session 5 "
    "is Labor Day. A week and a holiday is where homework goes to die."], None, []),

  (760, 765, "Name the four terms and the rewatch", [
    "Four terms today. Depth of field, dutch angle, pan tilt boom, parallax.",
    "Sheet 2 has two videos for each one. The first teaches the term. The second shows it "
    "working in something we have already watched together. Twenty-one minutes in total, and "
    "that is the required part."],
   ["Put the Sheet 2 link in Discord before you leave the room."], None, []),
 ],

 765: [
  (765, 770, "Exit ticket", [
    "Two lines on paper before you go. One term you learned today and where you saw it. One "
    "thing you are still unsure of."],
   ["Collect at the door. Stand there so it actually happens.",
    "Read them before Session 6 and open that class by answering the two most common by name."],
   None, []),
 ],
}
