#include "global.h"
#include "pokemon_storage_system.h"
#include "la_pc_features.h"
#include "script.h"
#include "event_data.h"
#include "constants/battle_pyramid.h"
#include "constants/maps.h"
#include "constants/map_groups.h"
static const u16 sRetiredMaps[] = {
    MAP_FALLARBOR_TOWN_BATTLE_TENT_LOBBY,
    MAP_FALLARBOR_TOWN_BATTLE_TENT_CORRIDOR,
    MAP_FALLARBOR_TOWN_BATTLE_TENT_BATTLE_ROOM,
    MAP_VERDANTURF_TOWN_BATTLE_TENT_LOBBY,
    MAP_VERDANTURF_TOWN_BATTLE_TENT_CORRIDOR,
    MAP_VERDANTURF_TOWN_BATTLE_TENT_BATTLE_ROOM,
    MAP_SLATEPORT_CITY_BATTLE_TENT_LOBBY,
    MAP_SLATEPORT_CITY_BATTLE_TENT_CORRIDOR,
    MAP_SLATEPORT_CITY_BATTLE_TENT_BATTLE_ROOM,
    MAP_LILYCOVE_CITY_CONTEST_LOBBY,
    MAP_LILYCOVE_CITY_CONTEST_HALL,
    MAP_SECRET_BASE_RED_CAVE1,
    MAP_SECRET_BASE_BROWN_CAVE1,
    MAP_SECRET_BASE_BLUE_CAVE1,
    MAP_SECRET_BASE_YELLOW_CAVE1,
    MAP_SECRET_BASE_TREE1,
    MAP_SECRET_BASE_SHRUB1,
    MAP_SECRET_BASE_RED_CAVE2,
    MAP_SECRET_BASE_BROWN_CAVE2,
    MAP_SECRET_BASE_BLUE_CAVE2,
    MAP_SECRET_BASE_YELLOW_CAVE2,
    MAP_SECRET_BASE_TREE2,
    MAP_SECRET_BASE_SHRUB2,
    MAP_SECRET_BASE_RED_CAVE3,
    MAP_SECRET_BASE_BROWN_CAVE3,
    MAP_SECRET_BASE_BLUE_CAVE3,
    MAP_SECRET_BASE_YELLOW_CAVE3,
    MAP_SECRET_BASE_TREE3,
    MAP_SECRET_BASE_SHRUB3,
    MAP_SECRET_BASE_RED_CAVE4,
    MAP_SECRET_BASE_BROWN_CAVE4,
    MAP_SECRET_BASE_BLUE_CAVE4,
    MAP_SECRET_BASE_YELLOW_CAVE4,
    MAP_SECRET_BASE_TREE4,
    MAP_SECRET_BASE_SHRUB4,
    MAP_RECORD_CORNER,
    MAP_CONTEST_HALL,
    MAP_UNUSED_CONTEST_HALL1,
    MAP_UNUSED_CONTEST_HALL2,
    MAP_UNUSED_CONTEST_HALL3,
    MAP_UNUSED_CONTEST_HALL4,
    MAP_UNUSED_CONTEST_HALL5,
    MAP_UNUSED_CONTEST_HALL6,
    MAP_CONTEST_HALL_BEAUTY,
    MAP_CONTEST_HALL_TOUGH,
    MAP_CONTEST_HALL_COOL,
    MAP_CONTEST_HALL_SMART,
    MAP_CONTEST_HALL_CUTE,
    MAP_UNION_ROOM,
    MAP_BATTLE_FRONTIER_OUTSIDE_WEST,
    MAP_BATTLE_FRONTIER_BATTLE_TOWER_LOBBY,
    MAP_BATTLE_FRONTIER_BATTLE_TOWER_ELEVATOR,
    MAP_BATTLE_FRONTIER_BATTLE_TOWER_CORRIDOR,
    MAP_BATTLE_FRONTIER_BATTLE_TOWER_BATTLE_ROOM,
    MAP_BATTLE_FRONTIER_OUTSIDE_EAST,
    MAP_BATTLE_FRONTIER_BATTLE_TOWER_MULTI_PARTNER_ROOM,
    MAP_BATTLE_FRONTIER_BATTLE_TOWER_MULTI_CORRIDOR,
    MAP_BATTLE_FRONTIER_BATTLE_TOWER_MULTI_BATTLE_ROOM,
    MAP_BATTLE_FRONTIER_BATTLE_DOME_LOBBY,
    MAP_BATTLE_FRONTIER_BATTLE_DOME_CORRIDOR,
    MAP_BATTLE_FRONTIER_BATTLE_DOME_PRE_BATTLE_ROOM,
    MAP_BATTLE_FRONTIER_BATTLE_DOME_BATTLE_ROOM,
    MAP_BATTLE_FRONTIER_BATTLE_PALACE_LOBBY,
    MAP_BATTLE_FRONTIER_BATTLE_PALACE_CORRIDOR,
    MAP_BATTLE_FRONTIER_BATTLE_PALACE_BATTLE_ROOM,
    MAP_BATTLE_FRONTIER_BATTLE_PYRAMID_LOBBY,
    MAP_BATTLE_FRONTIER_BATTLE_PYRAMID_FLOOR,
    MAP_BATTLE_FRONTIER_BATTLE_PYRAMID_TOP,
    MAP_BATTLE_FRONTIER_BATTLE_ARENA_LOBBY,
    MAP_BATTLE_FRONTIER_BATTLE_ARENA_CORRIDOR,
    MAP_BATTLE_FRONTIER_BATTLE_ARENA_BATTLE_ROOM,
    MAP_BATTLE_FRONTIER_BATTLE_FACTORY_LOBBY,
    MAP_BATTLE_FRONTIER_BATTLE_FACTORY_PRE_BATTLE_ROOM,
    MAP_BATTLE_FRONTIER_BATTLE_FACTORY_BATTLE_ROOM,
    MAP_BATTLE_FRONTIER_BATTLE_PIKE_LOBBY,
    MAP_BATTLE_FRONTIER_BATTLE_PIKE_CORRIDOR,
    MAP_BATTLE_FRONTIER_BATTLE_PIKE_THREE_PATH_ROOM,
    MAP_BATTLE_FRONTIER_BATTLE_PIKE_ROOM_NORMAL,
    MAP_BATTLE_FRONTIER_BATTLE_PIKE_ROOM_FINAL,
    MAP_BATTLE_FRONTIER_BATTLE_PIKE_ROOM_WILD_MONS,
    MAP_BATTLE_FRONTIER_RANKING_HALL,
    MAP_BATTLE_FRONTIER_LOUNGE1,
    MAP_BATTLE_FRONTIER_EXCHANGE_SERVICE_CORNER,
    MAP_BATTLE_FRONTIER_LOUNGE2,
    MAP_BATTLE_FRONTIER_LOUNGE3,
    MAP_BATTLE_FRONTIER_LOUNGE4,
    MAP_BATTLE_FRONTIER_SCOTTS_HOUSE,
    MAP_BATTLE_FRONTIER_LOUNGE5,
    MAP_BATTLE_FRONTIER_LOUNGE6,
    MAP_BATTLE_FRONTIER_LOUNGE7,
    MAP_BATTLE_FRONTIER_RECEPTION_GATE,
    MAP_BATTLE_FRONTIER_LOUNGE8,
    MAP_BATTLE_FRONTIER_LOUNGE9,
    MAP_BATTLE_FRONTIER_POKEMON_CENTER_1F,
    MAP_BATTLE_FRONTIER_POKEMON_CENTER_2F,
    MAP_BATTLE_FRONTIER_MART,
    MAP_TRAINER_HILL_ENTRANCE,
    MAP_TRAINER_HILL_1F,
    MAP_TRAINER_HILL_2F,
    MAP_TRAINER_HILL_3F,
    MAP_TRAINER_HILL_4F,
    MAP_TRAINER_HILL_ROOF,
    MAP_TRAINER_HILL_ELEVATOR,
    MAP_RECORD_CORNER_FRLG,
    MAP_UNION_ROOM_FRLG,
    MAP_KANTOAR_0_2_RECORDCORNER,
    MAP_KANTOAR_0_4_UNIONROOM,
    MAP_HNS_REGION_GATE_ROUTE40_TRAINERHILL_COURTYARD,
    MAP_HNS_REGION_SLATEPORTCITY_BATTLETENTLOBBY,
    MAP_HNS_REGION_SLATEPORTCITY_BATTLETENTCORRIDOR,
    MAP_HNS_REGION_SLATEPORTCITY_BATTLETENTBATTLEROOM,
    MAP_HNS_REGION_VERDANTURFTOWN_BATTLETENTLOBBY,
    MAP_HNS_REGION_VERDANTURFTOWN_BATTLETENTCORRIDOR,
    MAP_HNS_REGION_VERDANTURFTOWN_BATTLETENTBATTLEROOM,
    MAP_HNS_REGION_FALLARBORTOWN_BATTLETENTLOBBY,
    MAP_HNS_REGION_FALLARBORTOWN_BATTLETENTCORRIDOR,
    MAP_HNS_REGION_FALLARBORTOWN_BATTLETENTBATTLEROOM,
    MAP_HNS_REGION_NATIONALPARK_BUGCONTEST,
    MAP_HNS_REGION_UNIONROOM,
    MAP_HNS_REGION_TRAINERHILL_COURTYARD,
    MAP_HNS_REGION_TRAINERHILL_ENTRANCE,
    MAP_HNS_REGION_TRAINERHILL_1F,
    MAP_HNS_REGION_TRAINERHILL_2F,
    MAP_HNS_REGION_TRAINERHILL_3F,
    MAP_HNS_REGION_TRAINERHILL_4F,
    MAP_HNS_REGION_TRAINERHILL_ROOF,
    MAP_HNS_REGION_TRAINERHILL_ELEVATOR,
    MAP_HNS_REGION_BATTLEFRONTIER_OUTSIDEWEST,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLETOWERLOBBY,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLETOWERELEVATOR,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLETOWERCORRIDOR,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLETOWERBATTLEROOM,
    MAP_HNS_REGION_BATTLEFRONTIER_OUTSIDEEAST,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLETOWERMULTIPARTNERROOM,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLETOWERMULTICORRIDOR,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLETOWERMULTIBATTLEROOM,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEDOMELOBBY,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEDOMECORRIDOR,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEDOMEPREBATTLEROOM,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEDOMEBATTLEROOM,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPALACELOBBY,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPALACECORRIDOR,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPALACEBATTLEROOM,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPYRAMIDLOBBY,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPYRAMIDFLOOR,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPYRAMIDTOP,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEARENALOBBY,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEARENACORRIDOR,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEARENABATTLEROOM,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEFACTORYLOBBY,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEFACTORYPREBATTLEROOM,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEFACTORYBATTLEROOM,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPIKELOBBY,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPIKECORRIDOR,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPIKETHREEPATHROOM,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPIKEROOMNORMAL,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPIKEROOMFINAL,
    MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPIKEROOMWILDMONS,
    MAP_HNS_REGION_BATTLEFRONTIER_RANKINGHALL,
    MAP_HNS_REGION_BATTLEFRONTIER_LOUNGE1,
    MAP_HNS_REGION_BATTLEFRONTIER_EXCHANGESERVICECORNER,
    MAP_HNS_REGION_BATTLEFRONTIER_LOUNGE2,
    MAP_HNS_REGION_BATTLEFRONTIER_LOUNGE3,
    MAP_HNS_REGION_BATTLEFRONTIER_LOUNGE4,
    MAP_HNS_REGION_BATTLEFRONTIER_SCOTTSHOUSE,
    MAP_HNS_REGION_BATTLEFRONTIER_LOUNGE5,
    MAP_HNS_REGION_BATTLEFRONTIER_LOUNGE6,
    MAP_HNS_REGION_BATTLEFRONTIER_LOUNGE7,
    MAP_HNS_REGION_BATTLEFRONTIER_RECEPTIONGATE,
    MAP_HNS_REGION_BATTLEFRONTIER_LOUNGE8,
    MAP_HNS_REGION_BATTLEFRONTIER_LOUNGE9,
    MAP_HNS_REGION_BATTLEFRONTIER_POKEMONCENTER_1F,
    MAP_HNS_REGION_BATTLEFRONTIER_POKEMONCENTER_2F,
    MAP_HNS_REGION_BATTLEFRONTIER_MART,
    MAP_HNS_REGION_CONTESTHALL,
    MAP_HNS_REGION_CONTESTHALLBEAUTY,
    MAP_HNS_REGION_CONTESTHALLCOOL,
    MAP_HNS_REGION_CONTESTHALLCUTE,
    MAP_HNS_REGION_CONTESTHALLSMART,
    MAP_HNS_REGION_CONTESTHALLTOUGH,
    MAP_HNS_REGION_LILYCOVECITY_CONTESTHALL,
    MAP_HNS_REGION_LILYCOVECITY_CONTESTLOBBY,
    MAP_HNS_REGION_UNUSEDCONTESTHALL1,
    MAP_HNS_REGION_UNUSEDCONTESTHALL2,
    MAP_HNS_REGION_UNUSEDCONTESTHALL3,
    MAP_HNS_REGION_UNUSEDCONTESTHALL4,
    MAP_HNS_REGION_UNUSEDCONTESTHALL5,
    MAP_HNS_REGION_UNUSEDCONTESTHALL6,
};
bool32 LaPcRetiredMap(u32 group, u32 num)
{
    u32 i;
    for(i=0;i<ARRAY_COUNT(sRetiredMaps);i++)
        if(MAP_GROUP(sRetiredMaps[i])==group && MAP_NUM(sRetiredMaps[i])==num) return TRUE;
    return FALSE;
}
// BEGIN NAMED COLLECTION SPECIAL GATES
extern const u8 SPECIAL_SetPlayerSecretBase[];
extern const u8 SPECIAL_CheckPlayerHasSecretBase[];
extern const u8 SPECIAL_EnterSecretBase[];
extern const u8 SPECIAL_ClearAndLeaveSecretBase[];
extern const u8 SPECIAL_MoveOutOfSecretBase[];
extern const u8 SPECIAL_IsCurSecretBaseOwnedByAnotherPlayer[];
extern const u8 SPECIAL_GetCurSecretBaseRegistrationValidity[];
extern const u8 SPECIAL_ToggleCurSecretBaseRegistry[];
extern const u8 SPECIAL_ShowSecretBaseDecorationMenu[];
extern const u8 SPECIAL_ShowSecretBaseRegistryMenu[];
extern const u8 SPECIAL_PrepSecretBaseBattleFlags[];
extern const u8 SPECIAL_GetSecretBaseOwnerAndState[];
extern const u8 SPECIAL_InitSecretBaseDecorationSprites[];
extern const u8 SPECIAL_SetDecoration[];
extern const u8 SPECIAL_GetSecretBaseTypeInFrontOfPlayer[];
extern const u8 SPECIAL_SetSecretBaseOwnerGfxId[];
extern const u8 SPECIAL_PutAwayDecorationIteration[];
extern const u8 SPECIAL_EnterNewlyCreatedSecretBase[];
extern const u8 SPECIAL_DoSecretBasePCTurnOffEffect[];
extern const u8 SPECIAL_RecordMixingPlayerSpotTriggered[];
extern const u8 SPECIAL_TryRecordMixLinkup[];
extern const u8 SPECIAL_TryBerryBlenderLinkup[];
extern const u8 SPECIAL_SetContestCategoryStringVarForInterview[];
extern const u8 SPECIAL_GetContestWinnerId[];
extern const u8 SPECIAL_GetContestPlayerId[];
extern const u8 SPECIAL_GetNpcContestantLocalId[];
extern const u8 SPECIAL_BufferContestWinnerTrainerName[];
extern const u8 SPECIAL_BufferContestWinnerMonName[];
extern const u8 SPECIAL_BufferContestTrainerAndMonNames[];
extern const u8 SPECIAL_GetContestMonConditionRanking[];
extern const u8 SPECIAL_SetContestTrainerGfxIds[];
extern const u8 SPECIAL_TryEnterContestMon[];
extern const u8 SPECIAL_GetContestantNamesAtRank[];
extern const u8 SPECIAL_SetLinkContestPlayerGfx[];
extern const u8 SPECIAL_GetContestMonCondition[];
extern const u8 SPECIAL_HasMonWonThisContestBefore[];
extern const u8 SPECIAL_GiveMonContestRibbon[];
extern const u8 SPECIAL_IsContestDebugActive[];
extern const u8 SPECIAL_TryContestGModeLinkup[];
extern const u8 SPECIAL_TraderMenuGetDecoration[];
extern const u8 SPECIAL_DoesPlayerHaveNoDecorations[];
extern const u8 SPECIAL_IsDecorationCategoryFull[];
extern const u8 SPECIAL_TraderShowDecorationMenu[];
extern const u8 SPECIAL_TraderDoDecorationTrade[];
extern const u8 SPECIAL_ShouldReadyContestArtist[];
extern const u8 SPECIAL_SaveMuseumContestPainting[];
extern const u8 SPECIAL_DoesContestCategoryHaveMuseumPainting[];
extern const u8 SPECIAL_ShowContestPainting[];
extern const u8 SPECIAL_ShowLinkBattleRecords[];
extern const u8 SPECIAL_CallBattleTowerFunc[];
extern const u8 SPECIAL_CallBattleDomeFunction[];
extern const u8 SPECIAL_CallBattlePalaceFunction[];
extern const u8 SPECIAL_CallBattleArenaFunction[];
extern const u8 SPECIAL_CallBattleFactoryFunction[];
extern const u8 SPECIAL_CallBattlePikeFunction[];
extern const u8 SPECIAL_CallBattlePyramidFunction[];
extern const u8 SPECIAL_ChoosePartyForBattleFrontier[];
extern const u8 SPECIAL_GetBattleTowerSinglesStreak[];
extern const u8 SPECIAL_ShowBerryBlenderRecordWindow[];
extern const u8 SPECIAL_GetSecretBaseNearbyMapName[];
extern const u8 SPECIAL_DoContestHallWarp[];
extern const u8 SPECIAL_CopyCurSecretBaseOwnerName_StrVar1[];
extern const u8 SPECIAL_InteractWithShieldOrTVDecoration[];
extern const u8 SPECIAL_ShowContestEntryMonPic[];
extern const u8 SPECIAL_HideContestEntryMonPic[];
extern const u8 SPECIAL_GetContestMultiplayerId[];
extern const u8 SPECIAL_TryInitBattleTowerAwardManObjectEvent[];
extern const u8 SPECIAL_MoveOutOfSecretBaseFromOutside[];
extern const u8 SPECIAL_TryHideBattleTowerReporter[];
extern const u8 SPECIAL_GenerateContestRand[];
extern const u8 SPECIAL_InitSecretBaseVars[];
extern const u8 SPECIAL_DeclinedSecretBaseBattle[];
extern const u8 SPECIAL_DrewSecretBaseBattle[];
extern const u8 SPECIAL_WonSecretBaseBattle[];
extern const u8 SPECIAL_LostSecretBaseBattle[];
extern const u8 SPECIAL_GetMysteryGiftCardStat[];
extern const u8 SPECIAL_ShouldContestLadyShowGoOnAir[];
extern const u8 SPECIAL_HasPlayerGivenContestLadyPokeblock[];
extern const u8 SPECIAL_Script_BufferContestLadyCategoryAndMonName[];
extern const u8 SPECIAL_OpenPokeblockCaseForContestLady[];
extern const u8 SPECIAL_SetContestLadyGivenPokeblock[];
extern const u8 SPECIAL_GetContestLadyMonSpecies[];
extern const u8 SPECIAL_GetContestLadyCategory[];
extern const u8 SPECIAL_PutLilycoveContestLadyShowOnTheAir[];
extern const u8 SPECIAL_CloseBattlePikeCurtain[];
extern const u8 SPECIAL_RunUnionRoom[];
extern const u8 SPECIAL_Script_ResetUnionRoomTrade[];
extern const u8 SPECIAL_IsPokemonJumpSpeciesInParty[];
extern const u8 SPECIAL_ShowPokemonJumpRecords[];
extern const u8 SPECIAL_ShowDodrioBerryPickingRecords[];
extern const u8 SPECIAL_LinkContestWaitForConnection[];
extern const u8 SPECIAL_LinkContestTryShowWirelessIndicator[];
extern const u8 SPECIAL_LinkContestTryHideWirelessIndicator[];
extern const u8 SPECIAL_IsWirelessContest[];
extern const u8 SPECIAL_IsContestWithRSPlayer[];
extern const u8 SPECIAL_ClearLinkContestFlags[];
extern const u8 SPECIAL_TryContestEModeLinkup[];
extern const u8 SPECIAL_BufferBattleTowerElevatorFloors[];
extern const u8 SPECIAL_DoBattlePyramidMonsHaveHeldItem[];
extern const u8 SPECIAL_BattlePyramidChooseMonHeldItems[];
extern const u8 SPECIAL_SetBattleTowerLinkPlayerGfx[];
extern const u8 SPECIAL_BufferBattleFrontierTutorMoveName[];
extern const u8 SPECIAL_CloseBattleFrontierTutorWindow[];
extern const u8 SPECIAL_SaveForBattleTowerLink[];
extern const u8 SPECIAL_LinkRetireStatusWithBattleTowerPartner[];
extern const u8 SPECIAL_BattleTowerReconnectLink[];
extern const u8 SPECIAL_CallTrainerHillFunction[];
extern const u8 SPECIAL_ShowBerryCrushRankings[];
extern const u8 SPECIAL_GetBattlePyramidHint[];
extern const u8 SPECIAL_LoadLinkContestPlayerPalettes[];
extern const u8 SPECIAL_ShowTrainerHillRecords[];
extern const u8 SPECIAL_TrySetBattleTowerLinkType[];
static const u32 sRetiredSpecials[] = {
    (u32)SPECIAL_SetPlayerSecretBase,
    (u32)SPECIAL_CheckPlayerHasSecretBase,
    (u32)SPECIAL_EnterSecretBase,
    (u32)SPECIAL_ClearAndLeaveSecretBase,
    (u32)SPECIAL_MoveOutOfSecretBase,
    (u32)SPECIAL_IsCurSecretBaseOwnedByAnotherPlayer,
    (u32)SPECIAL_GetCurSecretBaseRegistrationValidity,
    (u32)SPECIAL_ToggleCurSecretBaseRegistry,
    (u32)SPECIAL_ShowSecretBaseDecorationMenu,
    (u32)SPECIAL_ShowSecretBaseRegistryMenu,
    (u32)SPECIAL_PrepSecretBaseBattleFlags,
    (u32)SPECIAL_GetSecretBaseOwnerAndState,
    (u32)SPECIAL_InitSecretBaseDecorationSprites,
    (u32)SPECIAL_SetDecoration,
    (u32)SPECIAL_GetSecretBaseTypeInFrontOfPlayer,
    (u32)SPECIAL_SetSecretBaseOwnerGfxId,
    (u32)SPECIAL_PutAwayDecorationIteration,
    (u32)SPECIAL_EnterNewlyCreatedSecretBase,
    (u32)SPECIAL_DoSecretBasePCTurnOffEffect,
    (u32)SPECIAL_RecordMixingPlayerSpotTriggered,
    (u32)SPECIAL_TryRecordMixLinkup,
    (u32)SPECIAL_TryBerryBlenderLinkup,
    (u32)SPECIAL_SetContestCategoryStringVarForInterview,
    (u32)SPECIAL_GetContestWinnerId,
    (u32)SPECIAL_GetContestPlayerId,
    (u32)SPECIAL_GetNpcContestantLocalId,
    (u32)SPECIAL_BufferContestWinnerTrainerName,
    (u32)SPECIAL_BufferContestWinnerMonName,
    (u32)SPECIAL_BufferContestTrainerAndMonNames,
    (u32)SPECIAL_GetContestMonConditionRanking,
    (u32)SPECIAL_SetContestTrainerGfxIds,
    (u32)SPECIAL_TryEnterContestMon,
    (u32)SPECIAL_GetContestantNamesAtRank,
    (u32)SPECIAL_SetLinkContestPlayerGfx,
    (u32)SPECIAL_GetContestMonCondition,
    (u32)SPECIAL_HasMonWonThisContestBefore,
    (u32)SPECIAL_GiveMonContestRibbon,
    (u32)SPECIAL_IsContestDebugActive,
    (u32)SPECIAL_TryContestGModeLinkup,
    (u32)SPECIAL_TraderMenuGetDecoration,
    (u32)SPECIAL_DoesPlayerHaveNoDecorations,
    (u32)SPECIAL_IsDecorationCategoryFull,
    (u32)SPECIAL_TraderShowDecorationMenu,
    (u32)SPECIAL_TraderDoDecorationTrade,
    (u32)SPECIAL_ShouldReadyContestArtist,
    (u32)SPECIAL_SaveMuseumContestPainting,
    (u32)SPECIAL_DoesContestCategoryHaveMuseumPainting,
    (u32)SPECIAL_ShowContestPainting,
    (u32)SPECIAL_ShowLinkBattleRecords,
    (u32)SPECIAL_CallBattleTowerFunc,
    (u32)SPECIAL_CallBattleDomeFunction,
    (u32)SPECIAL_CallBattlePalaceFunction,
    (u32)SPECIAL_CallBattleArenaFunction,
    (u32)SPECIAL_CallBattleFactoryFunction,
    (u32)SPECIAL_CallBattlePikeFunction,
    (u32)SPECIAL_CallBattlePyramidFunction,
    (u32)SPECIAL_ChoosePartyForBattleFrontier,
    (u32)SPECIAL_GetBattleTowerSinglesStreak,
    (u32)SPECIAL_ShowBerryBlenderRecordWindow,
    (u32)SPECIAL_GetSecretBaseNearbyMapName,
    (u32)SPECIAL_DoContestHallWarp,
    (u32)SPECIAL_CopyCurSecretBaseOwnerName_StrVar1,
    (u32)SPECIAL_InteractWithShieldOrTVDecoration,
    (u32)SPECIAL_ShowContestEntryMonPic,
    (u32)SPECIAL_HideContestEntryMonPic,
    (u32)SPECIAL_GetContestMultiplayerId,
    (u32)SPECIAL_TryInitBattleTowerAwardManObjectEvent,
    (u32)SPECIAL_MoveOutOfSecretBaseFromOutside,
    (u32)SPECIAL_TryHideBattleTowerReporter,
    (u32)SPECIAL_GenerateContestRand,
    (u32)SPECIAL_InitSecretBaseVars,
    (u32)SPECIAL_DeclinedSecretBaseBattle,
    (u32)SPECIAL_DrewSecretBaseBattle,
    (u32)SPECIAL_WonSecretBaseBattle,
    (u32)SPECIAL_LostSecretBaseBattle,
    (u32)SPECIAL_GetMysteryGiftCardStat,
    (u32)SPECIAL_ShouldContestLadyShowGoOnAir,
    (u32)SPECIAL_HasPlayerGivenContestLadyPokeblock,
    (u32)SPECIAL_Script_BufferContestLadyCategoryAndMonName,
    (u32)SPECIAL_OpenPokeblockCaseForContestLady,
    (u32)SPECIAL_SetContestLadyGivenPokeblock,
    (u32)SPECIAL_GetContestLadyMonSpecies,
    (u32)SPECIAL_GetContestLadyCategory,
    (u32)SPECIAL_PutLilycoveContestLadyShowOnTheAir,
    (u32)SPECIAL_CloseBattlePikeCurtain,
    (u32)SPECIAL_RunUnionRoom,
    (u32)SPECIAL_Script_ResetUnionRoomTrade,
    (u32)SPECIAL_IsPokemonJumpSpeciesInParty,
    (u32)SPECIAL_ShowPokemonJumpRecords,
    (u32)SPECIAL_ShowDodrioBerryPickingRecords,
    (u32)SPECIAL_LinkContestWaitForConnection,
    (u32)SPECIAL_LinkContestTryShowWirelessIndicator,
    (u32)SPECIAL_LinkContestTryHideWirelessIndicator,
    (u32)SPECIAL_IsWirelessContest,
    (u32)SPECIAL_IsContestWithRSPlayer,
    (u32)SPECIAL_ClearLinkContestFlags,
    (u32)SPECIAL_TryContestEModeLinkup,
    (u32)SPECIAL_BufferBattleTowerElevatorFloors,
    (u32)SPECIAL_DoBattlePyramidMonsHaveHeldItem,
    (u32)SPECIAL_BattlePyramidChooseMonHeldItems,
    (u32)SPECIAL_SetBattleTowerLinkPlayerGfx,
    (u32)SPECIAL_BufferBattleFrontierTutorMoveName,
    (u32)SPECIAL_CloseBattleFrontierTutorWindow,
    (u32)SPECIAL_SaveForBattleTowerLink,
    (u32)SPECIAL_LinkRetireStatusWithBattleTowerPartner,
    (u32)SPECIAL_BattleTowerReconnectLink,
    (u32)SPECIAL_CallTrainerHillFunction,
    (u32)SPECIAL_ShowBerryCrushRankings,
    (u32)SPECIAL_GetBattlePyramidHint,
    (u32)SPECIAL_LoadLinkContestPlayerPalettes,
    (u32)SPECIAL_ShowTrainerHillRecords,
    (u32)SPECIAL_TrySetBattleTowerLinkType,
};
bool32 LaPcBlockedSpecial(u32 id)
{
    if (!StorageIsCollectionMode()) return FALSE;
    // Ordinary pickups query their location before closing the item header.
    if (id == (u32)SPECIAL_CallBattlePyramidFunction
        && gSpecialVar_0x8004 == BATTLE_PYRAMID_FUNC_CURRENT_LOCATION) return FALSE;
    for (u32 i=0;i<ARRAY_COUNT(sRetiredSpecials);i++)
        if (id==sRetiredSpecials[i]) return TRUE;
    return FALSE;
}
// END NAMED COLLECTION SPECIAL GATES
bool32 LaPcBlockWarp(const struct MapHeader *map, s32 warpId)
{
    const struct WarpEvent *warp;
    if(!StorageIsCollectionMode() || warpId<0 || warpId>=map->events->warpCount) return FALSE;
    warp=&map->events->warps[warpId];
    if(!LaPcRetiredMap(warp->mapGroup,warp->mapNum)) return FALSE;
    ScriptContext_SetupScript(LaCollection_Blocked);
    return TRUE;
}
