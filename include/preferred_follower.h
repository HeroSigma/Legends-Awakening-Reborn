#ifndef GUARD_PREFERRED_FOLLOWER_H
#define GUARD_PREFERRED_FOLLOWER_H
#include "global.h"
struct Pokemon;
bool32 PreferredFollower_Set(u32 slot);
void PreferredFollower_Recall(void);
void PreferredFollower_Automatic(void);
bool32 PreferredFollower_IsRecalled(void);
struct Pokemon *PreferredFollower_Get(void);
#endif
