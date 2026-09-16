# Detailed foundation teaching — 2026-09-13

Version 2.2 replaces the short primary explanation in each of the seven playable
Python lessons with three separately authored teaching sections in English,
Afghan-oriented Dari, and Pashto. The sections explain the idea from a concrete
situation, trace the existing example, and guide practice and error recovery.
The example page includes its exact expected output. Existing exercise IDs and
saved progress remain compatible. Content is compiled into the offline app.

Authoring source: `tool/detailed_foundations.py`; regenerate the Dart bundle with
`python tool/detailed_foundations.py`. Coverage checks require all seven IDs,
all three languages and all three sections. Execution tests compare every
documented output with the actual in-app interpreter.

These checks establish structural coverage and executable examples. They do
not establish translation fluency or learning effectiveness. Dari and Pashto
text still requires review by Afghan teachers/native speakers and usability
sessions with beginning students. No such review has been performed.

This release does not claim that the other fourteen course outlines are full
beginner courses. Their module summaries, workshops and project briefs still
require detailed course-specific instruction and validation. They do not have
the same embedded execution support as the seven Python foundation lessons.
The in-app Python runner remains a limited interpreter, not full CPython.

Validation for this change: 110 Flutter tests passed, static analysis reported
no issues, translation inventory reported zero missing keys for both supported
Afghan languages, and refreshed Dari/Pashto lesson images were visually checked
at phone size. These are engineering checks, not certification of language quality.
