#include "global.h"
#include "item_acquisition.h"

// Shared ordinary-shop policy. Item use, script gifts, existing ownership and
// encounter/story gates are intentionally independent of shop availability.
bool32 Item_IsQuestRelic(enum Item item)
{
    if (item <= ITEM_NONE || item >= ITEMS_COUNT)
        return FALSE;

    // Plates are discoveries; Memories are reserved for the future Devon
    // vendor. Drives are Genesect modules. Do not blacklist generic relics,
    // fossils, or battle items simply because a Legendary can hold them.
    switch (gItemsInfo[item].sortType)
    {
    case ITEM_TYPE_PLATE:
    case ITEM_TYPE_MEMORY:
    case ITEM_TYPE_DRIVE:
        return TRUE;
    default:
        break;
    }

    switch (item)
    {
    case ITEM_RED_ORB:
    case ITEM_BLUE_ORB:
    case ITEM_SOUL_DEW:
    case ITEM_ADAMANT_ORB:
    case ITEM_LUSTROUS_ORB:
    case ITEM_GRISEOUS_ORB:
    case ITEM_ADAMANT_CRYSTAL:
    case ITEM_LUSTROUS_GLOBE:
    case ITEM_GRISEOUS_CORE:
    case ITEM_RUSTED_SWORD:
    case ITEM_RUSTED_SHIELD:
    case ITEM_WELLSPRING_MASK:
    case ITEM_HEARTHFLAME_MASK:
    case ITEM_CORNERSTONE_MASK:
    case ITEM_SCROLL_OF_DARKNESS:
    case ITEM_SCROLL_OF_WATERS:
    case ITEM_METEORITE:
    case ITEM_GRACIDEA:
    case ITEM_REVEAL_GLASS:
    case ITEM_DNA_SPLICERS:
    case ITEM_ZYGARDE_CUBE:
    case ITEM_PRISON_BOTTLE:
    case ITEM_N_SOLARIZER:
    case ITEM_N_LUNARIZER:
    case ITEM_REINS_OF_UNITY:
    case ITEM_EON_TICKET:
    case ITEM_MYSTIC_TICKET:
    case ITEM_AURORA_TICKET:
    case ITEM_OLD_SEA_MAP:
    case ITEM_MEWTWONITE_X:
    case ITEM_MEWTWONITE_Y:
    case ITEM_LATIASITE:
    case ITEM_LATIOSITE:
    case ITEM_DIANCITE:
    case ITEM_ZYGARDITE:
    case ITEM_HEATRANITE:
    case ITEM_DARKRANITE:
    case ITEM_ZERAORITE:
    case ITEM_MAGEARNITE:
    case ITEM_MEWNIUM_Z:
    case ITEM_TAPUNIUM_Z:
    case ITEM_SOLGANIUM_Z:
    case ITEM_LUNALIUM_Z:
    case ITEM_MARSHADIUM_Z:
    case ITEM_ULTRANECROZIUM_Z:
        return TRUE;
    default:
        return FALSE;
    }
}
