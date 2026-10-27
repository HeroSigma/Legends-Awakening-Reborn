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

#if !LA_FREE_SPACE

#endif // unused original Galar bank


#if !LA_FREE_SPACE

#endif // unused original Galar bank


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

#if !LA_FREE_SPACE

#endif // unused original Galar bank


#if !LA_FREE_SPACE

#endif // unused original Galar bank


#if !LA_FREE_SPACE

#endif // unused original Galar bank


#if !LA_FREE_SPACE

#endif // unused original Galar bank


#if !LA_FREE_SPACE

#endif // unused original Galar bank


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
const struct Tileset gTileset_BWABatch_primary_f2e_BWA_082D4A94 = {
 .isCompressed = TRUE,
 .isSecondary = FALSE,
 .tiles = gTileset_BWABatch_primary_f2e_BWA_082D4A94_Tiles,
 .palettes = gTileset_BWABatch_primary_f2e_BWA_082D4A94_Palettes,
 .metatiles = gTileset_BWABatch_primary_f2e_BWA_082D4A94_Metatiles,
 .metatileAttributes = gTileset_BWABatch_primary_f2e_BWA_082D4A94_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_primary_f2e_BWA_082D4BB4 = {
 .isCompressed = TRUE,
 .isSecondary = FALSE,
 .tiles = gTileset_BWABatch_primary_f2e_BWA_082D4BB4_Tiles,
 .palettes = gTileset_BWABatch_primary_f2e_BWA_082D4BB4_Palettes,
 .metatiles = gTileset_BWABatch_primary_f2e_BWA_082D4BB4_Metatiles,
 .metatileAttributes = gTileset_BWABatch_primary_f2e_BWA_082D4BB4_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4AC4 = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4AC4_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4AC4_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4AC4_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4AC4_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B24 = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B24_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B24_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B24_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B24_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B3C = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B3C_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B3C_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B3C_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B3C_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B54 = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B54_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B54_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B54_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B54_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B6C = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B6C_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B6C_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B6C_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B6C_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B9C = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B9C_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B9C_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B9C_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4B9C_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4BCC = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4BCC_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4BCC_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4BCC_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4BCC_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4DDC = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4DDC_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4DDC_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4DDC_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S082D4DDC_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S0873D7FC = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S0873D7FC_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S0873D7FC_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S0873D7FC_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4A94S0873D7FC_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4C74 = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4C74_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4C74_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4C74_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4C74_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4C8C = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4C8C_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4C8C_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4C8C_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4C8C_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4D04 = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4D04_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4D04_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4D04_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4D04_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4E84 = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4E84_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4E84_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4E84_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4E84_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4F5C = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4F5C_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4F5C_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4F5C_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S082D4F5C_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S0873D82C = {
 .isCompressed = TRUE,
 .isSecondary = TRUE,
 .tiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S0873D82C_Tiles,
 .palettes = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S0873D82C_Palettes,
 .metatiles = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S0873D82C_Metatiles,
 .metatileAttributes = gTileset_BWABatch_secondary_f2e_BWA_P082D4BB4S0873D82C_Attributes,
 .callback = NULL,
};

const struct Tileset gTileset_GSJohto_primary_f2e_GS_CHRONICLES_276_082D4A94 = {.isCompressed=TRUE ,
 .isSecondary=FALSE ,
 .tiles=gTileset_GSJohto_primary_f2e_GS_CHRONICLES_276_082D4A94_Tiles ,
 .palettes=gTileset_GSJohto_primary_f2e_GS_CHRONICLES_276_082D4A94_Palettes ,
 .metatiles=gTileset_GSJohto_primary_f2e_GS_CHRONICLES_276_082D4A94_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_primary_f2e_GS_CHRONICLES_276_082D4A94_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_primary_f2e_GS_CHRONICLES_276_082D4BB4 = {.isCompressed=TRUE ,
 .isSecondary=FALSE ,
 .tiles=gTileset_GSJohto_primary_f2e_GS_CHRONICLES_276_082D4BB4_Tiles ,
 .palettes=gTileset_GSJohto_primary_f2e_GS_CHRONICLES_276_082D4BB4_Palettes ,
 .metatiles=gTileset_GSJohto_primary_f2e_GS_CHRONICLES_276_082D4BB4_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_primary_f2e_GS_CHRONICLES_276_082D4BB4_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AAC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AAC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AAC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AAC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AAC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AC4 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AC4_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AC4_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AC4_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AC4_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4ADC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4ADC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4ADC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4ADC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4ADC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AF4 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AF4_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AF4_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AF4_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AF4_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B0C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B0C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B0C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B0C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B0C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B24 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B24_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B24_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B24_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B24_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B3C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B3C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B3C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B3C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B3C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B54 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B54_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B54_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B54_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B54_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B6C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B6C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B6C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B6C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B6C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B84 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B84_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B84_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B84_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B84_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B9C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B9C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B9C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B9C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4B9C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BCC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BCC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BCC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BCC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BCC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BE4 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BE4_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BE4_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BE4_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BE4_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BFC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BFC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BFC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BFC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4BFC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4C5C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4C5C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4C5C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4C5C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4C5C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4D94 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4D94_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4D94_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4D94_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4D94_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4DF4 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4DF4_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4DF4_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4DF4_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4DF4_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4E0C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4E0C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4E0C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4E0C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4E0C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4E24 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4E24_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4E24_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4E24_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4E24_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4EFC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4EFC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4EFC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4EFC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4EFC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4F74 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4F74_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4F74_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4F74_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4F74_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D5034 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D5034_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D5034_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D5034_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D5034_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D50AC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D50AC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D50AC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D50AC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D50AC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S0890384C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S0890384C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S0890384C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S0890384C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S0890384C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S08903F3C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S08903F3C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S08903F3C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S08903F3C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S08903F3C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S089A623C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S089A623C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S089A623C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S089A623C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S089A623C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S089A62CC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S089A62CC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S089A62CC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S089A62CC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S089A62CC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S08A74F54 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S08A74F54_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S08A74F54_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S08A74F54_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S08A74F54_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4BE4 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4BE4_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4BE4_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4BE4_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4BE4_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C14 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C14_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C14_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C14_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C14_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C2C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C2C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C2C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C2C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C2C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C5C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C5C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C5C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C5C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C5C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C74 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C74_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C74_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C74_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C74_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C8C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C8C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C8C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C8C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4C8C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CA4 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CA4_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CA4_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CA4_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CA4_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CBC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CBC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CBC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CBC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CBC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CEC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CEC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CEC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CEC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4CEC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D04 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D04_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D04_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D04_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D04_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D1C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D1C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D1C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D1C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D1C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D34 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D34_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D34_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D34_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D34_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D4C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D4C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D4C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D4C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D4C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D64 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D64_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D64_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D64_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4D64_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4DAC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4DAC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4DAC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4DAC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4DAC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E0C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E0C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E0C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E0C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E0C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E6C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E6C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E6C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E6C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E6C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E84 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E84_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E84_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E84_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E84_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E9C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E9C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E9C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E9C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4E9C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4EB4 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4EB4_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4EB4_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4EB4_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4EB4_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4ECC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4ECC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4ECC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4ECC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4ECC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4EFC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4EFC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4EFC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4EFC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4EFC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F14 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F14_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F14_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F14_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F14_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F2C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F2C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F2C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F2C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F2C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F44 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F44_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F44_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F44_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F44_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F5C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F5C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F5C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F5C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F5C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F74 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F74_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F74_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F74_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F74_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F8C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F8C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F8C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F8C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4F8C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4FBC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4FBC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4FBC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4FBC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4FBC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4FD4 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4FD4_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4FD4_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4FD4_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D4FD4_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D50C4 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D50C4_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D50C4_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D50C4_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D50C4_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D50DC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D50DC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D50DC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D50DC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S082D50DC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089035AC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089035AC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089035AC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089035AC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089035AC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089A626C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089A626C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089A626C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089A626C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089A626C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089A629C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089A629C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089A629C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089A629C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089A629C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFC5C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFC5C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFC5C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFC5C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFC5C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFC8C = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFC8C_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFC8C_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFC8C_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFC8C_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFCBC = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFCBC_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFCBC_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFCBC_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089AFCBC_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089BFF64 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089BFF64_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089BFF64_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089BFF64_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S089BFF64_Attributes ,
 .callback=NULL
};
const struct Tileset gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S08A74F54 = {.isCompressed=TRUE ,
 .isSecondary=TRUE ,
 .tiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S08A74F54_Tiles ,
 .palettes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S08A74F54_Palettes ,
 .metatiles=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S08A74F54_Metatiles ,
 .metatileAttributes=gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4BB4S08A74F54_Attributes ,
 .callback=NULL
};

const struct Tileset gTileset_KantoAR_primary_f2e_AESTHETICRED_DS_NORMAL_V12_082D4A94 = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gTileset_KantoAR_primary_f2e_AESTHETICRED_DS_NORMAL_V12_082D4A94_Tiles, .palettes=gTileset_KantoAR_primary_f2e_AESTHETICRED_DS_NORMAL_V12_082D4A94_Palettes, .metatiles=gTileset_KantoAR_primary_f2e_AESTHETICRED_DS_NORMAL_V12_082D4A94_Metatiles, .metatileAttributes=gTileset_KantoAR_primary_f2e_AESTHETICRED_DS_NORMAL_V12_082D4A94_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_primary_f2e_AESTHETICRED_DS_NORMAL_V12_082D4BB4 = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gTileset_KantoAR_primary_f2e_AESTHETICRED_DS_NORMAL_V12_082D4BB4_Tiles, .palettes=gTileset_KantoAR_primary_f2e_AESTHETICRED_DS_NORMAL_V12_082D4BB4_Palettes, .metatiles=gTileset_KantoAR_primary_f2e_AESTHETICRED_DS_NORMAL_V12_082D4BB4_Metatiles, .metatileAttributes=gTileset_KantoAR_primary_f2e_AESTHETICRED_DS_NORMAL_V12_082D4BB4_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AAC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AAC_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AAC_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AAC_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AAC_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AC4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AC4_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AC4_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AC4_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AC4_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4ADC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4ADC_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4ADC_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4ADC_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4ADC_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AF4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AF4_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AF4_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AF4_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4AF4_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B0C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B0C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B0C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B0C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B0C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B24 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B24_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B24_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B24_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B24_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B3C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B3C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B3C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B3C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B3C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B54 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B54_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B54_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B54_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B54_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B6C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B6C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B6C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B6C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B6C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B84 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B84_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B84_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B84_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B84_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B9C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B9C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B9C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B9C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4B9C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4BFC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4BFC_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4BFC_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4BFC_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4BFC_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4D94 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4D94_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4D94_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4D94_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4D94_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4DC4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4DC4_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4DC4_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4DC4_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4DC4_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4DF4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4DF4_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4DF4_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4DF4_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4DF4_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E0C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E0C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E0C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E0C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E0C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E24 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E24_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E24_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E24_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E24_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E54 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E54_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E54_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E54_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4E54_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4FEC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4FEC_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4FEC_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4FEC_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D4FEC_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D5004 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D5004_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D5004_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D5004_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D5004_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D501C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D501C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D501C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D501C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D501C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D504C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D504C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D504C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D504C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D504C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D5064 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D5064_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D5064_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D5064_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D5064_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D507C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D507C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D507C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D507C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D507C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D50AC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D50AC_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D50AC_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D50AC_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4A94S082D50AC_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4BCC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4BCC_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4BCC_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4BCC_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4BCC_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4BE4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4BE4_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4BE4_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4BE4_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4BE4_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C2C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C2C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C2C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C2C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C2C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C44 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C44_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C44_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C44_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C44_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C5C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C5C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C5C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C5C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C5C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C74 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C74_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C74_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C74_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C74_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C8C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C8C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C8C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C8C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4C8C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CA4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CA4_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CA4_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CA4_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CA4_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CBC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CBC_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CBC_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CBC_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CBC_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CEC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CEC_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CEC_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CEC_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4CEC_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D04 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D04_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D04_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D04_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D04_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D1C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D1C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D1C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D1C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D1C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D34 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D34_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D34_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D34_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D34_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D4C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D4C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D4C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D4C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D4C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D64 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D64_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D64_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D64_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D64_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D7C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D7C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D7C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D7C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4D7C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E24 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E24_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E24_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E24_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E24_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E6C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E6C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E6C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E6C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E6C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E84 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E84_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E84_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E84_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E84_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E9C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E9C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E9C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E9C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4E9C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EB4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EB4_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EB4_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EB4_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EB4_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4ECC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4ECC_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4ECC_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4ECC_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4ECC_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EE4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EE4_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EE4_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EE4_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EE4_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EFC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EFC_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EFC_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EFC_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4EFC_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F14 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F14_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F14_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F14_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F14_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F2C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F2C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F2C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F2C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F2C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F44 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F44_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F44_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F44_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F44_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F5C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F5C_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F5C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F5C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F5C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F74 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F74_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F74_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F74_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F74_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F8C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4ECC_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F8C_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F8C_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4F8C_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4FA4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4FA4_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4FA4_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4FA4_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D4FA4_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D5034 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D5034_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D5034_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D5034_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D5034_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D5094 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D5094_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D5094_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D5094_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D5094_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D50C4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D50C4_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D50C4_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D50C4_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D50C4_Attributes, .callback=NULL };

const struct Tileset gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D50DC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D50DC_Tiles, .palettes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D50DC_Palettes, .metatiles=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D50DC_Metatiles, .metatileAttributes=gTileset_KantoAR_secondary_f2e_AESTHETICRED_DS_NORMAL_V12_P082D4BB4S082D50DC_Attributes, .callback=NULL };

// BEGIN WESLEY_UNOVA_HEADERS
const struct Tileset gTileset_UnovaGeneral_Primary =
{
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_UnovaGeneral_Primary,
    .palettes = gTilesetPalettes_UnovaGeneral_Primary,
    .metatiles = gMetatiles_UnovaGeneral_Primary,
    .metatileAttributes = gMetatileAttributes_UnovaGeneral_Primary,
    .callback = InitTilesetAnim_UnovaGeneral,
};

const struct Tileset gTileset_UnovaNuvema_Secondary =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_UnovaNuvema_Secondary,
    .palettes = gTilesetPalettes_UnovaNuvema_Secondary,
    .metatiles = gMetatiles_UnovaNuvema_Secondary,
    .metatileAttributes = gMetatileAttributes_UnovaNuvema_Secondary,
    .callback = NULL,
};
// END WESLEY_UNOVA_HEADERS

// BEGIN NUVEMA_COMPLETE_ORIGINALS
const struct Tileset gTileset_UnovaNuvemaOriginal1_Primary = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gTilesetTiles_UnovaNuvemaOriginal1_Primary, .palettes=gTilesetPalettes_UnovaNuvemaOriginal1_Primary, .metatiles=gMetatiles_UnovaNuvemaOriginal1_Primary, .metatileAttributes=gMetatileAttributes_UnovaNuvemaOriginal1_Primary, .callback=NULL };

const struct Tileset gTileset_UnovaNuvemaOriginal1_Secondary = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTilesetTiles_UnovaNuvemaOriginal1_Secondary, .palettes=gTilesetPalettes_UnovaNuvemaOriginal1_Secondary, .metatiles=gMetatiles_UnovaNuvemaOriginal1_Secondary, .metatileAttributes=gMetatileAttributes_UnovaNuvemaOriginal1_Secondary, .callback=NULL };

const struct Tileset gTileset_UnovaNuvemaOriginal2_Primary = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gTilesetTiles_UnovaNuvemaOriginal2_Primary, .palettes=gTilesetPalettes_UnovaNuvemaOriginal2_Primary, .metatiles=gMetatiles_UnovaNuvemaOriginal2_Primary, .metatileAttributes=gMetatileAttributes_UnovaNuvemaOriginal2_Primary, .callback=NULL };

const struct Tileset gTileset_UnovaNuvemaOriginal2_Secondary = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTilesetTiles_UnovaNuvemaOriginal2_Secondary, .palettes=gTilesetPalettes_UnovaNuvemaOriginal2_Secondary, .metatiles=gMetatiles_UnovaNuvemaOriginal2_Secondary, .metatileAttributes=gMetatileAttributes_UnovaNuvemaOriginal2_Secondary, .callback=NULL };

const struct Tileset gTileset_UnovaNuvemaOriginal3_Primary = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gTilesetTiles_UnovaNuvemaOriginal3_Primary, .palettes=gTilesetPalettes_UnovaNuvemaOriginal3_Primary, .metatiles=gMetatiles_UnovaNuvemaOriginal3_Primary, .metatileAttributes=gMetatileAttributes_UnovaNuvemaOriginal3_Primary, .callback=NULL };

const struct Tileset gTileset_UnovaNuvemaOriginal3_Secondary = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTilesetTiles_UnovaNuvemaOriginal3_Secondary, .palettes=gTilesetPalettes_UnovaNuvemaOriginal3_Secondary, .metatiles=gMetatiles_UnovaNuvemaOriginal3_Secondary, .metatileAttributes=gMetatileAttributes_UnovaNuvemaOriginal3_Secondary, .callback=NULL };
// END NUVEMA_COMPLETE_ORIGINALS

const struct Tileset gTileset_AccumulaFullSheetTest_Primary = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_AccumulaFullSheetTest_Primary,
    .palettes = gTilesetPalettes_AccumulaFullSheetTest_Primary,
    .metatiles = gMetatiles_AccumulaFullSheetTest_Primary,
    .metatileAttributes = gMetatileAttributes_AccumulaFullSheetTest_Primary,
    .callback = NULL,
};

const struct Tileset gTileset_AccumulaFullSheetTest_Secondary = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_AccumulaFullSheetTest_Secondary,
    .palettes = gTilesetPalettes_AccumulaFullSheetTest_Secondary,
    .metatiles = gMetatiles_AccumulaFullSheetTest_Secondary,
    .metatileAttributes = gMetatileAttributes_AccumulaFullSheetTest_Secondary,
    .callback = NULL,
};

const struct Tileset gTileset_NuvemaFullSheetTest_Primary = {
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_NuvemaFullSheetTest_Primary,
    .palettes = gTilesetPalettes_NuvemaFullSheetTest_Primary,
    .metatiles = gMetatiles_NuvemaFullSheetTest_Primary,
    .metatileAttributes = gMetatileAttributes_NuvemaFullSheetTest_Primary,
    .callback = NULL,
};

const struct Tileset gTileset_NuvemaFullSheetTest_Secondary = {
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_NuvemaFullSheetTest_Secondary,
    .palettes = gTilesetPalettes_NuvemaFullSheetTest_Secondary,
    .metatiles = gMetatiles_NuvemaFullSheetTest_Secondary,
    .metatileAttributes = gMetatileAttributes_NuvemaFullSheetTest_Secondary,
    .callback = NULL,
};

// BEGIN MERCURY_JOHTO_HEADERS
const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_082D4A94 = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_8dec85fd64d41a309191, .palettes=gMercury_Palettes_1f46eae24510bcb3d93a, .metatiles=gMercury_Metatiles_511644c45d47fc61a94d, .metatileAttributes=gMercury_Attributes_7e7a7719bd0bcdb974c8, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_082D4B6C = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_b2886fd9f2f1e8eba25a, .palettes=gMercury_Palettes_f4f8371cee26f853374d, .metatiles=gMercury_Metatiles_1714b91834c2431081d6, .metatileAttributes=gMercury_Attributes_bad1fda143ec7f0f810e, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_082D4BB4 = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_f25b7209b6df1562428b, .palettes=gMercury_Palettes_cebf428cee928610e59d, .metatiles=gMercury_Metatiles_3a0d7179ce2fd481141a, .metatileAttributes=gMercury_Attributes_e47f5f11973f839f4b01, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_082D4D1C = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_b2f115673dee97ff5f5f, .palettes=gMercury_Palettes_9e12da51dec676559c0f, .metatiles=gMercury_Metatiles_4b2daf64d8a982ea168b, .metatileAttributes=gMercury_Attributes_e9f458cbba7824727e18, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_082D4D4C = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_bf29d60dc5fae932d709, .palettes=gMercury_Palettes_80a126a595847c564e64, .metatiles=gMercury_Metatiles_9860fd3daf8d9fee3e49, .metatileAttributes=gMercury_Attributes_48799d11cff75ba69876, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_082D4E0C = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_1f56d2bd82cbf8888d23, .palettes=gMercury_Palettes_c508ed672338bebd1e6c, .metatiles=gMercury_Metatiles_639a84da1daf74447373, .metatileAttributes=gMercury_Attributes_c7814d2401045bc6de8f, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_082D4F5C = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_729bf3ec7a24b913ee44, .palettes=gMercury_Palettes_e77caa2f0985ecc5a99b, .metatiles=gMercury_Metatiles_888aed00c2a5d2387d99, .metatileAttributes=gMercury_Attributes_b1347865fcf82982a1f3, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_082D501C = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_d4847231fd7f7325ab4d, .palettes=gMercury_Palettes_78fda11bb5737192373d, .metatiles=gMercury_Metatiles_edd27b924e1cffb76adb, .metatileAttributes=gMercury_Attributes_d9a90429379c55709312, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_082D50AC = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_110b678923502b584415, .palettes=gMercury_Palettes_db1a77d4077aa74cc707, .metatiles=gMercury_Metatiles_f65176e92873801354fa, .metatileAttributes=gMercury_Attributes_8b19a7c97d66074acf0f, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_08A7A00C = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_8f02034cf4e6e7e5407b, .palettes=gMercury_Palettes_b7b03128b6bf040425f7, .metatiles=gMercury_Metatiles_10fcbe0fbe489e6193aa, .metatileAttributes=gMercury_Attributes_55ab137e56145b2a27e5, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_08A853C4 = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_08f78acb76fe955f2b9c, .palettes=gMercury_Palettes_d45f34645e24512c957f, .metatiles=gMercury_Metatiles_2f94d0197751abaf3f8d, .metatileAttributes=gMercury_Attributes_1a878956f69b28a7b523, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_08A92F3C = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_9a574123e889d14f15fc, .palettes=gMercury_Palettes_2ae3421404f6b8cba89d, .metatiles=gMercury_Metatiles_05700df025bdbe852c25, .metatileAttributes=gMercury_Attributes_7217ed09f71351624312, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_08B0343C = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_6ca27adec2eb46db0159, .palettes=gMercury_Palettes_1fa8026e6dba29f57c6a, .metatiles=gMercury_Metatiles_c3c5df38623e6a799a22, .metatileAttributes=gMercury_Attributes_7a66d549f122cb4f852d, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_08BC7F3C = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_4547fb8f5c5e4a27c16a, .palettes=gMercury_Palettes_00b43fcbb1d4433d2147, .metatiles=gMercury_Metatiles_0012e332a987435b039c, .metatileAttributes=gMercury_Attributes_02d8495147c249594193, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_08BF937C = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_f25b7209b6df1562428b, .palettes=gMercury_Palettes_93de1ff9c6fa056babc3, .metatiles=gMercury_Metatiles_dc31a1dc756dc0ae8e1f, .metatileAttributes=gMercury_Attributes_63eeff4f4239c78d88de, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_08DB849C = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_20f7c20f959dd55b3b2a, .palettes=gMercury_Palettes_a75db6a11fd7e57d2e33, .metatiles=gMercury_Metatiles_7e2871eb400cc1893dba, .metatileAttributes=gMercury_Attributes_671055e040be398d491b, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_08DBAC74 = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_452a93a9a7e4d24a114b, .palettes=gMercury_Palettes_3066606e2d69b01063fc, .metatiles=gMercury_Metatiles_8c3e3e7e4d9caafe56cf, .metatileAttributes=gMercury_Attributes_25547b8ea1d5cde5f83b, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_08DDD6A0 = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_a0a72c2794a69d42d163, .palettes=gMercury_Palettes_ff433f09ff7a2f4b79c2, .metatiles=gMercury_Metatiles_b25a086eccd450fa10f8, .metatileAttributes=gMercury_Attributes_59ea06c137d000b266bc, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_08DDD6D0 = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_a0a72c2794a69d42d163, .palettes=gMercury_Palettes_ff433f09ff7a2f4b79c2, .metatiles=gMercury_Metatiles_b25a086eccd450fa10f8, .metatileAttributes=gMercury_Attributes_59ea06c137d000b266bc, .callback=NULL };

const struct Tileset gTileset_Mercury_primary_f2e_MERCURY_08DDD700 = { .isCompressed=TRUE, .isSecondary=FALSE, .tiles=gMercury_Tiles_a0a72c2794a69d42d163, .palettes=gMercury_Palettes_ff433f09ff7a2f4b79c2, .metatiles=gMercury_Metatiles_06a4be3bac5972153dfb, .metatileAttributes=gMercury_Attributes_ddf980e2fb25963e8f30, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4A94S082D4BFC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_3f794dfb26f31ebef3fc, .palettes=gMercury_Palettes_597d84227696c95065be, .metatiles=gMercury_Metatiles_d055e55134c1dd263c0a, .metatileAttributes=gMercury_Attributes_f88d9c7e264b88fab4ff, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4A94S082D4DF4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_073c3741d6a2b6e4047a, .palettes=gMercury_Palettes_6282421812dbaf801a2b, .metatiles=gMercury_Metatiles_c8a272571483b3ba4d11, .metatileAttributes=gMercury_Attributes_3271581b7eb1f0a6eb77, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4A94S08EF09AC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_1989835e9c2b90018f41, .palettes=gMercury_Palettes_c1af1f32472931e85063, .metatiles=gMercury_Metatiles_ae4f9c5adad9d2aba0c3, .metatileAttributes=gMercury_Attributes_824b25432d056312c27e, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS082D4B54 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_a3622260f4d7e522d2dd, .palettes=gMercury_Palettes_0d7ff272762d44518e66, .metatiles=gMercury_Metatiles_e45bd99f1e73e6a3f4a0, .metatileAttributes=gMercury_Attributes_a715162e0cb962121a7c, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS082D4B84 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_d96b89f7d7f0724f7fdd, .palettes=gMercury_Palettes_66591f9d43f38bf53bb1, .metatiles=gMercury_Metatiles_35d164fd1e71b42b8d5f, .metatileAttributes=gMercury_Attributes_b0a53aebe434741f21f1, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS082D4BFC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_1c9d8f4f2d92e6ba0de5, .palettes=gMercury_Palettes_ffe313c709b2cdc28292, .metatiles=gMercury_Metatiles_7999d30b23e0b505c2de, .metatileAttributes=gMercury_Attributes_bc7afceb7a85dd963269, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS082D4C2C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_1a4bdbabe1da10cdd06d, .palettes=gMercury_Palettes_e6110844ccf323261dcc, .metatiles=gMercury_Metatiles_5955a2abaeb25ea39665, .metatileAttributes=gMercury_Attributes_d16d2dbb28dc082c62f6, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS082D4DC4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_b54359776351aa6f4913, .palettes=gMercury_Palettes_d6cf2379e8e72b332a1e, .metatiles=gMercury_Metatiles_30a268037ffb1eb86088, .metatileAttributes=gMercury_Attributes_0a2acadb6b6e53b04dc3, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS082D4F14 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_54a72592cbca5e7dd3dc, .palettes=gMercury_Palettes_e18742b5d903319e07b5, .metatiles=gMercury_Metatiles_69bf25e07f69a1b1efba, .metatileAttributes=gMercury_Attributes_e1bc272ee04c692f24fe, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS082D4F8C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_cc98ceeda03349bb4b76, .palettes=gMercury_Palettes_2ca4df22029eee380375, .metatiles=gMercury_Metatiles_952be449c2c64df5abd2, .metatileAttributes=gMercury_Attributes_b00b8e7fee1edad9fb43, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS082D504C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_1efe4927c9c50aa2902b, .palettes=gMercury_Palettes_f9f1e592d1326d688962, .metatiles=gMercury_Metatiles_e6500f38d58843804dc1, .metatileAttributes=gMercury_Attributes_c5fc587932ca782cfc61, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS082D5064 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_350a7baedf223a3b3961, .palettes=gMercury_Palettes_94603736c428d77e0fc2, .metatiles=gMercury_Metatiles_1afb5efb2087a320f0f5, .metatileAttributes=gMercury_Attributes_bee926a097b635f440f8, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS082D507C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_739a6efc0e63bc5af36f, .palettes=gMercury_Palettes_38cf958aa2bfad8a176b, .metatiles=gMercury_Metatiles_65f3588fb2f375611f5b, .metatileAttributes=gMercury_Attributes_32d0f38fab33aa400593, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS082D5094 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_89ad87e74eefb3bbe971, .palettes=gMercury_Palettes_cfdb120306c49eedf817, .metatiles=gMercury_Metatiles_59d94b194e87d4499a25, .metatileAttributes=gMercury_Attributes_ba758561e42a7189402e, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS082D50AC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_4f246501b8031da28682, .palettes=gMercury_Palettes_301a638a706c14987339, .metatiles=gMercury_Metatiles_721c712e6074094d6b70, .metatileAttributes=gMercury_Attributes_c9d25da69379294121bd, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS08A18D04 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_ff6c2469022faee69df5, .palettes=gMercury_Palettes_47db2ab45516f15eef05, .metatiles=gMercury_Metatiles_7ba6f71fe0278bca7523, .metatileAttributes=gMercury_Attributes_9ad896c7445b900e24ce, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS08A375BC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_3ae3c6874003c0c880f8, .palettes=gMercury_Palettes_480719e0bcd58b93e41f, .metatiles=gMercury_Metatiles_397b0b3807db274f4f93, .metatileAttributes=gMercury_Attributes_aa8b7da24c44b815a7f3, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS08A70124 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_c2373d361b3b1a248f35, .palettes=gMercury_Palettes_4e69f3c5912fabdab074, .metatiles=gMercury_Metatiles_83d1a7f8cd2be41df35f, .metatileAttributes=gMercury_Attributes_bc54974cc7231058ef83, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS08A75164 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_42ad69c0f7116c1e9148, .palettes=gMercury_Palettes_74316ad682d7c5b23cca, .metatiles=gMercury_Metatiles_1faed0da6065ed1c61d6, .metatileAttributes=gMercury_Attributes_1557154a14421830f1a9, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS08BC11BC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_2bebfe8bfe6c254192c5, .palettes=gMercury_Palettes_5758c30c5d007242510d, .metatiles=gMercury_Metatiles_56a5f8642c701420c14b, .metatileAttributes=gMercury_Attributes_58d61a13531b2eab9cb9, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS08C16524 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_2098acbdf1b7c6f19716, .palettes=gMercury_Palettes_e34b0b1b714a3a748ab3, .metatiles=gMercury_Metatiles_e2a96f217dcdb8b1dfd0, .metatileAttributes=gMercury_Attributes_b739dac6012177695224, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS08D55064 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_471dbe85c3f94b3c36e9, .palettes=gMercury_Palettes_604bb521cd7df703ffc1, .metatiles=gMercury_Metatiles_11ab0f1f27108affa0e9, .metatileAttributes=gMercury_Attributes_017fbcf930d2b612bba6, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS08D5564C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_22ed46824d3be5d1a732, .palettes=gMercury_Palettes_1e8fa8136336144d68aa, .metatiles=gMercury_Metatiles_931e5f55ad7ffb6d099c, .metatileAttributes=gMercury_Attributes_6dd931e5b279c2f7e4e3, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS08D5B094 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_5a8adc983e8ae9bf1726, .palettes=gMercury_Palettes_c48f4a36ea5d62f8b045, .metatiles=gMercury_Metatiles_7c8e4f97bfdd1ef04a42, .metatileAttributes=gMercury_Attributes_41b287a7f352252df62b, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS08DA310C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_3d93c5741ba7157f37cf, .palettes=gMercury_Palettes_bb050bf929aaa9079953, .metatiles=gMercury_Metatiles_a0739179f1ae9fcab5b2, .metatileAttributes=gMercury_Attributes_e65f33da73208e697a55, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4B6CS08EF09AC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_411b1cee7f7be34d960e, .palettes=gMercury_Palettes_6441a6923235581b39fc, .metatiles=gMercury_Metatiles_666401ac38f0a219f8a6, .metatileAttributes=gMercury_Attributes_498cd37211e283db9b3d, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4BCC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_ec91abfadfba9874799e, .palettes=gMercury_Palettes_04485defdee49fae4714, .metatiles=gMercury_Metatiles_a6c8686acc6d42eff849, .metatileAttributes=gMercury_Attributes_0d8b8d2694584860c5e3, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4BE4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_8280fe6ca54fa918d5a5, .palettes=gMercury_Palettes_7abbcb82b4f4a317b5d5, .metatiles=gMercury_Metatiles_a40a9994d60ed7ca9f0a, .metatileAttributes=gMercury_Attributes_8f7b8b6417ecb9e5be7d, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4C2C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_8ced17869a9d036437a2, .palettes=gMercury_Palettes_6b1075fc3fb9dcb25101, .metatiles=gMercury_Metatiles_5ecb50156008a6989b06, .metatileAttributes=gMercury_Attributes_55da51bec123a492bb28, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4C44 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_549b0e70430ee1ba24eb, .palettes=gMercury_Palettes_e783d9a50de644895950, .metatiles=gMercury_Metatiles_374ac64d8f1f98b443ed, .metatileAttributes=gMercury_Attributes_de90ecc9935897c3621a, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4C5C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_f17ab37944d9f21efadb, .palettes=gMercury_Palettes_c71817f68da1d5c51796, .metatiles=gMercury_Metatiles_1424aa229bf0cc819b10, .metatileAttributes=gMercury_Attributes_7e381d775cdb68812338, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4C74 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_5f81e83f8779ba023063, .palettes=gMercury_Palettes_5804dc7b10f02df2f7c8, .metatiles=gMercury_Metatiles_1b1cd0d2072fca7a227f, .metatileAttributes=gMercury_Attributes_91148b2b0b3216faefe4, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4C8C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_f367de2a426d4cd7b5fa, .palettes=gMercury_Palettes_e8c1ab140c66cc0f47d0, .metatiles=gMercury_Metatiles_e4b0c97ed2fe58900b7e, .metatileAttributes=gMercury_Attributes_5992677e83ccd7d30155, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4CA4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_b5cf1881ea1ff162fa93, .palettes=gMercury_Palettes_13d8fdf0daacad2968ca, .metatiles=gMercury_Metatiles_a9c5de59281753db7a25, .metatileAttributes=gMercury_Attributes_8359e156ce5790df3929, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4D04 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_1243c870d6afab6da106, .palettes=gMercury_Palettes_95e2fe7aff523f182ca0, .metatiles=gMercury_Metatiles_aeb0d17b0c95b63ee96f, .metatileAttributes=gMercury_Attributes_39287ff8ac7fd00861ca, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4D7C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_0ac2708b253afdebe187, .palettes=gMercury_Palettes_c3936fa6c5528083c22c, .metatiles=gMercury_Metatiles_9daa43f7d6101ae6cbd1, .metatileAttributes=gMercury_Attributes_f70d2945cebfb457695e, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4DDC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_3b80e7379f6e079c36aa, .palettes=gMercury_Palettes_7aa38284a60e2351e150, .metatiles=gMercury_Metatiles_556cbea5953f07dcf84e, .metatileAttributes=gMercury_Attributes_ba7e9b6116371b417cc4, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4E24 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_d41e26c76a0b7233cf0f, .palettes=gMercury_Palettes_f39c2d79c57509957946, .metatiles=gMercury_Metatiles_2c31b61d794e50af0b96, .metatileAttributes=gMercury_Attributes_dc2f1b8f8c2879b71ec9, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4E84 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_e39e4940f2bf846dfa1f, .palettes=gMercury_Palettes_0080cd66474cc7298428, .metatiles=gMercury_Metatiles_84cf3b7b38caabe634a5, .metatileAttributes=gMercury_Attributes_5718c2b239a859c03a57, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4EB4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_e0a419c37d6031aca55c, .palettes=gMercury_Palettes_ddb48b4b7e9df7829d42, .metatiles=gMercury_Metatiles_8ee9271d4c7bd9505056, .metatileAttributes=gMercury_Attributes_dd786aef8f098843cead, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4EFC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_1eeeb83bdde1022e5a19, .palettes=gMercury_Palettes_04c04fe0726db5770651, .metatiles=gMercury_Metatiles_494138d189d30d426348, .metatileAttributes=gMercury_Attributes_76f2063ab99245701dbf, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4F2C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_389f8c27978f347a9b2e, .palettes=gMercury_Palettes_386dbc6116e1d286ad7b, .metatiles=gMercury_Metatiles_ad98c4bcc16234ec8557, .metatileAttributes=gMercury_Attributes_f7a097b0aa5da84db2c2, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4F5C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_a88e0a944543f353b601, .palettes=gMercury_Palettes_bd4b26b00f8339f51574, .metatiles=gMercury_Metatiles_e00cb911107ea0c8d686, .metatileAttributes=gMercury_Attributes_c06ec603b1f040c60740, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D4F74 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_3f6dc27cb75cb90deb4d, .palettes=gMercury_Palettes_7918d47ca8ca358a0260, .metatiles=gMercury_Metatiles_937f1cc22bfc4f45fcc1, .metatileAttributes=gMercury_Attributes_91e171dc26bad852e6b0, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D50C4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_a941c12329ede92f988a, .palettes=gMercury_Palettes_03b0f2f33d7860a5c59c, .metatiles=gMercury_Metatiles_7fdec336f2925508e979, .metatileAttributes=gMercury_Attributes_aecfdb026f7b3b0f1d98, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S082D50DC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_9b6f04c371431842f6e1, .palettes=gMercury_Palettes_a0e6fbd4925c0be4a355, .metatiles=gMercury_Metatiles_1a262f090d0ae0a5de86, .metatileAttributes=gMercury_Attributes_4e6986b72d1da171c976, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08A0017C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_5d741e2af8c2ae76e836, .palettes=gMercury_Palettes_386b66f7ef0cbc4802f2, .metatiles=gMercury_Metatiles_3b0bb657f939c4762313, .metatileAttributes=gMercury_Attributes_cbe691dc539ce2ed86fd, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08A001AC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_f51a1bb633abe328135a, .palettes=gMercury_Palettes_626647fe238e7553baa5, .metatiles=gMercury_Metatiles_6579e9f92334e0107a39, .metatileAttributes=gMercury_Attributes_4831c23006a2570c7a40, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08A5543C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_7e1b22c1c195d7a601a4, .palettes=gMercury_Palettes_24c0de4ff23fde30e44f, .metatiles=gMercury_Metatiles_7e27a08d823880a833fb, .metatileAttributes=gMercury_Attributes_d3345452e23d334bfe28, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08A64484 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_40b0bb22bede9e90d490, .palettes=gMercury_Palettes_19cef54770e41cd3eea3, .metatiles=gMercury_Metatiles_c8b7ef26ffad12156aae, .metatileAttributes=gMercury_Attributes_f7bf31317478762d346d, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08A882EC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_4a5f04186d41e6d3a9ba, .palettes=gMercury_Palettes_0b3559be29a33b179ebd, .metatiles=gMercury_Metatiles_2a071d5f9b6cc4ea6ae2, .metatileAttributes=gMercury_Attributes_c3bbdd35b41502b6d4e7, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08AD30DC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_c6407ac88f74fed43abf, .palettes=gMercury_Palettes_49aba72da66f189b376d, .metatiles=gMercury_Metatiles_e0664d4edbbde51422e1, .metatileAttributes=gMercury_Attributes_2a40acc2d6ec20bb7ccc, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08ADBF5C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_035b6463315a3b0c649c, .palettes=gMercury_Palettes_e77fff934f5c1b94794d, .metatiles=gMercury_Metatiles_319f0c4e11d3582c8912, .metatileAttributes=gMercury_Attributes_1b665f72e4a9eb7f1319, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08B031CC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_f03ddd4aca9920f283ef, .palettes=gMercury_Palettes_a00ea8dd6baf819cdf8a, .metatiles=gMercury_Metatiles_16802e8ac1b6276f2657, .metatileAttributes=gMercury_Attributes_96aeca1d2b29cbe9eea6, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08B031FC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_773fa8f5c1dfaa37d24d, .palettes=gMercury_Palettes_62845107f3967632c871, .metatiles=gMercury_Metatiles_7aa43b2428541709ec40, .metatileAttributes=gMercury_Attributes_3f49b6b1c9dc093cb478, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08B04D14 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_17b7d1426da07eb59d4c, .palettes=gMercury_Palettes_dc79ea5607f91024727c, .metatiles=gMercury_Metatiles_fd4e292bcceaa7199c8c, .metatileAttributes=gMercury_Attributes_a97ec0b306b7d1f8174d, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08B53584 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_d16e249905817cd3f55c, .palettes=gMercury_Palettes_f8a96ffb5af14a2a5951, .metatiles=gMercury_Metatiles_e5af57f913635b46448e, .metatileAttributes=gMercury_Attributes_abbdbe69eb5a08be00ab, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08BD4F5C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_aa78b4530b3cd2f8bcc6, .palettes=gMercury_Palettes_e416dd8a071c18d8d493, .metatiles=gMercury_Metatiles_11ba322fcdfae76bac8e, .metatileAttributes=gMercury_Attributes_b958b4cfa2b3252c063b, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08BF118C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_818fdeb80a96fc5b1e06, .palettes=gMercury_Palettes_b67e8b283bf9dc2c29d1, .metatiles=gMercury_Metatiles_cccb4e431b979ac79e16, .metatileAttributes=gMercury_Attributes_a68510322f1e5ff08803, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4BB4S08DB0E64 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_4417998191ade053eba1, .palettes=gMercury_Palettes_2f952e536103ec887768, .metatiles=gMercury_Metatiles_a2ebf581f9d55d7f3e16, .metatileAttributes=gMercury_Attributes_f17e1aec7e138ac457a0, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4D1CS082D4D34 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_76bda885541a2be5929d, .palettes=gMercury_Palettes_69aadc09585dca57d57c, .metatiles=gMercury_Metatiles_e59e1eb9cafcb0663424, .metatileAttributes=gMercury_Attributes_883a1d520434045a478f, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4D1CS08BEC20C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_5f8ab1e0dbfa034a8333, .palettes=gMercury_Palettes_b820aea91d40dd20c1c7, .metatiles=gMercury_Metatiles_eee86f5114691a325af3, .metatileAttributes=gMercury_Attributes_af7b10272b77592bf4cb, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4D4CS082D4BFC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_50bd99f45bd59c55e779, .palettes=gMercury_Palettes_96ca344aeabc86558a8c, .metatiles=gMercury_Metatiles_fdc4bea21dfd379e9eff, .metatileAttributes=gMercury_Attributes_7b799d17d21c1e577d33, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4D4CS08EF09AC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_0b83d53450fe825507e3, .palettes=gMercury_Palettes_ff7eb6e01d773d8da88b, .metatiles=gMercury_Metatiles_dbf16b99a9ec505f6ce4, .metatileAttributes=gMercury_Attributes_b9b5917631ffa36a7af7, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4E0CS082D4BFC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_8499c2ada1d6d56e94bf, .palettes=gMercury_Palettes_695b27c1242341932e41, .metatiles=gMercury_Metatiles_c8b550d6a2ea362d1241, .metatileAttributes=gMercury_Attributes_d75028065b1440aad831, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4F5CS082D4CBC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_5423b836b023dcece5aa, .palettes=gMercury_Palettes_b4a6f9b17a2c385ca5df, .metatiles=gMercury_Metatiles_123e698d756063f578cb, .metatileAttributes=gMercury_Attributes_2e3d2aa3e24efbb22b8a, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4F5CS082D4D64 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_2f051785720a16906ddb, .palettes=gMercury_Palettes_0c9afadd97bb21d0e257, .metatiles=gMercury_Metatiles_53385605de623391ce6c, .metatileAttributes=gMercury_Attributes_0e11a60b4d0bee380209, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4F5CS082D4D94 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_2fb5e789555c1faca67b, .palettes=gMercury_Palettes_47693388f0aae4129c4a, .metatiles=gMercury_Metatiles_9f8499ff34b680867c3b, .metatileAttributes=gMercury_Attributes_1a5a095af0ce6b3399fb, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4F5CS082D4E54 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_b501884f898b618a324c, .palettes=gMercury_Palettes_acaec8ef5e0761e062d7, .metatiles=gMercury_Metatiles_86ba80d44bd591b55c60, .metatileAttributes=gMercury_Attributes_2c83a2bcd83e2cf56c41, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4F5CS082D4E6C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_3aa258ad63508df4f219, .palettes=gMercury_Palettes_137890fb3bf2f9b1ede4, .metatiles=gMercury_Metatiles_2e00ea5f2a7e0292eaf2, .metatileAttributes=gMercury_Attributes_d9f8967d98020031e418, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4F5CS082D4F44 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_78013b6a6ba71878f5c9, .palettes=gMercury_Palettes_2273ca6cf5600912940f, .metatiles=gMercury_Metatiles_b1a43474d275b05111c6, .metatileAttributes=gMercury_Attributes_0ea249c02b3789ed6d32, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4F5CS08A15524 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_4855a3f412dbec26b4f6, .palettes=gMercury_Palettes_d3892ffd238f994a23dd, .metatiles=gMercury_Metatiles_a5658f5d5d29ed3d4414, .metatileAttributes=gMercury_Attributes_034234cb34f3d505c67c, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4F5CS08A33524 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_ddd83907162371028572, .palettes=gMercury_Palettes_d772fba15b41e640fa05, .metatiles=gMercury_Metatiles_9032d41f0d3abb310c7d, .metatileAttributes=gMercury_Attributes_a7b0e280837416ca1be4, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4F5CS08A511C4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_6234e4c27dfa85ad1984, .palettes=gMercury_Palettes_0947f46e5a983ec12736, .metatiles=gMercury_Metatiles_1a70a196ab53273d36f4, .metatileAttributes=gMercury_Attributes_7ea30626eb02bb5aaae1, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4F5CS08A553DC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_67832602e049ef5fdf07, .palettes=gMercury_Palettes_c38f16ec8f5d1a0a319c, .metatiles=gMercury_Metatiles_dc17010782a9553464d5, .metatileAttributes=gMercury_Attributes_7c560d021f4c5b1c6624, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D4F5CS08A882BC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_c7c097c40d677f6daa28, .palettes=gMercury_Palettes_9a3f8e5e88f0ce180c9b, .metatiles=gMercury_Metatiles_5f68149b933d51aace0e, .metatileAttributes=gMercury_Attributes_1d01a9b2ecf8b6a546ec, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D501CS082D4FA4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_f199a853c11afb017691, .palettes=gMercury_Palettes_781d16eb8ac9b190b81d, .metatiles=gMercury_Metatiles_eb0694d2e33a00be5fbe, .metatileAttributes=gMercury_Attributes_7d551e21500819f002b9, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D501CS082D4FEC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_6aa041b7ab8d74d8efb4, .palettes=gMercury_Palettes_c7023060652be311ac54, .metatiles=gMercury_Metatiles_71fe656bcf0e4f768e11, .metatileAttributes=gMercury_Attributes_00bbdd8a68bf77f35857, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D501CS082D5004 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_b924ea3cb8e534a5e8f0, .palettes=gMercury_Palettes_d67480a7572bc8f0b3f9, .metatiles=gMercury_Metatiles_99d9314bdaa078fdd7a0, .metatileAttributes=gMercury_Attributes_2440c5ddcd41b7024bc0, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D501CS082D5034 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_66981ee2b753af88ff2f, .palettes=gMercury_Palettes_3a56e8e0ca7b593c4e52, .metatiles=gMercury_Metatiles_83ae2f5a03395924901c, .metatileAttributes=gMercury_Attributes_670bf940651721abee0d, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D501CS08A2A6D4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_078279f1d118728962c1, .palettes=gMercury_Palettes_dcd33a115470d93c4428, .metatiles=gMercury_Metatiles_23d7f16eda640ef1d204, .metatileAttributes=gMercury_Attributes_6dae6f6472536d704e70, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D501CS08D5B094 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_1dbd37d9b699f60b546a, .palettes=gMercury_Palettes_ca05c28d924003551cff, .metatiles=gMercury_Metatiles_1858c6bc67b3b1410155, .metatileAttributes=gMercury_Attributes_4fdc29c1cc6e30b0eb82, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D501CS08DB0C3C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_6063ca947f7abab1e4b5, .palettes=gMercury_Palettes_9b74385b1eb8e5ff2706, .metatiles=gMercury_Metatiles_eb34f6cdd7842d859ce3, .metatileAttributes=gMercury_Attributes_9603d23b146059288092, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P082D50ACS082D4BFC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_8499c2ada1d6d56e94bf, .palettes=gMercury_Palettes_fbc2eb00d0c34ca239f5, .metatiles=gMercury_Metatiles_6c9ede925f541dac9466, .metatileAttributes=gMercury_Attributes_4c226e802cd62609e4cc, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P08A7A00CS08A27014 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_b7075dc86da780bfa873, .palettes=gMercury_Palettes_e8beb77eb57a58f63f1a, .metatiles=gMercury_Metatiles_d728e741e27a98a76b5c, .metatileAttributes=gMercury_Attributes_c027a6792221633d1659, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P08A853C4S08A5540C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_314677efe3876b416083, .palettes=gMercury_Palettes_89c6f530091627a6838f, .metatiles=gMercury_Metatiles_a570bb22b720cfbdb1b6, .metatileAttributes=gMercury_Attributes_ca4149bc17643c9d597a, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P08A92F3CS08A92EDC = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_5eca6ce6c96ab736efd6, .palettes=gMercury_Palettes_a56b1990c01059f28704, .metatiles=gMercury_Metatiles_155a1baeba4ff24126cc, .metatileAttributes=gMercury_Attributes_2ee2102ec8717b722e4d, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P08B0343CS08B042C4 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_eb9555b4b799ca8c96fa, .palettes=gMercury_Palettes_953461f7f369a4d1ad88, .metatiles=gMercury_Metatiles_f8f3106926a5fa5bb625, .metatileAttributes=gMercury_Attributes_a73dc43733f6bd30b334, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P08BC7F3CS08BC7F9C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_b7075dc86da780bfa873, .palettes=gMercury_Palettes_076a27c79e5ace2a3d47, .metatiles=gMercury_Metatiles_caa62f46a8ae14f419b0, .metatileAttributes=gMercury_Attributes_1f5675d0f1fd2dc3dda0, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P08BF937CS08BF340C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_2f5a0f8fbc072228b3e7, .palettes=gMercury_Palettes_b8406d24def7b069749b, .metatiles=gMercury_Metatiles_ccb0763c00e4a804b166, .metatileAttributes=gMercury_Attributes_cbb8c97b9c615921ebf2, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P08DB849CS08DB3D74 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_693cf39edf34ff216a99, .palettes=gMercury_Palettes_c380d7ea97b4df569ce4, .metatiles=gMercury_Metatiles_ddefafa3bcb24aa992bf, .metatileAttributes=gMercury_Attributes_556afd956ab6d6f41f1a, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P08DBAC74S08DB4D64 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_830c8dbee0f2949c2b4b, .palettes=gMercury_Palettes_8be6ab52cd0a544236e9, .metatiles=gMercury_Metatiles_58538fd9753b180e2d42, .metatileAttributes=gMercury_Attributes_51386b35873b21890bb3, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P08DDD6A0S082D4C5C = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_0e79921740ea54c0407d, .palettes=gMercury_Palettes_94efb0b74133da80154d, .metatiles=gMercury_Metatiles_5f7fd5404ac0273bef6b, .metatileAttributes=gMercury_Attributes_c3f9c4fe1c8183712d1d, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P08DDD6D0S08DDD6B8 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_819bbc40a3bfb21eb8b6, .palettes=gMercury_Palettes_2a2c6d5e6fdf30ef7013, .metatiles=gMercury_Metatiles_f8f3106926a5fa5bb625, .metatileAttributes=gMercury_Attributes_a73dc43733f6bd30b334, .callback=NULL };

const struct Tileset gTileset_Mercury_secondary_f2e_MERCURY_P08DDD700S08DDD6E8 = { .isCompressed=TRUE, .isSecondary=TRUE, .tiles=gMercury_Tiles_819bbc40a3bfb21eb8b6, .palettes=gMercury_Palettes_2a2c6d5e6fdf30ef7013, .metatiles=gMercury_Metatiles_f8f3106926a5fa5bb625, .metatileAttributes=gMercury_Attributes_a73dc43733f6bd30b334, .callback=NULL };
// END MERCURY_JOHTO_HEADERS

// BEGIN HNS_CANARY
void HnSCanary_InitTilesetAnim_JohtoGeneral(void);
void HnSCanary_InitTilesetAnim_EcruteakTheater(void);
const struct Tileset gTileset_HnSCanary_Johto_General_Hns = {.isCompressed=FALSE, .isSecondary=FALSE, .tiles=gHnSCanary_Johto_General_Hns_Tiles, .palettes=gHnSCanary_Johto_General_Hns_Palettes, .metatiles=gHnSCanary_Johto_General_Hns_Metatiles, .metatileAttributes=gHnSCanary_Johto_General_Hns_Attributes, .callback=HnSCanary_InitTilesetAnim_JohtoGeneral};
const struct Tileset gTileset_HnSCanary_Johto_General_Hns__NewBarkTown_Hns = {.isCompressed=FALSE, .isSecondary=TRUE, .tiles=gHnSCanary_Johto_General_Hns__NewBarkTown_Hns_Tiles, .palettes=gHnSCanary_Johto_General_Hns__NewBarkTown_Hns_Palettes, .metatiles=gHnSCanary_Johto_General_Hns__NewBarkTown_Hns_Metatiles, .metatileAttributes=gHnSCanary_Johto_General_Hns__NewBarkTown_Hns_Attributes, .callback=NULL};
const struct Tileset gTileset_HnSCanary_Johto_General_Hns__CherrygroveCity_Hns = {.isCompressed=FALSE, .isSecondary=TRUE, .tiles=gHnSCanary_Johto_General_Hns__CherrygroveCity_Hns_Tiles, .palettes=gHnSCanary_Johto_General_Hns__CherrygroveCity_Hns_Palettes, .metatiles=gHnSCanary_Johto_General_Hns__CherrygroveCity_Hns_Metatiles, .metatileAttributes=gHnSCanary_Johto_General_Hns__CherrygroveCity_Hns_Attributes, .callback=NULL};
const struct Tileset gTileset_HnSCanary_Johto_Building_Hns = {.isCompressed=FALSE, .isSecondary=FALSE, .tiles=gHnSCanary_Johto_Building_Hns_Tiles, .palettes=gHnSCanary_Johto_Building_Hns_Palettes, .metatiles=gHnSCanary_Johto_Building_Hns_Metatiles, .metatileAttributes=gHnSCanary_Johto_Building_Hns_Attributes, .callback=NULL};
const struct Tileset gTileset_HnSCanary_Johto_Building_Hns__Gate_Standard_Hns = {.isCompressed=FALSE, .isSecondary=TRUE, .tiles=gHnSCanary_Johto_Building_Hns__Gate_Standard_Hns_Tiles, .palettes=gHnSCanary_Johto_Building_Hns__Gate_Standard_Hns_Palettes, .metatiles=gHnSCanary_Johto_Building_Hns__Gate_Standard_Hns_Metatiles, .metatileAttributes=gHnSCanary_Johto_Building_Hns__Gate_Standard_Hns_Attributes, .callback=NULL};
const struct Tileset gTileset_HnSCanary_Johto_General_Hns__VioletCity_Hns = {.isCompressed=FALSE, .isSecondary=TRUE, .tiles=gHnSCanary_Johto_General_Hns__VioletCity_Hns_Tiles, .palettes=gHnSCanary_Johto_General_Hns__VioletCity_Hns_Palettes, .metatiles=gHnSCanary_Johto_General_Hns__VioletCity_Hns_Metatiles, .metatileAttributes=gHnSCanary_Johto_General_Hns__VioletCity_Hns_Attributes, .callback=NULL};
const struct Tileset gTileset_HnSCanary_Johto_Building_Hns__JohtoMart_Hns = {.isCompressed=FALSE, .isSecondary=TRUE, .tiles=gHnSCanary_Johto_Building_Hns__JohtoMart_Hns_Tiles, .palettes=gHnSCanary_Johto_Building_Hns__JohtoMart_Hns_Palettes, .metatiles=gHnSCanary_Johto_Building_Hns__JohtoMart_Hns_Metatiles, .metatileAttributes=gHnSCanary_Johto_Building_Hns__JohtoMart_Hns_Attributes, .callback=NULL};
const struct Tileset gTileset_HnSCanary_Johto_Building_Hns__EcruteakTheater_Hns = {.isCompressed=FALSE, .isSecondary=TRUE, .tiles=gHnSCanary_Johto_Building_Hns__EcruteakTheater_Hns_Tiles, .palettes=gHnSCanary_Johto_Building_Hns__EcruteakTheater_Hns_Palettes, .metatiles=gHnSCanary_Johto_Building_Hns__EcruteakTheater_Hns_Metatiles, .metatileAttributes=gHnSCanary_Johto_Building_Hns__EcruteakTheater_Hns_Attributes, .callback=HnSCanary_InitTilesetAnim_EcruteakTheater};
// END HNS_CANARY

/* HNS_REGION_GENERATED: visual assets only. */
void HnsRegion640_InitTilesetAnim_JohtoGeneral(void);
const struct Tileset gTileset_HnsRegion_Bea3d6307fbf5d9ae = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gHnsRegion_Tiles_bbc911ce3859ec85a4a9, .palettes=gHnsRegion_Bea3d6307fbf5d9ae_Palettes, .metatiles=gHnsRegion_Metatiles_9b9dbebacd6301537695, .metatileAttributes=gHnsRegion_Attributes_f2e16e762ca974dbae49, .callback=HnsRegion640_InitTilesetAnim_JohtoGeneral};
const struct Tileset gTileset_HnsRegion_Bc3569b82be797477 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_2b2355a6b0ee7b0f3f58, .palettes=gHnsRegion_Bc3569b82be797477_Palettes, .metatiles=gHnsRegion_Metatiles_c3df8f942ba4f2a33dce, .metatileAttributes=gHnsRegion_Attributes_b41eb2f91ca7dcc62cda, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bfab5bdd11d4b7fd3 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_1d734a7dc5bc3f59890b, .palettes=gHnsRegion_Bfab5bdd11d4b7fd3_Palettes, .metatiles=gHnsRegion_Metatiles_4398e17877699d97e120, .metatileAttributes=gHnsRegion_Attributes_61a75f41942ef04d2f60, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bae1a0a70f9ed06c0 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_9fa504cd464d92371165, .palettes=gHnsRegion_Bae1a0a70f9ed06c0_Palettes, .metatiles=gHnsRegion_Metatiles_fb243bf3ac70ea66dc36, .metatileAttributes=gHnsRegion_Attributes_54f68b02bc30ae3955f3, .callback=NULL};
void HnsRegion640_InitTilesetAnim_JohtoGeneral(void);
const struct Tileset gTileset_HnsRegion_B8851c7de3e487b48 = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gHnsRegion_Tiles_a0a1b33f1924171360c7, .palettes=gHnsRegion_B8851c7de3e487b48_Palettes, .metatiles=gHnsRegion_Metatiles_c3874f85739c3fc91900, .metatileAttributes=gHnsRegion_Attributes_1b08bc931f0b88e0f9e9, .callback=HnsRegion640_InitTilesetAnim_JohtoGeneral};
const struct Tileset gTileset_HnsRegion_Bedbcd3552ce6b27a = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_e09d449894495b0d3499, .palettes=gHnsRegion_Bedbcd3552ce6b27a_Palettes, .metatiles=gHnsRegion_Metatiles_7c211c2c28e92663e0ac, .metatileAttributes=gHnsRegion_Attributes_361b45218227bbe8a400, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B841268f5d91aa25a = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_7c6ac43e5f915c90d634, .palettes=gHnsRegion_B841268f5d91aa25a_Palettes, .metatiles=gHnsRegion_Metatiles_b9c3afaadcd550832913, .metatileAttributes=gHnsRegion_Attributes_63cdbde60bb418f727af, .callback=NULL};
void HnsRegion640_InitTilesetAnim_JohtoGeneral(void);
const struct Tileset gTileset_HnsRegion_Be07abc4e083801ad = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gHnsRegion_Tiles_c2a8877cf45c15406fb3, .palettes=gHnsRegion_Be07abc4e083801ad_Palettes, .metatiles=gHnsRegion_Metatiles_7bd3611350925efe31af, .metatileAttributes=gHnsRegion_Attributes_e196a295dc1ae9cc9e29, .callback=HnsRegion640_InitTilesetAnim_JohtoGeneral};
const struct Tileset gTileset_HnsRegion_B391267b2dff5cd19 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_8d4fdb4c45c556f987b5, .palettes=gHnsRegion_B391267b2dff5cd19_Palettes, .metatiles=gHnsRegion_Metatiles_81084d9196c12241fc67, .metatileAttributes=gHnsRegion_Attributes_70cf5151e3354f02ad1b, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bd48986176a290035 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_b1d9aca5838ce9bb19f7, .palettes=gHnsRegion_Bd48986176a290035_Palettes, .metatiles=gHnsRegion_Metatiles_db28345b6d18c92d1842, .metatileAttributes=gHnsRegion_Attributes_401265b8b95f33eff908, .callback=NULL};
void HnsRegion640_InitTilesetAnim_JohtoGeneral(void);
const struct Tileset gTileset_HnsRegion_B124bbf28a106a847 = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gHnsRegion_Tiles_2190290494d4d027840e, .palettes=gHnsRegion_B124bbf28a106a847_Palettes, .metatiles=gHnsRegion_Metatiles_7e5e4d947bd34c39db7e, .metatileAttributes=gHnsRegion_Attributes_265306f325eb762a5b3b, .callback=HnsRegion640_InitTilesetAnim_JohtoGeneral};
const struct Tileset gTileset_HnsRegion_B1bafd1ab9171af0c = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_8c1b9e90fee2fcac8fd7, .palettes=gHnsRegion_B1bafd1ab9171af0c_Palettes, .metatiles=gHnsRegion_Metatiles_4d6fcc104dced96d17c9, .metatileAttributes=gHnsRegion_Attributes_228f0ae6696373daec4a, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B4cf3bdfa845b2705 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_fd4571fa41c8de2f8550, .palettes=gHnsRegion_B4cf3bdfa845b2705_Palettes, .metatiles=gHnsRegion_Metatiles_c544a1ea02d5f8478647, .metatileAttributes=gHnsRegion_Attributes_81336c0a1b283de87bf3, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bde87427579a6ae29 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_98ae5e5b0b3943ffe38e, .palettes=gHnsRegion_Bde87427579a6ae29_Palettes, .metatiles=gHnsRegion_Metatiles_b7a79fbdff794b3f65b3, .metatileAttributes=gHnsRegion_Attributes_496ae5f9f173b78f3c43, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bc12ee2c173c5e5c9 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_4c6a77c434bf2d91a054, .palettes=gHnsRegion_Bc12ee2c173c5e5c9_Palettes, .metatiles=gHnsRegion_Metatiles_257f676a7826bcdcdf4d, .metatileAttributes=gHnsRegion_Attributes_bbce35e6e7f53d3dc30d, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bbba80233bf7fcc03 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_8136d48a88de2fc08192, .palettes=gHnsRegion_Bbba80233bf7fcc03_Palettes, .metatiles=gHnsRegion_Metatiles_1e6393cdd1dcd2c90ef6, .metatileAttributes=gHnsRegion_Attributes_6c7c10ed0f232ff59ed5, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B4e6eace9dcadab57 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_e33c7a13fb12bd495f5a, .palettes=gHnsRegion_B4e6eace9dcadab57_Palettes, .metatiles=gHnsRegion_Metatiles_1af612ffebb0c1b9cb7d, .metatileAttributes=gHnsRegion_Attributes_b5fd262eb356428b452b, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B49f73b4376e00393 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_671b41354e6b9e55cd66, .palettes=gHnsRegion_B49f73b4376e00393_Palettes, .metatiles=gHnsRegion_Metatiles_00e3a510b9f8d45a44f6, .metatileAttributes=gHnsRegion_Attributes_f490a2eea58d31596f3a, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bdb30b4b0207c9f84 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_f3aead75f1f01d3f45ce, .palettes=gHnsRegion_Bdb30b4b0207c9f84_Palettes, .metatiles=gHnsRegion_Metatiles_8cba1d4c99168c6ed074, .metatileAttributes=gHnsRegion_Attributes_c1241c56b821a085f420, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B754f598944bdb84e = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_1d734a7dc5bc3f59890b, .palettes=gHnsRegion_B754f598944bdb84e_Palettes, .metatiles=gHnsRegion_Metatiles_2002ed18ffcfe45f5b92, .metatileAttributes=gHnsRegion_Attributes_ecd11f69ade19ca6c747, .callback=NULL};
void HnsRegion640_InitTilesetAnim_JohtoGeneral(void);
const struct Tileset gTileset_HnsRegion_Bc48f4ca8b100f913 = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gHnsRegion_Tiles_0454b43c7b0d8d2aabfe, .palettes=gHnsRegion_Bc48f4ca8b100f913_Palettes, .metatiles=gHnsRegion_Metatiles_de16176401f24283dc28, .metatileAttributes=gHnsRegion_Attributes_3ab0c712a2c6502c51ef, .callback=HnsRegion640_InitTilesetAnim_JohtoGeneral};
const struct Tileset gTileset_HnsRegion_B925f687ed24cc4df = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_b9c41eda142ecd4a2cbc, .palettes=gHnsRegion_B925f687ed24cc4df_Palettes, .metatiles=gHnsRegion_Metatiles_ba4af89e664dc2de5512, .metatileAttributes=gHnsRegion_Attributes_7ff0e51e95034b66c0b5, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bd7d09951f9a8d459 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_bc26f808fde0c7511945, .palettes=gHnsRegion_Bd7d09951f9a8d459_Palettes, .metatiles=gHnsRegion_Metatiles_31321c3a0d17ca246de5, .metatileAttributes=gHnsRegion_Attributes_14150bb5e1659c5a5fe1, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B869ef10cdc09e1c4 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_cb9d58f6d965032b4d9b, .palettes=gHnsRegion_B869ef10cdc09e1c4_Palettes, .metatiles=gHnsRegion_Metatiles_fd694fcacca746dd2563, .metatileAttributes=gHnsRegion_Attributes_6c772fe6f6b60e8cc6fd, .callback=NULL};
void HnsRegion640_InitTilesetAnim_CeruleanCity_Hns(void);
const struct Tileset gTileset_HnsRegion_Bc1d5c323bc46eed1 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_5ff6fdece7b8fcf371f1, .palettes=gHnsRegion_Bc1d5c323bc46eed1_Palettes, .metatiles=gHnsRegion_Metatiles_8d1990d7ae78f41e3173, .metatileAttributes=gHnsRegion_Attributes_c1c3f7c8f80fee2a9d25, .callback=HnsRegion640_InitTilesetAnim_CeruleanCity_Hns};
const struct Tileset gTileset_HnsRegion_Bd7fff0140f3e0817 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_4caabfbcbe58d56ae6ff, .palettes=gHnsRegion_Bd7fff0140f3e0817_Palettes, .metatiles=gHnsRegion_Metatiles_5245f5ec87fb585899c1, .metatileAttributes=gHnsRegion_Attributes_c7b372a2cef10f324771, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bb6220cfc72613090 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_7327ce6ccb8ed72fcbeb, .palettes=gHnsRegion_Bb6220cfc72613090_Palettes, .metatiles=gHnsRegion_Metatiles_17ee92f250a9f59a8528, .metatileAttributes=gHnsRegion_Attributes_33efe033d20495a23e39, .callback=NULL};
void HnsRegion640_InitTilesetAnim_CeladonCity_Hns(void);
const struct Tileset gTileset_HnsRegion_Bd923aab956523e68 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_01f032dd5332cd9115d0, .palettes=gHnsRegion_Bd923aab956523e68_Palettes, .metatiles=gHnsRegion_Metatiles_042b2f5cf3e0255e08e0, .metatileAttributes=gHnsRegion_Attributes_556580929bf47c793efc, .callback=HnsRegion640_InitTilesetAnim_CeladonCity_Hns};
const struct Tileset gTileset_HnsRegion_B7560f6d246f15724 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_a7ee6db229098bdb890c, .palettes=gHnsRegion_B7560f6d246f15724_Palettes, .metatiles=gHnsRegion_Metatiles_c8185b745e339db9e2be, .metatileAttributes=gHnsRegion_Attributes_bc5cd6df1ff65533d2b7, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B0a73317edfd4895e = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_15b12f04bc1e99d50703, .palettes=gHnsRegion_B0a73317edfd4895e_Palettes, .metatiles=gHnsRegion_Metatiles_a072d49ffe9eaa0bc873, .metatileAttributes=gHnsRegion_Attributes_a198ae7b695fc562a4b5, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Baa2adf91d3c1aa9e = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_20a5ffed5d0c54de1a58, .palettes=gHnsRegion_Baa2adf91d3c1aa9e_Palettes, .metatiles=gHnsRegion_Metatiles_d6620e51a8bb1facf3a8, .metatileAttributes=gHnsRegion_Attributes_e263f7647465414b809c, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B3985e9e680dd786f = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_f3aead75f1f01d3f45ce, .palettes=gHnsRegion_B3985e9e680dd786f_Palettes, .metatiles=gHnsRegion_Metatiles_fa199c1611ee409ce785, .metatileAttributes=gHnsRegion_Attributes_a6c925678e5ebac700d6, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B9f42aa7893290dc7 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_de07d416dfa880f33e91, .palettes=gHnsRegion_B9f42aa7893290dc7_Palettes, .metatiles=gHnsRegion_Metatiles_74a0471b3a5abd4f6b2b, .metatileAttributes=gHnsRegion_Attributes_c7040bb7a9cf8fedb894, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bb1514df686bfafce = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_89ef29b633e6fb8ef25d, .palettes=gHnsRegion_Bb1514df686bfafce_Palettes, .metatiles=gHnsRegion_Metatiles_f8b85f51474f9746df99, .metatileAttributes=gHnsRegion_Attributes_3f8d726f76ee590b51ac, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B01222de7a8227af6 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_4c6a77c434bf2d91a054, .palettes=gHnsRegion_B01222de7a8227af6_Palettes, .metatiles=gHnsRegion_Metatiles_48b94f47fb22bfe6870e, .metatileAttributes=gHnsRegion_Attributes_48c88e168fea44644bc4, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B3be54c96cc738e05 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_bc26f808fde0c7511945, .palettes=gHnsRegion_B3be54c96cc738e05_Palettes, .metatiles=gHnsRegion_Metatiles_0a84512061f4d25b9793, .metatileAttributes=gHnsRegion_Attributes_2bf439639ddff30e5b8f, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bc22c74b66e524fab = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_bc26f808fde0c7511945, .palettes=gHnsRegion_Bc22c74b66e524fab_Palettes, .metatiles=gHnsRegion_Metatiles_3da509e9749c327edc50, .metatileAttributes=gHnsRegion_Attributes_60ade1d6f6f737395c72, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B25f3ca57455ea137 = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gHnsRegion_Tiles_39bb83cf1f236f576982, .palettes=gHnsRegion_B25f3ca57455ea137_Palettes, .metatiles=gHnsRegion_Metatiles_1000e1ff0a424f7994e3, .metatileAttributes=gHnsRegion_Attributes_aa919bab75a9efca5972, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Ba343f93335ab62c9 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_fb2a4a6997190282bf81, .palettes=gHnsRegion_Ba343f93335ab62c9_Palettes, .metatiles=gHnsRegion_Metatiles_e72035525409224ba4e5, .metatileAttributes=gHnsRegion_Attributes_a189a33c7fdf2b48598d, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Becb40317f5488618 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_f2d4015e0005513f4fc2, .palettes=gHnsRegion_Becb40317f5488618_Palettes, .metatiles=gHnsRegion_Metatiles_ef1ff5020fd161285620, .metatileAttributes=gHnsRegion_Attributes_8ae64d0b0a7750f9b39d, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bf201b5a84bc2a287 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_3e835c5edfa52be315f3, .palettes=gHnsRegion_Bf201b5a84bc2a287_Palettes, .metatiles=gHnsRegion_Metatiles_bd7a2a52842fa700d43a, .metatileAttributes=gHnsRegion_Attributes_aa56b692caa3c7086b1f, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B7843555bcb9138bb = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_cd6eb8ea9b3a9e9395d1, .palettes=gHnsRegion_B7843555bcb9138bb_Palettes, .metatiles=gHnsRegion_Metatiles_8d8b9d5fa7a975c15b17, .metatileAttributes=gHnsRegion_Attributes_e6151ec535314a76304d, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Baf5e4ff4905df416 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_d401f90c2eecdf19e7e8, .palettes=gHnsRegion_Baf5e4ff4905df416_Palettes, .metatiles=gHnsRegion_Metatiles_d0094e112093dbc72be6, .metatileAttributes=gHnsRegion_Attributes_d4c707810bc3acaa3c4d, .callback=NULL};
void HnsRegion640_InitTilesetAnim_EcruteakTheater(void);
const struct Tileset gTileset_HnsRegion_B8df4fb8ae430a655 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_f41d0e8450e21ff02bd9, .palettes=gHnsRegion_B8df4fb8ae430a655_Palettes, .metatiles=gHnsRegion_Metatiles_04b80836efa3a866628a, .metatileAttributes=gHnsRegion_Attributes_aaa84713891bae0e0994, .callback=HnsRegion640_InitTilesetAnim_EcruteakTheater};
const struct Tileset gTileset_HnsRegion_Bb9201d5c9cf2b5f5 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_6ccc0d86bd53874a6883, .palettes=gHnsRegion_Bb9201d5c9cf2b5f5_Palettes, .metatiles=gHnsRegion_Metatiles_293cd656ac130c8311f3, .metatileAttributes=gHnsRegion_Attributes_776aa77a60cc75b92490, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B500ac35c5dce0677 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_21231faaa2d7c140c515, .palettes=gHnsRegion_B500ac35c5dce0677_Palettes, .metatiles=gHnsRegion_Metatiles_71f444ef0952ce0f4777, .metatileAttributes=gHnsRegion_Attributes_4a947c38df267ceacad9, .callback=NULL};
void HnsRegion640_InitTilesetAnim_AzaleaTownGym(void);
const struct Tileset gTileset_HnsRegion_Beb24fa724ced9c72 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_2a0784bc2769bc6000f3, .palettes=gHnsRegion_Beb24fa724ced9c72_Palettes, .metatiles=gHnsRegion_Metatiles_9a1006c0dc02ce29ede3, .metatileAttributes=gHnsRegion_Attributes_aa2b779841ecff0a7041, .callback=HnsRegion640_InitTilesetAnim_AzaleaTownGym};
const struct Tileset gTileset_HnsRegion_Bcc3b9ef3b8891ea9 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_71872884a6c737139e79, .palettes=gHnsRegion_Bcc3b9ef3b8891ea9_Palettes, .metatiles=gHnsRegion_Metatiles_2158283b55b4fa600e4c, .metatileAttributes=gHnsRegion_Attributes_560e60b23d6c26c7910e, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B8022a8466bcb74f5 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_c8e57d6d259d55e28f50, .palettes=gHnsRegion_B8022a8466bcb74f5_Palettes, .metatiles=gHnsRegion_Metatiles_efa6097b5e3fe0852731, .metatileAttributes=gHnsRegion_Attributes_4859ef536fa57357d620, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B84ccc30d19116867 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_570b6ce86af61e6abb0d, .palettes=gHnsRegion_B84ccc30d19116867_Palettes, .metatiles=gHnsRegion_Metatiles_b6dfd7ecdab1daae4c72, .metatileAttributes=gHnsRegion_Attributes_2a9eedacc95d368618dd, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B7b9b18841be114a1 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_96c93ccef4102b54851f, .palettes=gHnsRegion_B7b9b18841be114a1_Palettes, .metatiles=gHnsRegion_Metatiles_30b0b310746256ea4ae0, .metatileAttributes=gHnsRegion_Attributes_f6d89c8bc0d8a7756f9c, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B2477a1afeabab908 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_aab356b45bfac4e050b2, .palettes=gHnsRegion_B2477a1afeabab908_Palettes, .metatiles=gHnsRegion_Metatiles_a499dddd52ebe4674d1c, .metatileAttributes=gHnsRegion_Attributes_10b19b0cf7161afae422, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B36c6cf5648e027c3 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_05d736db31c68ab2a3a6, .palettes=gHnsRegion_B36c6cf5648e027c3_Palettes, .metatiles=gHnsRegion_Metatiles_74e23334ea9907e791f1, .metatileAttributes=gHnsRegion_Attributes_ef6487c9fe927485d220, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B50cce5a934c981b2 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_044c60e4953c61fff1d2, .palettes=gHnsRegion_B50cce5a934c981b2_Palettes, .metatiles=gHnsRegion_Metatiles_f615a3bef7ca33382b57, .metatileAttributes=gHnsRegion_Attributes_d1bce7b995c0f935f2e4, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B30a11a12fa0e1604 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_460f2938c1ed339a02dc, .palettes=gHnsRegion_B30a11a12fa0e1604_Palettes, .metatiles=gHnsRegion_Metatiles_22655f9bbbba6bb8b820, .metatileAttributes=gHnsRegion_Attributes_be34aa11864200b307d1, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Ba8f52aa434624a31 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_5b1ea1626af268dee3b6, .palettes=gHnsRegion_Ba8f52aa434624a31_Palettes, .metatiles=gHnsRegion_Metatiles_9bb8e050cd6d910c2d25, .metatileAttributes=gHnsRegion_Attributes_1f8622111c067df2d539, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bb9b85f2f8886d65c = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_fc21d2044b3fc9ffd6b1, .palettes=gHnsRegion_Bb9b85f2f8886d65c_Palettes, .metatiles=gHnsRegion_Metatiles_3090078495a8680264ac, .metatileAttributes=gHnsRegion_Attributes_bf16e0b6b8361cc5c9ff, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B6559d938cd34b849 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_6a60d8f5cde35ad66352, .palettes=gHnsRegion_B6559d938cd34b849_Palettes, .metatiles=gHnsRegion_Metatiles_352a3d51b8577fd6e7b4, .metatileAttributes=gHnsRegion_Attributes_ea14da202348029a343f, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B229c22bcd540738a = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_fe6307513ee9428848a9, .palettes=gHnsRegion_B229c22bcd540738a_Palettes, .metatiles=gHnsRegion_Metatiles_f0e94399f04618b02918, .metatileAttributes=gHnsRegion_Attributes_41fb0fe656017329f87a, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B4a0adb33ec7e1342 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_ef477f928ec59f11ca4e, .palettes=gHnsRegion_B4a0adb33ec7e1342_Palettes, .metatiles=gHnsRegion_Metatiles_d3bea46e65cc73a3a707, .metatileAttributes=gHnsRegion_Attributes_44328f538a66c8b342af, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B2471ba7fa36fea56 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_ecf308ac4277d07686cb, .palettes=gHnsRegion_B2471ba7fa36fea56_Palettes, .metatiles=gHnsRegion_Metatiles_b38106d845002663dba5, .metatileAttributes=gHnsRegion_Attributes_709aba158eba23be1a49, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B45f1637b54228ff3 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_05d736db31c68ab2a3a6, .palettes=gHnsRegion_B45f1637b54228ff3_Palettes, .metatiles=gHnsRegion_Metatiles_74e23334ea9907e791f1, .metatileAttributes=gHnsRegion_Attributes_ef6487c9fe927485d220, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B0b77dab6d4d60f32 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_85c8c85e5f1b47e8eda1, .palettes=gHnsRegion_B0b77dab6d4d60f32_Palettes, .metatiles=gHnsRegion_Metatiles_76edf34debf605d184c4, .metatileAttributes=gHnsRegion_Attributes_9c82a54c0dbc3147f1fc, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bcea20eb5bb3320cb = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_6a403ec278d519a54841, .palettes=gHnsRegion_Bcea20eb5bb3320cb_Palettes, .metatiles=gHnsRegion_Metatiles_9e6a6c284caca19ec4d1, .metatileAttributes=gHnsRegion_Attributes_8d5e5c632d5a9b61d9d8, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B0c395c1e509cd021 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_b9f9020ff1ae52dfd276, .palettes=gHnsRegion_B0c395c1e509cd021_Palettes, .metatiles=gHnsRegion_Metatiles_90a7358f89e5a2c4c09d, .metatileAttributes=gHnsRegion_Attributes_8978fe581d27e2cbcb2b, .callback=NULL};
void HnsRegion640_InitTilesetAnim_BlackthornGym(void);
const struct Tileset gTileset_HnsRegion_B3cac0b6286c1bc98 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_72348edf4a36cbf8b371, .palettes=gHnsRegion_B3cac0b6286c1bc98_Palettes, .metatiles=gHnsRegion_Metatiles_d005339e03a93e84f4bd, .metatileAttributes=gHnsRegion_Attributes_afb85c9d84f61c8a2115, .callback=HnsRegion640_InitTilesetAnim_BlackthornGym};
const struct Tileset gTileset_HnsRegion_B3fed63a931138b81 = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gHnsRegion_Tiles_745d86cabccea7b0a622, .palettes=gHnsRegion_B3fed63a931138b81_Palettes, .metatiles=gHnsRegion_Metatiles_fab87e44eb742b97a82e, .metatileAttributes=gHnsRegion_Attributes_586618dc9f6d79ac3553, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bc97b1d567c1ecd40 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_e59973a7879e52b797ae, .palettes=gHnsRegion_Bc97b1d567c1ecd40_Palettes, .metatiles=gHnsRegion_Metatiles_d28125a5e420a50d1c6e, .metatileAttributes=gHnsRegion_Attributes_262d1656ce9dd9c6e7d4, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B7c87695a69777080 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_943ecc58b53923fb15be, .palettes=gHnsRegion_B7c87695a69777080_Palettes, .metatiles=gHnsRegion_Metatiles_133fe2cfa0f64294ebd2, .metatileAttributes=gHnsRegion_Attributes_116ed12d71d1ccae12d2, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bb5b4866511b8428c = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_eb6998287d2ca30c4a9c, .palettes=gHnsRegion_Bb5b4866511b8428c_Palettes, .metatiles=gHnsRegion_Metatiles_da2a1339f59da4fe9853, .metatileAttributes=gHnsRegion_Attributes_d21b199d7261864250b8, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B4ff9d20a54ed52cb = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_7947961533de708c3a2b, .palettes=gHnsRegion_B4ff9d20a54ed52cb_Palettes, .metatiles=gHnsRegion_Metatiles_5bdaba10226baba2657c, .metatileAttributes=gHnsRegion_Attributes_f6d870f23dbca1a2fcab, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B5bc59a533fa33b5b = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_ef477f928ec59f11ca4e, .palettes=gHnsRegion_B5bc59a533fa33b5b_Palettes, .metatiles=gHnsRegion_Metatiles_b814ec33868b3285ff4c, .metatileAttributes=gHnsRegion_Attributes_6f7a0d82c43da2f6d089, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B8c64fc8875ea6eb5 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_4785190f578766b11f88, .palettes=gHnsRegion_B8c64fc8875ea6eb5_Palettes, .metatiles=gHnsRegion_Metatiles_14c0411c9f2e55f49f83, .metatileAttributes=gHnsRegion_Attributes_6cab18a35e05110cc17e, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B8b986bdba8d1e22d = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_e4aafb00030e0914afd6, .palettes=gHnsRegion_B8b986bdba8d1e22d_Palettes, .metatiles=gHnsRegion_Metatiles_7cb7f5fb45e1e6d34738, .metatileAttributes=gHnsRegion_Attributes_5cd4506fadd3cca97fab, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B1c08da056689e24c = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_27b4ab34c4945ec9a93d, .palettes=gHnsRegion_B1c08da056689e24c_Palettes, .metatiles=gHnsRegion_Metatiles_9f419e6cf5c957583dff, .metatileAttributes=gHnsRegion_Attributes_a74b1161077b307f6f4c, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B83c4315cc5f8f9ee = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_d5d4a65a16e4ad63a349, .palettes=gHnsRegion_B83c4315cc5f8f9ee_Palettes, .metatiles=gHnsRegion_Metatiles_02a9c45a4d684f759257, .metatileAttributes=gHnsRegion_Attributes_907ef061738885203348, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B24f746a286538444 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_f0e91121a69d3e991b9f, .palettes=gHnsRegion_B24f746a286538444_Palettes, .metatiles=gHnsRegion_Metatiles_f3a6abee4bdf6e36293a, .metatileAttributes=gHnsRegion_Attributes_ef5bfe9c12b70da96790, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B0c0364069f9bc896 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_3f0d9837a4053f02cc40, .palettes=gHnsRegion_B0c0364069f9bc896_Palettes, .metatiles=gHnsRegion_Metatiles_6753b2a226b50d089559, .metatileAttributes=gHnsRegion_Attributes_7d4e0da011b70298391d, .callback=NULL};
void HnsRegion640_InitTilesetAnim_SilphCo_Hns(void);
const struct Tileset gTileset_HnsRegion_B3c3d9753f08d9cb1 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_0c9c4dd4a6d8780c8a59, .palettes=gHnsRegion_B3c3d9753f08d9cb1_Palettes, .metatiles=gHnsRegion_Metatiles_f382f26eff7a1243f560, .metatileAttributes=gHnsRegion_Attributes_37ae8ff5ea4707aedbba, .callback=HnsRegion640_InitTilesetAnim_SilphCo_Hns};
const struct Tileset gTileset_HnsRegion_B777d367e01f89313 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_3c1ecac4ef250541e07b, .palettes=gHnsRegion_B777d367e01f89313_Palettes, .metatiles=gHnsRegion_Metatiles_b88637011384862c59a6, .metatileAttributes=gHnsRegion_Attributes_a3ea9c66605fb9332268, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B1dfd9caadb3959a2 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_b2c09779cd62eeaf740d, .palettes=gHnsRegion_B1dfd9caadb3959a2_Palettes, .metatiles=gHnsRegion_Metatiles_c09e53d286362ab420d9, .metatileAttributes=gHnsRegion_Attributes_aae4e72ec88aae1163a6, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B4d4ee66a2d5d8e35 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_167ec95cb3924e31454d, .palettes=gHnsRegion_B4d4ee66a2d5d8e35_Palettes, .metatiles=gHnsRegion_Metatiles_9e8e0aeed26aae975c10, .metatileAttributes=gHnsRegion_Attributes_79b3f715bdf9ae7bfa43, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Be37917998a930ab5 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_650fd9d9f2fe0df9eb3f, .palettes=gHnsRegion_Be37917998a930ab5_Palettes, .metatiles=gHnsRegion_Metatiles_889c9254d40b220e6c1f, .metatileAttributes=gHnsRegion_Attributes_415d1f75af7cebb92e52, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bc26e5d71eb26ce06 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_694d81fd97bf9f375b08, .palettes=gHnsRegion_Bc26e5d71eb26ce06_Palettes, .metatiles=gHnsRegion_Metatiles_833ad8ad5a4ff1eef94c, .metatileAttributes=gHnsRegion_Attributes_a0361fdc4e1a683f347a, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B1453ffd31806c57d = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_d38317e7d137307a0ae0, .palettes=gHnsRegion_B1453ffd31806c57d_Palettes, .metatiles=gHnsRegion_Metatiles_dfc76ca433d038e3f695, .metatileAttributes=gHnsRegion_Attributes_020a8366440fede36b68, .callback=NULL};
void HnsRegion512_InitTilesetAnim_Building(void);
const struct Tileset gTileset_HnsRegion_B4af4dd65beb2ce26 = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gHnsRegion_Tiles_4b480ba4be41d62af25f, .palettes=gHnsRegion_B4af4dd65beb2ce26_Palettes, .metatiles=gHnsRegion_Metatiles_672eefdf43dd118416b7, .metatileAttributes=gHnsRegion_Attributes_f070143df9c0097230d1, .callback=HnsRegion512_InitTilesetAnim_Building};
const struct Tileset gTileset_HnsRegion_B5a1efd90c60f251b = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_afbc24f89c2634fc8823, .palettes=gHnsRegion_B5a1efd90c60f251b_Palettes, .metatiles=gHnsRegion_Metatiles_fe03401c3454cd3b7b65, .metatileAttributes=gHnsRegion_Attributes_b77b284f023797790372, .callback=NULL};
void HnsRegion512_InitTilesetAnim_General(void);
const struct Tileset gTileset_HnsRegion_Bc7ebf44ee878015a = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gHnsRegion_Tiles_24d47a59efccb7febfcd, .palettes=gHnsRegion_Bc7ebf44ee878015a_Palettes, .metatiles=gHnsRegion_Metatiles_a8f3d5a1f038e29b0355, .metatileAttributes=gHnsRegion_Attributes_816c26635c73100abeb4, .callback=HnsRegion512_InitTilesetAnim_General};
const struct Tileset gTileset_HnsRegion_B64cea65d6cb904b5 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_afbc24f89c2634fc8823, .palettes=gHnsRegion_B64cea65d6cb904b5_Palettes, .metatiles=gHnsRegion_Metatiles_fe03401c3454cd3b7b65, .metatileAttributes=gHnsRegion_Attributes_b77b284f023797790372, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B6897641db231e8a7 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_5a17ace90f57769a2b04, .palettes=gHnsRegion_B6897641db231e8a7_Palettes, .metatiles=gHnsRegion_Metatiles_4698eba94a6ceb8d9ecd, .metatileAttributes=gHnsRegion_Attributes_f43fba0a0a3a6b3d4890, .callback=NULL};
void HnsRegion640_InitTilesetAnim_SilphCo_Hns(void);
const struct Tileset gTileset_HnsRegion_Bd8cb73de210d06f3 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_6d7693e68f5fb59b88fd, .palettes=gHnsRegion_Bd8cb73de210d06f3_Palettes, .metatiles=gHnsRegion_Metatiles_dcb8fb96a3be2fa083cd, .metatileAttributes=gHnsRegion_Attributes_fda4161bbbf1d7cdef6b, .callback=HnsRegion640_InitTilesetAnim_SilphCo_Hns};
const struct Tileset gTileset_HnsRegion_B7d2551229275359b = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_ed88f4bde19709f94dca, .palettes=gHnsRegion_B7d2551229275359b_Palettes, .metatiles=gHnsRegion_Metatiles_e49137ad2ed17e7b6f64, .metatileAttributes=gHnsRegion_Attributes_ae3c83158f805f3bc269, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bb94b5d5a2516d1b4 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_b619799fe59e50bc65b6, .palettes=gHnsRegion_Bb94b5d5a2516d1b4_Palettes, .metatiles=gHnsRegion_Metatiles_9aa8f5f0cf4aadfe205d, .metatileAttributes=gHnsRegion_Attributes_f10474a52bcd03e8e30b, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B3da49c9dd45cd9e0 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_e13d79371c7d6d7039a5, .palettes=gHnsRegion_B3da49c9dd45cd9e0_Palettes, .metatiles=gHnsRegion_Metatiles_340ed01ce1644e7d54b7, .metatileAttributes=gHnsRegion_Attributes_f8cd25988bdfa3aeeffe, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B6663e152bf66b660 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_7cc8997fdb16662d939a, .palettes=gHnsRegion_B6663e152bf66b660_Palettes, .metatiles=gHnsRegion_Metatiles_b4ead9fe3075a867ea85, .metatileAttributes=gHnsRegion_Attributes_eaca9aa278762d29ab6e, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B1008cf802decd70a = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_cb5f1677274b47de68f6, .palettes=gHnsRegion_B1008cf802decd70a_Palettes, .metatiles=gHnsRegion_Metatiles_1f7f5d0330fecf77a834, .metatileAttributes=gHnsRegion_Attributes_0d0f57e47918896f67d7, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B82bcd45f4b45f9d9 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_78718127727724cc75f3, .palettes=gHnsRegion_B82bcd45f4b45f9d9_Palettes, .metatiles=gHnsRegion_Metatiles_7fbc1bdf1dcc06e6bd3c, .metatileAttributes=gHnsRegion_Attributes_b597210c7aa0c1fb3045, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B386becb11b294d92 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_2f4ea03a1b32face411f, .palettes=gHnsRegion_B386becb11b294d92_Palettes, .metatiles=gHnsRegion_Metatiles_2c2cd313247d7d9efde7, .metatileAttributes=gHnsRegion_Attributes_8a27de70a91d328afe88, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B163264dd5945fa70 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_e67a52e6aae9b0628493, .palettes=gHnsRegion_B163264dd5945fa70_Palettes, .metatiles=gHnsRegion_Metatiles_57965ca0d0c544e82e43, .metatileAttributes=gHnsRegion_Attributes_5aa9f89cefb5c4efc0df, .callback=NULL};
void HnsRegion640_InitTilesetAnim_NationalPark(void);
const struct Tileset gTileset_HnsRegion_Bf2138b66f21f8a2d = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_5def763b2f717d25d31d, .palettes=gHnsRegion_Bf2138b66f21f8a2d_Palettes, .metatiles=gHnsRegion_Metatiles_547b5621a7fa65050109, .metatileAttributes=gHnsRegion_Attributes_d7f0f4abc45479a29fd2, .callback=HnsRegion640_InitTilesetAnim_NationalPark};
const struct Tileset gTileset_HnsRegion_Ba1e84dfbd1bfab17 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_725b61e6e1cc930510fe, .palettes=gHnsRegion_Ba1e84dfbd1bfab17_Palettes, .metatiles=gHnsRegion_Metatiles_42aa81d301a4ed2c4916, .metatileAttributes=gHnsRegion_Attributes_b907d42c0550bc346355, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bbc6e8a0c5e1568e5 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_2f4ea03a1b32face411f, .palettes=gHnsRegion_Bbc6e8a0c5e1568e5_Palettes, .metatiles=gHnsRegion_Metatiles_2bce24f967f6753abae2, .metatileAttributes=gHnsRegion_Attributes_d2152af73ef1a8128b41, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B7c746690d49100ff = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_2940f19d9e79bb0f870b, .palettes=gHnsRegion_B7c746690d49100ff_Palettes, .metatiles=gHnsRegion_Metatiles_0d9b361dd5a31482e2f7, .metatileAttributes=gHnsRegion_Attributes_8bf4c6c8a87ce7f6b285, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bb05f9136b9d5b660 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_346afb31d98005293cab, .palettes=gHnsRegion_Bb05f9136b9d5b660_Palettes, .metatiles=gHnsRegion_Metatiles_cc1e857c0ad5748f73d6, .metatileAttributes=gHnsRegion_Attributes_eb9aebaefd53e56bad8e, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B93edae2d8a8b0a22 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_346afb31d98005293cab, .palettes=gHnsRegion_B93edae2d8a8b0a22_Palettes, .metatiles=gHnsRegion_Metatiles_79317f68d31516231486, .metatileAttributes=gHnsRegion_Attributes_86c3bf1f5597d921b18f, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B03edf5e7c0aaa3af = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_808d8f62a41e32a556fa, .palettes=gHnsRegion_B03edf5e7c0aaa3af_Palettes, .metatiles=gHnsRegion_Metatiles_9c39d9ef890f018b2367, .metatileAttributes=gHnsRegion_Attributes_98396a80a25f6a01ec07, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Be04efa2f6eea9327 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_c28d13c1065f0aa67530, .palettes=gHnsRegion_Be04efa2f6eea9327_Palettes, .metatiles=gHnsRegion_Metatiles_6d28a8e6fc0cdc6146a5, .metatileAttributes=gHnsRegion_Attributes_97fbb69925be79bf148b, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B3454274f5a2ebc70 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_9cdcfc75fedc7c2c49b6, .palettes=gHnsRegion_B3454274f5a2ebc70_Palettes, .metatiles=gHnsRegion_Metatiles_c144d3fa94c3c2de5aa9, .metatileAttributes=gHnsRegion_Attributes_149c5920a5c19fd6c370, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B8fe07f3b459833d2 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_0c18d84d5436143dc8eb, .palettes=gHnsRegion_B8fe07f3b459833d2_Palettes, .metatiles=gHnsRegion_Metatiles_3eefe2aeb1c0f600a8a9, .metatileAttributes=gHnsRegion_Attributes_ca0a1b79aa9985d28dea, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B7cbe06fefcf898dc = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_9bb204729a0acde2f467, .palettes=gHnsRegion_B7cbe06fefcf898dc_Palettes, .metatiles=gHnsRegion_Metatiles_c32366bce3c21e4b6b29, .metatileAttributes=gHnsRegion_Attributes_d055d271a58d3fb1d60b, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B71c7c0285825d073 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_f86bda2a6a2b4a7d1670, .palettes=gHnsRegion_B71c7c0285825d073_Palettes, .metatiles=gHnsRegion_Metatiles_c922690284f2c075b4e1, .metatileAttributes=gHnsRegion_Attributes_5f1e5752355924e92250, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bcb2582e39b146b86 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_6466cc5232853bea106b, .palettes=gHnsRegion_Bcb2582e39b146b86_Palettes, .metatiles=gHnsRegion_Metatiles_79c8490c37ffe8f4f9ab, .metatileAttributes=gHnsRegion_Attributes_2134b3b6c0a05f0f132c, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bc6d5bb944c425c49 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_e13d79371c7d6d7039a5, .palettes=gHnsRegion_Bc6d5bb944c425c49_Palettes, .metatiles=gHnsRegion_Metatiles_e6cf54337912450b5e8f, .metatileAttributes=gHnsRegion_Attributes_e0432148a9b8d1a1536a, .callback=NULL};
void HnsRegion512_InitTilesetAnim_JohtoGeneral(void);
const struct Tileset gTileset_HnsRegion_B5f2de6fd1e516824 = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gHnsRegion_Tiles_a0a1b33f1924171360c7, .palettes=gHnsRegion_B5f2de6fd1e516824_Palettes, .metatiles=gHnsRegion_Metatiles_c3874f85739c3fc91900, .metatileAttributes=gHnsRegion_Attributes_1b08bc931f0b88e0f9e9, .callback=HnsRegion512_InitTilesetAnim_JohtoGeneral};
const struct Tileset gTileset_HnsRegion_Bf254c761dddf8815 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_2b433dc0423dccc7e3d0, .palettes=gHnsRegion_Bf254c761dddf8815_Palettes, .metatiles=gHnsRegion_Metatiles_7eb6ab57b5bad8ad6630, .metatileAttributes=gHnsRegion_Attributes_4a72ec4b7521dc09d117, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B5fdb4f3e6b671d8f = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_f14b1d5c61199d7f1226, .palettes=gHnsRegion_B5fdb4f3e6b671d8f_Palettes, .metatiles=gHnsRegion_Metatiles_9a28af891931d76fa35c, .metatileAttributes=gHnsRegion_Attributes_9fc5a7fd7ab72f2217fb, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bb141ecb8120771ab = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_bb2a3dc8dd51a42b6014, .palettes=gHnsRegion_Bb141ecb8120771ab_Palettes, .metatiles=gHnsRegion_Metatiles_d56b99d59fb282f8b302, .metatileAttributes=gHnsRegion_Attributes_cc53078ff8b704c96750, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bc2d3da8ae36ebe32 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_1eb6bd8a7b424e91c048, .palettes=gHnsRegion_Bc2d3da8ae36ebe32_Palettes, .metatiles=gHnsRegion_Metatiles_f0cd5a912c5fffc570ff, .metatileAttributes=gHnsRegion_Attributes_18fa8df5f11e230bee7c, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bc71efc95bcdd95c8 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_46008390911156fdc7d2, .palettes=gHnsRegion_Bc71efc95bcdd95c8_Palettes, .metatiles=gHnsRegion_Metatiles_23989a94960ac1f36ab4, .metatileAttributes=gHnsRegion_Attributes_60ee78ce81caf30268a5, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B66b714a02efb718e = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_6e4d67800faa59f09ff3, .palettes=gHnsRegion_B66b714a02efb718e_Palettes, .metatiles=gHnsRegion_Metatiles_fad80983a63224924bdb, .metatileAttributes=gHnsRegion_Attributes_e03acdfb540c120d8ebf, .callback=NULL};
void HnsRegion640_InitTilesetAnim_MtSilverExp(void);
const struct Tileset gTileset_HnsRegion_B37af9eb04acd0e80 = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gHnsRegion_Tiles_7620def389b95bb0f7e7, .palettes=gHnsRegion_B37af9eb04acd0e80_Palettes, .metatiles=gHnsRegion_Metatiles_79be9a3c68ac93d15d67, .metatileAttributes=gHnsRegion_Attributes_4be7737015a1b34ebaa5, .callback=HnsRegion640_InitTilesetAnim_MtSilverExp};
const struct Tileset gTileset_HnsRegion_Bdf40c0fcc35879c0 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_46b5c6f99a4b5bbdd494, .palettes=gHnsRegion_Bdf40c0fcc35879c0_Palettes, .metatiles=gHnsRegion_Metatiles_0cafdd251979d7625808, .metatileAttributes=gHnsRegion_Attributes_f812d07aa43817662a4d, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bd596a532c31b7440 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_fd4571fa41c8de2f8550, .palettes=gHnsRegion_Bd596a532c31b7440_Palettes, .metatiles=gHnsRegion_Metatiles_06535067aec70cd97e1a, .metatileAttributes=gHnsRegion_Attributes_4a3ea6f89aea9abd1393, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Be763ab09b3243779 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_a7ee6db229098bdb890c, .palettes=gHnsRegion_Be763ab09b3243779_Palettes, .metatiles=gHnsRegion_Metatiles_b90273d2ddf17cdb7680, .metatileAttributes=gHnsRegion_Attributes_0256f8b1492d99975967, .callback=NULL};
void HnsRegion512_InitTilesetAnim_Rustboro(void);
const struct Tileset gTileset_HnsRegion_Bb06a056c9c2e6d6a = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_620ec73df2305bf92b25, .palettes=gHnsRegion_Bb06a056c9c2e6d6a_Palettes, .metatiles=gHnsRegion_Metatiles_88fd01fd5f9049049ea2, .metatileAttributes=gHnsRegion_Attributes_ce2bbec4b1b245fc7d0e, .callback=HnsRegion512_InitTilesetAnim_Rustboro};
void HnsRegion512_InitTilesetAnim_Fortree(void);
const struct Tileset gTileset_HnsRegion_B1c5fdd3c747bffef = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_0093f5ab75fee754e0e3, .palettes=gHnsRegion_B1c5fdd3c747bffef_Palettes, .metatiles=gHnsRegion_Metatiles_9ed38b3061fb3b8bc6e3, .metatileAttributes=gHnsRegion_Attributes_eba722553d205514bdcd, .callback=HnsRegion512_InitTilesetAnim_Fortree};
void HnsRegion512_InitTilesetAnim_Dewford(void);
const struct Tileset gTileset_HnsRegion_B6cdd18424415b56d = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_64e64b3684a272271c7a, .palettes=gHnsRegion_B6cdd18424415b56d_Palettes, .metatiles=gHnsRegion_Metatiles_076da21ab420afd71a19, .metatileAttributes=gHnsRegion_Attributes_e42b4ca29eb3cebb8159, .callback=HnsRegion512_InitTilesetAnim_Dewford};
const struct Tileset gTileset_HnsRegion_B34ef81d662697102 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_4028d3b99d9a24a41d95, .palettes=gHnsRegion_B34ef81d662697102_Palettes, .metatiles=gHnsRegion_Metatiles_552eeb6be3d564244b65, .metatileAttributes=gHnsRegion_Attributes_db4e6545ba8bfbb20fd9, .callback=NULL};
void HnsRegion512_InitTilesetAnim_BattleFrontierOutsideWest(void);
const struct Tileset gTileset_HnsRegion_Be5412f6eec33676d = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_6c83915e011aa93c1a66, .palettes=gHnsRegion_Be5412f6eec33676d_Palettes, .metatiles=gHnsRegion_Metatiles_6435cdc7af0dffb79b92, .metatileAttributes=gHnsRegion_Attributes_1a190d278656d28ee605, .callback=HnsRegion512_InitTilesetAnim_BattleFrontierOutsideWest};
void HnsRegion512_InitTilesetAnim_BattleFrontierOutsideEast(void);
const struct Tileset gTileset_HnsRegion_Ba479ba0c773d39cd = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_32804cb7575fa397b790, .palettes=gHnsRegion_Ba479ba0c773d39cd_Palettes, .metatiles=gHnsRegion_Metatiles_f0015d3efc2ccaddd2e0, .metatileAttributes=gHnsRegion_Attributes_1a13558994705b7ac6f5, .callback=HnsRegion512_InitTilesetAnim_BattleFrontierOutsideEast};
void HnsRegion512_InitTilesetAnim_BattleDome(void);
const struct Tileset gTileset_HnsRegion_Bc1fd78e473c49f42 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_ae8235425688a06d1b21, .palettes=gHnsRegion_Bc1fd78e473c49f42_Palettes, .metatiles=gHnsRegion_Metatiles_7c8d16efab6cd9f4d24d, .metatileAttributes=gHnsRegion_Attributes_8bbd29d12b5f4b422f4e, .callback=HnsRegion512_InitTilesetAnim_BattleDome};
const struct Tileset gTileset_HnsRegion_Bdddababb85e493f3 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_0f1e6b40052a425570bf, .palettes=gHnsRegion_Bdddababb85e493f3_Palettes, .metatiles=gHnsRegion_Metatiles_fb9f682179f3c84eb6bd, .metatileAttributes=gHnsRegion_Attributes_81500772037dc9a5d456, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Ba9465626b0777338 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_0f1e6b40052a425570bf, .palettes=gHnsRegion_Ba9465626b0777338_Palettes, .metatiles=gHnsRegion_Metatiles_fb9f682179f3c84eb6bd, .metatileAttributes=gHnsRegion_Attributes_81500772037dc9a5d456, .callback=NULL};
void HnsRegion512_InitTilesetAnim_BattlePyramid(void);
const struct Tileset gTileset_HnsRegion_B0972bd2aa8d5d29d = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_e76e5fd58eebc3173e75, .palettes=gHnsRegion_B0972bd2aa8d5d29d_Palettes, .metatiles=gHnsRegion_Metatiles_017c96dceba07e32dd1c, .metatileAttributes=gHnsRegion_Attributes_0f9c8924038937e1d9cc, .callback=HnsRegion512_InitTilesetAnim_BattlePyramid};
const struct Tileset gTileset_HnsRegion_B7e073bbc469dd70f = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_997b12bdc453152fd7ef, .palettes=gHnsRegion_B7e073bbc469dd70f_Palettes, .metatiles=gHnsRegion_Metatiles_d1f0ac63d475c6b0ed5f, .metatileAttributes=gHnsRegion_Attributes_4cde65d8449195a540ed, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B90b90846964877ca = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_09439e6faf19b1249f42, .palettes=gHnsRegion_B90b90846964877ca_Palettes, .metatiles=gHnsRegion_Metatiles_862bc3ffef169eecf2aa, .metatileAttributes=gHnsRegion_Attributes_65f9c3e1d32ccb8e0c3d, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Bb2c29566f41a2027 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_d34420d93ce1611e81af, .palettes=gHnsRegion_Bb2c29566f41a2027_Palettes, .metatiles=gHnsRegion_Metatiles_bb9a157e721b07a99031, .metatileAttributes=gHnsRegion_Attributes_a270439224728712b628, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Be6d7f54e98b5bbe5 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_88f7517c5a959feca476, .palettes=gHnsRegion_Be6d7f54e98b5bbe5_Palettes, .metatiles=gHnsRegion_Metatiles_c7fe12607669f588c224, .metatileAttributes=gHnsRegion_Attributes_5f70bf18a086007016e9, .callback=NULL};
const struct Tileset gTileset_HnsRegion_Beb6e38a41cdd99ae = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_1eb6bd8a7b424e91c048, .palettes=gHnsRegion_Beb6e38a41cdd99ae_Palettes, .metatiles=gHnsRegion_Metatiles_f0cd5a912c5fffc570ff, .metatileAttributes=gHnsRegion_Attributes_18fa8df5f11e230bee7c, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B7669cc4571757ae7 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_c641d8212a97eb88fa29, .palettes=gHnsRegion_B7669cc4571757ae7_Palettes, .metatiles=gHnsRegion_Metatiles_67a0033e931395afd75f, .metatileAttributes=gHnsRegion_Attributes_0440bfe0f5e802516ad9, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B405b72b962ee2778 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_0ee41757ab8ef51d759e, .palettes=gHnsRegion_B405b72b962ee2778_Palettes, .metatiles=gHnsRegion_Metatiles_df7edf83cf69f4e0f9ad, .metatileAttributes=gHnsRegion_Attributes_43f052d3e3443fe5fd37, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B45dcfc5095a6a5ac = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_6b8c7a7db3ec6e341e51, .palettes=gHnsRegion_B45dcfc5095a6a5ac_Palettes, .metatiles=gHnsRegion_Metatiles_8d0920c9da46ce5fcba9, .metatileAttributes=gHnsRegion_Attributes_f6999210cc95749e9cc9, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B2e45090793953695 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_6b8c7a7db3ec6e341e51, .palettes=gHnsRegion_B2e45090793953695_Palettes, .metatiles=gHnsRegion_Metatiles_8d0920c9da46ce5fcba9, .metatileAttributes=gHnsRegion_Attributes_f6999210cc95749e9cc9, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B348febbb165ee6e4 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_6685794ea7737912d128, .palettes=gHnsRegion_B348febbb165ee6e4_Palettes, .metatiles=gHnsRegion_Metatiles_52f599b0de0e3f1f7736, .metatileAttributes=gHnsRegion_Attributes_ce0085bdfc583da7b8f6, .callback=NULL};
const struct Tileset gTileset_HnsRegion_B9f4db14c0d79af5d = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_5a4cedb2023e81850f36, .palettes=gHnsRegion_B9f4db14c0d79af5d_Palettes, .metatiles=gHnsRegion_Metatiles_164e4be0e8c48abee839, .metatileAttributes=gHnsRegion_Attributes_03f0f60286ddf99ce605, .callback=NULL};
void HnsRegion640_InitTilesetAnim_General(void);
const struct Tileset gTileset_HnsRegion_B83bf468008f11017 = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gHnsRegion_Tiles_24d47a59efccb7febfcd, .palettes=gHnsRegion_B83bf468008f11017_Palettes, .metatiles=gHnsRegion_Metatiles_a8f3d5a1f038e29b0355, .metatileAttributes=gHnsRegion_Attributes_816c26635c73100abeb4, .callback=HnsRegion640_InitTilesetAnim_General};
const struct Tileset gTileset_HnsRegion_B83331b4d1cc3c48c = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_852a8d5a7687de57cff8, .palettes=gHnsRegion_B83331b4d1cc3c48c_Palettes, .metatiles=gHnsRegion_Metatiles_b7d6a48b1bd59dde042d, .metatileAttributes=gHnsRegion_Attributes_0c6eb5fb841c784ccf54, .callback=NULL};
void HnsRegion640_InitTilesetAnim_NationalPark(void);
const struct Tileset gTileset_HnsRegion_B7b9750a8fb870d04 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_406867a2c01666ee5a1e, .palettes=gHnsRegion_B7b9750a8fb870d04_Palettes, .metatiles=gHnsRegion_Metatiles_2634218cbcfc55ee69c5, .metatileAttributes=gHnsRegion_Attributes_6a14051fe6b7cff3d3d1, .callback=HnsRegion640_InitTilesetAnim_NationalPark};
const struct Tileset gTileset_HnsRegion_B0221ba93fc843062 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_c28d13c1065f0aa67530, .palettes=gHnsRegion_B0221ba93fc843062_Palettes, .metatiles=gHnsRegion_Metatiles_f5324782213cdacf428d, .metatileAttributes=gHnsRegion_Attributes_bd7b09e47d0874d273a0, .callback=NULL};
void HnsRegion512_InitTilesetAnim_Cave(void);
const struct Tileset gTileset_HnsRegion_B6e495b230bb9a391 = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gHnsRegion_Tiles_4087dee305bb1159cb8b, .palettes=gHnsRegion_B6e495b230bb9a391_Palettes, .metatiles=gHnsRegion_Metatiles_093e142296b06a0bc35a, .metatileAttributes=gHnsRegion_Attributes_72ac9775fc95d55c3f55, .callback=HnsRegion512_InitTilesetAnim_Cave};

