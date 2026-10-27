#ifndef GUARD_LEGENDS_TERA_H
#define GUARD_LEGENDS_TERA_H
#include "pokemon.h"
bool32 LegendsTeraUnlocked(void);
u16 LegendsShardForType(u32 type);
u16 LegendsChooseWildHeldItem(u16 species);
void LegendsAwardWildShards(void);
void LegendsAwardCaughtShard(u16 species, u16 partyIndex);
void LegendsPrepareTeraChange(void);
void LegendsCommitTeraChange(void);
#endif
