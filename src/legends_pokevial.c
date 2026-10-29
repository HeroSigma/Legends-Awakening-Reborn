#include "global.h"
#include "legends_pokevial.h"
#include "event_data.h"
#include "item.h"
#include "pokemon.h"
#include "string_util.h"
#include "constants/flags.h"
#include "constants/items.h"
#include "constants/vars.h"

u32 LegendsPokevialCharges(void)
{
    return min(VarGet(VAR_LA_POKEVIAL_CHARGES), 3);
}
void LegendsPokevialRefill(void)
{
    if (CheckBagHasItem(ITEM_POKEVIAL, 1))
        VarSet(VAR_LA_POKEVIAL_CHARGES, 3);
}
void LegendsPokevialGrant(void)
{
    if (CheckBagHasItem(ITEM_POKEVIAL, 1))
    {
        FlagSet(FLAG_LA_POKEVIAL_RECEIVED);
        LegendsPokevialRefill();
    }
}
// Results: 0 ready, 1 empty, 2 no injured usable party member, 3 not owned.
void LegendsPokevialPrepare(void)
{
    gSpecialVar_Result = 3;
    if (!CheckBagHasItem(ITEM_POKEVIAL, 1)) return;
    ConvertIntToDecimalStringN(gStringVar1, LegendsPokevialCharges(), STR_CONV_MODE_LEFT_ALIGN, 1);
    gSpecialVar_Result = 1;
    if (!LegendsPokevialCharges()) return;
    gSpecialVar_Result = 2;
    for (u32 i = 0; i < gPartiesCount[B_TRAINER_PLAYER]; i++)
    {
        struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][i];
        if (!GetMonData(mon, MON_DATA_SPECIES) || GetMonData(mon, MON_DATA_IS_EGG)) continue;
        if (GetMonData(mon, MON_DATA_HP) != GetMonData(mon, MON_DATA_MAX_HP)
            || GetMonData(mon, MON_DATA_STATUS)) { gSpecialVar_Result = 0; return; }
        for (u32 j = 0; j < MAX_MON_MOVES; j++)
        {
            u32 move = GetMonData(mon, MON_DATA_MOVE1 + j);
            if (move && GetMonData(mon, MON_DATA_PP1 + j)
                < CalculatePPWithBonus(move, GetMonData(mon, MON_DATA_PP_BONUSES), j))
            { gSpecialVar_Result = 0; return; }
        }
    }
}
void LegendsPokevialHeal(void)
{
    LegendsPokevialPrepare();
    if (gSpecialVar_Result) return;
    // Heal the party directly: HealPlayerParty would refill this item too.
    for (u32 i = 0; i < gPartiesCount[B_TRAINER_PLAYER]; i++)
        if (!GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_IS_EGG))
            HealPokemon(&gParties[B_TRAINER_PLAYER][i]);
    VarSet(VAR_LA_POKEVIAL_CHARGES, LegendsPokevialCharges() - 1);
    ConvertIntToDecimalStringN(gStringVar1, LegendsPokevialCharges(), STR_CONV_MODE_LEFT_ALIGN, 1);
}
