/* Isolated ARM test only; never included in a playable build. */
#include "reborn_pc_bank.h"
#include "reborn_pc_adapter.h"
#include <string.h>
#include "constants/characters.h"
static int Compare(const void *a, const void *b, u32 size)
{
    const u8 *x=a, *y=b;
    while (size--) if (*x++ != *y++) return 1;
    return 0;
}
#define CHECK(v) do { report[0]++; if (!(v)) { report[1] = __LINE__; return FALSE; } } while (0)
bool32 LaPcBankNativeTest(struct LaPcBankContext *ctx, struct LaPcBank *bank, struct BoxPokemon *source, u32 *report)
{
    struct BoxPokemon mon, result, original;
    u8 first[31], second[31], backup[30][31];
    u32 box, slot, value;
    report[0] = report[1] = 0;
    LaPcBankBind(ctx, bank);
    LaPcBankClear(ctx, LA_PC_COLLECTION_MODE);
    CHECK(LaPcBankBoxCount(ctx) == 60);
    CHECK(LaPcBankGet(ctx, 60, 0) == NULL);
    CHECK(LaPcBankGet(ctx, 0, 30) == NULL);
    CHECK(LaPcBankGet(NULL, 0, 0) == NULL);
    for (box = 0; box < 60; box++)
        for (slot = 0; slot < 30; slot++)
        {
            u32 index = box * 30 + slot;
            report[2] = index;
            mon = *source;
            value = index % 256;
            SetBoxMonData(&mon, MON_DATA_FRIENDSHIP, &value);
            value = index % 1024;
            SetBoxMonData(&mon, MON_DATA_EVOLUTION_TRACKER, &value);
            CHECK(LaPcBankSet(ctx, box, slot, &mon));
        }
    CHECK(LaPcBankGet(ctx, 0, 0) != NULL);
    CHECK(LaPcBankRead(ctx, 59, 29, &result));
    CHECK(ctx->cachedBox == 0);
    CHECK(LaPcBankSet(ctx, 59, 29, &result));
    CHECK(ctx->cachedBox == 0);
    CHECK(LaPcBankFlush(ctx));
    LaPcBankBind(ctx, bank); /* reload with an empty cache */
    for (box = 0; box < 60; box++)
        for (slot = 0; slot < 30; slot++)
        {
            u32 index = box * 30 + slot;
            CHECK(LaPcBankRead(ctx, box, slot, &result));
            CHECK(GetBoxMonData(&result, MON_DATA_FRIENDSHIP) == index % 256);
            CHECK(GetBoxMonData(&result, MON_DATA_EVOLUTION_TRACKER) == index % 1024);
            CHECK(LaPcEncodeBoxMon(&result, second));
            CHECK(Compare(second, bank->records.compact[box][slot], 31) == 0);
        }
    mon = *source;
    value = MOVES_COUNT;
    SetBoxMonData(&mon, MON_DATA_MOVE1, &value);
    memcpy(first, bank->records.compact[7][8], 31);
    CHECK(!LaPcBankSet(ctx, 7, 8, &mon));
    CHECK(Compare(first, bank->records.compact[7][8], 31) == 0);
    /* Direct pointer mutation must survive switching away and back. */
    value = 237;
    SetBoxMonData(LaPcBankGet(ctx, 0, 0), MON_DATA_FRIENDSHIP, &value);
    CHECK(LaPcBankGet(ctx, 59, 0) != NULL);
    CHECK(GetBoxMonData(LaPcBankGet(ctx, 0, 0), MON_DATA_FRIENDSHIP) == value);
    /* A source in the cache must be copied before destination loads. */
    CHECK(LaPcBankSet(ctx, 58, 29, LaPcBankGet(ctx, 0, 0)));
    CHECK(GetBoxMonData(LaPcBankGet(ctx, 58, 29), MON_DATA_FRIENDSHIP) == value);
    CHECK(LaPcBankFlush(ctx));
    memcpy(backup, bank->records.compact[58], sizeof(backup));
    original = *LaPcBankGet(ctx, 58, 1);
    value = 1;
    SetBoxMonData(LaPcBankGet(ctx, 58, 1), MON_DATA_SANITY_IS_BAD_EGG, &value);
    CHECK(!LaPcBankFlush(ctx));
    CHECK(Compare(backup, bank->records.compact[58], sizeof(backup)) == 0);
    CHECK(LaPcBankGet(ctx, 57, 0) == NULL);
    CHECK(ctx->cachedBox == 58);
    ctx->cache[1] = original;
    CHECK(LaPcBankFlush(ctx));
    CHECK(LaPcBankGet(ctx, 0, 0) != NULL);
    memcpy(first, bank->records.compact[2][0], 31);
    bank->records.compact[2][0][0] = 255;
    bank->records.compact[2][0][1] |= 7; /* invalid semantic species */
    CHECK(LaPcBankGet(ctx, 2, 0) == NULL);
    CHECK(ctx->cachedBox == 0);
    memcpy(bank->records.compact[2][0], first, 31);
    CHECK(LaPcBankGet(ctx, 2, 0) != NULL);
    value = 129;
    SetBoxMonData(LaPcBankGet(ctx, 3, 4), MON_DATA_FRIENDSHIP, &value);
    CHECK(LaPcBankMove(ctx, (struct LaPcBank *)((u8 *)bank + 4)));
    bank = (struct LaPcBank *)((u8 *)bank + 4);
    CHECK(!ctx->cacheValid);
    CHECK(ctx->bank == bank);
    CHECK(LaPcBankRead(ctx, 3, 4, &result));
    CHECK(GetBoxMonData(&result, MON_DATA_FRIENDSHIP) == value);
    CHECK(LaPcBankMove(ctx, (struct LaPcBank *)((u8 *)bank - 4)));
    bank = (struct LaPcBank *)((u8 *)bank - 4);
    CHECK(LaPcBankRead(ctx, 3, 4, &result));
    CHECK(GetBoxMonData(&result, MON_DATA_FRIENDSHIP) == value);
    /* Normal mode stores the complete native specimen without conversion. */
    LaPcBankClear(ctx, LA_PC_NORMAL_MODE);
    CHECK(LaPcBankBoxCount(ctx) == 14);
    CHECK(LaPcBankGet(ctx, 14, 0) == NULL);
    CHECK(LaPcBankSet(ctx, 13, 29, source));
    CHECK(LaPcBankRead(ctx, 13, 29, &result));
    CHECK(Compare(source, &result, sizeof(result)) == 0);
    CHECK(LaPcBankFlush(ctx));
    CHECK(!LaPcBankChangeMode(ctx, LA_PC_COLLECTION_MODE, FALSE));
    CHECK(LaPcBankBoxCount(ctx) == 14);
    CHECK(LaPcBankRead(ctx, 13, 29, &result));
    CHECK(Compare(source, &result, sizeof(result)) == 0);
    CHECK(LaPcBankChangeMode(ctx, LA_PC_NORMAL_MODE, TRUE));
    CHECK(LaPcBankRead(ctx, 13, 29, &result));
    CHECK(Compare(source, &result, sizeof(result)) == 0);
    bank->fusions[0].box = *source;
    CHECK(LaPcBankChangeMode(ctx, LA_PC_COLLECTION_MODE, TRUE));
    CHECK(LaPcBankBoxCount(ctx) == 60);
    CHECK(Compare(source, &bank->fusions[0].box, sizeof(result)) == 0);
    for (box = 0; box < 60; box++)
        for (slot = 0; slot < 30; slot++)
        {
            CHECK(LaPcBankRead(ctx, box, slot, &result));
            CHECK(GetBoxMonData(&result, MON_DATA_SPECIES) == SPECIES_NONE);
        }
    bank->currentBox = 59;
    CHECK(LaPcBankChangeMode(ctx, LA_PC_NORMAL_MODE, TRUE));
    CHECK(bank->currentBox == 0);
    CHECK(Compare(source, &bank->fusions[0].box, sizeof(result)) == 0);
    CHECK(bank->names[59][4] != EOS);
    CHECK(bank->names[59][6] == EOS);
    return TRUE;
}
