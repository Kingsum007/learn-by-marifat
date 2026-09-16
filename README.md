# Learn By Marifat Team — learn programming offline

A Flutter application for Afghan computer science students: 20 offline curricula, 320 detailed modules, 640 Bloom-aligned lesson plans, 60 real-world project assignments, and a bounded on-device Python teaching interpreter.

## Version 3.0: clearer paths and deeper courses

The course catalog now gives beginners one obvious starting action, compact searchable learning-path cards, visible ready/locked/completed states, prerequisite guidance, and responsive one- or two-column layouts. Subtle entrance and lesson-step transitions respect the device's reduced-motion preference. Every course now contains sixteen sequential modules and thirty-two sessions, including applied software-engineering studios with real use cases, testable examples, failure recovery, architecture, security, accessibility, performance, delivery, encouraging hints, and complete English, Afghanistan Dari, and Afghanistan Pashto text.

Version 3.0.1 removes repeated generic introductions from advanced modules and combines three repeated workshop reminders into one actionable checkpoint. Automated curriculum checks cap module explanation length and reject unsupported promises of guaranteed mastery, employment, or accreditation.

## Version 2.9: Marifat identity and support

The settings area now includes an About and Support page with the Marifat Team mission, a clearly voluntary donation option, and the HesabPay number `+93788070101` with one-tap copy. It includes a founder biography based on the supplied résumé and public contact details for email, website, LinkedIn, GitHub, phone, and WhatsApp. The official Code With Safi YouTube channel can be opened externally or copied. The supplied Marifat emblem is now the Android and Windows application icon. All course content remains available offline. See [About and Support](docs/ABOUT_AND_SUPPORT.md).

## Version 2.4: choose your coding language

Code Lab has 19 language/framework choices, separate saved drafts, remembered selection, and save/discard protection when switching. Python and read-only SQLite execute inside the app. Other choices provide offline editing, copy/save, and local tool instructions without a misleading Run button. Graded Python exercises remain Python-only. See [Code Lab behavior and compatibility](docs/LANGUAGE_LAB.md).

## Version 2.3: expanded courses and databases

All 304 non-Python modules include example walkthroughs, concrete practice tasks, encouraging hints, and review criteria in English, Dari, and Pashto. Every course contains sixteen modules; modules seven through sixteen cover course-specific advanced topics and applied software engineering through requirements, contracts, recovery, testing, architecture, security, accessibility, performance, and delivery. Five database courses add foundations, SQL, SQLite, PostgreSQL, and MongoDB. A bounded, read-only SQL practice area runs real SQLite queries on fresh fictional tables, without opening the student progress database. See [scope and validation](docs/COURSE_EXPANSION.md).

The seven Python foundation lessons retain their detailed three-language explanations from version 2.2.

## Version 2.1: offline learning adventure

Course entry now shows a mission map, XP, levels, badges and visible challenge progress. Correct Python foundation answers earn points once; completed lessons earn a bonus. Success feedback celebrates new progress. Other courses use short workshop views, with advanced reference material separate from the main path. See [reward rules and design sources](docs/GAMIFICATION.md) and [the Dari course map](preview/mission-fa.png).

## Version 2.0: Marifat beginner experience

The supplied Marifat logo and navy/teal identity replace the previous design. Home has a clear start/continue action and immediate language choices. Foundation lessons use short concept/example/practice views with a persistent next button. Three navigation destinations keep advanced tools out of the first learning step. Bloom is applied through the curriculum rather than displayed as interface terminology. Course search works with translated names; leaving unsaved code offers save, discard, or continued editing.

See [redesign decisions](docs/UX_REDESIGN.md), [Dari home](preview/overview-fa.png), and [Dari lesson](preview/lesson-fa.png).

## Implemented

- Three complete Python command-line reference projects with 15 regression tests, translated Bloom walkthroughs, and runnable in-app core exercises. Full reference programs require local CPython; they are not run by the teaching interpreter.
- Twenty beginner entry lessons with vocabulary, traced examples, prediction questions, hints, and small reference solutions.
- In-app source/notes workspaces for all 640 lesson plans and 60 projects; Python subset execution where supported.
- Searchable course catalog with prerequisites, sixteen modules and thirty-two lesson plans per course.
- Required zero-knowledge introduction for every non-Python course; completing its readiness check unlocks topic 1 and persists offline.
- Original explanations, worked code/design fragments, timed activities, measurable objectives, and evidence-based assessment prompts.
- Three project assignments per course with acceptance conditions, milestones, deliverables, and a five-dimension rubric.
- Local portfolio reflections, milestone checklists, self-assessment scores, and unsaved-change protection.
- Seven guided lessons and 21 exercises: multiple choice, code ordering, and coding.
- Runnable examples covering variables, arithmetic, conditions, loops, lists, and simple functions.
- Local code editor with explicit Save, Run, output, hints, and expected-output feedback.
- Search, bookmarks, completion tracking, and retry-safe progress.
- SQLite transactions, immutable state, serialized writes, and visible save failures.
- Validated JSON backup export/restore using native file dialogs, with replacement confirmation.
- Responsive phone/desktop screens, bundled fonts, dark appearance, Dari/Pashto content, right-to-left layout, and bundled Arabic typography.
- Domain and adapter boundaries, constructor injection, architecture decision records, requirements traceability, automated tests, and a CI workflow.

English, Dari, and Pashto translations cover the inventoried curriculum, beginner guides, Python exercises, and authored interface messages. Automated coverage checks do not replace native-speaker review; that review is pending. Code, filenames, learner input, and original license notices retain their original text.

## Offline contract

All core content and the runtime ship with the application. No account, activation, downloaded lesson pack, cloud compiler, API key, telemetry, or backend is required. Android's main manifest explicitly removes INTERNET and ACCESS_NETWORK_STATE from merged manifests. Automatic Android backup is disabled; use explicit local exports.

The teaching interpreter is **not full CPython**. It implements a documented Python subset with bounded resource use. Imports, packages, input(), classes, files, networking, f-strings, list methods, and full Python semantic compatibility are not available. The in-app language guide explains the limits. Coding tasks grade displayed output, not algorithm structure, and are intended for formative practice.

The other courses, advanced Python examples, and project builds require separately provisioned local development tools. All lesson plans and project instructions are readable offline inside this app; the app does not bundle all language compilers, SDKs, or all 60 finished project solutions. Three Python reference solutions now ship in projects/python and are readable in the app. Native iOS projects require a compatible Mac with Xcode. Each lesson plan and project now has a local workspace with up to four text files, 12,000 characters each, included in exported backups. Larger external SDK/build folders still need separate backups. Rubric scores are self-assessments, not verified credentials.

## Develop and run

Implemented and checked with Flutter **3.47.2**, Dart **3.13.2**, on Windows. Keep `pubspec.lock` for repeatable dependencies.

```sh
flutter pub get
flutter run -d windows
# or, with an Android device connected:
flutter run -d <device-id>
```

If Windows cannot create plugin symlinks, run `tool/prepare_windows.ps1` from the project directory after `flutter pub get`. It creates project-local junctions without changing Windows security settings. Run it again if package refresh recreates the ephemeral directory.

```sh
flutter analyze
flutter test --coverage
flutter test integration_test/startup_test.dart -d windows
flutter build windows --release --no-tree-shake-icons
flutter build apk --release --no-tree-shake-icons
```

`--no-tree-shake-icons` is needed on the current host because Application Control blocks Flutter's optional font-subsetting executable. It preserves the full icon font. On an unrestricted build host, icon subsetting can reduce size normally.

Android development requires installed SDK packages, accepted Android SDK licenses, and Gradle dependencies. Build tools may download dependencies; this is separate from offline use by students. Google Play builds require the owner-controlled upload key described in `android/key.properties.example`. The store build omits the voluntary HesabPay support card and keeps the learning experience fully offline. Run `tool/build_google_play.ps1 -AllowUnsigned` for a local validation bundle; configure the upload key and run `tool/build_google_play.ps1` for an uploadable signed bundle.

## Documentation

- [Python project reference pack](projects/python/README.md)
- [Architecture specification](docs/ARCHITECTURE.md)
- [Complete curriculum and lesson plans](docs/CURRICULUM.md)
- [Curriculum sources and teaching rationale](docs/CURRICULUM_SOURCES.md)
- [Architecture overview diagram](docs/architecture.svg)
- [Engineering architecture and decisions](docs/ENGINEERING.md)
- [Quality, threat model, and release procedure](docs/QUALITY_AND_RELEASE.md)
- [Verification report](docs/VERIFICATION.md)
- [Rendered desktop preview](preview/dashboard.png)
- [About, support, and public-information policy](docs/ABOUT_AND_SUPPORT.md)
- [Privacy policy](docs/PRIVACY_POLICY.md)
- [Google Play listing](distribution/google-play/STORE_LISTING.md)
- [Google Play data-safety answers](distribution/google-play/DATA_SAFETY.md)
- [Google Play release checklist](distribution/google-play/RELEASE_CHECKLIST.md)
- [Microsoft Store listing](distribution/microsoft-store/STORE_LISTING.md)
- [Microsoft Store release checklist](distribution/microsoft-store/RELEASE_CHECKLIST.md)

## Persistence and backup

Data is stored in `kohi.db` under the platform application-support directory. The version-1 SQLite table holds a version-2 JSON learner aggregate. Existing version-1 payloads migrate in memory with an empty portfolio and become version 2 on the next save. Writes and restore are transactional. A malformed or unknown-version backup is rejected before replacement. The original database is not silently reset on startup failure.

Save or run code before closing an exercise or terminating the app. Save portfolio evidence before leaving its page; unsaved evidence triggers a discard prompt. Backups include saved drafts, attempts, solved exercise IDs, bookmarks, preferences, and portfolio entries. They are readable JSON, not encrypted archives. Each reflection is limited to 4,000 characters and the complete backup to 1 MB of UTF-8 data.

Curriculum authors edit `tool/build_curriculum.py`, run `python tool/build_curriculum.py`, then `dart format lib/data/bundled_curriculum.dart`. This creates the compiled-in catalog, a distributable JSON catalog, and `docs/CURRICULUM.md` from one source. Keep IDs stable to preserve saved evidence. The JSON export is an authoring artifact; the application reads the generated bundled Dart data without a first-run asset download.

## Distribution

Distribute the entire Windows release folder together (EXE, DLLs, and `data`); the EXE alone is not sufficient. For Android, transfer a built APK to the device by USB or local sharing, and complete the airplane-mode acceptance procedure in the quality document.

For Microsoft Store submission, reserve the product first and copy its exact Package Identity Name and Publisher from Partner Center. Then run `tool/build_microsoft_store.ps1 -PackageName '<Name>' -Publisher '<Publisher>'`. The script builds the full Windows release and packages it as x64 MSIX. `-AllowPlaceholderIdentity` creates a clearly labelled local validation package that cannot be mistaken for the identity-correct Store upload.

Course updates currently ship in a new app version. No arbitrary content/plugin import is implemented. There is no claim of measured educational effectiveness until a student pilot and comparative evaluation are conducted.

The course text and mountain illustration were authored for this project. Roboto's license is in `assets/fonts/LICENSE.txt`; dependency licenses are available from Settings in the application.
