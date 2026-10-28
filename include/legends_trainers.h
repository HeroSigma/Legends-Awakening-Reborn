#ifndef GUARD_LEGENDS_TRAINERS_H
#define GUARD_LEGENDS_TRAINERS_H
#include "data.h"
bool32 LegendsTrainer_MoveLegal(u32 species, u32 level, u32 move);
bool32 LegendsTrainer_MemberLegal(const struct TrainerMon *mon);
u32 LegendsTrainer_Gimmick(u32 trainerId);
#endif
