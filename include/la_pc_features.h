#ifndef GUARD_LA_PC_FEATURES_H
#define GUARD_LA_PC_FEATURES_H
bool32 LaPcRetiredMap(u32 group, u32 num);
bool32 LaPcBlockedSpecial(u32 id);
bool32 LaPcBlockWarp(const struct MapHeader *, s32 warpId);
extern const u8 LaCollection_Blocked[];
#endif
