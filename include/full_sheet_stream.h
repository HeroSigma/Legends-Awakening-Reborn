#ifndef GUARD_FULL_SHEET_STREAM_H
#define GUARD_FULL_SHEET_STREAM_H
#include "global.h"
void FullSheetStreamRelease(void);
bool8 FullSheetStreamLoad(const struct MapLayout *layout);
bool8 FullSheetStreamOwnsTileset(const struct Tileset *tileset);
bool8 FullSheetStreamDraw(const struct MapLayout *layout, u16 metatileId, u16 offset);
void FullSheetStreamCommit(void);
void FullSheetStreamVBlank(void);
bool8 FullSheetStreamActive(void);
#endif
