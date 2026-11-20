#include "global.h"
#include "field_name_box.h"
#include "constants/opponents.h"
#include "constants/speaker_names.h"
#include "legends_ashes.h"
#include "caps.h"
#include "event_data.h"
#include "event_object_movement.h"
#include "field_player_avatar.h"
#include "fieldmap.h"
#include "main.h"
#include "overworld.h"
#include "pokemon.h"
#include "palette.h"
#include "script.h"
#include "sprite.h"
#include "constants/event_objects.h"
#include "constants/event_object_movement.h"
#include "constants/flags.h"
#include "constants/maps.h"
#include "constants/vars.h"
#include "constants/map_types.h"
#define HOOPA_LOCAL_ID LA_HOOPA_LOCAL_ID
// Three completed player positions keep Hoopa behind the normal follower.
static EWRAM_DATA s16 sTrail[3][2] = {0};
static EWRAM_DATA u16 sTrailMap = 0;
static EWRAM_DATA u8 sTrailSteps = 0;
extern const u8 LegendsAshes_HoopaInteract[], LegendsAshes_HoopaJoin[], LegendsAshes_Lockdown[], LegendsAshes_AdminGate[];
bool32 LegendsAshes_IsSilph(void)
{
    u32 num = gSaveBlock1Ptr->location.mapNum;
    return gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_KANTOAR_1_47_SILPHCO_1F)
        && num >= MAP_NUM(MAP_KANTOAR_1_56_SILPHCO_10F)
        && num <= MAP_NUM(MAP_KANTOAR_1_55_SILPHCO_9F);
}
void LegendsAshes_SetGraphics(void)
{
    VarSet(VAR_OBJ_GFX_ID_D, GetGraphicsIdForMon(SPECIES_HOOPA, FALSE, FALSE));
    VarSet(VAR_OBJ_GFX_ID_E, GetGraphicsIdForMon(SPECIES_MEWTWO, FALSE, FALSE));
    VarSet(VAR_OBJ_GFX_ID_F, GetGraphicsIdForMon(SPECIES_KIRLIA, TRUE, FALSE));
}
void LegendsAshes_HoopaPrepare(void)
{
    gSpecialVar_Result = FlagGet(FLAG_LA_HOOPA_COMPANION)
        && !FlagGet(FLAG_LA_HOOPA_JOINED) && FlagGet(FLAG_LA_RED_DEX_GIFTS)
        && GetCurrentLevelCap() >= 50;
}
void LegendsAshes_HoopaGranted(void)
{
    if (gSpecialVar_Result < MON_CANT_GIVE) {
        FlagSet(FLAG_LA_HOOPA_JOINED);
        FlagClear(FLAG_LA_HOOPA_COMPANION);
    }
}
bool32 LegendsAshes_BlockWarp(const struct MapHeader *map, u32 warpId)
{
    if (!FlagGet(FLAG_LA_PAST_SAFFRON_ARRIVED) || FlagGet(FLAG_LA_WALLY_RESCUED)) return FALSE;
    if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_KANTOAR_3_10_SAFFRONCITY)
        && gSaveBlock1Ptr->location.mapNum == MAP_NUM(MAP_KANTOAR_3_10_SAFFRONCITY)
        && warpId != 0) {
        ScriptContext_SetupScript(LegendsAshes_Lockdown);
        return TRUE;
    }
    return FALSE;
}
void LegendsAshes_Update(void)
{
    u32 id, playerId = gPlayerAvatar.objectEventId;
    u16 map = (gSaveBlock1Ptr->location.mapGroup << 8) | gSaveBlock1Ptr->location.mapNum;
    struct ObjectEvent *obj, *player;
    if (playerId >= OBJECT_EVENTS_COUNT || !gObjectEvents[playerId].active) return;
    id = GetObjectEventIdByLocalIdAndMap(HOOPA_LOCAL_ID, gSaveBlock1Ptr->location.mapNum, gSaveBlock1Ptr->location.mapGroup);
    if (!FlagGet(FLAG_LA_HOOPA_COMPANION) || FlagGet(FLAG_LA_HOOPA_JOINED)) {
        if (id < OBJECT_EVENTS_COUNT) RemoveObjectEvent(&gObjectEvents[id]);
        sTrailMap = 0xFFFF;
        return;
    }
    // Hoopa is a story companion, never a hidden seventh party member.
    if (!ScriptContext_IsEnabled() && !ArePlayerFieldControlsLocked()
        && !gPaletteFade.active && FlagGet(FLAG_LA_RED_DEX_GIFTS)
        && GetCurrentLevelCap() >= 50 && !FlagGet(FLAG_LA_HOOPA_JOIN_PROMPTED)) {
        FlagSet(FLAG_LA_HOOPA_JOIN_PROMPTED);
        ScriptContext_SetupScript(LegendsAshes_HoopaJoin);
        return;
    }
    player = &gObjectEvents[playerId];
    if (sTrailMap != map || id >= OBJECT_EVENTS_COUNT) {
        sTrailMap = map; sTrailSteps = 0;
        for (u32 i=0;i<3;i++) {sTrail[i][0]=player->currentCoords.x;sTrail[i][1]=player->currentCoords.y;}
    }
    if (id >= OBJECT_EVENTS_COUNT) {
        if (ScriptContext_IsEnabled() || ArePlayerFieldControlsLocked()) return;
        struct ObjectEventTemplate template = {
            .localId = HOOPA_LOCAL_ID,
            .graphicsId = GetGraphicsIdForMon(SPECIES_HOOPA, FALSE, FALSE),
            .x = player->currentCoords.x - MAP_OFFSET, .y = player->currentCoords.y - MAP_OFFSET,
            .elevation = player->currentElevation, .movementType = MOVEMENT_TYPE_NONE,
            .script = LegendsAshes_HoopaInteract,
        };
        id = SpawnSpecialObjectEvent(&template);
        if (id >= OBJECT_EVENTS_COUNT) return; // Busy maps retry when a slot opens.
        gObjectEvents[id].invisible = TRUE;
    }
    obj=&gObjectEvents[id];
    if (ScriptContext_IsEnabled() || ArePlayerFieldControlsLocked() || gPaletteFade.active) return;
    if (gMapHeader.mapType == MAP_TYPE_UNDERWATER || TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_SURFING | PLAYER_AVATAR_FLAG_UNDERWATER)) {
        obj->invisible = TRUE; return;
    }
    if (player->currentCoords.x != sTrail[0][0] || player->currentCoords.y != sTrail[0][1]) {
        for (u32 i=2;i>0;i--) {sTrail[i][0]=sTrail[i-1][0];sTrail[i][1]=sTrail[i-1][1];}
        sTrail[0][0]=player->currentCoords.x;sTrail[0][1]=player->currentCoords.y;
        if (sTrailSteps < 3) sTrailSteps++;
    }
    if (sTrailSteps < 2) return;
    obj->invisible=FALSE;
    if (ObjectEventIsMovementOverridden(obj) && !ObjectEventClearHeldMovementIfFinished(obj)) return;
    s32 dx=sTrail[2][0]-obj->currentCoords.x, dy=sTrail[2][1]-obj->currentCoords.y;
    if (abs(dx)+abs(dy)>4) {
        MoveObjectEventToMapCoords(obj,sTrail[2][0],sTrail[2][1]);
        return;
    }
    u32 dir=dx<0?DIR_WEST:dx>0?DIR_EAST:dy<0?DIR_NORTH:DIR_SOUTH;
    if (dx || dy) ObjectEventSetHeldMovement(obj,GetWalkFastMovementAction(dir));
    else ObjectEventSetHeldMovement(obj,GetFaceDirectionMovementAction(player->facingDirection));
}

// Historical Rocket grunts retain private saved flags and use the native trainer pipeline.
extern const u8 LegendsAshes_Grunt_0[], LegendsAshes_Grunt_0_Battle[];
extern const u8 LegendsPastSilph_F2_NPC2[], LegendsPastSilph_F2_NPC2_Battle[];
extern const u8 LegendsAshes_Grunt_1[], LegendsAshes_Grunt_1_Battle[];
extern const u8 LegendsAshes_Grunt_2[], LegendsAshes_Grunt_2_Battle[];
extern const u8 LegendsPastSilph_F4_NPC1[], LegendsPastSilph_F4_NPC1_Battle[];
extern const u8 LegendsAshes_Grunt_3[], LegendsAshes_Grunt_3_Battle[];
extern const u8 LegendsPastSilph_F5_NPC4[], LegendsPastSilph_F5_NPC4_Battle[];
extern const u8 LegendsAshes_Grunt_4[], LegendsAshes_Grunt_4_Battle[];
extern const u8 LegendsPastSilph_F6_NPC9[], LegendsPastSilph_F6_NPC9_Battle[];
extern const u8 LegendsAshes_Grunt_5[], LegendsAshes_Grunt_5_Battle[];
extern const u8 LegendsPastSilph_F7_NPC3[], LegendsPastSilph_F7_NPC3_Battle[];
extern const u8 LegendsPastSilph_F7_NPC4[], LegendsPastSilph_F7_NPC4_Battle[];
extern const u8 LegendsAshes_Grunt_6[], LegendsAshes_Grunt_6_Battle[];
extern const u8 LegendsPastSilph_F8_NPC1[], LegendsPastSilph_F8_NPC1_Battle[];
extern const u8 LegendsAshes_Grunt_7[], LegendsAshes_Grunt_7_Battle[];
extern const u8 LegendsPastSilph_F9_NPC3[], LegendsPastSilph_F9_NPC3_Battle[];
extern const u8 LegendsPastSilph_F10_NPC2[], LegendsPastSilph_F10_NPC2_Battle[];
extern const u8 LegendsPastSilph_F11_NPC3[], LegendsPastSilph_F11_NPC3_Battle[];
extern const u8 LegendsPastSilph_F11_NPC5[], LegendsPastSilph_F11_NPC5_Battle[];
static const struct { const u8 *script; const u8 *battle; u16 flag; u8 profile; } sPastSilphGrunts[] = {
    {LegendsAshes_Grunt_0, LegendsAshes_Grunt_0_Battle, 0x290, 1},
    {LegendsPastSilph_F2_NPC2, LegendsPastSilph_F2_NPC2_Battle, 0x282, 13},
    {LegendsAshes_Grunt_1, LegendsAshes_Grunt_1_Battle, 0x291, 2},
    {LegendsAshes_Grunt_2, LegendsAshes_Grunt_2_Battle, 0x292, 3},
    {LegendsPastSilph_F4_NPC1, LegendsPastSilph_F4_NPC1_Battle, 0x285, 16},
    {LegendsAshes_Grunt_3, LegendsAshes_Grunt_3_Battle, 0x293, 4},
    {LegendsPastSilph_F5_NPC4, LegendsPastSilph_F5_NPC4_Battle, 0x289, 20},
    {LegendsAshes_Grunt_4, LegendsAshes_Grunt_4_Battle, 0x294, 5},
    {LegendsPastSilph_F6_NPC9, LegendsPastSilph_F6_NPC9_Battle, 0x28B, 22},
    {LegendsAshes_Grunt_5, LegendsAshes_Grunt_5_Battle, 0x295, 6},
    {LegendsPastSilph_F7_NPC3, LegendsPastSilph_F7_NPC3_Battle, 0x28C, 23},
    {LegendsPastSilph_F7_NPC4, LegendsPastSilph_F7_NPC4_Battle, 0x28D, 24},
    {LegendsAshes_Grunt_6, LegendsAshes_Grunt_6_Battle, 0x296, 7},
    {LegendsPastSilph_F8_NPC1, LegendsPastSilph_F8_NPC1_Battle, 0x28F, 26},
    {LegendsAshes_Grunt_7, LegendsAshes_Grunt_7_Battle, 0x297, 8},
    {LegendsPastSilph_F9_NPC3, LegendsPastSilph_F9_NPC3_Battle, 0x29A, 29},
    {LegendsPastSilph_F10_NPC2, LegendsPastSilph_F10_NPC2_Battle, 0x29C, 31},
    {LegendsPastSilph_F11_NPC3, LegendsPastSilph_F11_NPC3_Battle, 0x29D, 32},
    {LegendsPastSilph_F11_NPC5, LegendsPastSilph_F11_NPC5_Battle, 0x29E, 33},
};
bool32 LegendsAshes_GruntAlreadyDefeated(const u8 *script)
{
    if (!LegendsAshes_IsSilph())
        return FALSE;
    for (u32 i = 0; i < ARRAY_COUNT(sPastSilphGrunts); i++)
        if (script == sPastSilphGrunts[i].script)
            return FlagGet(sPastSilphGrunts[i].flag)
                || (VarGet(VAR_LA_SILPH_OPPONENT) == sPastSilphGrunts[i].profile
                    && FlagGet(TRAINER_FLAGS_START + TRAINER_GRUNT_UNUSED));
    return FALSE;
}
const u8 *LegendsAshes_PrepareGruntApproach(const u8 *script)
{
    if (!LegendsAshes_IsSilph())
        return NULL;
    for (u32 i = 0; i < ARRAY_COUNT(sPastSilphGrunts); i++)
        if (script == sPastSilphGrunts[i].script)
        {
            VarSet(VAR_LA_SILPH_OPPONENT, sPastSilphGrunts[i].profile);
            FlagClear(TRAINER_FLAGS_START + TRAINER_GRUNT_UNUSED);
            gSpeakerName = gSpeakerNamesTable[SP_NAME_TEAM_ROCKET];
            return sPastSilphGrunts[i].battle;
        }
    return NULL;
}
