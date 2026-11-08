#include "global.h"
#include "pokemon.h"
#include "item.h"
#include "party_menu.h"
#include "item_menu.h"
#include "caps.h"
#include "data.h"
#include "constants/items.h"
#include "constants/item_effects.h"
u32 TrainingItem_MaxQuantity(struct Pokemon *mon, enum Item item)
{
    u32 bag = CountTotalItemQuantityInBag(item);
    if (!bag || GetMonData(mon, MON_DATA_IS_EGG))
        return 0;
    u32 type = GetItemEffectType(item);
    if (type == ITEM_EFFECT_RAISE_LEVEL)
    {
        u32 level = GetMonData(mon, MON_DATA_LEVEL), cap = GetCurrentLevelCap();
        if (level >= cap)
            return 1; // Existing Rare Candy evolution-only behavior is preserved.
        u32 param = GetItemHoldEffectParam(item);
        if (!param)
            return min(bag, cap - level);
        if (param > 5)
            return 1;
        u32 species = GetMonData(mon, MON_DATA_SPECIES);
        u32 remaining = gExperienceTables[gSpeciesInfo[species].growthRate][cap] - GetMonData(mon, MON_DATA_EXP);
        u32 exp = sExpCandyExperienceTable[param - 1];
        return min(bag, (remaining + exp - 1) / exp);
    }
    u32 ev;
    switch (type)
    {
    case ITEM_EFFECT_HP_EV: ev = MON_DATA_HP_EV; break;
    case ITEM_EFFECT_ATK_EV: ev = MON_DATA_ATK_EV; break;
    case ITEM_EFFECT_DEF_EV: ev = MON_DATA_DEF_EV; break;
    case ITEM_EFFECT_SPEED_EV: ev = MON_DATA_SPEED_EV; break;
    case ITEM_EFFECT_SPATK_EV: ev = MON_DATA_SPATK_EV; break;
    case ITEM_EFFECT_SPDEF_EV: ev = MON_DATA_SPDEF_EV; break;
    default: return 1;
    }
    const u8 *effect = GetItemEffect(item);
    s32 increase = (s8)effect[6];
    if (increase <= 0)
        return 1;
    if (GetItemEffectType(item) == ITEM_EFFECT_HP_EV && GetMonData(mon, MON_DATA_SPECIES) == SPECIES_SHEDINJA)
        return 0;
    u32 perStat = (effect[10] & ITEM10_IS_VITAMIN) ? EV_ITEM_RAISE_LIMIT : MAX_PER_STAT_EVS;
    u32 total = B_EV_ITEMS_CAP ? GetCurrentEVCap() : MAX_TOTAL_EVS;
    u32 current = GetMonData(mon, ev), used = GetMonEVCount(mon);
    if (current >= perStat || used >= total)
        return 0;
    return min(bag, (min(perStat-current, total-used) + increase-1) / increase);
}
u32 TrainingItem_Apply(struct Pokemon *mon, enum Item item, u32 slot, u32 count)
{
    u32 used = 0;
    while (used < count)
    {
        if (GetItemEffectType(item) == ITEM_EFFECT_RAISE_LEVEL
         && GetMonData(mon, MON_DATA_LEVEL) >= GetCurrentLevelCap())
            break;
        if (ExecuteTableBasedItemEffect(mon, item, slot, 0))
            break;
        used++;
    }
    return used;
}
