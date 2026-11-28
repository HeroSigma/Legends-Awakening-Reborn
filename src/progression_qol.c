#include "global.h"
#include "progression_qol.h"
#include "pokemon.h"
#include "event_data.h"
#include "item.h"
#include "constants/flags.h"
bool32 StrangeBall_CanCatch(enum Species species)
{
    if (species == SPECIES_NONE || species >= NUM_SPECIES) return FALSE;
    return gSpeciesInfo[species].isRestrictedLegendary
        || gSpeciesInfo[species].isSubLegendary
        || gSpeciesInfo[species].isMythical;
}
bool32 MasterBall_IsUnlocked(void) {return FlagGet(FLAG_SYS_GAME_CLEAR);}
void ProgressionQol_EnsureExpShare(void)
{
    // Only newly granted copies default to ON. Preserve existing OFF choices.
    if (!CheckBagHasItem(ITEM_EXP_SHARE,1))
    {
        if (!AddBagItem(ITEM_EXP_SHARE,1)) return;
        FlagSet(I_EXP_SHARE_FLAG);
    }
    FlagSet(FLAG_RECEIVED_EXP_SHARE);
}
