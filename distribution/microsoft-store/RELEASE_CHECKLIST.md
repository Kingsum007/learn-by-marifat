# Microsoft Store release checklist

## Prepared

- Flutter Windows x64 release for version 3.1.0.
- Manual MSIX manifest for a full-trust Win32 desktop application.
- English, Dari (Afghanistan) and Pashto (Afghanistan) resource declarations.
- Package logos, wide tile and splash assets using Marifat branding.
- Store listing copy and existing public privacy-policy HTML.
- Owner-identity build script that refuses to create a Store-named package with placeholder identity.

## Partner Center owner actions

1. Reserve the product name in Partner Center.
2. Open Product identity and copy the exact Package/Identity/Name and Package/Identity/Publisher values.
3. Run `tool/build_microsoft_store.ps1 -PackageName '<Name>' -Publisher '<Publisher>'`.
4. Host `distribution/privacy-policy.html` at a stable public HTTPS address.
5. Add the description and localized listings from `STORE_LISTING.md`.
6. Upload at least one PC screenshot; 5–8 useful localized screenshots are recommended.
7. Complete age rating, properties, privacy and support/contact fields.
8. From an Administrator PowerShell in an active desktop session, run `tool/test_microsoft_store.ps1 -PackagePath '<identity-correct.msix>'`; then test installation, first launch, lessons, local saving, backup/restore and offline behavior on a clean Windows 10/11 computer.
9. Upload the identity-correct `.msix` to a private audience or flight first, then submit publicly after acceptance testing.
