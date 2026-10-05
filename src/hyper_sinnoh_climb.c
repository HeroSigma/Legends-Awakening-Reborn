#include "global.h"
#include "fieldmap.h"
#include "hyper_sinnoh_climb.h"
#include "event_data.h"
#include "event_object_movement.h"
#include "pokemon.h"
#include "party_menu.h"
#include "constants/maps.h"
#include "constants/moves.h"
#include "constants/event_object_movement.h"

extern const u8 HyperSinnoh_RockClimb_SE[], HyperSinnoh_RockClimb_NW[], HyperSinnoh_RockClimb_NE[], HyperSinnoh_RockClimb_SW[];
struct AMapClimbRoute { u16 map; u8 localId; s16 x, y; u8 direction; const u8 *script; };
// Project-owned traversal recovered and runtime-tested in prior Legends Awakening.
// Source roots 098C3593/346C/3622/36AF. Only these verified NULL markers.
static const struct AMapClimbRoute sRoutes[] =
{
    {MAP_HYPERSINNOH_36_24_ROUTE_208, 9, 9, 11, DIR_EAST, HyperSinnoh_RockClimb_SE},
    {MAP_HYPERSINNOH_36_24_ROUTE_208, 14, 13, 15, DIR_WEST, HyperSinnoh_RockClimb_NW},
    {MAP_HYPERSINNOH_36_64_IRON_ISLAND, 3, 11, 21, DIR_EAST, HyperSinnoh_RockClimb_NE},
    {MAP_HYPERSINNOH_36_64_IRON_ISLAND, 4, 13, 19, DIR_WEST, HyperSinnoh_RockClimb_SW},
    {MAP_HYPERSINNOH_36_91_MT_CORONET, 1, 35, 13, DIR_EAST, HyperSinnoh_RockClimb_SE},
    {MAP_HYPERSINNOH_36_91_MT_CORONET, 4, 39, 17, DIR_WEST, HyperSinnoh_RockClimb_NW},
    {MAP_HYPERSINNOH_36_91_MT_CORONET, 5, 41, 26, DIR_EAST, HyperSinnoh_RockClimb_NE},
    {MAP_HYPERSINNOH_36_91_MT_CORONET, 6, 43, 24, DIR_WEST, HyperSinnoh_RockClimb_SW},
};

#include "hyper_sinnoh_vertical_climb.inc"

const u8 *HyperSinnoh_GetRockClimbInteraction(s16 x, s16 y, u8 direction)
{
    u32 i;
    const u8 *vertical = HyperSinnoh_GetVerticalClimbInteraction(x,y,direction);
    if (vertical != NULL)
        return vertical;
    for (i = 0; i < ARRAY_COUNT(sRoutes); i++)
    {
        const struct AMapClimbRoute *route = &sRoutes[i];
        s16 approachX = route->x + (route->direction == DIR_EAST ? -1 : 1);
        if (gSaveBlock1Ptr->location.mapGroup != MAP_GROUP(route->map)
         || gSaveBlock1Ptr->location.mapNum != MAP_NUM(route->map)
         || direction != route->direction || x != approachX + MAP_OFFSET || y != route->y + MAP_OFFSET)
            continue;
        return route->script;
    }
    return NULL;
}

// Keep destination move knowledge support and source-style learnability support.
// This is not a global mapping of Hyper's native address.
void HyperSinnoh_RockClimbSelectMon(void)
{
    u32 i;
    gSpecialVar_0x8004 = PARTY_SIZE;
    for (i = 0; i < PARTY_SIZE; i++)
    {
        struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][i];
        u16 species = GetMonData(mon, MON_DATA_SPECIES);
        if (species != SPECIES_NONE && !GetMonData(mon, MON_DATA_IS_EGG) && (MonKnowsMove(mon, MOVE_ROCK_CLIMB) || CanLearnTeachableMove(species, MOVE_ROCK_CLIMB)))
        {
            gSpecialVar_0x8004 = i;
            return;
        }
    }
}
