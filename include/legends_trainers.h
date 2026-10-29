#ifndef GUARD_LEGENDS_TRAINERS_H
#define GUARD_LEGENDS_TRAINERS_H
#include "data.h"
bool32 LegendsTrainer_MoveLegal(u32 species, u32 level, u32 move);
bool32 LegendsTrainer_MemberLegal(const struct TrainerMon *mon);
u32 LegendsTrainer_Gimmick(u32 trainerId);
bool32 LegendsTrainer_HasProfile(u32 trainerId);
bool32 LegendsTrainer_IsFormatChoice(u32 trainerId);
u32 LegendsTrainer_PlayerLevel(void);
u32 LegendsTrainer_ScaledLevel(u32 authoredLevel);
void LegendsTrainer_PrepareFormat(void);
void LegendsTrainer_SelectFormat(void);
#endif
