#include "reborn_pc_bank.h"
#include "reborn_pc_adapter.h"
#include "constants/characters.h"
#include <string.h>
STATIC_ASSERT(sizeof(struct LaPcBank) == 56804, CollectionBankSize);

void LaPcBankBind(struct LaPcBankContext *ctx, struct LaPcBank *bank)
{
    ctx->bank = bank;
    ctx->cacheValid = FALSE;
}

u32 LaPcBankBoxCount(const struct LaPcBankContext *ctx)
{
    if (ctx == NULL || ctx->bank == NULL || ctx->bank->version != 2)
        return 0;
    if (ctx->bank->mode == LA_PC_NORMAL_MODE)
        return LA_PC_NORMAL_BOXES;
    if (ctx->bank->mode == LA_PC_COLLECTION_MODE)
        return 60;
    return 0;
}

void LaPcBankClear(struct LaPcBankContext *ctx, u32 mode)
{
    u32 i, n;
    if (ctx == NULL || ctx->bank == NULL || mode > LA_PC_COLLECTION_MODE)
        return;
    memset(ctx->bank, 0, sizeof(*ctx->bank));
    ctx->bank->mode = mode;
    ctx->bank->version = 2;
    ctx->cacheValid = FALSE;
    for (i = 0; i < 60; i++)
    {
        u8 *name = ctx->bank->names[i];
        name[0] = CHAR_B; name[1] = CHAR_O; name[2] = CHAR_X;
        name[3] = CHAR_SPACE;
        n = 4;
        if (i + 1 >= 10)
            name[n++] = CHAR_0 + (i + 1) / 10;
        name[n++] = CHAR_0 + (i + 1) % 10;
        name[n] = EOS;
        ctx->bank->wallpapers[i] = i % 16;
    }
}

bool32 LaPcBankChangeMode(struct LaPcBankContext *ctx, u32 mode, bool32 confirmed)
{
    if (!LaPcBankBoxCount(ctx) || mode > LA_PC_COLLECTION_MODE)
        return FALSE;
    if (ctx->bank->mode == mode)
        return TRUE;
    if (confirmed != TRUE)
        return FALSE;
    /* This is intentionally destructive and must follow the Options warning.
     * Names, wallpapers, fusion partners and unrelated party/story data survive. */
    memset(&ctx->bank->records, 0, sizeof(ctx->bank->records));
    ctx->bank->mode = mode;
    ctx->cacheValid = FALSE;
    if (ctx->bank->currentBox >= LaPcBankBoxCount(ctx))
        ctx->bank->currentBox = 0;
    return TRUE;
}

bool32 LaPcBankFlush(struct LaPcBankContext *ctx)
{
    u8 pending[30][LA_PC_RECORD_BYTES];
    u32 slot;
    if (ctx == NULL || ctx->bank == NULL || !LaPcBankBoxCount(ctx))
        return FALSE;
    if (!ctx->cacheValid)
        return TRUE;
    if (ctx->bank->mode != LA_PC_COLLECTION_MODE || ctx->cachedBox >= 60)
        return FALSE;
    /* Commit the whole box only after all records encode successfully. */
    for (slot = 0; slot < 30; slot++)
        if (!LaPcEncodeBoxMon(&ctx->cache[slot], pending[slot]))
            return FALSE;
    memcpy(ctx->bank->records.compact[ctx->cachedBox], pending, sizeof(pending));
    return TRUE;
}

bool32 LaPcBankMove(struct LaPcBankContext *ctx, struct LaPcBank *destination)
{
    u32 i;
    u8 *src, *dst;
    if (destination == NULL || !LaPcBankFlush(ctx))
        return FALSE;
    src = (u8 *)ctx->bank;
    dst = (u8 *)destination;
    /* ASLR relocation may overlap. Flush before moving, then invalidate pointers. */
    if ((u32)dst > (u32)src)
    {
        for (i = sizeof(*destination); i != 0; i--)
            dst[i - 1] = src[i - 1];
    }
    else if (src != dst)
    {
        for (i = 0; i < sizeof(*destination); i++)
            dst[i] = src[i];
    }
    LaPcBankBind(ctx, destination);
    return TRUE;
}

static bool32 LoadBox(struct LaPcBankContext *ctx, u32 box)
{
    struct BoxPokemon scratch;
    u32 slot;
    if (ctx->cacheValid && ctx->cachedBox == box)
        return TRUE;
    if (!LaPcBankFlush(ctx))
        return FALSE;
    /* Validate first so failed decoding never replaces the current cache. */
    for (slot = 0; slot < 30; slot++)
        if (!LaPcDecodeBoxMon(ctx->bank->records.compact[box][slot], &scratch))
            return FALSE;
    for (slot = 0; slot < 30; slot++)
        if (!LaPcDecodeBoxMon(ctx->bank->records.compact[box][slot], &ctx->cache[slot]))
            return FALSE;
    ctx->cacheValid = TRUE;
    ctx->cachedBox = box;
    return TRUE;
}

struct BoxPokemon *LaPcBankGet(struct LaPcBankContext *ctx, u32 box, u32 slot)
{
    if (box >= LaPcBankBoxCount(ctx) || slot >= 30)
        return NULL;
    if (ctx->bank->mode == LA_PC_NORMAL_MODE)
        return &ctx->bank->records.native[box][slot];
    if (!LoadBox(ctx, box))
        return NULL;
    return &ctx->cache[slot];
}

bool32 LaPcBankRead(struct LaPcBankContext *ctx, u32 box, u32 slot, struct BoxPokemon *out)
{
    if (out == NULL || box >= LaPcBankBoxCount(ctx) || slot >= 30)
        return FALSE;
    if (ctx->bank->mode == LA_PC_NORMAL_MODE)
    {
        *out = ctx->bank->records.native[box][slot];
        return TRUE;
    }
    if (ctx->cacheValid && ctx->cachedBox == box)
    {
        *out = ctx->cache[slot];
        return TRUE;
    }
    /* Inventory scans must not invalidate a live summary-screen pointer. */
    return LaPcDecodeBoxMon(ctx->bank->records.compact[box][slot], out);
}

bool32 LaPcBankSet(struct LaPcBankContext *ctx, u32 box, u32 slot, const struct BoxPokemon *source)
{
    struct BoxPokemon copy;
    u8 validation[LA_PC_RECORD_BYTES];
    if (source == NULL || box >= LaPcBankBoxCount(ctx) || slot >= 30)
        return FALSE;
    copy = *source;
    if (ctx->bank->mode == LA_PC_NORMAL_MODE)
    {
        ctx->bank->records.native[box][slot] = copy;
        return TRUE;
    }
    if (!LaPcEncodeBoxMon(&copy, validation))
        return FALSE;
    if (ctx->cacheValid && ctx->cachedBox == box)
    {
        if (!LaPcDecodeBoxMon(validation, &copy))
            return FALSE;
        ctx->cache[slot] = copy;
    }
    else
    {
        /* An off-screen write must not disturb a live cached-box pointer. */
        memcpy(ctx->bank->records.compact[box][slot], validation, sizeof(validation));
    }
    return TRUE;
}
