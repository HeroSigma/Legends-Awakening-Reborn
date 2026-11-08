# Obedience follows permitted training levels

The legacy badge obedience threshold was 10 before Roxanne, causing level-16 Pokemon to disobey despite the new training cap. Battle obedience now uses at least the active story level cap. Before the Dex handoff it uses the opening training limit of 16. Existing higher badge allowances and special battle exemptions remain intact.

Native mGBA checks the actual obedience function for original and traded Pokemon at and below all Hoenn caps, including the opening. 1,068 assertions passed, plus 288 Start menu regression assertions. No save fields or storage format changed. The permanent release ROM was replaced with the battery save preserved byte for byte. Load through Continue after changing ROM builds; old emulator save states retain outdated executable addresses.
