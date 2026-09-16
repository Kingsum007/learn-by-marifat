# Verification report

Date: 15 September 2026. Host: Windows, Flutter 3.47.2, Dart 3.13.2.

## Version 3.1 publication candidate

Static analysis reports no issues, the translation audit inventories 420 authored interface/error messages with zero missing Dari or Pashto entries, and the full suite passes 134 tests with the upload-key-dependent store test skipped in the ordinary run. The store-specific run passes separately with `STORE_BUILD=true`, confirming that the direct HesabPay support panel is absent and the in-app privacy statement remains visible. The Windows release build succeeds.

Gradle completes the Android App Bundle for version 3.1.0+19. ZIP integrity passes, the bundle contains ARMv7, ARM64 and x86_64 libraries, and the merged release manifest confirms package `org.afghanlearn.kohi`, minimum SDK 24, target SDK 36, automatic backup disabled, and no INTERNET or ACCESS_NETWORK_STATE permission. The locally validated AAB is intentionally unsigned because the owner upload key is not present. Store copy, screenshots, icon, feature graphic, privacy page, Data safety answers and release checklist are packaged for review. A signed build, public HTTPS privacy URL, Play Console declarations and physical-device closed-track acceptance remain owner actions.

## Version 2.4 selectable Code Lab

123 Flutter unit/widget tests pass. The native Windows integration check passes language selection, Python execution and SQLite execution. Tests cover language-specific draft round trips, old backup compatibility, cancelled switches, failed writes, persisted selection, SQL dispatch and fixed Python exercises. Dari/Pashto selector layouts and actual dropdown selection are checked. Static analysis reports no issues. External language compilers and HTML preview are not included. See LANGUAGE_LAB.md.

## Version 2.3 courses and database learning

117 Flutter unit/widget tests pass and static analysis reports no issues. The
expanded catalog contains 20 courses, 320 planned sessions and 60 project briefs.
Guide coverage tests check all 304 non-Python modules and both local-language
translations. The translation inventory reports zero missing entries.

Two SQLite content test methods execute all 18 relational module scripts with
expected result checks and additional key, foreign-key and negative-price
rejection checks. SQL practice tests cover filtering, left joins, aggregation,
empty results, literal handling, duplicate result columns, fresh fixtures and
blocked mutations, file access, unbounded functions and recursive queries.

A native Windows integration test passes startup/storage, course navigation,
Python execution and real SQLite query rendering. Dari/Pashto database lesson
images were visually inspected after bundling Noto Sans Mono for code text.
The font is distributed with its original SIL Open Font License. Local server
courses and external framework fragments were not execution-tested here;
native-speaker review is still pending. See COURSE_EXPANSION.md for scope.

## Version 2.2 detailed foundation instruction

110 Flutter tests pass and static analysis reports no issues. All seven original
lesson examples execute in the offline interpreter and match their newly shown
expected outputs. Each lesson has three detailed teaching sections in English,
Dari and Pashto; coverage checks reject missing sections or languages. The UI
translation inventory has zero missing keys. Updated phone lesson images in
Dari and Pashto were visually inspected. Native-speaker review and novice
learning evaluation have not been performed. See DETAILED_TEACHING.md for scope.

## Version 2.1 offline gamification

All 108 Flutter unit/widget tests pass and static analysis reports no issues. The final Windows release build succeeds; executable version is 2.1.0+6. A native Windows integration test passes startup/storage, course-map navigation, and real Python execution. New reward tests cover known IDs, lesson bonuses, thresholds, wrong answers, duplicate concurrent submissions, failed writes and reopening persisted progress. Dark Dari/Pashto mission maps were rendered and visually inspected; playable lesson navigation is tested from those maps. Existing phone/desktop visual baselines were updated and then verified in a normal test run.

XP and badges are derived from saved solved IDs with no extra counter or schema migration. Replays cannot add points. Completion of all available foundation missions ends the next-level prompt. Rewards cover graded Python foundation exercises only; workshops and self-reported projects award no automatic XP. See GAMIFICATION.md for rules, sources and limits.

## Version 2.0 Marifat experience redesign

Final verification: 103 Flutter unit/widget tests pass; static analysis reports no issues. The Windows release build succeeds and reports 2.0.0+5. A native Windows integration run passes startup, local storage, course navigation, and Python execution. New journey tests cover the three-view beginner lesson, language selection before starting, settings access, and saving a draft when leaving the code lab.

Desktop and Dari/Pashto phone visuals were rendered and inspected, including the original supplied logo, home, project guidance, and foundation lesson. Screenshot tests explicitly wait for local logo decoding and load the Arabic font. Inline print() calls, lists and comparisons preserve LTR order inside RTL prose. Translation inventory: 1,601 keys, no missing Dari/Pashto entries. The bundled logo SHA-256 matches the supplied original.

No learner schema migration is introduced. Bloom labels are removed from the learner UI while curriculum level metadata and alignment tests remain. This is not a claim of measured novice usability, native-speaker approval, Android device acceptance, or completion of the remaining reference projects/runtimes. See UX_REDESIGN.md.

## Version 1.3 Python project reference implementations

All 98 Flutter tests pass and static analysis reports no issues. The final Windows release build succeeds and its executable reports version 1.3.0+4. The translation inventory covers 1,583 source strings with no missing Dari/Pashto entries. Dari and Pashto project walkthrough screenshots were rendered and visually inspected at 390 × 844. Inline code fragments now use directional isolation to preserve list/comparison order in RTL prose; a regression test verifies that behavior. Native-speaker review remains pending.

Three Python command-line projects implement the ledger, attendance analyst, and shop inventory briefs. Their 15 standard-library regression tests pass on CPython 3.14.7, including CLI round trips, invalid input preserving prior data, restart persistence, rollback under injected failures, duplicate attendance rejection, week boundaries, and prevention of oversales across connections. Source and test code are readable in the app. No external project dependencies are required.

Three separate teaching-core exercises execute successfully in the actual in-app Python VM. Their starter programs deliberately need learner completion. Solution loading requires confirmation and an explicit save before replacing persisted code. These exercises do not execute file/database requirements; full references still require CPython on a computer.

## Version 1.2 localization and workspaces

All 90 unit/widget tests pass. Static analysis reports no issues. One native Windows integration test also passes, exercising SQLite startup, curriculum navigation, and real isolate execution. New checks cover translation inventory and placeholder parity, workspace/evidence preservation, rejected invalid writes, version-2 backup migration, Dari/Pashto RTL UI with LTR code, explicit workspace saving, and phone screenshots using the bundled Noto Naskh Arabic font. Both localized 390 × 844 screenshots were visually inspected. English desktop golden checks remain passing.

The version 1.2.0+3 Windows release build succeeds with --release --no-pub --no-tree-shake-icons. Android/device acceptance remains unverified.

The translation generator reports zero missing keys across 1,552 inventoried source strings in its required inventory for Dari and Pashto. This is source coverage, not a native-speaker quality assessment. Pashto Cupertino control strings have a local delegate because Flutter does not supply one. Native review remains pending.

Fifteen authored beginner entry lessons are bundled. All 180 plans and 45 project briefs have local workspaces; these do not constitute 180 complete tutorials or 45 completed applications. See IMPLEMENTATION_STATUS.md for exact remaining scope.

## Project naming and architecture update

### Version 1.1 curriculum extension

The application now includes 15 searchable course curricula, 180 lesson plans, and 45 project assignments. The 82-test unit/widget suite passes, including prerequisite-cycle checks, all-six-level Bloom coverage per course, version-1 JSON migration, portfolio validation, real SQLite portfolio persistence, project evidence editing, and narrow-screen rubric layout. Static analysis reports no issues. The dashboard and course-catalog visual baselines were rendered and inspected at 1440 × 1040.

The first new native test exposed an ambiguous test finder matching both the search input and the Swift course title; the finder was narrowed to the course ListTile. This was a test-selection failure, not a startup or persistence failure. The corrected native Windows test passes: actual startup and SQLite initialization, course search, Swift curriculum navigation, and real Python isolate execution. A separate normal golden run passes against both inspected baselines.

The 82.6% coverage figure below belongs to the earlier 74-test implementation and is not claimed as current coverage. Structural curriculum tests do not prove instructional quality, and examples for external toolchains have not all been compiled on their respective platforms. Project assignments include briefs, acceptance conditions, and assessment plans; complete reference implementations for 45 projects are not included.

The version 1.1 Windows release build succeeds with `--release --no-pub --no-tree-shake-icons`. Its complete release folder is packaged with the source. Android APK compilation and physical-device airplane-mode acceptance remain unverified; this update does not remove those earlier limitations.

The product is now **Learn By Marifat Team**, with Dart package `learn_by_marifat_team` and Windows executable `learn_by_marifat_team.exe`. Android launcher text, Windows title/resources, in-app branding, backup dialogs, and documentation use the new name. Existing storage and backup identifiers remain compatible as described in `ARCHITECTURE.md`.

After the rename, static analysis reports no issues, all 74 automated tests pass, and the native Windows integration test passes. The updated dashboard baseline was rendered and visually inspected. The new architecture diagram is valid SVG/XML. The Windows CMake cache was regenerated to remove an old target-name reference.

## Historical version 1.0 verification

- Windows release build succeeds with `flutter build windows --release --no-pub --no-tree-shake-icons`. Distribute the full release ZIP, not the EXE alone.
- Static analysis: no issues.
- Dart formatting: source, unit/widget tests, and native integration test formatted.
- **74 automated tests pass**, covering runtime behavior and limits, all lesson examples, all code-ordering solutions, all coding reference solutions, grading, concurrent commands, failure recovery, backup validation, actual SQLite persistence, and widget interactions.
- **One native Windows integration test passes**: the real application initializes platform storage, opens SQLite, shows the bundled course, opens the code lab, saves a draft, and executes code through the real isolate adapter.
- Desktop visual baseline rendered and inspected at 1440 × 1040, with the actual bundled font and Material icons.
- Small-screen widget checks include a 390 × 844 viewport and a 360 × 800 viewport with text enlarged to 150%.

Measured line coverage from the automated suite: **1,061 / 1,285 lines (82.6%)** in the generated coverage report at this implementation stage. The native test is separate and is not included in this percentage. Line coverage does not imply full correctness or branch coverage.

## Problems found and fixed during verification

- Updated file-picker API: moved to current static APIs and bounded streaming file reads.
- Windows database initialization: select the FFI factory before accessing a mobile factory; native startup now passes.
- Command queue initialization: initialize the pending Future inside the first command, avoiding scheduling-context problems under widget tests.
- Nested runtime values: bound total nested value size before formatting or comparison can expand work excessively.
- Restored drafts: refresh editor state after a successful restore.
- Preview font loading: load bundled text and icon fonts for meaningful visual checks.

## Host build adjustments

- Windows disallows creating ordinary plugin symlinks. `tool/prepare_windows.ps1` uses junctions in the project's generated build directory; no OS security settings were changed.
- Windows Application Control blocks Flutter's optional `font-subset.exe`. The release build uses `--no-tree-shake-icons`, retaining the full icon font.
- The Android Gradle distribution could not be downloaded reliably on this connection. The wrapper uses the smaller Gradle 9.3.1 binary distribution with an official SHA-256 checksum and a configured timeout. Android packaging remains unverified until the download and build complete.

## Not claimed as complete

- No verified Android APK or airplane-mode test on a physical Android device.
- No production signing key, app-store submission, or public distribution.
- Native backup-picker interaction has not been exercised end-to-end; the backup codec, import validation, application persistence, and real SQLite reopening are tested.
- No full Dari/Pashto curriculum translation, local educator language review, TalkBack audit, or educational-effectiveness study.
- The runtime is a bounded Python teaching subset, not a CPython conformance implementation.

Run the real-device acceptance procedure in `QUALITY_AND_RELEASE.md` before describing the Android release as production-ready.
