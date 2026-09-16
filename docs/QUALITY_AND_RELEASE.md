# Quality and release procedure

## Reproducible checks

Use the Flutter version recorded in the README and the committed `pubspec.lock`.

```sh
flutter pub get
dart format --output=none --set-exit-if-changed lib test integration_test
flutter analyze
flutter test --coverage
flutter test integration_test/startup_test.dart -d windows
flutter test --dart-define=STORE_BUILD=true test/store_release_test.dart
tool/build_google_play.ps1
```

The developer machine needs internet to obtain the toolchain, Gradle, and packages the first time. The installed application does not. Do not confuse a build-time dependency download with a student runtime requirement.

Visual baseline: `preview/dashboard.png`, rendered by a Flutter widget test. Update deliberately with `flutter test --update-goldens test/ui_test.dart`, then inspect the image. Font/raster differences can make baselines platform-dependent; generate and compare on the same OS/toolchain.

## Test strategy

- Runtime tests cover all bundled examples and ordering solutions, operator precedence, strings, lists, branches, loops, functions, short-circuiting, and errors.
- Adversarial cases cover infinite loops, excessive recursion, huge ranges, huge strings, deeply repeated lists, malformed syntax, forbidden operations, and output overflow.
- Controller tests exercise concurrent updates, persistence failures, retry semantics, invalid submissions, and backup validation.
- Real SQLite test closes and reopens a file-backed database.
- Widget tests exercise starting a lesson, submitting a choice, running and saving code, small screens, and enlarged text.
- These tests do not demonstrate educational effectiveness, full Python conformance, or complete Android device compatibility.

## Airplane-mode acceptance on a real Android device

1. Copy the APK onto a representative device using USB or local transfer.
2. Disable mobile data and Wi-Fi before installation and first launch.
3. Start every lesson; check all examples are readable. Open the language guide.
4. Complete a choice, ordering task, and coding exercise. Confirm immediate feedback.
5. Run a while-True program and verify that the runner stops and the UI remains usable.
6. Save code; stop the app; reopen it. Confirm code and progress survive.
7. Export a backup to local storage. Change progress, then restore the backup and verify replacement.
8. Restart and repeat a lesson with large text and TalkBack enabled.
9. Check cold launch time, interaction latency, APK size, working memory, and battery use on actual low-end devices. Record measurements, not assumed targets.
10. Confirm no INTERNET permission exists in the merged APK manifest using Android build tools. Debug/profile tooling may have special requirements; the main manifest removes network permissions during merging.

## Threat model

Assets: learner progress, saved code, uninterrupted device use. Inputs: student programs and backup files. No account credentials or server tokens are stored.

The interpreter cannot import libraries or call host functions; it uses a fixed whitelist of built-ins. It is resource-bounded, but this is not a claim of formally verified sandbox security. The full app still has the platform's normal file-picker access. Backup reads are capped while streaming; decoded structures are validated before any replacement.

SQLite commits are atomic. Backups are unencrypted and intentionally user-readable. Android automatic backup is disabled; user-selected exports are the portable backup mechanism. Device encryption, device access control, and the user's choice of file provider are outside the app's control. No local score is tamper-proof.

## Release signing

Release builds do not fall back to a development key. Copy `android/key.properties.example` to the ignored `android/key.properties`, point it to the permanent owner-controlled upload key, and keep the keystore and passwords outside source control. `tool/build_google_play.ps1` then creates the signed App Bundle. `-AllowUnsigned` exists only for local validation and labels its output accordingly.

## Learning evaluation

Pilot usability and device compatibility first. For an effectiveness study, compare equivalent offline static materials against this app; use pre/post programming tasks and delayed retention measures, not only satisfaction or app completion. Define the primary outcome and conduct a power analysis before selecting the main study size. Collect only consented local exports. The earlier rapid literature review motivates the project but does not establish effectiveness.
