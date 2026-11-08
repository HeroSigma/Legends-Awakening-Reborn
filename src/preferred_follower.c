// Party-menu selection inspired by Kasenn's toggle_follower_from_party_menu.
// Identity keys follow party reordering without extending the save structures.
#include "global.h"
#include "preferred_follower.h"
#include "event_data.h"
#include "pokemon.h"
#define FOLLOW_SELECTED 0xA710
#define FOLLOW_LEGACY 0xA701
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
    VarSet(VAR_LA_FOLLOWER_SPECIES, GetMonData(mon, MON_DATA_SPECIES));
    VarSet(VAR_LA_FOLLOWER_MODE, FOLLOW_SELECTED + slot);
    return TRUE;
}
void PreferredFollower_Recall(void) { VarSet(VAR_LA_FOLLOWER_MODE, FOLLOW_RECALLED); }
void PreferredFollower_Automatic(void) { VarSet(VAR_LA_FOLLOWER_MODE, 0); }
bool32 PreferredFollower_IsRecalled(void) { return VarGet(VAR_LA_FOLLOWER_MODE) == FOLLOW_RECALLED; }
static bool32 MatchesIdentity(struct Pokemon *mon, u32 pid, u32 ot)
{
    return GetMonData(mon, MON_DATA_SPECIES) != SPECIES_NONE
        && GetMonData(mon, MON_DATA_PERSONALITY) == pid
        && GetMonData(mon, MON_DATA_OT_ID) == ot;
}
struct Pokemon *PreferredFollower_Get(void)
{
    u32 mode = VarGet(VAR_LA_FOLLOWER_MODE);
    if (mode != FOLLOW_LEGACY && (mode < FOLLOW_SELECTED || mode >= FOLLOW_SELECTED + PARTY_SIZE))
        return NULL;
    u32 pid = VarGet(VAR_LA_FOLLOWER_PID_LO) | ((u32)VarGet(VAR_LA_FOLLOWER_PID_HI) << 16);
    u32 ot = VarGet(VAR_LA_FOLLOWER_OT_LO) | ((u32)VarGet(VAR_LA_FOLLOWER_OT_HI) << 16);
    u32 species = mode == FOLLOW_LEGACY ? SPECIES_NONE : VarGet(VAR_LA_FOLLOWER_SPECIES);
    u32 slot = mode - FOLLOW_SELECTED;
    struct Pokemon *unique = NULL;
    u32 count = 0;
    // Compact storage/debug specimens may share PID and OT. Prefer the selected
    // slot when it still matches, then search by species after party reordering.
    if (slot < gPartiesCount[B_TRAINER_PLAYER])
    {
        struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][slot];
        if (MatchesIdentity(mon, pid, ot) && GetMonData(mon, MON_DATA_SPECIES) == species)
            return mon;
    }
    for (u32 i = 0; i < gPartiesCount[B_TRAINER_PLAYER]; i++)
    {
        struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][i];
        if (!MatchesIdentity(mon, pid, ot))
            continue;
        unique = mon;
        count++;
        if (species != SPECIES_NONE && GetMonData(mon, MON_DATA_SPECIES) == species)
            return mon;
    }
    // A unique identity still follows after evolution. Never guess between
    // several colliding identities if the selected species has left the party.
    if (count == 1)
    {
        if (mode == FOLLOW_LEGACY)
            return unique;
        u32 evolved = GetMonData(unique, MON_DATA_SPECIES);
        for (u32 i = 0; i < 3 && evolved != SPECIES_NONE; i++)
        {
            evolved = GetSpeciesPreEvolution(evolved);
            if (evolved == species)
                return unique;
        }
    }
    return NULL;
}
