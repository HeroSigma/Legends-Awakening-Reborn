// Party-menu selection inspired by Kasenn's toggle_follower_from_party_menu.
// Identity keys follow party reordering without extending the save structures.
#include "global.h"
#include "preferred_follower.h"
#include "event_data.h"
#include "pokemon.h"
#define FOLLOW_SELECTED 0xA701
#define FOLLOW_RECALLED 0xA702

bool32 PreferredFollower_Set(u32 slot)
{
    if (slot >= gPartiesCount[B_TRAINER_PLAYER])
        return FALSE;
    struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][slot];
    if (!GetMonData(mon, MON_DATA_SPECIES) || GetMonData(mon, MON_DATA_IS_EGG)
     || GetMonData(mon, MON_DATA_SANITY_IS_BAD_EGG) || !GetMonData(mon, MON_DATA_HP))
        return FALSE;
    u32 personality = GetMonData(mon, MON_DATA_PERSONALITY);
    u32 ot = GetMonData(mon, MON_DATA_OT_ID);
    VarSet(VAR_LA_FOLLOWER_PID_LO, personality);
    VarSet(VAR_LA_FOLLOWER_PID_HI, personality >> 16);
    VarSet(VAR_LA_FOLLOWER_OT_LO, ot);
    VarSet(VAR_LA_FOLLOWER_OT_HI, ot >> 16);
    VarSet(VAR_LA_FOLLOWER_MODE, FOLLOW_SELECTED);
    return TRUE;
}
void PreferredFollower_Recall(void) { VarSet(VAR_LA_FOLLOWER_MODE, FOLLOW_RECALLED); }
void PreferredFollower_Automatic(void) { VarSet(VAR_LA_FOLLOWER_MODE, 0); }
bool32 PreferredFollower_IsRecalled(void) { return VarGet(VAR_LA_FOLLOWER_MODE) == FOLLOW_RECALLED; }
struct Pokemon *PreferredFollower_Get(void)
{
    if (VarGet(VAR_LA_FOLLOWER_MODE) != FOLLOW_SELECTED)
        return NULL;
    u32 pid = VarGet(VAR_LA_FOLLOWER_PID_LO) | ((u32)VarGet(VAR_LA_FOLLOWER_PID_HI) << 16);
    u32 ot = VarGet(VAR_LA_FOLLOWER_OT_LO) | ((u32)VarGet(VAR_LA_FOLLOWER_OT_HI) << 16);
    for (u32 i = 0; i < gPartiesCount[B_TRAINER_PLAYER]; i++)
    {
        struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][i];
        if (GetMonData(mon, MON_DATA_SPECIES) && GetMonData(mon, MON_DATA_PERSONALITY) == pid
         && GetMonData(mon, MON_DATA_OT_ID) == ot)
            return mon;
    }
    return NULL;
}
