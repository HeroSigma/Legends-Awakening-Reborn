// Ground-mount renderer adapted from Aio Silver/Lucky Capybara's EE-Ride-System.
// Native foot collisions, HM travel and avatar flags remain authoritative.
#include "global.h"
#include "pokeride.h"
#include "main.h"
#include "script.h"
#include "field_move.h"
#include "constants/field_move.h"
#include "follower_npc.h"
#include "pokemon.h"
#include "event_data.h"
#include "event_object_movement.h"
#include "field_player_avatar.h"
#include "overworld.h"
#include "sprite.h"
#include "sound.h"
#include "constants/event_objects.h"
#include "constants/event_object_movement.h"
#include "constants/songs.h"
#include "constants/flags.h"
#define POKERIDE_SPRITE_UP 0
#define POKERIDE_SPRITE_DOWN 1
#define POKERIDE_SPRITE_SIDE 2
#define POKERIDE_SPRITE_COUNT 3
#define POKERIDE_FLAG_NONE 0
#define POKERIDE_FLAG_CAN_RIDE (1 << 0)
#define POKERIDE_FLAG_CAN_SWIM (1 << 1)
#define POKERIDE_FLAG_CAN_CLIMB (1 << 2)
#define POKERIDE_FLAG_CAN_FLY (1 << 3)
struct PokeRideSpriteInfo { s8 playerY, monY, playerX; s8 monX:7; u8 playerRendersInFront:1; };
struct PokeRideInfo { struct PokeRideSpriteInfo spriteInfo[3]; u8 flags; };
#include "data/pokeride_info.h"
static EWRAM_DATA struct {
    u32 pid, ot;
    u16 species, gfx;
    u8 slot, sprite;
    bool8 active, hasSprite, waterMode, airMode;
    u8 airHeight;
} sRide = {0};

static const struct PokeRideInfo *RideInfo(u32 species)
{
    if (species == SPECIES_NONE || species >= NUM_SPECIES)
        return NULL;
    if (!(sPokeRideInfo[species].flags & POKERIDE_FLAG_CAN_RIDE))
        species = GET_BASE_SPECIES_ID(species);
    return &sPokeRideInfo[species];
}
bool32 PokeRide_IsValidSpecies(u32 species)
{
    const struct PokeRideInfo *info = RideInfo(species);
    return info != NULL && (info->flags & POKERIDE_FLAG_CAN_RIDE);
}
bool32 PokeRide_IsActive(void) { return sRide.active; }
bool32 __attribute__((noinline)) PokeRide_IsWaterMode(void) { return sRide.active && sRide.waterMode; }
bool32 PokeRide_HidesSurfBlob(void) { return PokeRide_IsWaterMode() && sRide.hasSprite; }
bool32 PokeRide_CanDismount(void)
{
    return !PokeRide_IsAirborne()
        && (!PokeRide_IsWaterMode() || !(gPlayerAvatar.flags & PLAYER_AVATAR_FLAG_SURFING));
}
bool32 PokeRide_IsWaterSpecies(u32 species)
{
    const struct PokeRideInfo *info = RideInfo(species);
    return info != NULL && (info->flags & POKERIDE_FLAG_CAN_SWIM);
}
u16 PokeRide_PlayerGraphics(u32 gender)
{
    if (PokeRide_IsWaterMode())
        return gender ? OBJ_EVENT_GFX_LA_MAY_WATER_RIDING : OBJ_EVENT_GFX_LA_BRENDAN_WATER_RIDING;
    return gender ? OBJ_EVENT_GFX_LA_MAY_RIDING : OBJ_EVENT_GFX_LA_BRENDAN_RIDING;
}
static struct Pokemon *CurrentRideMon(void)
{
    for (u32 i = 0; i < gPartiesCount[B_TRAINER_PLAYER]; i++)
    {
        struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][i];
        if (GetMonData(mon, MON_DATA_SPECIES) == sRide.species
         && GetMonData(mon, MON_DATA_PERSONALITY) == sRide.pid && GetMonData(mon, MON_DATA_OT_ID) == sRide.ot
         && GetMonData(mon, MON_DATA_HP) && !GetMonData(mon, MON_DATA_IS_EGG) && !mon->box.isBadEgg)
            return mon;
    }
    return NULL;
}
static bool32 RideMonPresent(void) { return CurrentRideMon() != NULL; }
bool32 PokeRide_IsAirSpecies(u32 species)
{
    const struct PokeRideInfo *info = RideInfo(species);
    return info != NULL && (info->flags & POKERIDE_FLAG_CAN_FLY);
}
bool32 PokeRide_CanFly(void)
{
    struct Pokemon *mon = CurrentRideMon();
    return sRide.active && mon != NULL && IsMapTypeOutdoors(gMapHeader.mapType)
        && IsFieldMoveUnlocked(FIELD_MOVE_FLY) && PokeRide_IsAirSpecies(sRide.species)
        && FieldMove_CanAssist(mon, FIELD_MOVE_FLY);
}
bool32 __attribute__((noinline)) PokeRide_IsAirborne(void)
{
    return sRide.active && (sRide.airMode || sRide.airHeight);
}
bool32 __attribute__((noinline)) PokeRide_ToggleFlight(void)
{
    if (!sRide.active)
        return FALSE;
    if (sRide.airMode)
    {
        sRide.airMode = FALSE;
        return TRUE;
    }
    if (!PokeRide_CanFly())
        return FALSE;
    sRide.airMode = TRUE;
    return TRUE;
}
static void FreeMountSprite(void)
{
    if (!sRide.hasSprite)
        return;
    struct Sprite *sprite = &gSprites[sRide.sprite];
    u32 palette = sprite->oam.paletteNum, tileStart = sprite->sheetTileStart;
    u16 palTag = GetSpritePaletteTagByPaletteNum(palette);
    u16 tileTag = GetSpriteTileTagByTileStart(tileStart);
    bool32 sharedPal = FALSE, sharedTiles = FALSE;
    for (u32 i = 0; i < MAX_SPRITES; i++)
        if (i != sRide.sprite && gSprites[i].inUse)
        {
            sharedPal |= gSprites[i].oam.paletteNum == palette;
            sharedTiles |= gSprites[i].usingSheet && gSprites[i].sheetTileStart == tileStart;
        }
    bool32 sheet = sprite->usingSheet;
    DestroySprite(sprite);
    if (!sharedPal && palTag != TAG_NONE)
        FreeSpritePaletteByTag(palTag);
    if (sheet && !sharedTiles && tileTag != TAG_NONE)
        FreeSpriteTilesByTag(tileTag);
    sRide.hasSprite = FALSE;
}
void PokeRide_Stop(void)
{
    if (!sRide.active)
        return;
    sRide.active = FALSE;
    sRide.waterMode = FALSE;
    sRide.airMode = FALSE;
    sRide.airHeight = 0;
    FreeMountSprite();
    if (gMain.callback2 == CB2_Overworld && gPlayerAvatar.objectEventId < OBJECT_EVENTS_COUNT)
    {
        struct ObjectEvent *player = &gObjectEvents[gPlayerAvatar.objectEventId];
        if (player->active && player->spriteId < MAX_SPRITES)
        {
            gSprites[player->spriteId].x2 = gSprites[player->spriteId].y2 = 0;
            u32 state = PLAYER_AVATAR_STATE_NORMAL;
            if (gPlayerAvatar.flags & PLAYER_AVATAR_FLAG_SURFING) state = PLAYER_AVATAR_STATE_SURFING;
            else if (gPlayerAvatar.flags & PLAYER_AVATAR_FLAG_UNDERWATER) state = PLAYER_AVATAR_STATE_UNDERWATER;
            else if (gPlayerAvatar.flags & PLAYER_AVATAR_FLAG_MACH_BIKE) state = PLAYER_AVATAR_STATE_MACH_BIKE;
            else if (gPlayerAvatar.flags & PLAYER_AVATAR_FLAG_ACRO_BIKE) state = PLAYER_AVATAR_STATE_ACRO_BIKE;
            ObjectEventSetGraphicsId(player, GetPlayerAvatarGraphicsIdByStateId(state));
        }
    }
}
void PokeRide_ResetSprites(void) { sRide.hasSprite = FALSE; }
bool32 PokeRide_Start(u32 slot)
{
    bool32 surfing = gPlayerAvatar.flags & PLAYER_AVATAR_FLAG_SURFING;
    if (gMain.inBattle || PokeRide_IsAirborne() || slot >= gPartiesCount[B_TRAINER_PLAYER] || !FlagGet(FLAG_SYS_B_DASH)
     || (!IsMapTypeOutdoors(gMapHeader.mapType) && !surfing) || PlayerHasFollowerNPC()
     || (gPlayerAvatar.flags & (PLAYER_AVATAR_FLAG_BIKE | PLAYER_AVATAR_FLAG_UNDERWATER)))
        return FALSE;
    struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][slot];
    u32 species = GetMonData(mon, MON_DATA_SPECIES);
    if (!PokeRide_IsValidSpecies(species) || !GetMonData(mon, MON_DATA_HP)
     || GetMonData(mon, MON_DATA_IS_EGG) || mon->box.isBadEgg)
        return FALSE;
    if (surfing && (!IsFieldMoveUnlocked(FIELD_MOVE_SURF) || !PokeRide_IsWaterSpecies(species)
        || !FieldMove_CanAssist(mon, FIELD_MOVE_SURF)))
        return FALSE;
    PokeRide_Stop();
    sRide.waterMode = surfing;
    sRide.pid = GetMonData(mon, MON_DATA_PERSONALITY);
    sRide.ot = GetMonData(mon, MON_DATA_OT_ID);
    sRide.species = species;
    sRide.slot = slot;
    sRide.gfx = GetGraphicsIdForMon(species, GetMonData(mon, MON_DATA_IS_SHINY), GetMonGender(mon) == MON_FEMALE);
    sRide.active = TRUE;
    return TRUE;
}
bool32 PokeRide_BeginSurf(u32 slot)
{
    if (!(gPlayerAvatar.flags & PLAYER_AVATAR_FLAG_SURFING))
        return FALSE;
    return PokeRide_Start(slot);
}
bool32 PokeRide_ProcessInput(void)
{
    if (sRide.active && ((JOY_NEW(L_BUTTON) && JOY_HELD(R_BUTTON))
        || (JOY_NEW(R_BUTTON) && JOY_HELD(L_BUTTON))))
    {
        if (PokeRide_CanDismount())
        {
            PokeRide_Stop();
            PlaySE(SE_SELECT);
        }
        else
            PlaySE(SE_WALL_HIT);
        return TRUE;
    }
    if (sRide.active && JOY_NEW(B_BUTTON) && PokeRide_IsAirSpecies(sRide.species))
    {
        PlaySE(PokeRide_ToggleFlight() ? SE_M_FLY : SE_WALL_HIT);
        return TRUE;
    }
    return FALSE;
}
void PokeRide_BeforeMovement(struct ObjectEvent *object, struct Sprite *sprite)
{
    if (sRide.active && object->isPlayer)
        sprite->x2 = sprite->y2 = 0;
}
void PokeRide_AfterMovement(struct ObjectEvent *object, struct Sprite *sprite)
{
    if (!sRide.active || !object->isPlayer)
        return;
    bool32 surfing = gPlayerAvatar.flags & PLAYER_AVATAR_FLAG_SURFING;
    if ((!IsMapTypeOutdoors(gMapHeader.mapType) && !surfing) || !RideMonPresent() || PlayerHasFollowerNPC()
     || (gPlayerAvatar.flags & (PLAYER_AVATAR_FLAG_BIKE | PLAYER_AVATAR_FLAG_UNDERWATER))
     || (!sRide.waterMode && (gPlayerAvatar.flags & PLAYER_AVATAR_FLAG_FORCED_MOVE))
     || (surfing && (!sRide.waterMode || !IsFieldMoveUnlocked(FIELD_MOVE_SURF) || !PokeRide_IsWaterSpecies(sRide.species))))
    {
        PokeRide_Stop();
        return;
    }
    // Let the native Surf entry/exit and scripted field-move poses finish.
    if (sRide.waterMode && (ScriptContext_IsEnabled() || gPlayerAvatar.preventStep))
        return;
    if (!sRide.waterMode && ScriptContext_IsEnabled())
    {
        PokeRide_Stop();
        return;
    }
    if (sRide.waterMode && !surfing)
        sRide.waterMode = FALSE;
    if (sRide.airMode && !PokeRide_CanFly())
        sRide.airMode = FALSE;
    if (sRide.airMode && sRide.airHeight < 12)
        sRide.airHeight++;
    else if (!sRide.airMode && sRide.airHeight)
        sRide.airHeight--;
    u16 gfx = PokeRide_PlayerGraphics(gPlayerAvatar.gender);
    if (object->graphicsId != gfx)
        ObjectEventSetGraphicsId(object, gfx);
    if (!sRide.hasSprite)
    {
        RemoveFollowingPokemon();
        u32 id = CreateObjectGraphicsSprite(sRide.gfx, SpriteCallbackDummy, sprite->x, sprite->y, sprite->subpriority);
        if (id >= MAX_SPRITES)
        {
            PokeRide_Stop();
            return;
        }
        sRide.sprite = id;
        sRide.hasSprite = TRUE;
        gSprites[id].coordOffsetEnabled = TRUE;
    }
    struct Sprite *mount = &gSprites[sRide.sprite];
    u32 dir = object->facingDirection;
    u32 pose = dir == DIR_NORTH ? POKERIDE_SPRITE_UP : dir == DIR_SOUTH ? POKERIDE_SPRITE_DOWN : POKERIDE_SPRITE_SIDE;
    const struct PokeRideSpriteInfo *offset = &RideInfo(sRide.species)->spriteInfo[pose];
    s32 flip = dir == DIR_WEST || dir == DIR_NORTHWEST || dir == DIR_SOUTHWEST ? -1 : 1;
    u32 animDir = pose == POKERIDE_SPRITE_SIDE ? (flip < 0 ? DIR_WEST : DIR_EAST) : dir;
    StartSpriteAnimIfDifferent(mount, (gPlayerAvatar.runningState == MOVING || PokeRide_IsAirborne() ? ANIM_STD_GO_SOUTH : ANIM_STD_FACE_SOUTH) + animDir - DIR_SOUTH);
    s32 bob = sRide.waterMode && ((gMain.vblankCounter1 >> 4) & 1) ? -1 : 0;
    mount->x = sprite->x; mount->y = sprite->y;
    mount->x2 = offset->monX * flip; mount->y2 = offset->monY + bob - sRide.airHeight;
    mount->oam.priority = sprite->oam.priority;
    // Reborn's follower art can overlap the seated head in the front pose.
    bool32 riderFront = offset->playerRendersInFront || pose == POKERIDE_SPRITE_DOWN;
    mount->subpriority = riderFront ? sprite->subpriority + 1 : (sprite->subpriority ? sprite->subpriority - 1 : 0);
    mount->invisible = sprite->invisible;
    sprite->x2 += offset->playerX * flip;
    sprite->y2 += offset->playerY + bob - sRide.airHeight;
}
