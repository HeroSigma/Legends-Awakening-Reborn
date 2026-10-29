#ifndef GUARD_LA_POKERIDE_H
#define GUARD_LA_POKERIDE_H
#include "global.h"
struct ObjectEvent;
struct Sprite;
bool32 PokeRide_Start(u32 slot);
void PokeRide_Stop(void);
bool32 PokeRide_BeginSurf(u32 slot);
bool32 PokeRide_IsWaterMode(void);
bool32 PokeRide_HidesSurfBlob(void);
bool32 PokeRide_CanDismount(void);
bool32 PokeRide_IsWaterSpecies(u32 species);
bool32 PokeRide_IsActive(void);
bool32 PokeRide_IsValidSpecies(u32 species);
bool32 PokeRide_ProcessInput(void);
void PokeRide_ResetSprites(void);
void PokeRide_BeforeMovement(struct ObjectEvent *object, struct Sprite *sprite);
void PokeRide_AfterMovement(struct ObjectEvent *object, struct Sprite *sprite);
u16 PokeRide_PlayerGraphics(u32 gender);
#endif
