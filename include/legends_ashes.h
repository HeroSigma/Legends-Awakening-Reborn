#ifndef GUARD_LEGENDS_ASHES_H
#define GUARD_LEGENDS_ASHES_H
#define LA_HOOPA_LOCAL_ID 248 // Outside generated wild slots 249-252.
void LegendsAshes_Update(void);
void LegendsAshes_SetGraphics(void);
void LegendsAshes_HoopaPrepare(void);
void LegendsAshes_HoopaGranted(void);
bool32 LegendsAshes_IsSilph(void);
bool32 LegendsAshes_BlockWarp(const struct MapHeader *map, u32 warpId);
#endif
