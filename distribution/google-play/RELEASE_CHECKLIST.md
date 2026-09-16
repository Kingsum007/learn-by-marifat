# Google Play release checklist

## Completed in the repository

- Versioned Flutter release with stable progress migrations.
- Android target and compile SDK set to API 36.
- Release builds no longer use the shared debug signing key.
- Owner-controlled upload-key configuration supported through ignored `android/key.properties`.
- Store build hides the optional HesabPay support panel.
- Main manifest removes internet and network-state permissions and disables automatic backup.
- Adaptive, round, and legacy Marifat launcher icons are included.
- English, Dari, and Pashto store copy is prepared.
- Privacy policy and Data safety answers are prepared.
- Automated analysis, tests, translation audit, Windows build, and archive integrity checks are available.
- The validation AAB is intentionally named `learn-by-marifat-team-google-play-unsigned.aab`; do not upload it. The signed build script uses the upload key and produces `learn-by-marifat-team-google-play.aab`.

## Owner actions required before submission

1. Confirm that `org.afghanlearn.kohi` is the permanent Play application ID. It cannot be changed for later updates.
2. Create and securely retain an upload keystore, then copy `android/key.properties.example` to `android/key.properties` and fill it locally.
3. Accept the Android SDK licenses on the release machine.
4. Host `distribution/privacy-policy.html` on a stable public HTTPS address.
5. Confirm the target audience and complete Play Console's IARC content-rating form.
6. Create the app in Play Console, upload the signed `.aab`, and complete the prepared declarations.
7. Use a closed testing track first. Install from Play, test on real low-resource Android devices in airplane mode, and verify backup import/export before production rollout.
