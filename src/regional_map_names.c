#include "global.h"
#include "regional_map_names.h"
#include "constants/layouts.h"

// Presentation metadata does not change saved met-location IDs.

static const u8 sUnovaRoute1Name[] = _("Route 1");

static const u8 sLocationName0[] = _("Accumula Town");
static const u8 sLocationName1[] = _("Acuity Lakefront");
static const u8 sLocationName2[] = _("Amity Square");
static const u8 sLocationName3[] = _("Azalea Town");
static const u8 sLocationName4[] = _("Battle Colosseum");
static const u8 sLocationName5[] = _("Bell Tower");
static const u8 sLocationName6[] = _("Berry Forest");
static const u8 sLocationName7[] = _("Birth Island");
static const u8 sLocationName8[] = _("Blackthorn City");
static const u8 sLocationName9[] = _("Bond Bridge");
static const u8 sLocationName10[] = _("Burned Tower");
static const u8 sLocationName11[] = _("Canalave City");
static const u8 sLocationName12[] = _("Cape Brink");
static const u8 sLocationName13[] = _("Castelia City");
static const u8 sLocationName14[] = _("Castelia Docks");
static const u8 sLocationName15[] = _("Castelia Waterfront");
static const u8 sLocationName16[] = _("Celadon City");
static const u8 sLocationName17[] = _("Celestic Town");
static const u8 sLocationName18[] = _("Cerulean Cave");
static const u8 sLocationName19[] = _("Cerulean City");
static const u8 sLocationName20[] = _("Cherrygrove City");
static const u8 sLocationName21[] = _("Cianwood City");
static const u8 sLocationName22[] = _("Cinnabar Island");
static const u8 sLocationName23[] = _("Cliff Cave");
static const u8 sLocationName24[] = _("Crown Shrine");
static const u8 sLocationName25[] = _("Dark Cave");
static const u8 sLocationName26[] = _("Desert Ruins");
static const u8 sLocationName27[] = _("Digletts Cave");
static const u8 sLocationName28[] = _("Dragon's Den");
static const u8 sLocationName29[] = _("Dreamyard");
static const u8 sLocationName30[] = _("Driftveil City");
static const u8 sLocationName31[] = _("Ecruteak City");
static const u8 sLocationName32[] = _("Eterna City");
static const u8 sLocationName33[] = _("Eterna Forest");
static const u8 sLocationName34[] = _("Five Island");
static const u8 sLocationName35[] = _("Floaroma Town");
static const u8 sLocationName36[] = _("Four Island");
static const u8 sLocationName37[] = _("Fuchsia City");
static const u8 sLocationName38[] = _("Fuego Ironworks");
static const u8 sLocationName39[] = _("Goldenrod City");
static const u8 sLocationName40[] = _("Goldenrod Sewers");
static const u8 sLocationName41[] = _("Goldenrod Tower");
static const u8 sLocationName42[] = _("Great Marsh");
static const u8 sLocationName43[] = _("Hearthome City");
static const u8 sLocationName44[] = _("Ice Path");
static const u8 sLocationName45[] = _("Icefall Cave");
static const u8 sLocationName46[] = _("Ilex Forest");
static const u8 sLocationName47[] = _("Indigo Plateau");
static const u8 sLocationName48[] = _("Iron Island");
static const u8 sLocationName49[] = _("Johto Area");
static const u8 sLocationName50[] = _("Jubilife City");
static const u8 sLocationName51[] = _("Kindle Road");
static const u8 sLocationName52[] = _("Lake Acuity");
static const u8 sLocationName53[] = _("Lake Valor");
static const u8 sLocationName54[] = _("Lake Verity");
static const u8 sLocationName55[] = _("Lake of Rage");
static const u8 sLocationName56[] = _("Lavender Town");
static const u8 sLocationName57[] = _("Lighthouse");
static const u8 sLocationName58[] = _("Lost Cave");
static const u8 sLocationName59[] = _("Lost Tower");
static const u8 sLocationName60[] = _("Mahogany Town");
static const u8 sLocationName61[] = _("Memorial Pillar");
static const u8 sLocationName62[] = _("Mt Ember");
static const u8 sLocationName63[] = _("Mt Moon");
static const u8 sLocationName64[] = _("Mt. Coronet");
static const u8 sLocationName65[] = _("Mt. Mortar");
static const u8 sLocationName66[] = _("Mt. Silver");
static const u8 sLocationName67[] = _("Nacrene City");
static const u8 sLocationName68[] = _("National Park");
static const u8 sLocationName69[] = _("Navel Rock");
static const u8 sLocationName70[] = _("New Bark Town");
static const u8 sLocationName71[] = _("Nuvema Town");
static const u8 sLocationName72[] = _("Old Chateau");
static const u8 sLocationName73[] = _("Olivine City");
static const u8 sLocationName74[] = _("One Island");
static const u8 sLocationName75[] = _("Oreburgh City");
static const u8 sLocationName76[] = _("Oreburgh Gate");
static const u8 sLocationName77[] = _("Oreburgh Mine");
static const u8 sLocationName78[] = _("Pal Park");
static const u8 sLocationName79[] = _("Pallet Town");
static const u8 sLocationName80[] = _("Pastoria City");
static const u8 sLocationName81[] = _("Pewter City");
static const u8 sLocationName82[] = _("Pinwheel Forest");
static const u8 sLocationName83[] = _("Pokemon League");
static const u8 sLocationName84[] = _("Pokemon Mansion");
static const u8 sLocationName85[] = _("Pokemon Tower");
static const u8 sLocationName86[] = _("Power Plant");
static const u8 sLocationName87[] = _("Prototype");
static const u8 sLocationName88[] = _("Ravaged Path");
static const u8 sLocationName89[] = _("Record Corner");
static const u8 sLocationName90[] = _("Regigigas Temple");
static const u8 sLocationName91[] = _("Resort Gorgeous");
static const u8 sLocationName92[] = _("Rock Tunnel");
static const u8 sLocationName93[] = _("Rocket HQ");
static const u8 sLocationName94[] = _("Rocket Hideout");
static const u8 sLocationName95[] = _("Route 2");
static const u8 sLocationName96[] = _("Route 201");
static const u8 sLocationName97[] = _("Route 202");
static const u8 sLocationName98[] = _("Route 203");
static const u8 sLocationName99[] = _("Route 204");
static const u8 sLocationName100[] = _("Route 205");
static const u8 sLocationName101[] = _("Route 206");
static const u8 sLocationName102[] = _("Route 207");
static const u8 sLocationName103[] = _("Route 208");
static const u8 sLocationName104[] = _("Route 209");
static const u8 sLocationName105[] = _("Route 210");
static const u8 sLocationName106[] = _("Route 211");
static const u8 sLocationName107[] = _("Route 212");
static const u8 sLocationName108[] = _("Route 213");
static const u8 sLocationName109[] = _("Route 214");
static const u8 sLocationName110[] = _("Route 215");
static const u8 sLocationName111[] = _("Route 216");
static const u8 sLocationName112[] = _("Route 217");
static const u8 sLocationName113[] = _("Route 218");
static const u8 sLocationName114[] = _("Route 219");
static const u8 sLocationName115[] = _("Route 220");
static const u8 sLocationName116[] = _("Route 221");
static const u8 sLocationName117[] = _("Route 222");
static const u8 sLocationName118[] = _("Route 223");
static const u8 sLocationName119[] = _("Route 27");
static const u8 sLocationName120[] = _("Route 28");
static const u8 sLocationName121[] = _("Route 29");
static const u8 sLocationName122[] = _("Route 30");
static const u8 sLocationName123[] = _("Route 31");
static const u8 sLocationName124[] = _("Route 32");
static const u8 sLocationName125[] = _("Route 33");
static const u8 sLocationName126[] = _("Route 34");
static const u8 sLocationName127[] = _("Route 35");
static const u8 sLocationName128[] = _("Route 36");
static const u8 sLocationName129[] = _("Route 37");
static const u8 sLocationName130[] = _("Route 38");
static const u8 sLocationName131[] = _("Route 39");
static const u8 sLocationName132[] = _("Route 4");
static const u8 sLocationName133[] = _("Route 40");
static const u8 sLocationName134[] = _("Route 41");
static const u8 sLocationName135[] = _("Route 42");
static const u8 sLocationName136[] = _("Route 43");
static const u8 sLocationName137[] = _("Route 44");
static const u8 sLocationName138[] = _("Route 45");
static const u8 sLocationName139[] = _("Route 46");
static const u8 sLocationName140[] = _("Route 47");
static const u8 sLocationName141[] = _("Route 48");
static const u8 sLocationName142[] = _("Route 5");
static const u8 sLocationName143[] = _("Route1");
static const u8 sLocationName144[] = _("Route10");
static const u8 sLocationName145[] = _("Route11");
static const u8 sLocationName146[] = _("Route12");
static const u8 sLocationName147[] = _("Route13");
static const u8 sLocationName148[] = _("Route14");
static const u8 sLocationName149[] = _("Route15");
static const u8 sLocationName150[] = _("Route16");
static const u8 sLocationName151[] = _("Route17");
static const u8 sLocationName152[] = _("Route18");
static const u8 sLocationName153[] = _("Route19");
static const u8 sLocationName154[] = _("Route2");
static const u8 sLocationName155[] = _("Route20");
static const u8 sLocationName156[] = _("Route21");
static const u8 sLocationName157[] = _("Route22");
static const u8 sLocationName158[] = _("Route23");
static const u8 sLocationName159[] = _("Route24");
static const u8 sLocationName160[] = _("Route25");
static const u8 sLocationName161[] = _("Route3");
static const u8 sLocationName162[] = _("Route4");
static const u8 sLocationName163[] = _("Route5");
static const u8 sLocationName164[] = _("Route6");
static const u8 sLocationName165[] = _("Route7");
static const u8 sLocationName166[] = _("Route8");
static const u8 sLocationName167[] = _("Route9");
static const u8 sLocationName168[] = _("Ruin Valley");
static const u8 sLocationName169[] = _("Ruins of Alph");
static const u8 sLocationName170[] = _("S.S. Anne");
static const u8 sLocationName171[] = _("SSAnne");
static const u8 sLocationName172[] = _("Safari Zone");
static const u8 sLocationName173[] = _("Saffron City");
static const u8 sLocationName174[] = _("Sandgem Town");
static const u8 sLocationName175[] = _("Seafoam Islands");
static const u8 sLocationName176[] = _("Sendoff Spring");
static const u8 sLocationName177[] = _("Sevault Canyon");
static const u8 sLocationName178[] = _("Seven Island");
static const u8 sLocationName179[] = _("Silph Co");
static const u8 sLocationName180[] = _("Sinjoh Ruins");
static const u8 sLocationName181[] = _("Sinnoh League");
static const u8 sLocationName182[] = _("Sinnoh Region");
static const u8 sLocationName183[] = _("Six Island");
static const u8 sLocationName184[] = _("Slowpoke Well");
static const u8 sLocationName185[] = _("Snowpoint City");
static const u8 sLocationName186[] = _("Solaceon Ruins");
static const u8 sLocationName187[] = _("Solaceon Town");
static const u8 sLocationName188[] = _("Spear Pillar");
static const u8 sLocationName189[] = _("Spring Path");
static const u8 sLocationName190[] = _("Sprout Tower");
static const u8 sLocationName191[] = _("Striaton City");
static const u8 sLocationName192[] = _("Sunyshore City");
static const u8 sLocationName193[] = _("Tanoby Ruins");
static const u8 sLocationName194[] = _("Three Island");
static const u8 sLocationName195[] = _("Tohjo Falls");
static const u8 sLocationName196[] = _("Trade Center");
static const u8 sLocationName197[] = _("Trainer Tower");
static const u8 sLocationName198[] = _("Treasure Beach");
static const u8 sLocationName199[] = _("Twinleaf Town");
static const u8 sLocationName200[] = _("Two Island");
static const u8 sLocationName201[] = _("Underground Path");
static const u8 sLocationName202[] = _("Union Cave");
static const u8 sLocationName203[] = _("Union Room");
static const u8 sLocationName204[] = _("Valley Windworks");
static const u8 sLocationName205[] = _("Valor Lakefront");
static const u8 sLocationName206[] = _("Veilstone City");
static const u8 sLocationName207[] = _("Verity Lakefront");
static const u8 sLocationName208[] = _("Vermilion City");
static const u8 sLocationName209[] = _("Victory Road");
static const u8 sLocationName210[] = _("Violet City");
static const u8 sLocationName211[] = _("Viridian City");
static const u8 sLocationName212[] = _("Viridian Forest");
static const u8 sLocationName213[] = _("Water Labyrinth");
static const u8 sLocationName214[] = _("Water Path");
static const u8 sLocationName215[] = _("Whirl Islands");
static const u8 sUnovaRoute3Name[] = _("Route 3");
static const struct { u16 layout; const u8 *name; } sRegionalMapNames[] = {
    {LAYOUT_AMAP_3_22_ROUTE_3_LAYOUT, sUnovaRoute3Name},
    {LAYOUT_AMAP_3_21_ROUTE_3_LAYOUT, sUnovaRoute3Name},
    {LAYOUT_AMAP_1_114_PINHWEEL_FOREST_LAYOUT, sLocationName82},
    {LAYOUT_AMAP_1_95_PINHWEEL_FOREST_LAYOUT, sLocationName82},
    {LAYOUT_AMAP_3_0_NUVEMA_TOWN_LAYOUT, sLocationName71},
    {LAYOUT_AMAP_3_2_STRIATON_CITY_LAYOUT, sLocationName191},
    {LAYOUT_AMAP_3_3_NACRENE_CITY_LAYOUT, sLocationName67},
    {LAYOUT_BWA_1_30, sLocationName13},
    {LAYOUT_BWA_39_0, sLocationName29},
    {LAYOUT_BWA_3_20, sLocationName95},
    {LAYOUT_BWA_3_23, sLocationName132},
    {LAYOUT_BWA_3_24, sLocationName142},
    {LAYOUT_BWA_3_4, sLocationName13},
    {LAYOUT_BWA_3_45, sLocationName14},
    {LAYOUT_BWA_3_46, sLocationName15},
    {LAYOUT_BWA_3_6, sLocationName30},
    {LAYOUT_BWA_42_0, sLocationName71},
    {LAYOUT_BWA_4_0, sLocationName71},
    {LAYOUT_BWA_4_1, sLocationName71},
    {LAYOUT_BWA_4_2, sLocationName71},
    {LAYOUT_BWA_4_5, sLocationName71},
    {LAYOUT_BWA_5_4, sLocationName0},
    {LAYOUT_BWA_6_2, sLocationName191},
    {LAYOUT_BWA_6_4, sLocationName191},
    {LAYOUT_BWA_6_5, sLocationName191},
    {LAYOUT_BWA_8_0, sLocationName13},
    {LAYOUT_GSJOHTO_10_0_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_10_10_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_11_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_12_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_13_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_14_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_15_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_16_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_17_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_18_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_19_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_1_GOLDENROD_SEWERS, sLocationName40},
    {LAYOUT_GSJOHTO_10_2_GOLDENROD_SEWERS, sLocationName40},
    {LAYOUT_GSJOHTO_10_3_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_10_4_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_10_5_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_10_6_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_7_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_8_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_10_9_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_11_0_OLIVINE_CITY, sLocationName73},
    {LAYOUT_GSJOHTO_11_1_OLIVINE_CITY, sLocationName73},
    {LAYOUT_GSJOHTO_11_2_OLIVINE_CITY, sLocationName73},
    {LAYOUT_GSJOHTO_11_3_OLIVINE_CITY, sLocationName73},
    {LAYOUT_GSJOHTO_11_4_OLIVINE_CITY, sLocationName73},
    {LAYOUT_GSJOHTO_11_5_OLIVINE_CITY, sLocationName73},
    {LAYOUT_GSJOHTO_11_6_OLIVINE_CITY, sLocationName73},
    {LAYOUT_GSJOHTO_11_7_OLIVINE_CITY, sLocationName73},
    {LAYOUT_GSJOHTO_11_8_OLIVINE_CITY, sLocationName73},
    {LAYOUT_GSJOHTO_11_9_OLIVINE_CITY, sLocationName73},
    {LAYOUT_GSJOHTO_12_0_CIANWOOD_CITY, sLocationName21},
    {LAYOUT_GSJOHTO_12_1_ROUTE_42, sLocationName135},
    {LAYOUT_GSJOHTO_12_2_CIANWOOD_CITY, sLocationName21},
    {LAYOUT_GSJOHTO_12_3_CIANWOOD_CITY, sLocationName21},
    {LAYOUT_GSJOHTO_12_4_CIANWOOD_CITY, sLocationName21},
    {LAYOUT_GSJOHTO_12_5_CIANWOOD_CITY, sLocationName21},
    {LAYOUT_GSJOHTO_12_6_CIANWOOD_CITY, sLocationName21},
    {LAYOUT_GSJOHTO_12_7_ROUTE_48, sLocationName141},
    {LAYOUT_GSJOHTO_13_0_MAP_13_00, sLocationName49},
    {LAYOUT_GSJOHTO_13_1_MAP_13_01, sLocationName49},
    {LAYOUT_GSJOHTO_14_0_CIANWOOD_CITY, sLocationName21},
    {LAYOUT_GSJOHTO_14_1_BLACKTHORN_CITY, sLocationName8},
    {LAYOUT_GSJOHTO_14_2_DRAGON_S_DEN, sLocationName28},
    {LAYOUT_GSJOHTO_14_3_BLACKTHORN_CITY, sLocationName8},
    {LAYOUT_GSJOHTO_14_4_BLACKTHORN_CITY, sLocationName8},
    {LAYOUT_GSJOHTO_14_5_BLACKTHORN_CITY, sLocationName8},
    {LAYOUT_GSJOHTO_14_6_BLACKTHORN_CITY, sLocationName8},
    {LAYOUT_GSJOHTO_14_8_BLACKTHORN_CITY, sLocationName8},
    {LAYOUT_GSJOHTO_14_9_BLACKTHORN_CITY, sLocationName8},
    {LAYOUT_GSJOHTO_15_0_CHERRYGROVE_CITY, sLocationName20},
    {LAYOUT_GSJOHTO_15_1_ROUTE_30, sLocationName122},
    {LAYOUT_GSJOHTO_15_2_NEW_BARK_TOWN, sLocationName70},
    {LAYOUT_GSJOHTO_15_3_NEW_BARK_TOWN, sLocationName70},
    {LAYOUT_GSJOHTO_16_0_ROUTE_34, sLocationName126},
    {LAYOUT_GSJOHTO_16_1_ROUTE_33, sLocationName125},
    {LAYOUT_GSJOHTO_17_0_ROUTE_34, sLocationName126},
    {LAYOUT_GSJOHTO_17_1_ROUTE_29, sLocationName121},
    {LAYOUT_GSJOHTO_18_0_ROUTE_32, sLocationName124},
    {LAYOUT_GSJOHTO_18_1_ROUTE_35, sLocationName127},
    {LAYOUT_GSJOHTO_19_0_ROUTE_35, sLocationName127},
    {LAYOUT_GSJOHTO_1_0_ILEX_FOREST, sLocationName46},
    {LAYOUT_GSJOHTO_1_10_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_11_NEW_BARK_TOWN, sLocationName70},
    {LAYOUT_GSJOHTO_1_12_NATIONAL_PARK, sLocationName68},
    {LAYOUT_GSJOHTO_1_13_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_14_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_15_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_16_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_17_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_18_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_19_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_1_DARK_CAVE, sLocationName25},
    {LAYOUT_GSJOHTO_1_20_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_21_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_22_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_23_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_24_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_25_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_26_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_27_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_28_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_29_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_2_DARK_CAVE, sLocationName25},
    {LAYOUT_GSJOHTO_1_30_UNION_CAVE, sLocationName202},
    {LAYOUT_GSJOHTO_1_31_UNION_CAVE, sLocationName202},
    {LAYOUT_GSJOHTO_1_32_SLOWPOKE_WELL, sLocationName184},
    {LAYOUT_GSJOHTO_1_33_ICE_PATH, sLocationName44},
    {LAYOUT_GSJOHTO_1_34_ICE_PATH, sLocationName44},
    {LAYOUT_GSJOHTO_1_35_ICE_PATH, sLocationName44},
    {LAYOUT_GSJOHTO_1_36_ROUTE_36, sLocationName128},
    {LAYOUT_GSJOHTO_1_37_SPROUT_TOWER, sLocationName190},
    {LAYOUT_GSJOHTO_1_38_NATIONAL_PARK, sLocationName68},
    {LAYOUT_GSJOHTO_1_39_VICTORY_ROAD, sLocationName209},
    {LAYOUT_GSJOHTO_1_3_CIANWOOD_CITY, sLocationName21},
    {LAYOUT_GSJOHTO_1_40_VICTORY_ROAD, sLocationName209},
    {LAYOUT_GSJOHTO_1_41_VICTORY_ROAD, sLocationName209},
    {LAYOUT_GSJOHTO_1_42_VICTORY_ROAD, sLocationName209},
    {LAYOUT_GSJOHTO_1_43_VICTORY_ROAD, sLocationName209},
    {LAYOUT_GSJOHTO_1_44_VICTORY_ROAD, sLocationName209},
    {LAYOUT_GSJOHTO_1_45_MAP_01_45, sLocationName49},
    {LAYOUT_GSJOHTO_1_46_CLIFF_CAVE, sLocationName23},
    {LAYOUT_GSJOHTO_1_47_GOLDENROD_TOWER, sLocationName41},
    {LAYOUT_GSJOHTO_1_48_GOLDENROD_TOWER, sLocationName41},
    {LAYOUT_GSJOHTO_1_49_GOLDENROD_TOWER, sLocationName41},
    {LAYOUT_GSJOHTO_1_4_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_50_GOLDENROD_TOWER, sLocationName41},
    {LAYOUT_GSJOHTO_1_51_GOLDENROD_TOWER, sLocationName41},
    {LAYOUT_GSJOHTO_1_52_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_1_53_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_1_54_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_1_55_GOLDENROD_TOWER, sLocationName41},
    {LAYOUT_GSJOHTO_1_56_ROCKET_HQ, sLocationName93},
    {LAYOUT_GSJOHTO_1_57_ROCKET_HQ, sLocationName93},
    {LAYOUT_GSJOHTO_1_58_ROCKET_HQ, sLocationName93},
    {LAYOUT_GSJOHTO_1_59_BURNED_TOWER, sLocationName10},
    {LAYOUT_GSJOHTO_1_5_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_60_BURNED_TOWER, sLocationName10},
    {LAYOUT_GSJOHTO_1_61_LIGHTHOUSE, sLocationName57},
    {LAYOUT_GSJOHTO_1_62_LIGHTHOUSE, sLocationName57},
    {LAYOUT_GSJOHTO_1_63_LIGHTHOUSE, sLocationName57},
    {LAYOUT_GSJOHTO_1_64_LIGHTHOUSE, sLocationName57},
    {LAYOUT_GSJOHTO_1_65_LIGHTHOUSE, sLocationName57},
    {LAYOUT_GSJOHTO_1_66_LIGHTHOUSE, sLocationName57},
    {LAYOUT_GSJOHTO_1_67_ICE_PATH, sLocationName44},
    {LAYOUT_GSJOHTO_1_6_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_71_NATIONAL_PARK, sLocationName68},
    {LAYOUT_GSJOHTO_1_72_MT_MORTAR, sLocationName65},
    {LAYOUT_GSJOHTO_1_73_MT_MORTAR, sLocationName65},
    {LAYOUT_GSJOHTO_1_74_MT_MORTAR, sLocationName65},
    {LAYOUT_GSJOHTO_1_75_MAP_01_75, sLocationName49},
    {LAYOUT_GSJOHTO_1_76_MAP_01_76, sLocationName49},
    {LAYOUT_GSJOHTO_1_77_MAP_01_77, sLocationName49},
    {LAYOUT_GSJOHTO_1_78_MAP_01_78, sLocationName49},
    {LAYOUT_GSJOHTO_1_79_MAP_01_79, sLocationName49},
    {LAYOUT_GSJOHTO_1_7_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_80_MAP_01_80, sLocationName49},
    {LAYOUT_GSJOHTO_1_81_UNION_CAVE, sLocationName202},
    {LAYOUT_GSJOHTO_1_82_UNION_CAVE, sLocationName202},
    {LAYOUT_GSJOHTO_1_83_WHIRL_ISLANDS, sLocationName215},
    {LAYOUT_GSJOHTO_1_84_WHIRL_ISLANDS, sLocationName215},
    {LAYOUT_GSJOHTO_1_85_WHIRL_ISLANDS, sLocationName215},
    {LAYOUT_GSJOHTO_1_86_WHIRL_ISLANDS, sLocationName215},
    {LAYOUT_GSJOHTO_1_87_MT_MORTAR, sLocationName65},
    {LAYOUT_GSJOHTO_1_88_RUINS_OF_ALPH, sLocationName169},
    {LAYOUT_GSJOHTO_1_89_RUINS_OF_ALPH, sLocationName169},
    {LAYOUT_GSJOHTO_1_8_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_1_90_RUINS_OF_ALPH, sLocationName169},
    {LAYOUT_GSJOHTO_1_91_SLOWPOKE_WELL, sLocationName184},
    {LAYOUT_GSJOHTO_1_92_UNION_CAVE, sLocationName202},
    {LAYOUT_GSJOHTO_1_93_BELL_TOWER, sLocationName5},
    {LAYOUT_GSJOHTO_1_94_BELL_TOWER, sLocationName5},
    {LAYOUT_GSJOHTO_1_95_GOLDENROD_SEWERS, sLocationName40},
    {LAYOUT_GSJOHTO_1_96_OLIVINE_CITY, sLocationName73},
    {LAYOUT_GSJOHTO_1_97_DRAGON_S_DEN, sLocationName28},
    {LAYOUT_GSJOHTO_1_98_ROUTE_29, sLocationName121},
    {LAYOUT_GSJOHTO_1_9_S_S_ANNE, sLocationName170},
    {LAYOUT_GSJOHTO_20_0_ROUTE_42, sLocationName135},
    {LAYOUT_GSJOHTO_21_0_ROUTE_48, sLocationName141},
    {LAYOUT_GSJOHTO_22_0_MAP_22_00, sLocationName49},
    {LAYOUT_GSJOHTO_22_1_ROUTE_39, sLocationName131},
    {LAYOUT_GSJOHTO_23_0_ROUTE_36, sLocationName128},
    {LAYOUT_GSJOHTO_23_1_ROUTE_40, sLocationName133},
    {LAYOUT_GSJOHTO_23_2_NEW_BARK_TOWN, sLocationName70},
    {LAYOUT_GSJOHTO_24_0_ROUTE_31, sLocationName123},
    {LAYOUT_GSJOHTO_24_1_ROUTE_43, sLocationName136},
    {LAYOUT_GSJOHTO_25_1_ROUTE_36, sLocationName128},
    {LAYOUT_GSJOHTO_25_2_ROUTE_44, sLocationName137},
    {LAYOUT_GSJOHTO_26_1_NEW_BARK_TOWN, sLocationName70},
    {LAYOUT_GSJOHTO_27_0_ROUTE_47, sLocationName140},
    {LAYOUT_GSJOHTO_28_0_ROUTE_48, sLocationName141},
    {LAYOUT_GSJOHTO_29_0_ROUTE_28, sLocationName120},
    {LAYOUT_GSJOHTO_30_0_MT_SILVER, sLocationName66},
    {LAYOUT_GSJOHTO_32_0_CLIFF_CAVE, sLocationName23},
    {LAYOUT_GSJOHTO_32_1_CLIFF_CAVE, sLocationName23},
    {LAYOUT_GSJOHTO_32_2_CLIFF_CAVE, sLocationName23},
    {LAYOUT_GSJOHTO_32_3_CLIFF_CAVE, sLocationName23},
    {LAYOUT_GSJOHTO_32_4_CLIFF_CAVE, sLocationName23},
    {LAYOUT_GSJOHTO_33_0_LIGHTHOUSE, sLocationName57},
    {LAYOUT_GSJOHTO_33_1_LIGHTHOUSE, sLocationName57},
    {LAYOUT_GSJOHTO_33_4_LIGHTHOUSE, sLocationName57},
    {LAYOUT_GSJOHTO_34_0_LAKE_OF_RAGE, sLocationName55},
    {LAYOUT_GSJOHTO_34_4_LAKE_OF_RAGE, sLocationName55},
    {LAYOUT_GSJOHTO_34_5_LAKE_OF_RAGE, sLocationName55},
    {LAYOUT_GSJOHTO_34_6_LAKE_OF_RAGE, sLocationName55},
    {LAYOUT_GSJOHTO_34_7_LAKE_OF_RAGE, sLocationName55},
    {LAYOUT_GSJOHTO_35_0_ROUTE_34, sLocationName126},
    {LAYOUT_GSJOHTO_35_3_LAKE_OF_RAGE, sLocationName55},
    {LAYOUT_GSJOHTO_35_4_ROUTE_38, sLocationName130},
    {LAYOUT_GSJOHTO_3_0_NEW_BARK_TOWN, sLocationName70},
    {LAYOUT_GSJOHTO_3_10_BLACKTHORN_CITY, sLocationName8},
    {LAYOUT_GSJOHTO_3_11_LAKE_OF_RAGE, sLocationName55},
    {LAYOUT_GSJOHTO_3_19_ROUTE_29, sLocationName121},
    {LAYOUT_GSJOHTO_3_1_CHERRYGROVE_CITY, sLocationName20},
    {LAYOUT_GSJOHTO_3_20_ROUTE_30, sLocationName122},
    {LAYOUT_GSJOHTO_3_21_ROUTE_31, sLocationName123},
    {LAYOUT_GSJOHTO_3_22_ROUTE_32, sLocationName124},
    {LAYOUT_GSJOHTO_3_23_ROUTE_33, sLocationName125},
    {LAYOUT_GSJOHTO_3_24_ROUTE_34, sLocationName126},
    {LAYOUT_GSJOHTO_3_25_ROUTE_35, sLocationName127},
    {LAYOUT_GSJOHTO_3_26_ROUTE_36, sLocationName128},
    {LAYOUT_GSJOHTO_3_27_ROUTE_37, sLocationName129},
    {LAYOUT_GSJOHTO_3_28_ROUTE_38, sLocationName130},
    {LAYOUT_GSJOHTO_3_29_ROUTE_39, sLocationName131},
    {LAYOUT_GSJOHTO_3_2_VIOLET_CITY, sLocationName210},
    {LAYOUT_GSJOHTO_3_30_ROUTE_40, sLocationName133},
    {LAYOUT_GSJOHTO_3_31_ROUTE_41, sLocationName134},
    {LAYOUT_GSJOHTO_3_32_ROUTE_42, sLocationName135},
    {LAYOUT_GSJOHTO_3_33_ROUTE_43, sLocationName136},
    {LAYOUT_GSJOHTO_3_34_ROUTE_44, sLocationName137},
    {LAYOUT_GSJOHTO_3_35_ROUTE_45, sLocationName138},
    {LAYOUT_GSJOHTO_3_36_ROUTE_46, sLocationName139},
    {LAYOUT_GSJOHTO_3_37_ROUTE_47, sLocationName140},
    {LAYOUT_GSJOHTO_3_38_ROUTE_48, sLocationName141},
    {LAYOUT_GSJOHTO_3_39_ROUTE_27, sLocationName119},
    {LAYOUT_GSJOHTO_3_3_AZALEA_TOWN, sLocationName3},
    {LAYOUT_GSJOHTO_3_40_ROUTE_27, sLocationName119},
    {LAYOUT_GSJOHTO_3_41_TOHJO_FALLS, sLocationName195},
    {LAYOUT_GSJOHTO_3_42_ROUTE_28, sLocationName120},
    {LAYOUT_GSJOHTO_3_43_SINJOH_RUINS, sLocationName180},
    {LAYOUT_GSJOHTO_3_44_MT_SILVER, sLocationName66},
    {LAYOUT_GSJOHTO_3_4_MAHOGANY_TOWN, sLocationName60},
    {LAYOUT_GSJOHTO_3_5_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_3_66_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_3_6_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_3_7_OLIVINE_CITY, sLocationName73},
    {LAYOUT_GSJOHTO_3_8_CIANWOOD_CITY, sLocationName21},
    {LAYOUT_GSJOHTO_3_9_MAP_03_09, sLocationName49},
    {LAYOUT_GSJOHTO_4_0_NEW_BARK_TOWN, sLocationName70},
    {LAYOUT_GSJOHTO_4_1_NEW_BARK_TOWN, sLocationName70},
    {LAYOUT_GSJOHTO_4_2_NEW_BARK_TOWN, sLocationName70},
    {LAYOUT_GSJOHTO_4_3_NEW_BARK_TOWN, sLocationName70},
    {LAYOUT_GSJOHTO_5_0_CHERRYGROVE_CITY, sLocationName20},
    {LAYOUT_GSJOHTO_5_1_MAHOGANY_TOWN, sLocationName60},
    {LAYOUT_GSJOHTO_5_2_CHERRYGROVE_CITY, sLocationName20},
    {LAYOUT_GSJOHTO_5_3_CHERRYGROVE_CITY, sLocationName20},
    {LAYOUT_GSJOHTO_5_4_CHERRYGROVE_CITY, sLocationName20},
    {LAYOUT_GSJOHTO_6_0_VIOLET_CITY, sLocationName210},
    {LAYOUT_GSJOHTO_6_1_VIOLET_CITY, sLocationName210},
    {LAYOUT_GSJOHTO_6_2_VIOLET_CITY, sLocationName210},
    {LAYOUT_GSJOHTO_6_3_VIOLET_CITY, sLocationName210},
    {LAYOUT_GSJOHTO_6_4_RUINS_OF_ALPH, sLocationName169},
    {LAYOUT_GSJOHTO_6_5_VIOLET_CITY, sLocationName210},
    {LAYOUT_GSJOHTO_6_7_VIOLET_CITY, sLocationName210},
    {LAYOUT_GSJOHTO_7_0_AZALEA_TOWN, sLocationName3},
    {LAYOUT_GSJOHTO_7_1_AZALEA_TOWN, sLocationName3},
    {LAYOUT_GSJOHTO_7_2_VIOLET_CITY, sLocationName210},
    {LAYOUT_GSJOHTO_7_3_AZALEA_TOWN, sLocationName3},
    {LAYOUT_GSJOHTO_7_5_AZALEA_TOWN, sLocationName3},
    {LAYOUT_GSJOHTO_7_6_AZALEA_TOWN, sLocationName3},
    {LAYOUT_GSJOHTO_7_7_AZALEA_TOWN, sLocationName3},
    {LAYOUT_GSJOHTO_7_8_CIANWOOD_CITY, sLocationName21},
    {LAYOUT_GSJOHTO_7_9_AZALEA_TOWN, sLocationName3},
    {LAYOUT_GSJOHTO_8_0_MAHOGANY_TOWN, sLocationName60},
    {LAYOUT_GSJOHTO_8_1_ROUTE_43, sLocationName136},
    {LAYOUT_GSJOHTO_8_2_MAHOGANY_TOWN, sLocationName60},
    {LAYOUT_GSJOHTO_8_3_MAHOGANY_TOWN, sLocationName60},
    {LAYOUT_GSJOHTO_8_4_ROUTE_43, sLocationName136},
    {LAYOUT_GSJOHTO_8_5_LAKE_OF_RAGE, sLocationName55},
    {LAYOUT_GSJOHTO_9_0_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_9_1_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_9_2_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_9_3_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_9_4_CIANWOOD_CITY, sLocationName21},
    {LAYOUT_GSJOHTO_9_5_ECRUTEAK_CITY, sLocationName31},
    {LAYOUT_GSJOHTO_9_6_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_GSJOHTO_9_7_GOLDENROD_CITY, sLocationName39},
    {LAYOUT_HYPERSINNOH_26_67_CANALAVE_CITY, sLocationName11},
    {LAYOUT_HYPERSINNOH_34_37_SINNOH_LEAGUE, sLocationName181},
    {LAYOUT_HYPERSINNOH_35_11_SPEAR_PILLAR, sLocationName188},
    {LAYOUT_HYPERSINNOH_35_14_SOLACEON_RUINS, sLocationName186},
    {LAYOUT_HYPERSINNOH_35_16_ROUTE_210, sLocationName105},
    {LAYOUT_HYPERSINNOH_35_29_LOST_TOWER, sLocationName59},
    {LAYOUT_HYPERSINNOH_35_81_CROWN_SHRINE, sLocationName24},
    {LAYOUT_HYPERSINNOH_35_82_CROWN_SHRINE, sLocationName24},
    {LAYOUT_HYPERSINNOH_35_88_DESERT_RUINS, sLocationName26},
    {LAYOUT_HYPERSINNOH_36_0_TWINLEAF_TOWN, sLocationName199},
    {LAYOUT_HYPERSINNOH_36_10_CELESTIC_TOWN, sLocationName17},
    {LAYOUT_HYPERSINNOH_36_11_CANALAVE_CITY, sLocationName11},
    {LAYOUT_HYPERSINNOH_36_12_SNOWPOINT_CITY, sLocationName185},
    {LAYOUT_HYPERSINNOH_36_13_SUNYSHORE_CITY, sLocationName192},
    {LAYOUT_HYPERSINNOH_36_14_SINNOH_LEAGUE, sLocationName181},
    {LAYOUT_HYPERSINNOH_36_15_ROUTE_201, sLocationName96},
    {LAYOUT_HYPERSINNOH_36_16_VERITY_LAKEFRONT, sLocationName207},
    {LAYOUT_HYPERSINNOH_36_17_ROUTE_202, sLocationName97},
    {LAYOUT_HYPERSINNOH_36_18_ROUTE_203, sLocationName98},
    {LAYOUT_HYPERSINNOH_36_19_ROUTE_204, sLocationName99},
    {LAYOUT_HYPERSINNOH_36_1_SANDGEM_TOWN, sLocationName174},
    {LAYOUT_HYPERSINNOH_36_20_ROUTE_205, sLocationName100},
    {LAYOUT_HYPERSINNOH_36_21_ROUTE_205, sLocationName100},
    {LAYOUT_HYPERSINNOH_36_22_ROUTE_206, sLocationName101},
    {LAYOUT_HYPERSINNOH_36_23_ROUTE_207, sLocationName102},
    {LAYOUT_HYPERSINNOH_36_24_ROUTE_208, sLocationName103},
    {LAYOUT_HYPERSINNOH_36_25_ROUTE_209, sLocationName104},
    {LAYOUT_HYPERSINNOH_36_26_ROUTE_210, sLocationName105},
    {LAYOUT_HYPERSINNOH_36_27_ROUTE_210, sLocationName105},
    {LAYOUT_HYPERSINNOH_36_28_ROUTE_211, sLocationName106},
    {LAYOUT_HYPERSINNOH_36_29_ROUTE_212, sLocationName107},
    {LAYOUT_HYPERSINNOH_36_2_JUBILIFE_CITY, sLocationName50},
    {LAYOUT_HYPERSINNOH_36_30_ROUTE_212, sLocationName107},
    {LAYOUT_HYPERSINNOH_36_31_ROUTE_213, sLocationName108},
    {LAYOUT_HYPERSINNOH_36_32_ROUTE_213, sLocationName108},
    {LAYOUT_HYPERSINNOH_36_33_ROUTE_214, sLocationName109},
    {LAYOUT_HYPERSINNOH_36_34_ROUTE_215, sLocationName110},
    {LAYOUT_HYPERSINNOH_36_35_ROUTE_216, sLocationName111},
    {LAYOUT_HYPERSINNOH_36_36_ROUTE_217, sLocationName112},
    {LAYOUT_HYPERSINNOH_36_37_ROUTE_218, sLocationName113},
    {LAYOUT_HYPERSINNOH_36_38_ROUTE_219, sLocationName114},
    {LAYOUT_HYPERSINNOH_36_39_ROUTE_220, sLocationName115},
    {LAYOUT_HYPERSINNOH_36_3_OREBURGH_CITY, sLocationName75},
    {LAYOUT_HYPERSINNOH_36_40_ROUTE_221, sLocationName116},
    {LAYOUT_HYPERSINNOH_36_41_ROUTE_222, sLocationName117},
    {LAYOUT_HYPERSINNOH_36_42_ROUTE_223, sLocationName118},
    {LAYOUT_HYPERSINNOH_36_43_LAKE_VERITY, sLocationName54},
    {LAYOUT_HYPERSINNOH_36_44_LAKE_VALOR, sLocationName53},
    {LAYOUT_HYPERSINNOH_36_45_LAKE_ACUITY, sLocationName52},
    {LAYOUT_HYPERSINNOH_36_46_SENDOFF_SPRING, sLocationName176},
    {LAYOUT_HYPERSINNOH_36_47_VALOR_LAKEFRONT, sLocationName205},
    {LAYOUT_HYPERSINNOH_36_48_ACUITY_LAKEFRONT, sLocationName1},
    {LAYOUT_HYPERSINNOH_36_49_SPRING_PATH, sLocationName189},
    {LAYOUT_HYPERSINNOH_36_4_FLOAROMA_TOWN, sLocationName35},
    {LAYOUT_HYPERSINNOH_36_50_LAKE_VERITY, sLocationName54},
    {LAYOUT_HYPERSINNOH_36_51_LAKE_VALOR, sLocationName53},
    {LAYOUT_HYPERSINNOH_36_52_LAKE_ACUITY, sLocationName52},
    {LAYOUT_HYPERSINNOH_36_53_ETERNA_FOREST, sLocationName33},
    {LAYOUT_HYPERSINNOH_36_54_VALLEY_WINDWORKS, sLocationName204},
    {LAYOUT_HYPERSINNOH_36_55_FUEGO_IRONWORKS, sLocationName38},
    {LAYOUT_HYPERSINNOH_36_56_AMITY_SQUARE, sLocationName2},
    {LAYOUT_HYPERSINNOH_36_57_PAL_PARK, sLocationName78},
    {LAYOUT_HYPERSINNOH_36_58_OREBURGH_GATE, sLocationName76},
    {LAYOUT_HYPERSINNOH_36_59_OREBURGH_GATE, sLocationName76},
    {LAYOUT_HYPERSINNOH_36_5_FLOAROMA_TOWN, sLocationName35},
    {LAYOUT_HYPERSINNOH_36_60_OREBURGH_CITY, sLocationName75},
    {LAYOUT_HYPERSINNOH_36_61_OREBURGH_MINE, sLocationName77},
    {LAYOUT_HYPERSINNOH_36_62_PASTORIA_CITY, sLocationName80},
    {LAYOUT_HYPERSINNOH_36_63_RAVAGED_PATH, sLocationName88},
    {LAYOUT_HYPERSINNOH_36_64_IRON_ISLAND, sLocationName48},
    {LAYOUT_HYPERSINNOH_36_65_IRON_ISLAND, sLocationName48},
    {LAYOUT_HYPERSINNOH_36_66_IRON_ISLAND, sLocationName48},
    {LAYOUT_HYPERSINNOH_36_67_IRON_ISLAND, sLocationName48},
    {LAYOUT_HYPERSINNOH_36_68_IRON_ISLAND, sLocationName48},
    {LAYOUT_HYPERSINNOH_36_69_IRON_ISLAND, sLocationName48},
    {LAYOUT_HYPERSINNOH_36_6_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_36_70_IRON_ISLAND, sLocationName48},
    {LAYOUT_HYPERSINNOH_36_71_VICTORY_ROAD, sLocationName209},
    {LAYOUT_HYPERSINNOH_36_72_VICTORY_ROAD, sLocationName209},
    {LAYOUT_HYPERSINNOH_36_73_VICTORY_ROAD, sLocationName209},
    {LAYOUT_HYPERSINNOH_36_74_REGIGIGAS_TEMPLE, sLocationName90},
    {LAYOUT_HYPERSINNOH_36_75_REGIGIGAS_TEMPLE, sLocationName90},
    {LAYOUT_HYPERSINNOH_36_76_REGIGIGAS_TEMPLE, sLocationName90},
    {LAYOUT_HYPERSINNOH_36_77_REGIGIGAS_TEMPLE, sLocationName90},
    {LAYOUT_HYPERSINNOH_36_78_REGIGIGAS_TEMPLE, sLocationName90},
    {LAYOUT_HYPERSINNOH_36_79_REGIGIGAS_TEMPLE, sLocationName90},
    {LAYOUT_HYPERSINNOH_36_7_HEARTHOME_CITY, sLocationName43},
    {LAYOUT_HYPERSINNOH_36_80_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_81_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_82_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_83_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_84_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_85_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_86_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_87_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_88_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_89_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_8_SOLACEON_TOWN, sLocationName187},
    {LAYOUT_HYPERSINNOH_36_90_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_91_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_92_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_93_ETERNA_FOREST, sLocationName33},
    {LAYOUT_HYPERSINNOH_36_94_MT_CORONET, sLocationName64},
    {LAYOUT_HYPERSINNOH_36_95_SPEAR_PILLAR, sLocationName188},
    {LAYOUT_HYPERSINNOH_36_96_SPEAR_PILLAR, sLocationName188},
    {LAYOUT_HYPERSINNOH_36_9_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_100_HEARTHOME_CITY, sLocationName43},
    {LAYOUT_HYPERSINNOH_37_101_SINNOH_REGION, sLocationName182},
    {LAYOUT_HYPERSINNOH_37_109_JUBILIFE_CITY, sLocationName50},
    {LAYOUT_HYPERSINNOH_37_10_FLOAROMA_TOWN, sLocationName35},
    {LAYOUT_HYPERSINNOH_37_110_FLOAROMA_TOWN, sLocationName35},
    {LAYOUT_HYPERSINNOH_37_111_FLOAROMA_TOWN, sLocationName35},
    {LAYOUT_HYPERSINNOH_37_112_OREBURGH_CITY, sLocationName75},
    {LAYOUT_HYPERSINNOH_37_113_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_37_114_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_37_115_SUNYSHORE_CITY, sLocationName192},
    {LAYOUT_HYPERSINNOH_37_116_OREBURGH_CITY, sLocationName75},
    {LAYOUT_HYPERSINNOH_37_117_PASTORIA_CITY, sLocationName80},
    {LAYOUT_HYPERSINNOH_37_11_FLOAROMA_TOWN, sLocationName35},
    {LAYOUT_HYPERSINNOH_37_12_FLOAROMA_TOWN, sLocationName35},
    {LAYOUT_HYPERSINNOH_37_13_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_37_14_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_37_15_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_37_16_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_37_17_HEARTHOME_CITY, sLocationName43},
    {LAYOUT_HYPERSINNOH_37_18_HEARTHOME_CITY, sLocationName43},
    {LAYOUT_HYPERSINNOH_37_19_HEARTHOME_CITY, sLocationName43},
    {LAYOUT_HYPERSINNOH_37_1_TWINLEAF_TOWN, sLocationName199},
    {LAYOUT_HYPERSINNOH_37_20_HEARTHOME_CITY, sLocationName43},
    {LAYOUT_HYPERSINNOH_37_21_HEARTHOME_CITY, sLocationName43},
    {LAYOUT_HYPERSINNOH_37_22_SOLACEON_TOWN, sLocationName187},
    {LAYOUT_HYPERSINNOH_37_23_SOLACEON_TOWN, sLocationName187},
    {LAYOUT_HYPERSINNOH_37_24_SOLACEON_TOWN, sLocationName187},
    {LAYOUT_HYPERSINNOH_37_25_SOLACEON_TOWN, sLocationName187},
    {LAYOUT_HYPERSINNOH_37_26_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_27_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_28_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_29_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_2_SANDGEM_TOWN, sLocationName174},
    {LAYOUT_HYPERSINNOH_37_30_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_31_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_32_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_33_PASTORIA_CITY, sLocationName80},
    {LAYOUT_HYPERSINNOH_37_34_PASTORIA_CITY, sLocationName80},
    {LAYOUT_HYPERSINNOH_37_35_PASTORIA_CITY, sLocationName80},
    {LAYOUT_HYPERSINNOH_37_37_CELESTIC_TOWN, sLocationName17},
    {LAYOUT_HYPERSINNOH_37_38_CELESTIC_TOWN, sLocationName17},
    {LAYOUT_HYPERSINNOH_37_39_CELESTIC_TOWN, sLocationName17},
    {LAYOUT_HYPERSINNOH_37_3_SANDGEM_TOWN, sLocationName174},
    {LAYOUT_HYPERSINNOH_37_40_CANALAVE_CITY, sLocationName11},
    {LAYOUT_HYPERSINNOH_37_41_CANALAVE_CITY, sLocationName11},
    {LAYOUT_HYPERSINNOH_37_42_CANALAVE_CITY, sLocationName11},
    {LAYOUT_HYPERSINNOH_37_43_SNOWPOINT_CITY, sLocationName185},
    {LAYOUT_HYPERSINNOH_37_44_SNOWPOINT_CITY, sLocationName185},
    {LAYOUT_HYPERSINNOH_37_45_SNOWPOINT_CITY, sLocationName185},
    {LAYOUT_HYPERSINNOH_37_46_SUNYSHORE_CITY, sLocationName192},
    {LAYOUT_HYPERSINNOH_37_47_SUNYSHORE_CITY, sLocationName192},
    {LAYOUT_HYPERSINNOH_37_48_SUNYSHORE_CITY, sLocationName192},
    {LAYOUT_HYPERSINNOH_37_49_SINNOH_LEAGUE, sLocationName181},
    {LAYOUT_HYPERSINNOH_37_4_SANDGEM_TOWN, sLocationName174},
    {LAYOUT_HYPERSINNOH_37_52_FUEGO_IRONWORKS, sLocationName38},
    {LAYOUT_HYPERSINNOH_37_53_VALLEY_WINDWORKS, sLocationName204},
    {LAYOUT_HYPERSINNOH_37_54_OLD_CHATEAU, sLocationName72},
    {LAYOUT_HYPERSINNOH_37_55_OLD_CHATEAU, sLocationName72},
    {LAYOUT_HYPERSINNOH_37_56_OLD_CHATEAU, sLocationName72},
    {LAYOUT_HYPERSINNOH_37_57_OLD_CHATEAU, sLocationName72},
    {LAYOUT_HYPERSINNOH_37_58_GREAT_MARSH, sLocationName42},
    {LAYOUT_HYPERSINNOH_37_59_GREAT_MARSH, sLocationName42},
    {LAYOUT_HYPERSINNOH_37_5_SANDGEM_TOWN, sLocationName174},
    {LAYOUT_HYPERSINNOH_37_60_GREAT_MARSH, sLocationName42},
    {LAYOUT_HYPERSINNOH_37_61_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_37_62_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_37_63_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_37_64_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_37_65_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_37_66_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_67_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_68_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_69_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_6_OREBURGH_CITY, sLocationName75},
    {LAYOUT_HYPERSINNOH_37_70_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_71_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_72_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_73_HEARTHOME_CITY, sLocationName43},
    {LAYOUT_HYPERSINNOH_37_74_OREBURGH_CITY, sLocationName75},
    {LAYOUT_HYPERSINNOH_37_75_JUBILIFE_CITY, sLocationName50},
    {LAYOUT_HYPERSINNOH_37_76_JUBILIFE_CITY, sLocationName50},
    {LAYOUT_HYPERSINNOH_37_77_JUBILIFE_CITY, sLocationName50},
    {LAYOUT_HYPERSINNOH_37_78_JUBILIFE_CITY, sLocationName50},
    {LAYOUT_HYPERSINNOH_37_79_JUBILIFE_CITY, sLocationName50},
    {LAYOUT_HYPERSINNOH_37_7_OREBURGH_CITY, sLocationName75},
    {LAYOUT_HYPERSINNOH_37_80_JUBILIFE_CITY, sLocationName50},
    {LAYOUT_HYPERSINNOH_37_81_JUBILIFE_CITY, sLocationName50},
    {LAYOUT_HYPERSINNOH_37_82_OREBURGH_CITY, sLocationName75},
    {LAYOUT_HYPERSINNOH_37_83_ETERNA_CITY, sLocationName32},
    {LAYOUT_HYPERSINNOH_37_84_HEARTHOME_CITY, sLocationName43},
    {LAYOUT_HYPERSINNOH_37_85_HEARTHOME_CITY, sLocationName43},
    {LAYOUT_HYPERSINNOH_37_86_CANALAVE_CITY, sLocationName11},
    {LAYOUT_HYPERSINNOH_37_87_CANALAVE_CITY, sLocationName11},
    {LAYOUT_HYPERSINNOH_37_88_CANALAVE_CITY, sLocationName11},
    {LAYOUT_HYPERSINNOH_37_89_CANALAVE_CITY, sLocationName11},
    {LAYOUT_HYPERSINNOH_37_8_OREBURGH_CITY, sLocationName75},
    {LAYOUT_HYPERSINNOH_37_90_SNOWPOINT_CITY, sLocationName185},
    {LAYOUT_HYPERSINNOH_37_91_PASTORIA_CITY, sLocationName80},
    {LAYOUT_HYPERSINNOH_37_92_SUNYSHORE_CITY, sLocationName192},
    {LAYOUT_HYPERSINNOH_37_93_VEILSTONE_CITY, sLocationName206},
    {LAYOUT_HYPERSINNOH_37_94_SINNOH_REGION, sLocationName182},
    {LAYOUT_HYPERSINNOH_37_95_SINNOH_REGION, sLocationName182},
    {LAYOUT_HYPERSINNOH_37_97_CANALAVE_CITY, sLocationName11},
    {LAYOUT_HYPERSINNOH_37_98_CANALAVE_CITY, sLocationName11},
    {LAYOUT_HYPERSINNOH_37_99_CANALAVE_CITY, sLocationName11},
    {LAYOUT_HYPERSINNOH_37_9_FLOAROMA_TOWN, sLocationName35},
    {LAYOUT_KANTOAR_0_0_BATTLECOLOSSEUM_2P, sLocationName4},
    {LAYOUT_KANTOAR_0_1_TRADECENTER, sLocationName196},
    {LAYOUT_KANTOAR_0_2_RECORDCORNER, sLocationName89},
    {LAYOUT_KANTOAR_0_3_BATTLECOLOSSEUM_4P, sLocationName4},
    {LAYOUT_KANTOAR_0_4_UNIONROOM, sLocationName203},
    {LAYOUT_KANTOAR_10_0_CELADONCITY_DEPARTMENTSTORE_1F, sLocationName16},
    {LAYOUT_KANTOAR_10_10_CELADONCITY_CONDOMINIUMS_ROOF, sLocationName16},
    {LAYOUT_KANTOAR_10_11_CELADONCITY_CONDOMINIUMS_ROOFROOM, sLocationName16},
    {LAYOUT_KANTOAR_10_12_CELADONCITY_POKEMONCENTER_1F, sLocationName16},
    {LAYOUT_KANTOAR_10_13_CELADONCITY_POKEMONCENTER_2F, sLocationName16},
    {LAYOUT_KANTOAR_10_14_CELADONCITY_GAMECORNER, sLocationName16},
    {LAYOUT_KANTOAR_10_15_CELADONCITY_GAMECORNER_PRIZEROOM, sLocationName16},
    {LAYOUT_KANTOAR_10_16_CELADONCITY_GYM, sLocationName16},
    {LAYOUT_KANTOAR_10_17_CELADONCITY_RESTAURANT, sLocationName16},
    {LAYOUT_KANTOAR_10_18_CELADONCITY_HOUSE1, sLocationName16},
    {LAYOUT_KANTOAR_10_19_CELADONCITY_HOTEL, sLocationName16},
    {LAYOUT_KANTOAR_10_1_CELADONCITY_DEPARTMENTSTORE_2F, sLocationName16},
    {LAYOUT_KANTOAR_10_2_CELADONCITY_DEPARTMENTSTORE_3F, sLocationName16},
    {LAYOUT_KANTOAR_10_3_CELADONCITY_DEPARTMENTSTORE_4F, sLocationName16},
    {LAYOUT_KANTOAR_10_4_CELADONCITY_DEPARTMENTSTORE_5F, sLocationName16},
    {LAYOUT_KANTOAR_10_5_CELADONCITY_DEPARTMENTSTORE_ROOF, sLocationName16},
    {LAYOUT_KANTOAR_10_6_CELADONCITY_DEPARTMENTSTORE_ELEVATOR, sLocationName16},
    {LAYOUT_KANTOAR_10_7_CELADONCITY_CONDOMINIUMS_1F, sLocationName16},
    {LAYOUT_KANTOAR_10_8_CELADONCITY_CONDOMINIUMS_2F, sLocationName16},
    {LAYOUT_KANTOAR_10_9_CELADONCITY_CONDOMINIUMS_3F, sLocationName16},
    {LAYOUT_KANTOAR_11_0_FUCHSIACITY_SAFARIZONE_ENTRANCE, sLocationName37},
    {LAYOUT_KANTOAR_11_1_FUCHSIACITY_MART, sLocationName37},
    {LAYOUT_KANTOAR_11_2_FUCHSIACITY_SAFARIZONE_OFFICE, sLocationName37},
    {LAYOUT_KANTOAR_11_3_FUCHSIACITY_GYM, sLocationName37},
    {LAYOUT_KANTOAR_11_4_FUCHSIACITY_HOUSE1, sLocationName37},
    {LAYOUT_KANTOAR_11_5_FUCHSIACITY_POKEMONCENTER_1F, sLocationName37},
    {LAYOUT_KANTOAR_11_6_FUCHSIACITY_POKEMONCENTER_2F, sLocationName37},
    {LAYOUT_KANTOAR_11_7_FUCHSIACITY_WARDENSHOUSE, sLocationName37},
    {LAYOUT_KANTOAR_11_8_FUCHSIACITY_HOUSE2, sLocationName37},
    {LAYOUT_KANTOAR_11_9_FUCHSIACITY_HOUSE3, sLocationName37},
    {LAYOUT_KANTOAR_12_0_CINNABARISLAND_GYM, sLocationName22},
    {LAYOUT_KANTOAR_12_1_CINNABARISLAND_POKEMONLAB_ENTRANCE, sLocationName22},
    {LAYOUT_KANTOAR_12_2_CINNABARISLAND_POKEMONLAB_LOUNGE, sLocationName22},
    {LAYOUT_KANTOAR_12_3_CINNABARISLAND_POKEMONLAB_RESEARCHROOM, sLocationName22},
    {LAYOUT_KANTOAR_12_4_CINNABARISLAND_POKEMONLAB_EXPERIMENTROOM, sLocationName22},
    {LAYOUT_KANTOAR_12_5_CINNABARISLAND_POKEMONCENTER_1F, sLocationName22},
    {LAYOUT_KANTOAR_12_6_CINNABARISLAND_POKEMONCENTER_2F, sLocationName22},
    {LAYOUT_KANTOAR_12_7_CINNABARISLAND_MART, sLocationName22},
    {LAYOUT_KANTOAR_13_0_INDIGOPLATEAU_POKEMONCENTER_1F, sLocationName47},
    {LAYOUT_KANTOAR_13_1_INDIGOPLATEAU_POKEMONCENTER_2F, sLocationName47},
    {LAYOUT_KANTOAR_14_0_SAFFRONCITY_COPYCATSHOUSE_1F, sLocationName173},
    {LAYOUT_KANTOAR_14_1_SAFFRONCITY_COPYCATSHOUSE_2F, sLocationName173},
    {LAYOUT_KANTOAR_14_2_SAFFRONCITY_DOJO, sLocationName173},
    {LAYOUT_KANTOAR_14_3_SAFFRONCITY_GYM, sLocationName173},
    {LAYOUT_KANTOAR_14_4_SAFFRONCITY_HOUSE, sLocationName173},
    {LAYOUT_KANTOAR_14_5_SAFFRONCITY_MART, sLocationName173},
    {LAYOUT_KANTOAR_14_6_SAFFRONCITY_POKEMONCENTER_1F, sLocationName173},
    {LAYOUT_KANTOAR_14_7_SAFFRONCITY_POKEMONCENTER_2F, sLocationName173},
    {LAYOUT_KANTOAR_14_8_SAFFRONCITY_MRPSYCHICSHOUSE, sLocationName173},
    {LAYOUT_KANTOAR_14_9_SAFFRONCITY_POKEMONTRAINERFANCLUB, sLocationName173},
    {LAYOUT_KANTOAR_15_0_ROUTE2_VIRIDIANFOREST_SOUTHENTRANCE, sLocationName154},
    {LAYOUT_KANTOAR_15_1_ROUTE2_HOUSE, sLocationName154},
    {LAYOUT_KANTOAR_15_2_ROUTE2_EASTBUILDING, sLocationName154},
    {LAYOUT_KANTOAR_15_3_ROUTE2_VIRIDIANFOREST_NORTHENTRANCE, sLocationName154},
    {LAYOUT_KANTOAR_16_0_ROUTE4_POKEMONCENTER_1F, sLocationName162},
    {LAYOUT_KANTOAR_16_1_ROUTE4_POKEMONCENTER_2F, sLocationName162},
    {LAYOUT_KANTOAR_17_0_ROUTE5_POKEMONDAYCARE, sLocationName163},
    {LAYOUT_KANTOAR_17_1_ROUTE5_SOUTHENTRANCE, sLocationName163},
    {LAYOUT_KANTOAR_18_0_ROUTE6_NORTHENTRANCE, sLocationName164},
    {LAYOUT_KANTOAR_18_1_ROUTE6_UNUSEDHOUSE, sLocationName164},
    {LAYOUT_KANTOAR_19_0_ROUTE7_EASTENTRANCE, sLocationName165},
    {LAYOUT_KANTOAR_1_0_VIRIDIANFOREST, sLocationName212},
    {LAYOUT_KANTOAR_1_100_MTEMBER_SUMMITPATH_3F, sLocationName62},
    {LAYOUT_KANTOAR_1_101_MTEMBER_SUMMIT, sLocationName62},
    {LAYOUT_KANTOAR_1_102_MTEMBER_RUBYPATH_B5F, sLocationName62},
    {LAYOUT_KANTOAR_1_103_MTEMBER_RUBYPATH_1F, sLocationName62},
    {LAYOUT_KANTOAR_1_104_MTEMBER_RUBYPATH_B1F, sLocationName62},
    {LAYOUT_KANTOAR_1_105_MTEMBER_RUBYPATH_B2F, sLocationName62},
    {LAYOUT_KANTOAR_1_106_MTEMBER_RUBYPATH_B3F, sLocationName62},
    {LAYOUT_KANTOAR_1_107_MTEMBER_RUBYPATH_B1F_STAIRS, sLocationName62},
    {LAYOUT_KANTOAR_1_108_MTEMBER_RUBYPATH_B2F_STAIRS, sLocationName62},
    {LAYOUT_KANTOAR_1_109_THREEISLAND_BERRYFOREST, sLocationName6},
    {LAYOUT_KANTOAR_1_10_SSANNE_KITCHEN, sLocationName171},
    {LAYOUT_KANTOAR_1_110_FOURISLAND_ICEFALLCAVE_ENTRANCE, sLocationName45},
    {LAYOUT_KANTOAR_1_111_FOURISLAND_ICEFALLCAVE_1F, sLocationName45},
    {LAYOUT_KANTOAR_1_112_FOURISLAND_ICEFALLCAVE_B1F, sLocationName45},
    {LAYOUT_KANTOAR_1_113_FOURISLAND_ICEFALLCAVE_BACK, sLocationName45},
    {LAYOUT_KANTOAR_1_114_FIVEISLAND_ROCKETWAREHOUSE, sLocationName34},
    {LAYOUT_KANTOAR_1_115_SIXISLAND_DOTTEDHOLE_1F, sLocationName183},
    {LAYOUT_KANTOAR_1_116_SIXISLAND_DOTTEDHOLE_B1F, sLocationName183},
    {LAYOUT_KANTOAR_1_117_SIXISLAND_DOTTEDHOLE_B2F, sLocationName183},
    {LAYOUT_KANTOAR_1_118_SIXISLAND_DOTTEDHOLE_B3F, sLocationName183},
    {LAYOUT_KANTOAR_1_119_SIXISLAND_DOTTEDHOLE_B4F, sLocationName183},
    {LAYOUT_KANTOAR_1_11_SSANNE_CAPTAINSOFFICE, sLocationName171},
    {LAYOUT_KANTOAR_1_120_SIXISLAND_DOTTEDHOLE_SAPPHIREROOM, sLocationName183},
    {LAYOUT_KANTOAR_1_121_SIXISLAND_PATTERNBUSH, sLocationName183},
    {LAYOUT_KANTOAR_1_122_SIXISLAND_ALTERINGCAVE, sLocationName183},
    {LAYOUT_KANTOAR_1_12_SSANNE_1F_ROOM1, sLocationName171},
    {LAYOUT_KANTOAR_1_13_SSANNE_1F_ROOM2, sLocationName171},
    {LAYOUT_KANTOAR_1_14_SSANNE_1F_ROOM3, sLocationName171},
    {LAYOUT_KANTOAR_1_15_SSANNE_1F_ROOM4, sLocationName171},
    {LAYOUT_KANTOAR_1_16_SSANNE_1F_ROOM5, sLocationName171},
    {LAYOUT_KANTOAR_1_17_SSANNE_1F_ROOM7, sLocationName171},
    {LAYOUT_KANTOAR_1_18_SSANNE_2F_ROOM1, sLocationName171},
    {LAYOUT_KANTOAR_1_19_SSANNE_2F_ROOM2, sLocationName171},
    {LAYOUT_KANTOAR_1_1_MTMOON_1F, sLocationName63},
    {LAYOUT_KANTOAR_1_20_SSANNE_2F_ROOM3, sLocationName171},
    {LAYOUT_KANTOAR_1_21_SSANNE_2F_ROOM4, sLocationName171},
    {LAYOUT_KANTOAR_1_22_SSANNE_2F_ROOM5, sLocationName171},
    {LAYOUT_KANTOAR_1_23_SSANNE_2F_ROOM6, sLocationName171},
    {LAYOUT_KANTOAR_1_24_SSANNE_B1F_ROOM1, sLocationName171},
    {LAYOUT_KANTOAR_1_25_SSANNE_B1F_ROOM2, sLocationName171},
    {LAYOUT_KANTOAR_1_26_SSANNE_B1F_ROOM3, sLocationName171},
    {LAYOUT_KANTOAR_1_27_SSANNE_B1F_ROOM4, sLocationName171},
    {LAYOUT_KANTOAR_1_28_SSANNE_B1F_ROOM5, sLocationName171},
    {LAYOUT_KANTOAR_1_29_SSANNE_1F_ROOM6, sLocationName171},
    {LAYOUT_KANTOAR_1_2_MTMOON_B1F, sLocationName63},
    {LAYOUT_KANTOAR_1_30_UNDERGROUNDPATH_NORTHENTRANCE, sLocationName201},
    {LAYOUT_KANTOAR_1_31_UNDERGROUNDPATH_NORTHSOUTHTUNNEL, sLocationName201},
    {LAYOUT_KANTOAR_1_32_UNDERGROUNDPATH_SOUTHENTRANCE, sLocationName201},
    {LAYOUT_KANTOAR_1_33_UNDERGROUNDPATH_WESTENTRANCE, sLocationName201},
    {LAYOUT_KANTOAR_1_34_UNDERGROUNDPATH_EASTWESTTUNNEL, sLocationName201},
    {LAYOUT_KANTOAR_1_35_UNDERGROUNDPATH_EASTENTRANCE, sLocationName201},
    {LAYOUT_KANTOAR_1_36_DIGLETTSCAVE_NORTHENTRANCE, sLocationName27},
    {LAYOUT_KANTOAR_1_37_DIGLETTSCAVE_B1F, sLocationName27},
    {LAYOUT_KANTOAR_1_38_DIGLETTSCAVE_SOUTHENTRANCE, sLocationName27},
    {LAYOUT_KANTOAR_1_39_VICTORYROAD_1F, sLocationName209},
    {LAYOUT_KANTOAR_1_3_MTMOON_B2F, sLocationName63},
    {LAYOUT_KANTOAR_1_40_VICTORYROAD_2F, sLocationName209},
    {LAYOUT_KANTOAR_1_41_VICTORYROAD_3F, sLocationName209},
    {LAYOUT_KANTOAR_1_42_ROCKETHIDEOUT_B1F, sLocationName94},
    {LAYOUT_KANTOAR_1_43_ROCKETHIDEOUT_B2F, sLocationName94},
    {LAYOUT_KANTOAR_1_44_ROCKETHIDEOUT_B3F, sLocationName94},
    {LAYOUT_KANTOAR_1_45_ROCKETHIDEOUT_B4F, sLocationName94},
    {LAYOUT_KANTOAR_1_46_ROCKETHIDEOUT_ELEVATOR, sLocationName94},
    {LAYOUT_KANTOAR_1_47_SILPHCO_1F, sLocationName179},
    {LAYOUT_KANTOAR_1_48_SILPHCO_2F, sLocationName179},
    {LAYOUT_KANTOAR_1_49_SILPHCO_3F, sLocationName179},
    {LAYOUT_KANTOAR_1_4_SSANNE_EXTERIOR, sLocationName171},
    {LAYOUT_KANTOAR_1_50_SILPHCO_4F, sLocationName179},
    {LAYOUT_KANTOAR_1_51_SILPHCO_5F, sLocationName179},
    {LAYOUT_KANTOAR_1_52_SILPHCO_6F, sLocationName179},
    {LAYOUT_KANTOAR_1_53_SILPHCO_7F, sLocationName179},
    {LAYOUT_KANTOAR_1_54_SILPHCO_8F, sLocationName179},
    {LAYOUT_KANTOAR_1_55_SILPHCO_9F, sLocationName179},
    {LAYOUT_KANTOAR_1_56_SILPHCO_10F, sLocationName179},
    {LAYOUT_KANTOAR_1_57_SILPHCO_11F, sLocationName179},
    {LAYOUT_KANTOAR_1_58_SILPHCO_ELEVATOR, sLocationName179},
    {LAYOUT_KANTOAR_1_59_POKEMONMANSION_1F, sLocationName84},
    {LAYOUT_KANTOAR_1_5_SSANNE_1F_CORRIDOR, sLocationName171},
    {LAYOUT_KANTOAR_1_60_POKEMONMANSION_2F, sLocationName84},
    {LAYOUT_KANTOAR_1_61_POKEMONMANSION_3F, sLocationName84},
    {LAYOUT_KANTOAR_1_62_POKEMONMANSION_B1F, sLocationName84},
    {LAYOUT_KANTOAR_1_63_SAFARIZONE_CENTER, sLocationName172},
    {LAYOUT_KANTOAR_1_64_SAFARIZONE_EAST, sLocationName172},
    {LAYOUT_KANTOAR_1_65_SAFARIZONE_NORTH, sLocationName172},
    {LAYOUT_KANTOAR_1_66_SAFARIZONE_WEST, sLocationName172},
    {LAYOUT_KANTOAR_1_67_SAFARIZONE_CENTER_RESTHOUSE, sLocationName172},
    {LAYOUT_KANTOAR_1_68_SAFARIZONE_EAST_RESTHOUSE, sLocationName172},
    {LAYOUT_KANTOAR_1_69_SAFARIZONE_NORTH_RESTHOUSE, sLocationName172},
    {LAYOUT_KANTOAR_1_6_SSANNE_2F_CORRIDOR, sLocationName171},
    {LAYOUT_KANTOAR_1_70_SAFARIZONE_WEST_RESTHOUSE, sLocationName172},
    {LAYOUT_KANTOAR_1_71_SAFARIZONE_SECRETHOUSE, sLocationName172},
    {LAYOUT_KANTOAR_1_72_CERULEANCAVE_1F, sLocationName18},
    {LAYOUT_KANTOAR_1_73_CERULEANCAVE_2F, sLocationName18},
    {LAYOUT_KANTOAR_1_74_CERULEANCAVE_B1F, sLocationName18},
    {LAYOUT_KANTOAR_1_75_POKEMONLEAGUE_LORELEISROOM, sLocationName83},
    {LAYOUT_KANTOAR_1_76_POKEMONLEAGUE_BRUNOSROOM, sLocationName83},
    {LAYOUT_KANTOAR_1_77_POKEMONLEAGUE_AGATHASROOM, sLocationName83},
    {LAYOUT_KANTOAR_1_78_POKEMONLEAGUE_LANCESROOM, sLocationName83},
    {LAYOUT_KANTOAR_1_79_POKEMONLEAGUE_CHAMPIONSROOM, sLocationName83},
    {LAYOUT_KANTOAR_1_7_SSANNE_3F_CORRIDOR, sLocationName171},
    {LAYOUT_KANTOAR_1_80_POKEMONLEAGUE_HALLOFFAME, sLocationName83},
    {LAYOUT_KANTOAR_1_81_ROCKTUNNEL_1F, sLocationName92},
    {LAYOUT_KANTOAR_1_82_ROCKTUNNEL_B1F, sLocationName92},
    {LAYOUT_KANTOAR_1_83_SEAFOAMISLANDS_1F, sLocationName175},
    {LAYOUT_KANTOAR_1_84_SEAFOAMISLANDS_B1F, sLocationName175},
    {LAYOUT_KANTOAR_1_85_SEAFOAMISLANDS_B2F, sLocationName175},
    {LAYOUT_KANTOAR_1_86_SEAFOAMISLANDS_B3F, sLocationName175},
    {LAYOUT_KANTOAR_1_87_SEAFOAMISLANDS_B4F, sLocationName175},
    {LAYOUT_KANTOAR_1_88_POKEMONTOWER_1F, sLocationName85},
    {LAYOUT_KANTOAR_1_89_POKEMONTOWER_2F, sLocationName85},
    {LAYOUT_KANTOAR_1_8_SSANNE_B1F_CORRIDOR, sLocationName171},
    {LAYOUT_KANTOAR_1_90_POKEMONTOWER_3F, sLocationName85},
    {LAYOUT_KANTOAR_1_91_POKEMONTOWER_4F, sLocationName85},
    {LAYOUT_KANTOAR_1_92_POKEMONTOWER_5F, sLocationName85},
    {LAYOUT_KANTOAR_1_93_POKEMONTOWER_6F, sLocationName85},
    {LAYOUT_KANTOAR_1_94_POKEMONTOWER_7F, sLocationName85},
    {LAYOUT_KANTOAR_1_95_POWERPLANT, sLocationName86},
    {LAYOUT_KANTOAR_1_96_MTEMBER_RUBYPATH_B4F, sLocationName62},
    {LAYOUT_KANTOAR_1_97_MTEMBER_EXTERIOR, sLocationName62},
    {LAYOUT_KANTOAR_1_98_MTEMBER_SUMMITPATH_1F, sLocationName62},
    {LAYOUT_KANTOAR_1_99_MTEMBER_SUMMITPATH_2F, sLocationName62},
    {LAYOUT_KANTOAR_1_9_SSANNE_DECK, sLocationName171},
    {LAYOUT_KANTOAR_20_0_ROUTE8_WESTENTRANCE, sLocationName166},
    {LAYOUT_KANTOAR_21_0_ROUTE10_POKEMONCENTER_1F, sLocationName144},
    {LAYOUT_KANTOAR_21_1_ROUTE10_POKEMONCENTER_2F, sLocationName144},
    {LAYOUT_KANTOAR_22_0_ROUTE11_EASTENTRANCE_1F, sLocationName145},
    {LAYOUT_KANTOAR_22_1_ROUTE11_EASTENTRANCE_2F, sLocationName145},
    {LAYOUT_KANTOAR_23_0_ROUTE12_NORTHENTRANCE_1F, sLocationName146},
    {LAYOUT_KANTOAR_23_1_ROUTE12_NORTHENTRANCE_2F, sLocationName146},
    {LAYOUT_KANTOAR_23_2_ROUTE12_FISHINGHOUSE, sLocationName146},
    {LAYOUT_KANTOAR_24_0_ROUTE15_WESTENTRANCE_1F, sLocationName149},
    {LAYOUT_KANTOAR_24_1_ROUTE15_WESTENTRANCE_2F, sLocationName149},
    {LAYOUT_KANTOAR_25_0_ROUTE16_HOUSE, sLocationName150},
    {LAYOUT_KANTOAR_25_1_ROUTE16_NORTHENTRANCE_1F, sLocationName150},
    {LAYOUT_KANTOAR_25_2_ROUTE16_NORTHENTRANCE_2F, sLocationName150},
    {LAYOUT_KANTOAR_26_0_ROUTE18_EASTENTRANCE_1F, sLocationName152},
    {LAYOUT_KANTOAR_26_1_ROUTE18_EASTENTRANCE_2F, sLocationName152},
    {LAYOUT_KANTOAR_27_0_ROUTE19_UNUSEDHOUSE, sLocationName153},
    {LAYOUT_KANTOAR_28_0_ROUTE22_NORTHENTRANCE, sLocationName157},
    {LAYOUT_KANTOAR_29_0_ROUTE23_UNUSEDHOUSE, sLocationName158},
    {LAYOUT_KANTOAR_2_0_NAVELROCK_EXTERIOR, sLocationName69},
    {LAYOUT_KANTOAR_2_10_TRAINERTOWER_LOBBY, sLocationName197},
    {LAYOUT_KANTOAR_2_11_TRAINERTOWER_ELEVATOR, sLocationName197},
    {LAYOUT_KANTOAR_2_12_FIVEISLAND_LOSTCAVE_ENTRANCE, sLocationName58},
    {LAYOUT_KANTOAR_2_13_FIVEISLAND_LOSTCAVE_ROOM1, sLocationName58},
    {LAYOUT_KANTOAR_2_14_FIVEISLAND_LOSTCAVE_ROOM2, sLocationName58},
    {LAYOUT_KANTOAR_2_15_FIVEISLAND_LOSTCAVE_ROOM3, sLocationName58},
    {LAYOUT_KANTOAR_2_16_FIVEISLAND_LOSTCAVE_ROOM4, sLocationName58},
    {LAYOUT_KANTOAR_2_17_FIVEISLAND_LOSTCAVE_ROOM5, sLocationName58},
    {LAYOUT_KANTOAR_2_18_FIVEISLAND_LOSTCAVE_ROOM6, sLocationName58},
    {LAYOUT_KANTOAR_2_19_FIVEISLAND_LOSTCAVE_ROOM7, sLocationName58},
    {LAYOUT_KANTOAR_2_1_TRAINERTOWER_1F, sLocationName197},
    {LAYOUT_KANTOAR_2_20_FIVEISLAND_LOSTCAVE_ROOM8, sLocationName58},
    {LAYOUT_KANTOAR_2_21_FIVEISLAND_LOSTCAVE_ROOM9, sLocationName58},
    {LAYOUT_KANTOAR_2_22_FIVEISLAND_LOSTCAVE_ROOM10, sLocationName58},
    {LAYOUT_KANTOAR_2_23_FIVEISLAND_LOSTCAVE_ROOM11, sLocationName58},
    {LAYOUT_KANTOAR_2_24_FIVEISLAND_LOSTCAVE_ROOM12, sLocationName58},
    {LAYOUT_KANTOAR_2_25_FIVEISLAND_LOSTCAVE_ROOM13, sLocationName58},
    {LAYOUT_KANTOAR_2_26_FIVEISLAND_LOSTCAVE_ROOM14, sLocationName58},
    {LAYOUT_KANTOAR_2_27_SEVENISLAND_TANOBYRUINS_MONEANCHAMBER, sLocationName193},
    {LAYOUT_KANTOAR_2_28_SEVENISLAND_TANOBYRUINS_LIPTOOCHAMBER, sLocationName193},
    {LAYOUT_KANTOAR_2_29_SEVENISLAND_TANOBYRUINS_WEEPTHCHAMBER, sLocationName193},
    {LAYOUT_KANTOAR_2_2_TRAINERTOWER_2F, sLocationName197},
    {LAYOUT_KANTOAR_2_30_SEVENISLAND_TANOBYRUINS_DILFORDCHAMBER, sLocationName193},
    {LAYOUT_KANTOAR_2_31_SEVENISLAND_TANOBYRUINS_SCUFIBCHAMBER, sLocationName193},
    {LAYOUT_KANTOAR_2_32_SEVENISLAND_TANOBYRUINS_RIXYCHAMBER, sLocationName193},
    {LAYOUT_KANTOAR_2_33_SEVENISLAND_TANOBYRUINS_VIAPOISCHAMBER, sLocationName193},
    {LAYOUT_KANTOAR_2_34_THREEISLAND_DUNSPARCETUNNEL, sLocationName194},
    {LAYOUT_KANTOAR_2_35_SEVENISLAND_SEVAULTCANYON_TANOBYKEY, sLocationName177},
    {LAYOUT_KANTOAR_2_36_NAVELROCK_1F, sLocationName69},
    {LAYOUT_KANTOAR_2_37_NAVELROCK_SUMMIT, sLocationName69},
    {LAYOUT_KANTOAR_2_38_NAVELROCK_BASE, sLocationName69},
    {LAYOUT_KANTOAR_2_39_NAVELROCK_SUMMITPATH_2F, sLocationName69},
    {LAYOUT_KANTOAR_2_3_TRAINERTOWER_3F, sLocationName197},
    {LAYOUT_KANTOAR_2_40_NAVELROCK_SUMMITPATH_3F, sLocationName69},
    {LAYOUT_KANTOAR_2_41_NAVELROCK_SUMMITPATH_4F, sLocationName69},
    {LAYOUT_KANTOAR_2_42_NAVELROCK_SUMMITPATH_5F, sLocationName69},
    {LAYOUT_KANTOAR_2_43_NAVELROCK_BASEPATH_B1F, sLocationName69},
    {LAYOUT_KANTOAR_2_44_NAVELROCK_BASEPATH_B2F, sLocationName69},
    {LAYOUT_KANTOAR_2_45_NAVELROCK_BASEPATH_B3F, sLocationName69},
    {LAYOUT_KANTOAR_2_46_NAVELROCK_BASEPATH_B4F, sLocationName69},
    {LAYOUT_KANTOAR_2_47_NAVELROCK_BASEPATH_B5F, sLocationName69},
    {LAYOUT_KANTOAR_2_48_NAVELROCK_BASEPATH_B6F, sLocationName69},
    {LAYOUT_KANTOAR_2_49_NAVELROCK_BASEPATH_B7F, sLocationName69},
    {LAYOUT_KANTOAR_2_4_TRAINERTOWER_4F, sLocationName197},
    {LAYOUT_KANTOAR_2_50_NAVELROCK_BASEPATH_B8F, sLocationName69},
    {LAYOUT_KANTOAR_2_51_NAVELROCK_BASEPATH_B9F, sLocationName69},
    {LAYOUT_KANTOAR_2_52_NAVELROCK_BASEPATH_B10F, sLocationName69},
    {LAYOUT_KANTOAR_2_53_NAVELROCK_BASEPATH_B11F, sLocationName69},
    {LAYOUT_KANTOAR_2_54_NAVELROCK_B1F, sLocationName69},
    {LAYOUT_KANTOAR_2_55_NAVELROCK_FORK, sLocationName69},
    {LAYOUT_KANTOAR_2_56_BIRTHISLAND_EXTERIOR, sLocationName7},
    {LAYOUT_KANTOAR_2_57_ONEISLAND_KINDLEROAD_EMBERSPA, sLocationName51},
    {LAYOUT_KANTOAR_2_58_BIRTHISLAND_HARBOR, sLocationName7},
    {LAYOUT_KANTOAR_2_59_NAVELROCK_HARBOR, sLocationName69},
    {LAYOUT_KANTOAR_2_5_TRAINERTOWER_5F, sLocationName197},
    {LAYOUT_KANTOAR_2_6_TRAINERTOWER_6F, sLocationName197},
    {LAYOUT_KANTOAR_2_7_TRAINERTOWER_7F, sLocationName197},
    {LAYOUT_KANTOAR_2_8_TRAINERTOWER_8F, sLocationName197},
    {LAYOUT_KANTOAR_2_9_TRAINERTOWER_ROOF, sLocationName197},
    {LAYOUT_KANTOAR_30_0_ROUTE25_SEACOTTAGE, sLocationName160},
    {LAYOUT_KANTOAR_31_0_SEVENISLAND_HOUSE_ROOM1, sLocationName178},
    {LAYOUT_KANTOAR_31_1_SEVENISLAND_HOUSE_ROOM2, sLocationName178},
    {LAYOUT_KANTOAR_31_2_SEVENISLAND_MART, sLocationName178},
    {LAYOUT_KANTOAR_31_3_SEVENISLAND_POKEMONCENTER_1F, sLocationName178},
    {LAYOUT_KANTOAR_31_4_SEVENISLAND_POKEMONCENTER_2F, sLocationName178},
    {LAYOUT_KANTOAR_31_5_SEVENISLAND_UNUSEDHOUSE, sLocationName178},
    {LAYOUT_KANTOAR_31_6_SEVENISLAND_HARBOR, sLocationName178},
    {LAYOUT_KANTOAR_32_0_ONEISLAND_POKEMONCENTER_1F, sLocationName74},
    {LAYOUT_KANTOAR_32_1_ONEISLAND_POKEMONCENTER_2F, sLocationName74},
    {LAYOUT_KANTOAR_32_2_ONEISLAND_HOUSE1, sLocationName74},
    {LAYOUT_KANTOAR_32_3_ONEISLAND_HOUSE2, sLocationName74},
    {LAYOUT_KANTOAR_32_4_ONEISLAND_HARBOR, sLocationName74},
    {LAYOUT_KANTOAR_33_0_TWOISLAND_JOYFULGAMECORNER, sLocationName200},
    {LAYOUT_KANTOAR_33_1_TWOISLAND_HOUSE, sLocationName200},
    {LAYOUT_KANTOAR_33_2_TWOISLAND_POKEMONCENTER_1F, sLocationName200},
    {LAYOUT_KANTOAR_33_3_TWOISLAND_POKEMONCENTER_2F, sLocationName200},
    {LAYOUT_KANTOAR_33_4_TWOISLAND_HARBOR, sLocationName200},
    {LAYOUT_KANTOAR_34_0_THREEISLAND_HOUSE1, sLocationName194},
    {LAYOUT_KANTOAR_34_1_THREEISLAND_POKEMONCENTER_1F, sLocationName194},
    {LAYOUT_KANTOAR_34_2_THREEISLAND_POKEMONCENTER_2F, sLocationName194},
    {LAYOUT_KANTOAR_34_3_THREEISLAND_MART, sLocationName194},
    {LAYOUT_KANTOAR_34_4_THREEISLAND_HOUSE2, sLocationName194},
    {LAYOUT_KANTOAR_34_5_THREEISLAND_HOUSE3, sLocationName194},
    {LAYOUT_KANTOAR_34_6_THREEISLAND_HOUSE4, sLocationName194},
    {LAYOUT_KANTOAR_34_7_THREEISLAND_HOUSE5, sLocationName194},
    {LAYOUT_KANTOAR_35_0_FOURISLAND_POKEMONDAYCARE, sLocationName36},
    {LAYOUT_KANTOAR_35_1_FOURISLAND_POKEMONCENTER_1F, sLocationName36},
    {LAYOUT_KANTOAR_35_2_FOURISLAND_POKEMONCENTER_2F, sLocationName36},
    {LAYOUT_KANTOAR_35_3_FOURISLAND_HOUSE1, sLocationName36},
    {LAYOUT_KANTOAR_35_4_FOURISLAND_LORELEISHOUSE, sLocationName36},
    {LAYOUT_KANTOAR_35_5_FOURISLAND_HARBOR, sLocationName36},
    {LAYOUT_KANTOAR_35_6_FOURISLAND_HOUSE2, sLocationName36},
    {LAYOUT_KANTOAR_35_7_FOURISLAND_MART, sLocationName36},
    {LAYOUT_KANTOAR_36_0_FIVEISLAND_POKEMONCENTER_1F, sLocationName34},
    {LAYOUT_KANTOAR_36_1_FIVEISLAND_POKEMONCENTER_2F, sLocationName34},
    {LAYOUT_KANTOAR_36_2_FIVEISLAND_HARBOR, sLocationName34},
    {LAYOUT_KANTOAR_36_3_FIVEISLAND_HOUSE1, sLocationName34},
    {LAYOUT_KANTOAR_36_4_FIVEISLAND_HOUSE2, sLocationName34},
    {LAYOUT_KANTOAR_37_0_SIXISLAND_POKEMONCENTER_1F, sLocationName183},
    {LAYOUT_KANTOAR_37_1_SIXISLAND_POKEMONCENTER_2F, sLocationName183},
    {LAYOUT_KANTOAR_37_2_SIXISLAND_HARBOR, sLocationName183},
    {LAYOUT_KANTOAR_37_3_SIXISLAND_HOUSE, sLocationName183},
    {LAYOUT_KANTOAR_37_4_SIXISLAND_MART, sLocationName183},
    {LAYOUT_KANTOAR_38_0_THREEISLAND_HARBOR, sLocationName194},
    {LAYOUT_KANTOAR_39_0_FIVEISLAND_RESORTGORGEOUS_HOUSE, sLocationName91},
    {LAYOUT_KANTOAR_3_0_PALLETTOWN, sLocationName79},
    {LAYOUT_KANTOAR_3_10_SAFFRONCITY, sLocationName173},
    {LAYOUT_KANTOAR_3_11_SAFFRONCITY_CONNECTION, sLocationName173},
    {LAYOUT_KANTOAR_3_12_ONEISLAND, sLocationName74},
    {LAYOUT_KANTOAR_3_13_TWOISLAND, sLocationName200},
    {LAYOUT_KANTOAR_3_14_THREEISLAND, sLocationName194},
    {LAYOUT_KANTOAR_3_15_FOURISLAND, sLocationName36},
    {LAYOUT_KANTOAR_3_16_FIVEISLAND, sLocationName34},
    {LAYOUT_KANTOAR_3_17_SEVENISLAND, sLocationName178},
    {LAYOUT_KANTOAR_3_18_SIXISLAND, sLocationName183},
    {LAYOUT_KANTOAR_3_19_ROUTE1, sLocationName143},
    {LAYOUT_KANTOAR_3_1_VIRIDIANCITY, sLocationName211},
    {LAYOUT_KANTOAR_3_20_ROUTE2, sLocationName154},
    {LAYOUT_KANTOAR_3_21_ROUTE3, sLocationName161},
    {LAYOUT_KANTOAR_3_22_ROUTE4, sLocationName162},
    {LAYOUT_KANTOAR_3_23_ROUTE5, sLocationName163},
    {LAYOUT_KANTOAR_3_24_ROUTE6, sLocationName164},
    {LAYOUT_KANTOAR_3_25_ROUTE7, sLocationName165},
    {LAYOUT_KANTOAR_3_26_ROUTE8, sLocationName166},
    {LAYOUT_KANTOAR_3_27_ROUTE9, sLocationName167},
    {LAYOUT_KANTOAR_3_28_ROUTE10, sLocationName144},
    {LAYOUT_KANTOAR_3_29_ROUTE11, sLocationName145},
    {LAYOUT_KANTOAR_3_2_PEWTERCITY, sLocationName81},
    {LAYOUT_KANTOAR_3_30_ROUTE12, sLocationName146},
    {LAYOUT_KANTOAR_3_31_ROUTE13, sLocationName147},
    {LAYOUT_KANTOAR_3_32_ROUTE14, sLocationName148},
    {LAYOUT_KANTOAR_3_33_ROUTE15, sLocationName149},
    {LAYOUT_KANTOAR_3_34_ROUTE16, sLocationName150},
    {LAYOUT_KANTOAR_3_35_ROUTE17, sLocationName151},
    {LAYOUT_KANTOAR_3_36_ROUTE18, sLocationName152},
    {LAYOUT_KANTOAR_3_37_ROUTE19, sLocationName153},
    {LAYOUT_KANTOAR_3_38_ROUTE20, sLocationName155},
    {LAYOUT_KANTOAR_3_39_ROUTE21_NORTH, sLocationName156},
    {LAYOUT_KANTOAR_3_3_CERULEANCITY, sLocationName19},
    {LAYOUT_KANTOAR_3_40_ROUTE21_SOUTH, sLocationName156},
    {LAYOUT_KANTOAR_3_41_ROUTE22, sLocationName157},
    {LAYOUT_KANTOAR_3_42_ROUTE23, sLocationName158},
    {LAYOUT_KANTOAR_3_43_ROUTE24, sLocationName159},
    {LAYOUT_KANTOAR_3_44_ROUTE25, sLocationName160},
    {LAYOUT_KANTOAR_3_45_ONEISLAND_KINDLEROAD, sLocationName51},
    {LAYOUT_KANTOAR_3_46_ONEISLAND_TREASUREBEACH, sLocationName198},
    {LAYOUT_KANTOAR_3_47_TWOISLAND_CAPEBRINK, sLocationName12},
    {LAYOUT_KANTOAR_3_48_THREEISLAND_BONDBRIDGE, sLocationName9},
    {LAYOUT_KANTOAR_3_49_THREEISLAND_PORT, sLocationName194},
    {LAYOUT_KANTOAR_3_4_LAVENDERTOWN, sLocationName56},
    {LAYOUT_KANTOAR_3_50_PROTOTYPE_SEVIIISLE_6, sLocationName87},
    {LAYOUT_KANTOAR_3_51_PROTOTYPE_SEVIIISLE_7, sLocationName87},
    {LAYOUT_KANTOAR_3_52_PROTOTYPE_SEVIIISLE_8, sLocationName87},
    {LAYOUT_KANTOAR_3_53_PROTOTYPE_SEVIIISLE_9, sLocationName87},
    {LAYOUT_KANTOAR_3_54_FIVEISLAND_RESORTGORGEOUS, sLocationName91},
    {LAYOUT_KANTOAR_3_55_FIVEISLAND_WATERLABYRINTH, sLocationName213},
    {LAYOUT_KANTOAR_3_56_FIVEISLAND_MEADOW, sLocationName34},
    {LAYOUT_KANTOAR_3_57_FIVEISLAND_MEMORIALPILLAR, sLocationName61},
    {LAYOUT_KANTOAR_3_58_SIXISLAND_OUTCASTISLAND, sLocationName183},
    {LAYOUT_KANTOAR_3_59_SIXISLAND_GREENPATH, sLocationName183},
    {LAYOUT_KANTOAR_3_5_VERMILIONCITY, sLocationName208},
    {LAYOUT_KANTOAR_3_60_SIXISLAND_WATERPATH, sLocationName214},
    {LAYOUT_KANTOAR_3_61_SIXISLAND_RUINVALLEY, sLocationName168},
    {LAYOUT_KANTOAR_3_62_SEVENISLAND_TRAINERTOWER, sLocationName197},
    {LAYOUT_KANTOAR_3_63_SEVENISLAND_SEVAULTCANYON_ENTRANCE, sLocationName177},
    {LAYOUT_KANTOAR_3_64_SEVENISLAND_SEVAULTCANYON, sLocationName177},
    {LAYOUT_KANTOAR_3_65_SEVENISLAND_TANOBYRUINS, sLocationName193},
    {LAYOUT_KANTOAR_3_6_CELADONCITY, sLocationName16},
    {LAYOUT_KANTOAR_3_7_FUCHSIACITY, sLocationName37},
    {LAYOUT_KANTOAR_3_8_CINNABARISLAND, sLocationName22},
    {LAYOUT_KANTOAR_3_9_INDIGOPLATEAU_EXTERIOR, sLocationName47},
    {LAYOUT_KANTOAR_40_0_TWOISLAND_CAPEBRINK_HOUSE, sLocationName12},
    {LAYOUT_KANTOAR_41_0_SIXISLAND_WATERPATH_HOUSE1, sLocationName214},
    {LAYOUT_KANTOAR_41_1_SIXISLAND_WATERPATH_HOUSE2, sLocationName214},
    {LAYOUT_KANTOAR_42_0_SEVENISLAND_SEVAULTCANYON_HOUSE, sLocationName177},
    {LAYOUT_KANTOAR_4_0_PALLETTOWN_PLAYERSHOUSE_1F, sLocationName79},
    {LAYOUT_KANTOAR_4_1_PALLETTOWN_PLAYERSHOUSE_2F, sLocationName79},
    {LAYOUT_KANTOAR_4_2_PALLETTOWN_RIVALSHOUSE, sLocationName79},
    {LAYOUT_KANTOAR_4_3_PALLETTOWN_PROFESSOROAKSLAB, sLocationName79},
    {LAYOUT_KANTOAR_5_0_VIRIDIANCITY_HOUSE, sLocationName211},
    {LAYOUT_KANTOAR_5_1_VIRIDIANCITY_GYM, sLocationName211},
    {LAYOUT_KANTOAR_5_2_VIRIDIANCITY_SCHOOL, sLocationName211},
    {LAYOUT_KANTOAR_5_3_VIRIDIANCITY_MART, sLocationName211},
    {LAYOUT_KANTOAR_5_4_VIRIDIANCITY_POKEMONCENTER_1F, sLocationName211},
    {LAYOUT_KANTOAR_5_5_VIRIDIANCITY_POKEMONCENTER_2F, sLocationName211},
    {LAYOUT_KANTOAR_6_0_PEWTERCITY_MUSEUM_1F, sLocationName81},
    {LAYOUT_KANTOAR_6_1_PEWTERCITY_MUSEUM_2F, sLocationName81},
    {LAYOUT_KANTOAR_6_2_PEWTERCITY_GYM, sLocationName81},
    {LAYOUT_KANTOAR_6_3_PEWTERCITY_MART, sLocationName81},
    {LAYOUT_KANTOAR_6_4_PEWTERCITY_HOUSE1, sLocationName81},
    {LAYOUT_KANTOAR_6_5_PEWTERCITY_POKEMONCENTER_1F, sLocationName81},
    {LAYOUT_KANTOAR_6_6_PEWTERCITY_POKEMONCENTER_2F, sLocationName81},
    {LAYOUT_KANTOAR_6_7_PEWTERCITY_HOUSE2, sLocationName81},
    {LAYOUT_KANTOAR_7_0_CERULEANCITY_HOUSE1, sLocationName19},
    {LAYOUT_KANTOAR_7_1_CERULEANCITY_HOUSE2, sLocationName19},
    {LAYOUT_KANTOAR_7_2_CERULEANCITY_HOUSE3, sLocationName19},
    {LAYOUT_KANTOAR_7_3_CERULEANCITY_POKEMONCENTER_1F, sLocationName19},
    {LAYOUT_KANTOAR_7_4_CERULEANCITY_POKEMONCENTER_2F, sLocationName19},
    {LAYOUT_KANTOAR_7_5_CERULEANCITY_GYM, sLocationName19},
    {LAYOUT_KANTOAR_7_6_CERULEANCITY_BIKESHOP, sLocationName19},
    {LAYOUT_KANTOAR_7_7_CERULEANCITY_MART, sLocationName19},
    {LAYOUT_KANTOAR_7_8_CERULEANCITY_HOUSE4, sLocationName19},
    {LAYOUT_KANTOAR_7_9_CERULEANCITY_HOUSE5, sLocationName19},
    {LAYOUT_KANTOAR_8_0_LAVENDERTOWN_POKEMONCENTER_1F, sLocationName56},
    {LAYOUT_KANTOAR_8_1_LAVENDERTOWN_POKEMONCENTER_2F, sLocationName56},
    {LAYOUT_KANTOAR_8_2_LAVENDERTOWN_VOLUNTEERPOKEMONHOUSE, sLocationName56},
    {LAYOUT_KANTOAR_8_3_LAVENDERTOWN_HOUSE1, sLocationName56},
    {LAYOUT_KANTOAR_8_4_LAVENDERTOWN_HOUSE2, sLocationName56},
    {LAYOUT_KANTOAR_8_5_LAVENDERTOWN_MART, sLocationName56},
    {LAYOUT_KANTOAR_9_0_VERMILIONCITY_HOUSE1, sLocationName208},
    {LAYOUT_KANTOAR_9_1_VERMILIONCITY_POKEMONCENTER_1F, sLocationName208},
    {LAYOUT_KANTOAR_9_2_VERMILIONCITY_POKEMONCENTER_2F, sLocationName208},
    {LAYOUT_KANTOAR_9_3_VERMILIONCITY_POKEMONFANCLUB, sLocationName208},
    {LAYOUT_KANTOAR_9_4_VERMILIONCITY_HOUSE2, sLocationName208},
    {LAYOUT_KANTOAR_9_5_VERMILIONCITY_MART, sLocationName208},
    {LAYOUT_KANTOAR_9_6_VERMILIONCITY_GYM, sLocationName208},
    {LAYOUT_KANTOAR_9_7_VERMILIONCITY_HOUSE3, sLocationName208},
    {LAYOUT_BWA_3_19_ROUTE_1, sUnovaRoute1Name},
};

#include "mercury_johto_names.inc"
#include "hns_region_names.inc"

const u8 *RegionalMapDisplayName(const struct MapHeader *header)
{
    const u8 *hnsName = HnsRegionDisplayName(header->mapLayoutId);
    if (hnsName != NULL)
        return hnsName;
    const u8 *mercuryName = MercuryJohtoDisplayName(header->mapLayoutId);
    u32 i;
    if (mercuryName != NULL)
        return mercuryName;
    for (i = 0; i < ARRAY_COUNT(sRegionalMapNames); i++)
        if (sRegionalMapNames[i].layout == header->mapLayoutId)
            return sRegionalMapNames[i].name;
    return NULL;
}
