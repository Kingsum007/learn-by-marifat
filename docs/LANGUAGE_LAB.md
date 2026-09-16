# Selectable Code Lab — version 2.4

The general Code Lab offers Python, HTML, CSS, JavaScript, Java, Kotlin, Swift,
C++, Dart, SQLite SQL, PostgreSQL, MongoDB, React, React Native, Node.js,
Express.js, Android Compose, iOS SwiftUI, and Flutter. Each selection supplies
a relevant filename, starter, separate draft, and tool requirements. Language
and framework names retain their standard technical spelling; interface
instructions are available in English, Dari and Pashto.

Python runs with the existing bounded teaching interpreter. SQL runs SELECT
queries using the existing isolated SQLite practice engine. Other choices are
offline code editors with save/copy support and the course's local setup
instructions. They have no Run button and are never sent to the Python runner.
This release does not add external compilers, JavaScript execution, HTML
preview, syntax highlighting, or automatic native project builds.

Switching a changed editor offers keep editing, discard, or save and switch.
A failed save or preference write keeps the old language and code visible.
Successful switching restores the destination draft and clears stale results.
The selected language is saved locally and restored at startup. Graded Python
exercises remain fixed to Python regardless of the general lab preference.

The language registry lives in `lib/domain/lab_language.dart`. Python retains
the existing `playground` draft ID. Other choices use an explicit allowlist of
`lab-<language>` draft IDs. The optional `labLanguage` preference defaults to
Python for older backups; payload version 3 and database schema 1 are retained.
Old backups remain readable. Use version 2.4 or newer to restore backups
containing the additional language drafts. Drafts retain the 12,000-character
storage limit; SQLite execution still has its separate 2,000-character query
limit and read-only restrictions. The separate SQL practice screen remains a
temporary scratch area; SQL drafts in Code Lab can be saved and backed up.

Tests cover draft round trips, older backups, invalid IDs, switch cancellation,
save/discard behavior, failed writes, remembered selection, SQLite dispatch,
and fixed-language exercise editing. Dari and Pashto phone layouts and actual
dropdown selection are also tested.
