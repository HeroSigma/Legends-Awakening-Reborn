#include "global.h"
#include "full_sheet_stream.h"

// Unova full-sheet test maps were retired. Retain the shared engine hooks so
// normal tileset rendering continues without linking the test-map payloads.
void FullSheetStreamRelease(void) {}
bool8 FullSheetStreamLoad(const struct MapLayout *layout) { return FALSE; }
bool8 FullSheetStreamOwnsTileset(const struct Tileset *tileset) { return FALSE; }
bool8 FullSheetStreamDraw(const struct MapLayout *layout, u16 metatileId, u16 offset) { return FALSE; }
void FullSheetStreamCommit(void) {}
void FullSheetStreamVBlank(void) {}
bool8 FullSheetStreamActive(void) { return FALSE; }
