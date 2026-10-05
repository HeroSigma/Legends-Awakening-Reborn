#include "fieldmap.h"

// Whether a palette has a night version, located at ((x + 9) % 16).pal
#define SWAP_PAL(x) ((x) < NUM_PALS_IN_PRIMARY ? 1 << (x) : 1 << ((x) - NUM_PALS_IN_PRIMARY))

const struct Tileset gTileset_SecretBase =
{
    .isCompressed = FALSE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_SecretBase,
    .palettes = gTilesetPalettes_SecretBase,
    .metatiles = gMetatiles_SecretBasePrimary,
    .metatileAttributes = gMetatileAttributes_SecretBasePrimary,
    .callback = NULL,
};

const struct Tileset gTileset_SecretBaseRedCave =
{
    .isCompressed = FALSE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SecretBaseRedCave,
    .palettes = gTilesetPalettes_SecretBaseRedCave,
    .metatiles = gMetatiles_SecretBaseSecondary,
    .metatileAttributes = gMetatileAttributes_SecretBaseSecondary,
    .callback = NULL,
};

const struct Tileset *const gTilesetPointer_SecretBase = &gTileset_SecretBase;
const struct Tileset *const gTilesetPointer_SecretBaseRedCave = &gTileset_SecretBaseRedCave;

#if !IS_FRLG

const struct Tileset gTileset_General =
{
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_General,
    .palettes = gTilesetPalettes_General,
    .metatiles = gMetatiles_General,
    .metatileAttributes = gMetatileAttributes_General,
    .callback = InitTilesetAnim_General,
};

const struct Tileset gTileset_Petalburg =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Petalburg,
    .palettes = gTilesetPalettes_Petalburg,
    .metatiles = gMetatiles_Petalburg,
    .metatileAttributes = gMetatileAttributes_Petalburg,
    .callback = InitTilesetAnim_Petalburg,
};

const struct Tileset gTileset_Rustboro =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Rustboro,
    .palettes = gTilesetPalettes_Rustboro,
    .metatiles = gMetatiles_Rustboro,
    .metatileAttributes = gMetatileAttributes_Rustboro,
    .callback = InitTilesetAnim_Rustboro,
};

const struct Tileset gTileset_Dewford =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Dewford,
    .palettes = gTilesetPalettes_Dewford,
    .metatiles = gMetatiles_Dewford,
    .metatileAttributes = gMetatileAttributes_Dewford,
    .callback = InitTilesetAnim_Dewford,
};

const struct Tileset gTileset_Slateport =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Slateport,
    .palettes = gTilesetPalettes_Slateport,
    .metatiles = gMetatiles_Slateport,
    .metatileAttributes = gMetatileAttributes_Slateport,
    .callback = InitTilesetAnim_Slateport,
};

const struct Tileset gTileset_Mauville =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Mauville,
    .palettes = gTilesetPalettes_Mauville,
    .metatiles = gMetatiles_Mauville,
    .metatileAttributes = gMetatileAttributes_Mauville,
    .callback = InitTilesetAnim_Mauville,
};

const struct Tileset gTileset_Lavaridge =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Lavaridge,
    .palettes = gTilesetPalettes_Lavaridge,
    .metatiles = gMetatiles_Lavaridge,
    .metatileAttributes = gMetatileAttributes_Lavaridge,
    .callback = InitTilesetAnim_Lavaridge,
};

const struct Tileset gTileset_Fallarbor =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Fallarbor,
    .palettes = gTilesetPalettes_Fallarbor,
    .metatiles = gMetatiles_Fallarbor,
    .metatileAttributes = gMetatileAttributes_Fallarbor,
    .callback = InitTilesetAnim_Fallarbor,
};

const struct Tileset gTileset_Fortree =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Fortree,
    .palettes = gTilesetPalettes_Fortree,
    .metatiles = gMetatiles_Fortree,
    .metatileAttributes = gMetatileAttributes_Fortree,
    .callback = InitTilesetAnim_Fortree,
};

const struct Tileset gTileset_Lilycove =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Lilycove,
    .palettes = gTilesetPalettes_Lilycove,
    .metatiles = gMetatiles_Lilycove,
    .metatileAttributes = gMetatileAttributes_Lilycove,
    .callback = InitTilesetAnim_Lilycove,
};

const struct Tileset gTileset_Mossdeep =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Mossdeep,
    .palettes = gTilesetPalettes_Mossdeep,
    .metatiles = gMetatiles_Mossdeep,
    .metatileAttributes = gMetatileAttributes_Mossdeep,
    .callback = InitTilesetAnim_Mossdeep,
};

const struct Tileset gTileset_EverGrande =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_EverGrande,
    .palettes = gTilesetPalettes_EverGrande,
    .metatiles = gMetatiles_EverGrande,
    .metatileAttributes = gMetatileAttributes_EverGrande,
    .callback = InitTilesetAnim_EverGrande,
};

const struct Tileset gTileset_Pacifidlog =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Pacifidlog,
    .palettes = gTilesetPalettes_Pacifidlog,
    .metatiles = gMetatiles_Pacifidlog,
    .metatileAttributes = gMetatileAttributes_Pacifidlog,
    .callback = InitTilesetAnim_Pacifidlog,
};

const struct Tileset gTileset_Sootopolis =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Sootopolis,
    .palettes = gTilesetPalettes_Sootopolis,
    .metatiles = gMetatiles_Sootopolis,
    .metatileAttributes = gMetatileAttributes_Sootopolis,
    .callback = InitTilesetAnim_Sootopolis,
};

const struct Tileset gTileset_BattleFrontierOutsideWest =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BattleFrontierOutsideWest,
    .palettes = gTilesetPalettes_BattleFrontierOutsideWest,
    .metatiles = gMetatiles_BattleFrontierOutsideWest,
    .metatileAttributes = gMetatileAttributes_BattleFrontierOutsideWest,
    .callback = InitTilesetAnim_BattleFrontierOutsideWest,
};

const struct Tileset gTileset_BattleFrontierOutsideEast =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BattleFrontierOutsideEast,
    .palettes = gTilesetPalettes_BattleFrontierOutsideEast,
    .metatiles = gMetatiles_BattleFrontierOutsideEast,
    .metatileAttributes = gMetatileAttributes_BattleFrontierOutsideEast,
    .callback = InitTilesetAnim_BattleFrontierOutsideEast,
};

const struct Tileset gTileset_Building =
{
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_InsideBuilding,
    .palettes = gTilesetPalettes_InsideBuilding,
    .metatiles = gMetatiles_InsideBuilding,
    .metatileAttributes = gMetatileAttributes_InsideBuilding,
    .callback = InitTilesetAnim_Building,
};

const struct Tileset gTileset_Shop =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Shop,
    .palettes = gTilesetPalettes_Shop,
    .metatiles = gMetatiles_Shop,
    .metatileAttributes = gMetatileAttributes_Shop,
    .callback = NULL,
};

const struct Tileset gTileset_PokemonCenter =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PokemonCenter,
    .palettes = gTilesetPalettes_PokemonCenter,
    .metatiles = gMetatiles_PokemonCenter,
    .metatileAttributes = gMetatileAttributes_PokemonCenter,
    .callback = NULL,
};

const struct Tileset gTileset_Cave =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Cave,
    .palettes = gTilesetPalettes_Cave,
    .metatiles = gMetatiles_Cave,
    .metatileAttributes = gMetatileAttributes_Cave,
    .callback = InitTilesetAnim_Cave,
};

const struct Tileset gTileset_PokemonSchool =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PokemonSchool,
    .palettes = gTilesetPalettes_PokemonSchool,
    .metatiles = gMetatiles_PokemonSchool,
    .metatileAttributes = gMetatileAttributes_PokemonSchool,
    .callback = NULL,
};

const struct Tileset gTileset_PokemonFanClub =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PokemonFanClub,
    .palettes = gTilesetPalettes_PokemonFanClub,
    .metatiles = gMetatiles_PokemonFanClub,
    .metatileAttributes = gMetatileAttributes_PokemonFanClub,
    .callback = NULL,
};

const struct Tileset gTileset_Unused1 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Unused1,
    .palettes = gTilesetPalettes_Unused1,
    .metatiles = gMetatiles_Unused1,
    .metatileAttributes = gMetatileAttributes_Unused1,
    .callback = NULL,
};

const struct Tileset gTileset_MeteorFalls =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_MeteorFalls,
    .palettes = gTilesetPalettes_MeteorFalls,
    .metatiles = gMetatiles_MeteorFalls,
    .metatileAttributes = gMetatileAttributes_MeteorFalls,
    .callback = NULL,
};

const struct Tileset gTileset_OceanicMuseum =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_OceanicMuseum,
    .palettes = gTilesetPalettes_OceanicMuseum,
    .metatiles = gMetatiles_OceanicMuseum,
    .metatileAttributes = gMetatileAttributes_OceanicMuseum,
    .callback = NULL,
};

const struct Tileset gTileset_CableClub =
{
    .isCompressed = FALSE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_CableClub,
    .palettes = gTilesetPalettes_CableClub,
    .metatiles = gMetatiles_CableClub,
    .metatileAttributes = gMetatileAttributes_CableClub,
    .callback = NULL,
};

const struct Tileset gTileset_SeashoreHouse =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SeashoreHouse,
    .palettes = gTilesetPalettes_SeashoreHouse,
    .metatiles = gMetatiles_SeashoreHouse,
    .metatileAttributes = gMetatileAttributes_SeashoreHouse,
    .callback = NULL,
};

const struct Tileset gTileset_PrettyPetalFlowerShop =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PrettyPetalFlowerShop,
    .palettes = gTilesetPalettes_PrettyPetalFlowerShop,
    .metatiles = gMetatiles_PrettyPetalFlowerShop,
    .metatileAttributes = gMetatileAttributes_PrettyPetalFlowerShop,
    .callback = NULL,
};

const struct Tileset gTileset_PokemonDayCare =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PokemonDayCare,
    .palettes = gTilesetPalettes_PokemonDayCare,
    .metatiles = gMetatiles_PokemonDayCare,
    .metatileAttributes = gMetatileAttributes_PokemonDayCare,
    .callback = NULL,
};

const struct Tileset gTileset_Facility =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Facility,
    .palettes = gTilesetPalettes_Facility,
    .metatiles = gMetatiles_Facility,
    .metatileAttributes = gMetatileAttributes_Facility,
    .callback = NULL,
};

const struct Tileset gTileset_BikeShop =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BikeShop,
    .palettes = gTilesetPalettes_BikeShop,
    .metatiles = gMetatiles_BikeShop,
    .metatileAttributes = gMetatileAttributes_BikeShop,
    .callback = InitTilesetAnim_BikeShop,
};

const struct Tileset gTileset_RusturfTunnel =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_RusturfTunnel,
    .palettes = gTilesetPalettes_RusturfTunnel,
    .metatiles = gMetatiles_RusturfTunnel,
    .metatileAttributes = gMetatileAttributes_RusturfTunnel,
    .callback = NULL,
};

const struct Tileset gTileset_SecretBaseBrownCave =
{
    .isCompressed = FALSE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SecretBaseBrownCave,
    .palettes = gTilesetPalettes_SecretBaseBrownCave,
    .metatiles = gMetatiles_SecretBaseSecondary,
    .metatileAttributes = gMetatileAttributes_SecretBaseSecondary,
    .callback = NULL,
};

const struct Tileset gTileset_SecretBaseTree =
{
    .isCompressed = FALSE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SecretBaseTree,
    .palettes = gTilesetPalettes_SecretBaseTree,
    .metatiles = gMetatiles_SecretBaseSecondary,
    .metatileAttributes = gMetatileAttributes_SecretBaseSecondary,
    .callback = NULL,
};

const struct Tileset gTileset_SecretBaseShrub =
{
    .isCompressed = FALSE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SecretBaseShrub,
    .palettes = gTilesetPalettes_SecretBaseShrub,
    .metatiles = gMetatiles_SecretBaseSecondary,
    .metatileAttributes = gMetatileAttributes_SecretBaseSecondary,
    .callback = NULL,
};

const struct Tileset gTileset_SecretBaseBlueCave =
{
    .isCompressed = FALSE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SecretBaseBlueCave,
    .palettes = gTilesetPalettes_SecretBaseBlueCave,
    .metatiles = gMetatiles_SecretBaseSecondary,
    .metatileAttributes = gMetatileAttributes_SecretBaseSecondary,
    .callback = NULL,
};

const struct Tileset gTileset_SecretBaseYellowCave =
{
    .isCompressed = FALSE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SecretBaseYellowCave,
    .palettes = gTilesetPalettes_SecretBaseYellowCave,
    .metatiles = gMetatiles_SecretBaseSecondary,
    .metatileAttributes = gMetatileAttributes_SecretBaseSecondary,
    .callback = NULL,
};

const struct Tileset gTileset_InsideOfTruck =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_InsideOfTruck,
    .palettes = gTilesetPalettes_InsideOfTruck,
    .metatiles = gMetatiles_InsideOfTruck,
    .metatileAttributes = gMetatileAttributes_InsideOfTruck,
    .callback = NULL,
};

const struct Tileset gTileset_Unused2 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Unused2,
    .palettes = gTilesetPalettes_Unused2,
    .metatiles = gMetatiles_Unused2,
    .metatileAttributes = gMetatileAttributes_Unused2,
    .callback = NULL,
};

const struct Tileset gTileset_Contest =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Contest,
    .palettes = gTilesetPalettes_Contest,
    .metatiles = gMetatiles_Contest,
    .metatileAttributes = gMetatileAttributes_Contest,
    .callback = NULL,
};

const struct Tileset gTileset_LilycoveMuseum =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_LilycoveMuseum,
    .palettes = gTilesetPalettes_LilycoveMuseum,
    .metatiles = gMetatiles_LilycoveMuseum,
    .metatileAttributes = gMetatileAttributes_LilycoveMuseum,
    .callback = NULL,
};

const struct Tileset gTileset_BrendansMaysHouse =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BrendansMaysHouse,
    .palettes = gTilesetPalettes_BrendansMaysHouse,
    .metatiles = gMetatiles_BrendansMaysHouse,
    .metatileAttributes = gMetatileAttributes_BrendansMaysHouse,
    .callback = NULL,
};

const struct Tileset gTileset_Lab =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Lab,
    .palettes = gTilesetPalettes_Lab,
    .metatiles = gMetatiles_Lab,
    .metatileAttributes = gMetatileAttributes_Lab,
    .callback = NULL,
};

const struct Tileset gTileset_Underwater =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Underwater,
    .palettes = gTilesetPalettes_Underwater,
    .metatiles = gMetatiles_Underwater,
    .metatileAttributes = gMetatileAttributes_Underwater,
    .callback = InitTilesetAnim_Underwater,
};

const struct Tileset gTileset_PetalburgGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PetalburgGym,
    .palettes = gTilesetPalettes_PetalburgGym,
    .metatiles = gMetatiles_PetalburgGym,
    .metatileAttributes = gMetatileAttributes_PetalburgGym,
    .callback = NULL,
};

const struct Tileset gTileset_SootopolisGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SootopolisGym,
    .palettes = gTilesetPalettes_SootopolisGym,
    .metatiles = gMetatiles_SootopolisGym,
    .metatileAttributes = gMetatileAttributes_SootopolisGym,
    .callback = InitTilesetAnim_SootopolisGym,
};

const struct Tileset gTileset_GenericBuilding =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_GenericBuilding,
    .palettes = gTilesetPalettes_GenericBuilding,
    .metatiles = gMetatiles_GenericBuilding,
    .metatileAttributes = gMetatileAttributes_GenericBuilding,
    .callback = NULL,
};

const struct Tileset gTileset_MauvilleGameCorner =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_MauvilleGameCorner,
    .palettes = gTilesetPalettes_MauvilleGameCorner,
    .metatiles = gMetatiles_MauvilleGameCorner,
    .metatileAttributes = gMetatileAttributes_MauvilleGameCorner,
    .callback = NULL,
};

const struct Tileset gTileset_RustboroGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_RustboroGym,
    .palettes = gTilesetPalettes_RustboroGym,
    .metatiles = gMetatiles_RustboroGym,
    .metatileAttributes = gMetatileAttributes_RustboroGym,
    .callback = NULL,
};

const struct Tileset gTileset_DewfordGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_DewfordGym,
    .palettes = gTilesetPalettes_DewfordGym,
    .metatiles = gMetatiles_DewfordGym,
    .metatileAttributes = gMetatileAttributes_DewfordGym,
    .callback = NULL,
};

const struct Tileset gTileset_MauvilleGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_MauvilleGym,
    .palettes = gTilesetPalettes_MauvilleGym,
    .metatiles = gMetatiles_MauvilleGym,
    .metatileAttributes = gMetatileAttributes_MauvilleGym,
    .callback = InitTilesetAnim_MauvilleGym,
};

const struct Tileset gTileset_LavaridgeGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_LavaridgeGym,
    .palettes = gTilesetPalettes_LavaridgeGym,
    .metatiles = gMetatiles_LavaridgeGym,
    .metatileAttributes = gMetatileAttributes_LavaridgeGym,
    .callback = NULL,
};

const struct Tileset gTileset_TrickHousePuzzle =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_TrickHousePuzzle,
    .palettes = gTilesetPalettes_TrickHousePuzzle,
    .metatiles = gMetatiles_TrickHousePuzzle,
    .metatileAttributes = gMetatileAttributes_TrickHousePuzzle,
    .callback = NULL,
};

const struct Tileset gTileset_FortreeGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_FortreeGym,
    .palettes = gTilesetPalettes_FortreeGym,
    .metatiles = gMetatiles_FortreeGym,
    .metatileAttributes = gMetatileAttributes_FortreeGym,
    .callback = NULL,
};

const struct Tileset gTileset_MossdeepGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_MossdeepGym,
    .palettes = gTilesetPalettes_MossdeepGym,
    .metatiles = gMetatiles_MossdeepGym,
    .metatileAttributes = gMetatileAttributes_MossdeepGym,
    .callback = NULL,
};

const struct Tileset gTileset_InsideShip =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_InsideShip,
    .palettes = gTilesetPalettes_InsideShip,
    .metatiles = gMetatiles_InsideShip,
    .metatileAttributes = gMetatileAttributes_InsideShip,
    .callback = NULL,
};

const struct Tileset gTileset_EliteFour =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_EliteFour,
    .palettes = gTilesetPalettes_EliteFour,
    .metatiles = gMetatiles_EliteFour,
    .metatileAttributes = gMetatileAttributes_EliteFour,
    .callback = InitTilesetAnim_EliteFour,
};

const struct Tileset gTileset_BattleFrontier =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BattleFrontier,
    .palettes = gTilesetPalettes_BattleFrontier,
    .metatiles = gMetatiles_BattleFrontier,
    .metatileAttributes = gMetatileAttributes_BattleFrontier,
    .callback = NULL,
};

const struct Tileset gTileset_BattlePalace =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BattlePalace,
    .palettes = gTilesetPalettes_BattlePalace,
    .metatiles = gMetatiles_BattlePalace,
    .metatileAttributes = gMetatileAttributes_BattlePalace,
    .callback = NULL,
};

const struct Tileset gTileset_BattleDome =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BattleDome,
    .palettes = gTilesetPalettes_BattleDome,
    .metatiles = gMetatiles_BattleDome,
    .metatileAttributes = gMetatileAttributes_BattleDome,
    .callback = InitTilesetAnim_BattleDome,
};

const struct Tileset gTileset_BattleFactory =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BattleFactory,
    .palettes = gTilesetPalettes_BattleFactory,
    .metatiles = gMetatiles_BattleFactory,
    .metatileAttributes = gMetatileAttributes_BattleFactory,
    .callback = NULL,
};

const struct Tileset gTileset_BattlePike =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BattlePike,
    .palettes = gTilesetPalettes_BattlePike,
    .metatiles = gMetatiles_BattlePike,
    .metatileAttributes = gMetatileAttributes_BattlePike,
    .callback = NULL,
};

const struct Tileset gTileset_BattleArena =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BattleArena,
    .palettes = gTilesetPalettes_BattleArena,
    .metatiles = gMetatiles_BattleArena,
    .metatileAttributes = gMetatileAttributes_BattleArena,
    .callback = NULL,
};

const struct Tileset gTileset_BattlePyramid =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BattlePyramid,
    .palettes = gTilesetPalettes_BattlePyramid,
    .metatiles = gMetatiles_BattlePyramid,
    .metatileAttributes = gMetatileAttributes_BattlePyramid,
    .callback = InitTilesetAnim_BattlePyramid,
};

const struct Tileset gTileset_MirageTower =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_MirageTower,
    .palettes = gTilesetPalettes_MirageTower,
    .metatiles = gMetatiles_MirageTower,
    .metatileAttributes = gMetatileAttributes_MirageTower,
    .callback = NULL,
};

const struct Tileset gTileset_MossdeepGameCorner =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_MossdeepGameCorner,
    .palettes = gTilesetPalettes_MossdeepGameCorner,
    .metatiles = gMetatiles_MossdeepGameCorner,
    .metatileAttributes = gMetatileAttributes_MossdeepGameCorner,
    .callback = NULL,
};

const struct Tileset gTileset_IslandHarbor =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_IslandHarbor,
    .palettes = gTilesetPalettes_IslandHarbor,
    .metatiles = gMetatiles_IslandHarbor,
    .metatileAttributes = gMetatileAttributes_IslandHarbor,
    .callback = NULL,
};

const struct Tileset gTileset_TrainerHill =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_TrainerHill,
    .palettes = gTilesetPalettes_TrainerHill,
    .metatiles = gMetatiles_TrainerHill,
    .metatileAttributes = gMetatileAttributes_TrainerHill,
    .callback = NULL,
};

const struct Tileset gTileset_NavelRock =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_NavelRock,
    .palettes = gTilesetPalettes_NavelRock,
    .metatiles = gMetatiles_NavelRock,
    .metatileAttributes = gMetatileAttributes_NavelRock,
    .callback = NULL,
};

const struct Tileset gTileset_BattleFrontierRankingHall =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BattleFrontierRankingHall,
    .palettes = gTilesetPalettes_BattleFrontierRankingHall,
    .metatiles = gMetatiles_BattleFrontierRankingHall,
    .metatileAttributes = gMetatileAttributes_BattleFrontierRankingHall,
    .callback = NULL,
};

const struct Tileset gTileset_BattleTent =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BattleTent,
    .palettes = gTilesetPalettes_BattleTent,
    .metatiles = gMetatiles_BattleTent,
    .metatileAttributes = gMetatileAttributes_BattleTent,
    .callback = NULL,
};

const struct Tileset gTileset_MysteryEventsHouse =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_MysteryEventsHouse,
    .palettes = gTilesetPalettes_MysteryEventsHouse,
    .metatiles = gMetatiles_MysteryEventsHouse,
    .metatileAttributes = gMetatileAttributes_MysteryEventsHouse,
    .callback = NULL,
};

const struct Tileset gTileset_UnionRoom =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_UnionRoom,
    .palettes = gTilesetPalettes_UnionRoom,
    .metatiles = gMetatiles_UnionRoom,
    .metatileAttributes = gMetatileAttributes_UnionRoom,
    .callback = NULL,
};

#else

// FRLG tilesets
const struct Tileset gTileset_BuildingFrlg =
{
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Building_Frlg,
    .palettes = gTilesetPalettes_Building_Frlg,
    .metatiles = gMetatiles_Building_Frlg,
    .metatileAttributes = gMetatileAttributes_Building_Frlg,
    .callback = NULL,
};

const struct Tileset gTileset_General_Frlg =
{
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_General_Frlg,
    .palettes = gTilesetPalettes_General_Frlg,
    .metatiles = gMetatiles_General_Frlg,
    .metatileAttributes = gMetatileAttributes_General_Frlg,
    .callback = InitTilesetAnim_General_Frlg,
};

const struct Tileset gTileset_PalletTown =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PalletTown,
    .palettes = gTilesetPalettes_PalletTown,
    .metatiles = gMetatiles_PalletTown,
    .metatileAttributes = gMetatileAttributes_PalletTown,
    .callback = NULL,
};

const struct Tileset gTileset_ViridianCity =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_ViridianCity,
    .palettes = gTilesetPalettes_ViridianCity,
    .metatiles = gMetatiles_ViridianCity,
    .metatileAttributes = gMetatileAttributes_ViridianCity,
    .callback = NULL,
};

const struct Tileset gTileset_PewterCity =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PewterCity,
    .palettes = gTilesetPalettes_PewterCity,
    .metatiles = gMetatiles_PewterCity,
    .metatileAttributes = gMetatileAttributes_PewterCity,
    .callback = NULL,
};

const struct Tileset gTileset_CeruleanCity =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_CeruleanCity,
    .palettes = gTilesetPalettes_CeruleanCity,
    .metatiles = gMetatiles_CeruleanCity,
    .metatileAttributes = gMetatileAttributes_CeruleanCity,
    .callback = NULL,
};

const struct Tileset gTileset_LavenderTown =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_LavenderTown,
    .palettes = gTilesetPalettes_LavenderTown,
    .metatiles = gMetatiles_LavenderTown,
    .metatileAttributes = gMetatileAttributes_LavenderTown,
    .callback = NULL,
};

const struct Tileset gTileset_VermilionCity =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_VermilionCity,
    .palettes = gTilesetPalettes_VermilionCity,
    .metatiles = gMetatiles_VermilionCity,
    .metatileAttributes = gMetatileAttributes_VermilionCity,
    .callback = NULL,
};

const struct Tileset gTileset_CeladonCity =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_CeladonCity,
    .palettes = gTilesetPalettes_CeladonCity,
    .metatiles = gMetatiles_CeladonCity,
    .metatileAttributes = gMetatileAttributes_CeladonCity,
    .callback = InitTilesetAnim_CeladonCity,
};

const struct Tileset gTileset_FuchsiaCity =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_FuchsiaCity,
    .palettes = gTilesetPalettes_FuchsiaCity,
    .metatiles = gMetatiles_FuchsiaCity,
    .metatileAttributes = gMetatileAttributes_FuchsiaCity,
    .callback = NULL,
};

const struct Tileset gTileset_CinnabarIsland =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_CinnabarIsland,
    .palettes = gTilesetPalettes_CinnabarIsland,
    .metatiles = gMetatiles_CinnabarIsland,
    .metatileAttributes = gMetatileAttributes_CinnabarIsland,
    .callback = NULL,
};

const struct Tileset gTileset_IndigoPlateau =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_IndigoPlateau,
    .palettes = gTilesetPalettes_IndigoPlateau,
    .metatiles = gMetatiles_IndigoPlateau,
    .metatileAttributes = gMetatileAttributes_IndigoPlateau,
    .callback = NULL,
};

const struct Tileset gTileset_SaffronCity =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SaffronCity,
    .palettes = gTilesetPalettes_SaffronCity,
    .metatiles = gMetatiles_SaffronCity,
    .metatileAttributes = gMetatileAttributes_SaffronCity,
    .callback = NULL,
};

const struct Tileset gTileset_Mart =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Mart,
    .palettes = gTilesetPalettes_Mart,
    .metatiles = gMetatiles_Mart,
    .metatileAttributes = gMetatileAttributes_Mart,
    .callback = NULL,
};

const struct Tileset gTileset_PokemonCenterFrlg =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PokemonCenter_Frlg,
    .palettes = gTilesetPalettes_PokemonCenter_Frlg,
    .metatiles = gMetatiles_PokemonCenter_Frlg,
    .metatileAttributes = gMetatileAttributes_PokemonCenter_Frlg,
    .callback = NULL,
};

const struct Tileset gTileset_Cave_Frlg =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Cave_Frlg,
    .palettes = gTilesetPalettes_Cave_Frlg,
    .metatiles = gMetatiles_Cave_Frlg,
    .metatileAttributes = gMetatileAttributes_Cave_Frlg,
    .callback = NULL,
};

const struct Tileset gTileset_Museum =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Museum,
    .palettes = gTilesetPalettes_Museum,
    .metatiles = gMetatiles_Museum,
    .metatileAttributes = gMetatileAttributes_Museum,
    .callback = NULL,
};

const struct Tileset gTileset_CableClub_Frlg =
{
    .isCompressed = FALSE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_CableClub_Frlg,
    .palettes = gTilesetPalettes_CableClub_Frlg,
    .metatiles = gMetatiles_CableClub_Frlg,
    .metatileAttributes = gMetatileAttributes_CableClub_Frlg,
    .callback = NULL,
};

const struct Tileset gTileset_BikeShop_Frlg =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BikeShop_Frlg,
    .palettes = gTilesetPalettes_BikeShop_Frlg,
    .metatiles = gMetatiles_BikeShop_Frlg,
    .metatileAttributes = gMetatileAttributes_BikeShop_Frlg,
    .callback = NULL,
};

const struct Tileset gTileset_GenericBuilding1 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_GenericBuilding1,
    .palettes = gTilesetPalettes_GenericBuilding1,
    .metatiles = gMetatiles_GenericBuilding1,
    .metatileAttributes = gMetatileAttributes_GenericBuilding1,
    .callback = NULL,
};

const struct Tileset gTileset_Lab_Frlg =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Lab_Frlg,
    .palettes = gTilesetPalettes_Lab_Frlg,
    .metatiles = gMetatiles_Lab_Frlg,
    .metatileAttributes = gMetatileAttributes_Lab_Frlg,
    .callback = NULL,
};

const struct Tileset gTileset_FuchsiaGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_FuchsiaGym,
    .palettes = gTilesetPalettes_FuchsiaGym,
    .metatiles = gMetatiles_FuchsiaGym,
    .metatileAttributes = gMetatileAttributes_FuchsiaGym,
    .callback = NULL,
};

const struct Tileset gTileset_ViridianGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_ViridianGym,
    .palettes = gTilesetPalettes_ViridianGym,
    .metatiles = gMetatiles_ViridianGym,
    .metatileAttributes = gMetatileAttributes_ViridianGym,
    .callback = NULL,
};

const struct Tileset gTileset_HoennBuilding =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_HoennBuilding,
    .palettes = gTilesetPalettes_HoennBuilding,
    .metatiles = gMetatiles_HoennBuilding,
    .metatileAttributes = gMetatileAttributes_HoennBuilding,
    .callback = NULL,
};

const struct Tileset gTileset_GameCorner =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_GameCorner,
    .palettes = gTilesetPalettes_GameCorner,
    .metatiles = gMetatiles_GameCorner,
    .metatileAttributes = gMetatileAttributes_GameCorner,
    .callback = NULL,
};

const struct Tileset gTileset_PewterGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PewterGym,
    .palettes = gTilesetPalettes_PewterGym,
    .metatiles = gMetatiles_PewterGym,
    .metatileAttributes = gMetatileAttributes_PewterGym,
    .callback = NULL,
};

const struct Tileset gTileset_CeruleanGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_CeruleanGym,
    .palettes = gTilesetPalettes_CeruleanGym,
    .metatiles = gMetatiles_CeruleanGym,
    .metatileAttributes = gMetatileAttributes_CeruleanGym,
    .callback = NULL,
};

const struct Tileset gTileset_VermilionGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_VermilionGym,
    .palettes = gTilesetPalettes_VermilionGym,
    .metatiles = gMetatiles_VermilionGym,
    .metatileAttributes = gMetatileAttributes_VermilionGym,
    .callback = InitTilesetAnim_VermilionGym,
};

const struct Tileset gTileset_CeladonGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_CeladonGym,
    .palettes = gTilesetPalettes_CeladonGym,
    .metatiles = gMetatiles_CeladonGym,
    .metatileAttributes = gMetatileAttributes_CeladonGym,
    .callback = InitTilesetAnim_CeladonGym,
};

const struct Tileset gTileset_SaffronGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SaffronGym,
    .palettes = gTilesetPalettes_SaffronGym,
    .metatiles = gMetatiles_SaffronGym,
    .metatileAttributes = gMetatileAttributes_SaffronGym,
    .callback = NULL,
};

const struct Tileset gTileset_CinnabarGym =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_CinnabarGym,
    .palettes = gTilesetPalettes_CinnabarGym,
    .metatiles = gMetatiles_CinnabarGym,
    .metatileAttributes = gMetatileAttributes_CinnabarGym,
    .callback = NULL,
};

const struct Tileset gTileset_SSAnne =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SSAnne,
    .palettes = gTilesetPalettes_SSAnne,
    .metatiles = gMetatiles_SSAnne,
    .metatileAttributes = gMetatileAttributes_SSAnne,
    .callback = NULL,
};

const struct Tileset gTileset_ViridianForest =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_ViridianForest,
    .palettes = gTilesetPalettes_ViridianForest,
    .metatiles = gMetatiles_ViridianForest,
    .metatileAttributes = gMetatileAttributes_ViridianForest,
    .callback = NULL,
};

const struct Tileset gTileset_UnusedGatehouse1 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_UnusedGatehouse1,
    .palettes = gTilesetPalettes_UnusedGatehouse1,
    .metatiles = gMetatiles_UnusedGatehouse1,
    .metatileAttributes = gMetatileAttributes_UnusedGatehouse1,
    .callback = NULL,
};

const struct Tileset gTileset_RockTunnel =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_RockTunnel,
    .palettes = gTilesetPalettes_RockTunnel,
    .metatiles = gMetatiles_RockTunnel,
    .metatileAttributes = gMetatileAttributes_RockTunnel,
    .callback = NULL,
};

const struct Tileset gTileset_DiglettsCave =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_DiglettsCave,
    .palettes = gTilesetPalettes_DiglettsCave,
    .metatiles = gMetatiles_DiglettsCave,
    .metatileAttributes = gMetatileAttributes_DiglettsCave,
    .callback = NULL,
};

const struct Tileset gTileset_SeafoamIslands =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SeafoamIslands,
    .palettes = gTilesetPalettes_SeafoamIslands,
    .metatiles = gMetatiles_SeafoamIslands,
    .metatileAttributes = gMetatileAttributes_SeafoamIslands,
    .callback = NULL,
};

const struct Tileset gTileset_UnusedGatehouse2 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_UnusedGatehouse2,
    .palettes = gTilesetPalettes_UnusedGatehouse2,
    .metatiles = gMetatiles_UnusedGatehouse2,
    .metatileAttributes = gMetatileAttributes_UnusedGatehouse2,
    .callback = NULL,
};

const struct Tileset gTileset_CeruleanCave =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_CeruleanCave,
    .palettes = gTilesetPalettes_CeruleanCave,
    .metatiles = gMetatiles_CeruleanCave,
    .metatileAttributes = gMetatileAttributes_CeruleanCave,
    .callback = NULL,
};

const struct Tileset gTileset_DepartmentStore =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_DepartmentStore,
    .palettes = gTilesetPalettes_DepartmentStore,
    .metatiles = gMetatiles_DepartmentStore,
    .metatileAttributes = gMetatileAttributes_DepartmentStore,
    .callback = NULL,
};

const struct Tileset gTileset_GenericBuilding2 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_GenericBuilding2,
    .palettes = gTilesetPalettes_GenericBuilding2,
    .metatiles = gMetatiles_GenericBuilding2,
    .metatileAttributes = gMetatileAttributes_GenericBuilding2,
    .callback = NULL,
};

const struct Tileset gTileset_PowerPlant =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PowerPlant,
    .palettes = gTilesetPalettes_PowerPlant,
    .metatiles = gMetatiles_PowerPlant,
    .metatileAttributes = gMetatileAttributes_PowerPlant,
    .callback = NULL,
};

const struct Tileset gTileset_SeaCottage =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SeaCottage,
    .palettes = gTilesetPalettes_SeaCottage,
    .metatiles = gMetatiles_SeaCottage,
    .metatileAttributes = gMetatileAttributes_SeaCottage,
    .callback = NULL,
};

const struct Tileset gTileset_SilphCo =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Condominiums,
    .palettes = gTilesetPalettes_Condominiums,
    .metatiles = gMetatiles_SilphCo,
    .metatileAttributes = gMetatileAttributes_SilphCo,
    .callback = InitTilesetAnim_SilphCo,
};

const struct Tileset gTileset_UndergroundPath =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_UndergroundPath,
    .palettes = gTilesetPalettes_UndergroundPath,
    .metatiles = gMetatiles_UndergroundPath,
    .metatileAttributes = gMetatileAttributes_UndergroundPath,
    .callback = NULL,
};

const struct Tileset gTileset_PokemonTower =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PokemonTower,
    .palettes = gTilesetPalettes_PokemonTower,
    .metatiles = gMetatiles_PokemonTower,
    .metatileAttributes = gMetatileAttributes_PokemonTower,
    .callback = NULL,
};

const struct Tileset gTileset_SafariZoneBuilding =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SafariZoneBuilding,
    .palettes = gTilesetPalettes_SafariZoneBuilding,
    .metatiles = gMetatiles_SafariZoneBuilding,
    .metatileAttributes = gMetatileAttributes_SafariZoneBuilding,
    .callback = NULL,
};

const struct Tileset gTileset_PokemonMansion =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PokemonMansion,
    .palettes = gTilesetPalettes_PokemonMansion,
    .metatiles = gMetatiles_PokemonMansion,
    .metatileAttributes = gMetatileAttributes_PokemonMansion,
    .callback = NULL,
};

const struct Tileset gTileset_RestaurantHotel =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_RestaurantHotel,
    .palettes = gTilesetPalettes_RestaurantHotel,
    .metatiles = gMetatiles_RestaurantHotel,
    .metatileAttributes = gMetatileAttributes_RestaurantHotel,
    .callback = NULL,
};

const struct Tileset gTileset_School =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_School,
    .palettes = gTilesetPalettes_School,
    .metatiles = gMetatiles_School,
    .metatileAttributes = gMetatileAttributes_School,
    .callback = NULL,
};

const struct Tileset gTileset_FanClubDaycare =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_FanClubDaycare,
    .palettes = gTilesetPalettes_FanClubDaycare,
    .metatiles = gMetatiles_FanClubDaycare,
    .metatileAttributes = gMetatileAttributes_FanClubDaycare,
    .callback = NULL,
};

const struct Tileset gTileset_Condominiums =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Condominiums,
    .palettes = gTilesetPalettes_Condominiums,
    .metatiles = gMetatiles_Condominiums,
    .metatileAttributes = gMetatileAttributes_Condominiums,
    .callback = NULL,
};

const struct Tileset gTileset_BurgledHouse =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BurgledHouse,
    .palettes = gTilesetPalettes_BurgledHouse,
    .metatiles = gMetatiles_BurgledHouse,
    .metatileAttributes = gMetatileAttributes_BurgledHouse,
    .callback = NULL,
};

const struct Tileset gTileset_MtEmber =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_MtEmber,
    .palettes = gTilesetPalettes_MtEmber,
    .metatiles = gMetatiles_MtEmber,
    .metatileAttributes = gMetatileAttributes_MtEmber,
    .callback = InitTilesetAnim_MtEmber,
};

const struct Tileset gTileset_BerryForest =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_BerryForest,
    .palettes = gTilesetPalettes_BerryForest,
    .metatiles = gMetatiles_BerryForest,
    .metatileAttributes = gMetatileAttributes_BerryForest,
    .callback = NULL,
};

const struct Tileset gTileset_NavelRock_Frlg =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_NavelRock_Frlg,
    .palettes = gTilesetPalettes_NavelRock_Frlg,
    .metatiles = gMetatiles_NavelRock_Frlg,
    .metatileAttributes = gMetatileAttributes_NavelRock_Frlg,
    .callback = NULL,
};

const struct Tileset gTileset_TanobyRuins =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_TanobyRuins,
    .palettes = gTilesetPalettes_TanobyRuins,
    .metatiles = gMetatiles_TanobyRuins,
    .metatileAttributes = gMetatileAttributes_TanobyRuins,
    .callback = NULL,
};

const struct Tileset gTileset_SeviiIslands123 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SeviiIslands123,
    .palettes = gTilesetPalettes_SeviiIslands123,
    .metatiles = gMetatiles_SeviiIslands123,
    .metatileAttributes = gMetatileAttributes_SeviiIslands123,
    .callback = NULL,
};

const struct Tileset gTileset_SeviiIslands45 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SeviiIslands45,
    .palettes = gTilesetPalettes_SeviiIslands45,
    .metatiles = gMetatiles_SeviiIslands45,
    .metatileAttributes = gMetatileAttributes_SeviiIslands45,
    .callback = NULL,
};

const struct Tileset gTileset_SeviiIslands67 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_SeviiIslands67,
    .palettes = gTilesetPalettes_SeviiIslands67,
    .metatiles = gMetatiles_SeviiIslands67,
    .metatileAttributes = gMetatileAttributes_SeviiIslands67,
    .callback = NULL,
};

const struct Tileset gTileset_TrainerTower =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_TrainerTower,
    .palettes = gTilesetPalettes_TrainerTower,
    .metatiles = gMetatiles_TrainerTower,
    .metatileAttributes = gMetatileAttributes_TrainerTower,
    .callback = NULL,
};

const struct Tileset gTileset_IslandHarbor_Frlg =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_IslandHarbor_Frlg,
    .palettes = gTilesetPalettes_IslandHarbor_Frlg,
    .metatiles = gMetatiles_IslandHarbor_Frlg,
    .metatileAttributes = gMetatileAttributes_IslandHarbor_Frlg,
    .callback = NULL,
};

const struct Tileset gTileset_PokemonLeague =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_PokemonLeague,
    .palettes = gTilesetPalettes_PokemonLeague,
    .metatiles = gMetatiles_PokemonLeague,
    .metatileAttributes = gMetatileAttributes_PokemonLeague,
    .callback = NULL,
};

const struct Tileset gTileset_HallOfFame =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_HallOfFame,
    .palettes = gTilesetPalettes_HallOfFame,
    .metatiles = gMetatiles_HallOfFame,
    .metatileAttributes = gMetatileAttributes_HallOfFame,
    .callback = NULL,
};

#endif // IS_FRLG

// BEGIN LEGENDS AWAKENING IMPORTED TILESETS

const struct Tileset gTileset_LA_UnovaGeneral =
{
    .isCompressed = FALSE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_LA_UnovaGeneral,
    .palettes = gTilesetPalettes_LA_UnovaGeneral,
    .metatiles = gMetatiles_LA_UnovaGeneral,
    .metatileAttributes = gMetatileAttributes_LA_UnovaGeneral,
    .callback = NULL,
};

const struct Tileset gTileset_LA_NuvemaTown =
{
    .isCompressed = FALSE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_LA_NuvemaTown,
    .palettes = gTilesetPalettes_LA_NuvemaTown,
    .metatiles = gMetatiles_LA_NuvemaTown,
    .metatileAttributes = gMetatileAttributes_LA_NuvemaTown,
    .callback = NULL,
};

// END LEGENDS AWAKENING IMPORTED TILESETS




const struct Tileset gTileset_AMap_Primary_BWA_082D4A94 =
{
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_AMap_Primary_BWA_082D4A94,
    .palettes = gTilesetPalettes_AMap_Primary_BWA_082D4A94,
    .metatiles = gMetatiles_AMap_Primary_BWA_082D4A94,
    .metatileAttributes = gMetatileAttributes_AMap_Primary_BWA_082D4A94,
    .callback = NULL,
};

const struct Tileset gTileset_AMap_Secondary_BWA_P082D4A94S082D4AAC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_AMap_Secondary_BWA_P082D4A94S082D4AAC,
    .palettes = gTilesetPalettes_AMap_Secondary_BWA_P082D4A94S082D4AAC,
    .metatiles = gMetatiles_AMap_Secondary_BWA_P082D4A94S082D4AAC,
    .metatileAttributes = gMetatileAttributes_AMap_Secondary_BWA_P082D4A94S082D4AAC,
    .callback = NULL,
};

const struct Tileset gTileset_AMap_Primary_SWSH_082D4A94 =
{
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_AMap_Primary_SWSH_082D4A94,
    .palettes = gTilesetPalettes_AMap_Primary_SWSH_082D4A94,
    .metatiles = gMetatiles_AMap_Primary_SWSH_082D4A94,
    .metatileAttributes = gMetatileAttributes_AMap_Primary_SWSH_082D4A94,
    .callback = NULL,
};

const struct Tileset gTileset_AMap_Secondary_SWSH_P082D4A94S082D504C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_AMap_Secondary_SWSH_P082D4A94S082D504C,
    .palettes = gTilesetPalettes_AMap_Secondary_SWSH_P082D4A94S082D504C,
    .metatiles = gMetatiles_AMap_Secondary_SWSH_P082D4A94S082D504C,
    .metatileAttributes = gMetatileAttributes_AMap_Secondary_SWSH_P082D4A94S082D504C,
    .callback = NULL,
};

const struct Tileset gTileset_AMap_Secondary_BWA_P082D4A94S082D504C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_AMap_Secondary_BWA_P082D4A94S082D504C,
    .palettes = gTilesetPalettes_AMap_Secondary_BWA_P082D4A94S082D504C,
    .metatiles = gMetatiles_AMap_Secondary_BWA_P082D4A94S082D504C,
    .metatileAttributes = gMetatileAttributes_AMap_Secondary_BWA_P082D4A94S082D504C,
    .callback = NULL,
};

const struct Tileset gTileset_AMap_Secondary_BWA_P082D4A94S082D4AF4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_AMap_Secondary_BWA_P082D4A94S082D4AF4,
    .palettes = gTilesetPalettes_AMap_Secondary_BWA_P082D4A94S082D4AF4,
    .metatiles = gMetatiles_AMap_Secondary_BWA_P082D4A94S082D4AF4,
    .metatileAttributes = gMetatileAttributes_AMap_Secondary_BWA_P082D4A94S082D4AF4,
    .callback = NULL,
};

const struct Tileset gTileset_AMap_Secondary_BWA_P082D4A94S082D4DC4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_AMap_Secondary_BWA_P082D4A94S082D4DC4,
    .palettes = gTilesetPalettes_AMap_Secondary_BWA_P082D4A94S082D4DC4,
    .metatiles = gMetatiles_AMap_Secondary_BWA_P082D4A94S082D4DC4,
    .metatileAttributes = gMetatileAttributes_AMap_Secondary_BWA_P082D4A94S082D4DC4,
    .callback = NULL,
};

const struct Tileset gTileset_AMap_Secondary_BWA_P082D4A94S082D4B0C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_AMap_Secondary_BWA_P082D4A94S082D4B0C,
    .palettes = gTilesetPalettes_AMap_Secondary_BWA_P082D4A94S082D4B0C,
    .metatiles = gMetatiles_AMap_Secondary_BWA_P082D4A94S082D4B0C,
    .metatileAttributes = gMetatileAttributes_AMap_Secondary_BWA_P082D4A94S082D4B0C,
    .callback = NULL,
};

const struct Tileset gTileset_AMap_Secondary_SWSH_P082D4A94S082D4AAC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_AMap_Secondary_SWSH_P082D4A94S082D4AAC,
    .palettes = gTilesetPalettes_AMap_Secondary_SWSH_P082D4A94S082D4AAC,
    .metatiles = gMetatiles_AMap_Secondary_SWSH_P082D4A94S082D4AAC,
    .metatileAttributes = gMetatileAttributes_AMap_Secondary_SWSH_P082D4A94S082D4AAC,
    .callback = NULL,
};

const struct Tileset gTileset_AMap_Secondary_SWSH_P082D4A94S082D4B0C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_AMap_Secondary_SWSH_P082D4A94S082D4B0C,
    .palettes = gTilesetPalettes_AMap_Secondary_SWSH_P082D4A94S082D4B0C,
    .metatiles = gMetatiles_AMap_Secondary_SWSH_P082D4A94S082D4B0C,
    .metatileAttributes = gMetatileAttributes_AMap_Secondary_SWSH_P082D4A94S082D4B0C,
    .callback = NULL,
};

const struct Tileset gTileset_AMap_Secondary_SWSH_P082D4A94S082D4AF4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_AMap_Secondary_SWSH_P082D4A94S082D4AF4,
    .palettes = gTilesetPalettes_AMap_Secondary_SWSH_P082D4A94S082D4AF4,
    .metatiles = gMetatiles_AMap_Secondary_SWSH_P082D4A94S082D4AF4,
    .metatileAttributes = gMetatileAttributes_AMap_Secondary_SWSH_P082D4A94S082D4AF4,
    .callback = NULL,
};

const struct Tileset gTileset_AMap_Secondary_SWSH_P082D4A94S082D4ADC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_AMap_Secondary_SWSH_P082D4A94S082D4ADC,
    .palettes = gTilesetPalettes_AMap_Secondary_SWSH_P082D4A94S082D4ADC,
    .metatiles = gMetatiles_AMap_Secondary_SWSH_P082D4A94S082D4ADC,
    .metatileAttributes = gMetatileAttributes_AMap_Secondary_SWSH_P082D4A94S082D4ADC,
    .callback = NULL,
};

const struct Tileset gTileset_AMap_Secondary_SWSH_P082D4A94S082D4DF4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_AMap_Secondary_SWSH_P082D4A94S082D4DF4,
    .palettes = gTilesetPalettes_AMap_Secondary_SWSH_P082D4A94S082D4DF4,
    .metatiles = gMetatiles_AMap_Secondary_SWSH_P082D4A94S082D4DF4,
    .metatileAttributes = gMetatileAttributes_AMap_Secondary_SWSH_P082D4A94S082D4DF4,
    .callback = NULL,
};

/* Hyper definitions exposed directly for Porymap; same compiled assets. */
/* Proven Hyper asset bank; no map registration or gameplay. */
const struct Tileset gTileset_Hyper_Primary_083DF704 =
{
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Primary_083DF704,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Primary_083DF884 =
{
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF884,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF884,
    .metatiles = gMetatiles_Hyper_Primary_083DF884,
    .metatileAttributes = gMetatileAttributes_Hyper_Primary_083DF884,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF884,
};

const struct Tileset gTileset_Hyper_Primary_083DFC5C =
{
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DFC5C,
    .palettes = gTilesetPalettes_Hyper_Primary_083DFC5C,
    .metatiles = gMetatiles_Hyper_Primary_083DFC5C,
    .metatileAttributes = gMetatileAttributes_Hyper_Primary_083DFC5C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF71C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF71C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF71C,
    .metatiles = gMetatiles_Hyper_Secondary_083DF71C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF71C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF734 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF734,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF734,
    .metatiles = gMetatiles_Hyper_Secondary_083DF734,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF734,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF734,
};

const struct Tileset gTileset_Hyper_Secondary_083DF74C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF74C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF74C,
    .metatiles = gMetatiles_Hyper_Secondary_083DF74C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF74C,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF74C,
};

const struct Tileset gTileset_Hyper_Secondary_083DF764 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF764,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF764,
    .metatiles = gMetatiles_Hyper_Secondary_083DF764,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF764,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF764,
};

const struct Tileset gTileset_Hyper_Secondary_083DF77C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF77C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF77C,
    .metatiles = gMetatiles_Hyper_Secondary_083DF77C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF77C,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF77C,
};

const struct Tileset gTileset_Hyper_Secondary_083DF794 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF794,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF794,
    .metatiles = gMetatiles_Hyper_Secondary_083DF794,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF794,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF794,
};

const struct Tileset gTileset_Hyper_Secondary_083DF7AC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7AC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7AC,
    .metatiles = gMetatiles_Hyper_Secondary_083DF7AC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF7AC,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF7C4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7C4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7C4,
    .metatiles = gMetatiles_Hyper_Secondary_083DF7C4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF7C4,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF7DC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7DC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7DC,
    .metatiles = gMetatiles_Hyper_Secondary_083DF7DC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF7DC,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF7F4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Secondary_083DF7F4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF7F4,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF80C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF80C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF80C,
    .metatiles = gMetatiles_Hyper_Secondary_083DF80C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF80C,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF80C,
};

const struct Tileset gTileset_Hyper_Secondary_083DF824 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF824,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF824,
    .metatiles = gMetatiles_Hyper_Secondary_083DF824,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF824,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF824,
};

const struct Tileset gTileset_Hyper_Secondary_083DF83C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF83C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF83C,
    .metatiles = gMetatiles_Hyper_Secondary_083DF83C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF83C,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF83C,
};

const struct Tileset gTileset_Hyper_Secondary_083DF854 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF854,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF854,
    .metatiles = gMetatiles_Hyper_Secondary_083DF854,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF854,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF854,
};

const struct Tileset gTileset_Hyper_Secondary_083DF86C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF86C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF86C,
    .metatiles = gMetatiles_Hyper_Secondary_083DF86C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF86C,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF86C,
};

const struct Tileset gTileset_Hyper_Secondary_083DF89C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF89C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF89C,
    .metatiles = gMetatiles_Hyper_Secondary_083DF89C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF89C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF8B4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8B4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8B4,
    .metatiles = gMetatiles_Hyper_Secondary_083DF8B4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF8B4,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF8CC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8CC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8CC,
    .metatiles = gMetatiles_Hyper_Secondary_083DF8CC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF8CC,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF8CC,
};

const struct Tileset gTileset_Hyper_Secondary_083DF8E4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8E4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8E4,
    .metatiles = gMetatiles_Hyper_Secondary_083DF8E4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF8E4,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF8FC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8FC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8FC,
    .metatiles = gMetatiles_Hyper_Secondary_083DF8FC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF8FC,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF92C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF92C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF92C,
    .metatiles = gMetatiles_Hyper_Secondary_083DF92C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF92C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF944 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF944,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF944,
    .metatiles = gMetatiles_Hyper_Secondary_083DF944,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF944,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF95C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF95C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF95C,
    .metatiles = gMetatiles_Hyper_Secondary_083DF95C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF95C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF974 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF974,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF974,
    .metatiles = gMetatiles_Hyper_Secondary_083DF974,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF974,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF98C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF98C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF98C,
    .metatiles = gMetatiles_Hyper_Secondary_083DF98C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF98C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF9A4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9A4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9A4,
    .metatiles = gMetatiles_Hyper_Secondary_083DF9A4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF9A4,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF9BC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9BC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9BC,
    .metatiles = gMetatiles_Hyper_Secondary_083DF9BC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF9BC,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DF9D4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9D4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9D4,
    .metatiles = gMetatiles_Hyper_Secondary_083DF9D4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF9D4,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF9D4,
};

const struct Tileset gTileset_Hyper_Secondary_083DF9EC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9EC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9EC,
    .metatiles = gMetatiles_Hyper_Secondary_083DF9EC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DF9EC,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFA04 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFA04,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFA04,
    .metatiles = gMetatiles_Hyper_Secondary_083DFA04,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFA04,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFA1C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFA1C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFA1C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFA1C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFA1C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFA34 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFA34,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFA34,
    .metatiles = gMetatiles_Hyper_Secondary_083DFA34,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFA34,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFA4C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFA4C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFA4C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFA4C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFA4C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFA64 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFA64,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFA64,
    .metatiles = gMetatiles_Hyper_Secondary_083DFA64,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFA64,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFA7C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFA7C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFA7C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFA7C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFA7C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFA94 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFA94,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFA94,
    .metatiles = gMetatiles_Hyper_Secondary_083DFA94,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFA94,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFAC4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFAC4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFAC4,
    .metatiles = gMetatiles_Hyper_Secondary_083DFAC4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFAC4,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFADC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFADC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFADC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFADC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFADC,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFAF4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFAF4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFAF4,
    .metatiles = gMetatiles_Hyper_Secondary_083DFAF4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFAF4,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFB0C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB0C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB0C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB0C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFB0C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFB24 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB24,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB24,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB24,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFB24,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DFB24,
};

const struct Tileset gTileset_Hyper_Secondary_083DFB3C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB3C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB3C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB3C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFB3C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFB54 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB54,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB54,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB54,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFB54,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DFB54,
};

const struct Tileset gTileset_Hyper_Secondary_083DFB6C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFB6C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFB84 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB84,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB84,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB84,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFB84,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFB9C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB9C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB9C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB9C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFB9C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFBB4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBB4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBB4,
    .metatiles = gMetatiles_Hyper_Secondary_083DFBB4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFBB4,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFBCC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBCC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBCC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFBCC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFBCC,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DFBCC,
};

const struct Tileset gTileset_Hyper_Secondary_083DFBE4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBE4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBE4,
    .metatiles = gMetatiles_Hyper_Secondary_083DFBE4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFBE4,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFBFC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBFC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBFC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFBFC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFBFC,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFC14 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC14,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC14,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC14,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFC14,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFC2C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC2C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC2C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC2C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFC2C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFC44 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC44,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC44,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC44,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFC44,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFC7C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC7C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC7C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC7C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFC7C,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DFC7C,
};

const struct Tileset gTileset_Hyper_Secondary_083DFC94 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC94,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC94,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC94,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFC94,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFCAC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFCAC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFCAC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFCAC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFCAC,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFCC4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFCC4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFCC4,
    .metatiles = gMetatiles_Hyper_Secondary_083DFCC4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFCC4,
    .callback = InitTilesetAnim_BattleDome,
};

const struct Tileset gTileset_Hyper_Secondary_083DFCDC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFCDC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFCDC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFCDC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFCDC,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFCF4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFCF4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFCF4,
    .metatiles = gMetatiles_Hyper_Secondary_083DFCF4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFCF4,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFD0C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD0C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD0C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD0C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFD0C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFD24 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD24,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD24,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD24,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFD24,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DFD24,
};

const struct Tileset gTileset_Hyper_Secondary_083DFD3C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD3C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD3C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD3C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFD3C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFD54 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD54,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD54,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD54,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFD54,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFD6C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFD6C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFD84 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD84,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD84,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD84,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFD84,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFD9C =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD9C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD9C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD9C,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFD9C,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFDB4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFDB4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFDB4,
    .metatiles = gMetatiles_Hyper_Secondary_083DFDB4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFDB4,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFDCC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFDCC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFDCC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFDCC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFDCC,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFDE4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFDE4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFDE4,
    .metatiles = gMetatiles_Hyper_Secondary_083DFDE4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFDE4,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_083DFDFC =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFDFC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFDFC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFDFC,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_083DFDFC,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Secondary_08A5FEB4 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_08A5FEB4,
    .palettes = gTilesetPalettes_Hyper_Secondary_08A5FEB4,
    .metatiles = gMetatiles_Hyper_Secondary_08A5FEB4,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_08A5FEB4,
    .callback = InitTilesetAnim_HyperAsset_Secondary_08A5FEB4,
};

/* Canonical Route105 weather/Dive behavior derivative; shared Hyper graphics. */
const struct Tileset gTileset_Hyper_Primary_Route105 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Route105,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Canary5_JaggedPass_Secondary = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF794,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF794,
    .metatiles = gMetatiles_Hyper_Secondary_083DF794,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_JaggedPass_Secondary,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF794,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_1_Dragonspiral_Tower_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD3C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD3C,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_1_Dragonspiral_Tower_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_1_Dragonspiral_Tower_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_10_Basement_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9BC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9BC,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_10_Basement_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_10_Basement_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_15_Ultra_Space_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_15_Ultra_Space_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_15_Ultra_Space_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_45_Desert_Ruins_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD3C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD3C,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_45_Desert_Ruins_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_45_Desert_Ruins_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_48_Ultra_Space_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_48_Ultra_Space_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_48_Ultra_Space_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_49_Ultra_Space_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_49_Ultra_Space_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_49_Ultra_Space_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_52_Ultra_Space_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_52_Ultra_Space_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_52_Ultra_Space_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_67_Timeless_Woods_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_67_Timeless_Woods_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_67_Timeless_Woods_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_35_30_Crescent_Isle_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF734,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF734,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_35_30_Crescent_Isle_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_35_30_Crescent_Isle_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF734,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_51_Ultra_Space_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_51_Ultra_Space_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_51_Ultra_Space_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_39_Allearth_Forest_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF734,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF734,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_39_Allearth_Forest_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_39_Allearth_Forest_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF734,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_38_Allearth_Forest_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF734,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF734,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_38_Allearth_Forest_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_38_Allearth_Forest_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF734,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_50_Ultra_Space_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_50_Ultra_Space_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_50_Ultra_Space_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_53_Mt_Silver_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7AC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7AC,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_53_Mt_Silver_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_53_Mt_Silver_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_35_4_Rainbow_Castle_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9BC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9BC,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_35_4_Rainbow_Castle_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_35_4_Rainbow_Castle_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_77_Champion_Island_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFCC4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFCC4,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_77_Champion_Island_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_77_Champion_Island_Portals,
    .callback = InitTilesetAnim_BattleDome,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_12_Unown_Ruins_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_12_Unown_Ruins_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_12_Unown_Ruins_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_83_Rainbow_Castle_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9BC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9BC,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_83_Rainbow_Castle_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_83_Rainbow_Castle_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_82_Rainbow_Castle_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9BC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9BC,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_82_Rainbow_Castle_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_82_Rainbow_Castle_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_84_Rainbow_Castle_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBFC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBFC,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_84_Rainbow_Castle_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_84_Rainbow_Castle_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary5_HyperHoenn_34_89_Rainbow_Castle_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9BC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9BC,
    .metatiles = gMetatiles_Hyper_Canary5_HyperHoenn_34_89_Rainbow_Castle_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary5_HyperHoenn_34_89_Rainbow_Castle_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary6_HyperHoenn_34_33_Ultra_Space_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary6_HyperHoenn_34_33_Ultra_Space_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary6_HyperHoenn_34_33_Ultra_Space_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary6_HyperHoenn_35_55_Ultra_Space_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary6_HyperHoenn_35_55_Ultra_Space_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary6_HyperHoenn_35_55_Ultra_Space_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary6_HyperHoenn_34_24_EV_Training_Cave_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8CC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8CC,
    .metatiles = gMetatiles_Hyper_Canary6_HyperHoenn_34_24_EV_Training_Cave_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary6_HyperHoenn_34_24_EV_Training_Cave_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF8CC,
};

const struct Tileset gTileset_Hyper_Canary6_HyperHoenn_35_56_Remote_Island_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF74C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF74C,
    .metatiles = gMetatiles_Hyper_Canary6_HyperHoenn_35_56_Remote_Island_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary6_HyperHoenn_35_56_Remote_Island_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF74C,
};

const struct Tileset gTileset_Hyper_Canary6_HyperHoenn_35_66_Remote_Island_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8CC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8CC,
    .metatiles = gMetatiles_Hyper_Canary6_HyperHoenn_35_66_Remote_Island_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary6_HyperHoenn_35_66_Remote_Island_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF8CC,
};

const struct Tileset gTileset_Hyper_Canary6_HyperHoenn_35_70_Remote_Island_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9EC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9EC,
    .metatiles = gMetatiles_Hyper_Canary6_HyperHoenn_35_70_Remote_Island_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary6_HyperHoenn_35_70_Remote_Island_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary6_HyperHoenn_35_62_Remote_Island_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8CC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8CC,
    .metatiles = gMetatiles_Hyper_Canary6_HyperHoenn_35_62_Remote_Island_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary6_HyperHoenn_35_62_Remote_Island_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF8CC,
};

const struct Tileset gTileset_Hyper_Canary6_HyperHoenn_34_32_Ultra_Space_Zero_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary6_HyperHoenn_34_32_Ultra_Space_Zero_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary6_HyperHoenn_34_32_Ultra_Space_Zero_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary7_HyperHoenn_34_40_Couriway_Town_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF77C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF77C,
    .metatiles = gMetatiles_Hyper_Canary7_HyperHoenn_34_40_Couriway_Town_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary7_HyperHoenn_34_40_Couriway_Town_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF77C,
};

const struct Tileset gTileset_Hyper_Canary7_HyperHoenn_34_47_Ultra_Space_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary7_HyperHoenn_34_47_Ultra_Space_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary7_HyperHoenn_34_47_Ultra_Space_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary8_HyperHoenn_34_66_Mountain_Top_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF824,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF824,
    .metatiles = gMetatiles_Hyper_Canary8_HyperHoenn_34_66_Mountain_Top_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary8_HyperHoenn_34_66_Mountain_Top_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF824,
};

const struct Tileset gTileset_Hyper_Secondary_08305DE0 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_08305DE0,
    .palettes = gTilesetPalettes_Hyper_Secondary_08305DE0,
    .metatiles = gMetatiles_Hyper_Secondary_08305DE0,
    .metatileAttributes = gMetatileAttributes_Hyper_Secondary_08305DE0,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary9_HyperHoenn_34_65_Outer_Space_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB0C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB0C,
    .metatiles = gMetatiles_Hyper_Canary9_HyperHoenn_34_65_Outer_Space_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_HyperHoenn_34_65_Outer_Space_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary9_HyperHoenn_34_30_Test_of_Heart_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC7C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC7C,
    .metatiles = gMetatiles_Hyper_Canary9_HyperHoenn_34_30_Test_of_Heart_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_HyperHoenn_34_30_Test_of_Heart_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DFC7C,
};

const struct Tileset gTileset_Hyper_Canary9_HyperHoenn_34_13_Distortion_World_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_08305DE0,
    .palettes = gTilesetPalettes_Hyper_Secondary_08305DE0,
    .metatiles = gMetatiles_Hyper_Canary9_HyperHoenn_34_13_Distortion_World_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_HyperHoenn_34_13_Distortion_World_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary9_HyperHoenn_34_29_Ultra_Alliance_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC7C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC7C,
    .metatiles = gMetatiles_Hyper_Canary9_HyperHoenn_34_29_Ultra_Alliance_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_HyperHoenn_34_29_Ultra_Alliance_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DFC7C,
};

const struct Tileset gTileset_Hyper_Canary9_HyperHoenn_37_120_Ancient_Retreat_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_08305DE0,
    .palettes = gTilesetPalettes_Hyper_Secondary_08305DE0,
    .metatiles = gMetatiles_Hyper_Canary9_HyperHoenn_37_120_Ancient_Retreat_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_HyperHoenn_37_120_Ancient_Retreat_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary9_HyperHoenn_34_31_Test_of_Heart_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC7C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC7C,
    .metatiles = gMetatiles_Hyper_Canary9_HyperHoenn_34_31_Test_of_Heart_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_HyperHoenn_34_31_Test_of_Heart_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DFC7C,
};

const struct Tileset gTileset_Hyper_Canary9_HyperHoenn_37_96_Distortion_World_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_08305DE0,
    .palettes = gTilesetPalettes_Hyper_Secondary_08305DE0,
    .metatiles = gMetatiles_Hyper_Canary9_HyperHoenn_37_96_Distortion_World_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_HyperHoenn_37_96_Distortion_World_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary9_HyperHoenn_34_26_Ultra_Alliance_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC7C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC7C,
    .metatiles = gMetatiles_Hyper_Canary9_HyperHoenn_34_26_Ultra_Alliance_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_HyperHoenn_34_26_Ultra_Alliance_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DFC7C,
};

const struct Tileset gTileset_Hyper_Canary9_HyperHoenn_34_42_Steven_s_Island_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF764,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF764,
    .metatiles = gMetatiles_Hyper_Canary9_HyperHoenn_34_42_Steven_s_Island_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_HyperHoenn_34_42_Steven_s_Island_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF764,
};

const struct Tileset gTileset_Hyper_Canary9_EverGrandeCity_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF80C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF80C,
    .metatiles = gMetatiles_Hyper_Canary9_EverGrandeCity_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_EverGrandeCity_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF80C,
};

const struct Tileset gTileset_Hyper_Canary9_Route133_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF824,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF824,
    .metatiles = gMetatiles_Hyper_Canary9_Route133_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_Route133_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF824,
};

const struct Tileset gTileset_Hyper_Canary9_Underwater_SootopolisCity_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB24,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB24,
    .metatiles = gMetatiles_Hyper_Canary9_Underwater_SootopolisCity_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_Underwater_SootopolisCity_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DFB24,
};

const struct Tileset gTileset_Hyper_Canary9_CaveOfOrigin_B1F_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8CC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8CC,
    .metatiles = gMetatiles_Hyper_Canary9_CaveOfOrigin_B1F_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_CaveOfOrigin_B1F_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF8CC,
};

const struct Tileset gTileset_Hyper_Canary9_AquaHideout_B1F_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9BC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9BC,
    .metatiles = gMetatiles_Hyper_Canary9_AquaHideout_B1F_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_AquaHideout_B1F_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary9_Route126_Dive = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary9_Route126_Dive,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_Route126_Dive,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary9_Route127_Dive = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary9_Route127_Dive,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_Route127_Dive,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary9_Route128_Dive = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7F4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7F4,
    .metatiles = gMetatiles_Hyper_Canary9_Route128_Dive,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_Route128_Dive,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Canary9_Underwater_Route126_Dive = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB24,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB24,
    .metatiles = gMetatiles_Hyper_Canary9_Underwater_Route126_Dive,
    .metatileAttributes = gMetatileAttributes_Hyper_Canary9_Underwater_Route126_Dive,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DFB24,
};

const struct Tileset gTileset_Hyper_finalization_HyperHoenn_35_35_Temple_of_the_End_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFADC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFADC,
    .metatiles = gMetatiles_Hyper_finalization_HyperHoenn_35_35_Temple_of_the_End_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_finalization_HyperHoenn_35_35_Temple_of_the_End_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_LittlerootTown_BrendansHouse_2F_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFAF4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFAF4,
    .metatiles = gMetatiles_Hyper_Secondary_083DFAF4,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_LittlerootTown_BrendansHouse_2F_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_LittlerootTown_MaysHouse_2F_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFAF4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFAF4,
    .metatiles = gMetatiles_Hyper_Secondary_083DFAF4,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_LittlerootTown_MaysHouse_2F_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_LittlerootTown_ProfessorBirchsLab_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB0C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB0C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB0C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_LittlerootTown_ProfessorBirchsLab_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_OldaleTown_House1_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_OldaleTown_House1_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_OldaleTown_House2_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_OldaleTown_House2_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_DewfordTown_House1_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_DewfordTown_House1_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_PetalburgCity_WallysHouse_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_PetalburgCity_WallysHouse_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_PetalburgCity_House1_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_PetalburgCity_House1_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_SlateportCity_House_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_SlateportCity_House_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_MauvilleCity_GameCorner_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB84,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB84,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB84,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_MauvilleCity_GameCorner_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_RustboroCity_House2_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_RustboroCity_House2_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_RustboroCity_Flat2_1F_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_RustboroCity_Flat2_1F_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_RustboroCity_Flat2_2F_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_RustboroCity_Flat2_2F_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_RustboroCity_Flat2_3F_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_RustboroCity_Flat2_3F_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_RustboroCity_House3_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_RustboroCity_House3_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_BattleFrontier_BattlePalaceBattleRoom_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_BattleFrontier_BattlePalaceBattleRoom_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_BattleFrontier_RankingHall_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFDB4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFDB4,
    .metatiles = gMetatiles_Hyper_Secondary_083DFDB4,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_BattleFrontier_RankingHall_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_BattleFrontier_Lounge1_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC94,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC94,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC94,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_BattleFrontier_Lounge1_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_BattleFrontier_Lounge3_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC94,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC94,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC94,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_BattleFrontier_Lounge3_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_BattleFrontier_Lounge4_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC94,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC94,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC94,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_BattleFrontier_Lounge4_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_BattleFrontier_Lounge6_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC94,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC94,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC94,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_BattleFrontier_Lounge6_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_BattleFrontier_Lounge7_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC94,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC94,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC94,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_BattleFrontier_Lounge7_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_BattleFrontier_Lounge8_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC94,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC94,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC94,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_BattleFrontier_Lounge8_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_BattleFrontier_Lounge9_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC94,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC94,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC94,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_BattleFrontier_Lounge9_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_ArtisanCave_B1F_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_ArtisanCave_B1F_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_ArtisanCave_B1F_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8CC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8CC,
    .metatiles = gMetatiles_Hyper_Secondary_083DF8CC,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_ArtisanCave_B1F_1,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF8CC,
};

const struct Tileset gTileset_Hyper_Final_ArtisanCave_1F_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_ArtisanCave_1F_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_ArtisanCave_1F_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8CC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8CC,
    .metatiles = gMetatiles_Hyper_Secondary_083DF8CC,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_ArtisanCave_1F_1,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF8CC,
};

const struct Tileset gTileset_Hyper_Final_AlteringCave_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_AlteringCave_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_AlteringCave_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8CC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8CC,
    .metatiles = gMetatiles_Hyper_Secondary_083DF8CC,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_AlteringCave_1,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF8CC,
};

const struct Tileset gTileset_Hyper_Final_InsideOfTruck_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_InsideOfTruck_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_SSTidalCorridor_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_SSTidalCorridor_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_SSTidalCorridor_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC44,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC44,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC44,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_SSTidalCorridor_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_SSTidalLowerDeck_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_SSTidalLowerDeck_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_SSTidalLowerDeck_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC44,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC44,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC44,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_SSTidalLowerDeck_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_SSTidalRooms_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_SSTidalRooms_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_SSTidalRooms_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC44,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC44,
    .metatiles = gMetatiles_Hyper_Secondary_083DFC44,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_SSTidalRooms_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_SouthernIsland_Exterior_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_SouthernIsland_Exterior_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_SouthernIsland_Exterior_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF734,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF734,
    .metatiles = gMetatiles_Hyper_Secondary_083DF734,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_SouthernIsland_Exterior_1,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF734,
};

const struct Tileset gTileset_Hyper_Final_SouthernIsland_Interior_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_SouthernIsland_Interior_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_SouthernIsland_Interior_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF734,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF734,
    .metatiles = gMetatiles_Hyper_Secondary_083DF734,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_SouthernIsland_Interior_1,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF734,
};

const struct Tileset gTileset_Hyper_Final_FarawayIsland_Entrance_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_FarawayIsland_Entrance_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_FarawayIsland_Entrance_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF734,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF734,
    .metatiles = gMetatiles_Hyper_Secondary_083DF734,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_FarawayIsland_Entrance_1,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF734,
};

const struct Tileset gTileset_Hyper_Final_FarawayIsland_Interior_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_FarawayIsland_Interior_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_FarawayIsland_Interior_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF7C4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF7C4,
    .metatiles = gMetatiles_Hyper_Secondary_083DF7C4,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_FarawayIsland_Interior_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Exterior_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Exterior_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Exterior_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF74C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF74C,
    .metatiles = gMetatiles_Hyper_Secondary_083DF74C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Exterior_1,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF74C,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Entrance_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Entrance_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Entrance_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD9C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD9C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD9C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Entrance_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_B1F_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_B1F_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_B1F_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD9C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD9C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD9C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_B1F_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Fork_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Fork_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Fork_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD9C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD9C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD9C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Fork_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Up2_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Up2_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Up2_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD9C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD9C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD9C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Up2_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Up4_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Up4_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Up4_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD9C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD9C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD9C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Up4_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Down02_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Down02_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Down02_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD9C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD9C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD9C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Down02_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Down04_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Down04_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Down04_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD9C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD9C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD9C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Down04_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Down06_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Down06_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Down06_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD9C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD9C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD9C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Down06_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Down08_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Down08_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Down08_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD9C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD9C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD9C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Down08_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Down10_0 = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Hyper_Primary_083DF704,
    .palettes = gTilesetPalettes_Hyper_Primary_083DF704,
    .metatiles = gMetatiles_Hyper_Primary_083DF704,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Down10_0,
    .callback = InitTilesetAnim_HyperAsset_Primary_083DF704,
};

const struct Tileset gTileset_Hyper_Final_NavelRock_Down10_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD9C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD9C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFD9C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_NavelRock_Down10_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_Route110_TrickHouseEntrance_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_Route110_TrickHouseEntrance_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_Route110_TrickHouseEnd_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_Route110_TrickHouseEnd_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_Route110_TrickHouseCorridor_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB6C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB6C,
    .metatiles = gMetatiles_Hyper_Secondary_083DFB6C,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_Route110_TrickHouseCorridor_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_Route110_TrickHousePuzzle1_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBFC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBFC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFBFC,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_Route110_TrickHousePuzzle1_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_Route110_TrickHousePuzzle2_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBFC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBFC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFBFC,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_Route110_TrickHousePuzzle2_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_Route110_TrickHousePuzzle3_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBFC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBFC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFBFC,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_Route110_TrickHousePuzzle3_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_Route110_TrickHousePuzzle4_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBFC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBFC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFBFC,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_Route110_TrickHousePuzzle4_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_Route110_TrickHousePuzzle5_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBFC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBFC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFBFC,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_Route110_TrickHousePuzzle5_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_Route110_TrickHousePuzzle6_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBFC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBFC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFBFC,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_Route110_TrickHousePuzzle6_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_Route110_TrickHousePuzzle7_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBFC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBFC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFBFC,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_Route110_TrickHousePuzzle7_1,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_Final_Route110_TrickHousePuzzle8_1 = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFBFC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFBFC,
    .metatiles = gMetatiles_Hyper_Secondary_083DFBFC,
    .metatileAttributes = gMetatileAttributes_Hyper_Final_Route110_TrickHousePuzzle8_1,
    .callback = NULL,
};

/* Additional recovered Hyper asset banks. */
const struct Tileset gTileset_Hyper_Primary_089CBC6C = {
 .isCompressed = TRUE,
 .isSecondary = FALSE,
 .tiles = gTilesetTiles_Hyper_Primary_089CBC6C,
 .palettes = gTilesetPalettes_Hyper_Primary_089CBC6C,
 .metatiles = gMetatiles_Hyper_Primary_089CBC6C,
 .metatileAttributes = gMetatileAttributes_Hyper_Primary_089CBC6C,
 .callback = InitTilesetAnim_HyperAsset_Primary_089CBC6C,
};
const struct Tileset gTileset_Hyper_Secondary_089CD34C = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTilesetTiles_Hyper_Secondary_089CD34C,
 .palettes = gTilesetPalettes_Hyper_Secondary_089CD34C,
 .metatiles = gMetatiles_Hyper_Secondary_089CD34C,
 .metatileAttributes = gMetatileAttributes_Hyper_Secondary_089CD34C,
 .callback = NULL,
};
const struct Tileset gTileset_Hyper_Secondary_08A62224 = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTilesetTiles_Hyper_Secondary_08A62224,
 .palettes = gTilesetPalettes_Hyper_Secondary_08A62224,
 .metatiles = gMetatiles_Hyper_Secondary_08A62224,
 .metatileAttributes = gMetatileAttributes_Hyper_Secondary_08A62224,
 .callback = NULL,
};
const struct Tileset gTileset_Hyper_Secondary_08A6550C = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTilesetTiles_Hyper_Secondary_08A6550C,
 .palettes = gTilesetPalettes_Hyper_Secondary_08A6550C,
 .metatiles = gMetatiles_Hyper_Secondary_08A6550C,
 .metatileAttributes = gMetatileAttributes_Hyper_Secondary_08A6550C,
 .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_35_11_Spear_Pillar_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_08305DE0,
    .palettes = gTilesetPalettes_Hyper_Secondary_08305DE0,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_35_11_Spear_Pillar_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_35_11_Spear_Pillar_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_35_14_Solaceon_Ruins_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8CC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8CC,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_35_14_Solaceon_Ruins_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_35_14_Solaceon_Ruins_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF8CC,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_35_88_Desert_Ruins_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFD3C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFD3C,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_35_88_Desert_Ruins_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_35_88_Desert_Ruins_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_36_2_Jubilife_City_Portals = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTilesetTiles_Hyper_Secondary_08A62224,
 .palettes = gTilesetPalettes_Hyper_Secondary_08A62224,
 .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_36_2_Jubilife_City_Portals,
 .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_36_2_Jubilife_City_Portals,
 .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_36_27_Route_210_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF77C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF77C,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_36_27_Route_210_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_36_27_Route_210_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF77C,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_36_92_Mt_Coronet_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_08305DE0,
    .palettes = gTilesetPalettes_Hyper_Secondary_08305DE0,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_36_92_Mt_Coronet_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_36_92_Mt_Coronet_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_36_95_Spear_Pillar_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_08305DE0,
    .palettes = gTilesetPalettes_Hyper_Secondary_08305DE0,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_36_95_Spear_Pillar_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_36_95_Spear_Pillar_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_36_96_Spear_Pillar_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_08305DE0,
    .palettes = gTilesetPalettes_Hyper_Secondary_08305DE0,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_36_96_Spear_Pillar_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_36_96_Spear_Pillar_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_37_52_Fuego_Ironworks_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9D4,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9D4,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_37_52_Fuego_Ironworks_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_37_52_Fuego_Ironworks_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF9D4,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_37_69_Veilstone_City_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9BC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9BC,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_37_69_Veilstone_City_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_37_69_Veilstone_City_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_37_84_Hearthome_City_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFC2C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFC2C,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_37_84_Hearthome_City_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_37_84_Hearthome_City_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_37_86_Canalave_City_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF9BC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF9BC,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_37_86_Canalave_City_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_37_86_Canalave_City_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperSinnoh_37_90_Snowpoint_City_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DF8CC,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DF8CC,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperSinnoh_37_90_Snowpoint_City_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperSinnoh_37_90_Snowpoint_City_Portals,
    .callback = InitTilesetAnim_HyperAsset_Secondary_083DF8CC,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperHoenn_34_13_Distortion_World_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_08305DE0,
    .palettes = gTilesetPalettes_Hyper_Secondary_08305DE0,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperHoenn_34_13_Distortion_World_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperHoenn_34_13_Distortion_World_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperHoenn_34_65_Outer_Space_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_083DFB0C,
    .palettes = gTilesetPalettes_Hyper_Secondary_083DFB0C,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperHoenn_34_65_Outer_Space_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperHoenn_34_65_Outer_Space_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperHoenn_37_96_Distortion_World_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_08305DE0,
    .palettes = gTilesetPalettes_Hyper_Secondary_08305DE0,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperHoenn_37_96_Distortion_World_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperHoenn_37_96_Distortion_World_Portals,
    .callback = NULL,
};

const struct Tileset gTileset_Hyper_sinnoh_HyperHoenn_37_120_Ancient_Retreat_Portals = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Hyper_Secondary_08305DE0,
    .palettes = gTilesetPalettes_Hyper_Secondary_08305DE0,
    .metatiles = gMetatiles_Hyper_sinnoh_HyperHoenn_37_120_Ancient_Retreat_Portals,
    .metatileAttributes = gMetatileAttributes_Hyper_sinnoh_HyperHoenn_37_120_Ancient_Retreat_Portals,
    .callback = NULL,
};
