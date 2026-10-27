#ifndef GUARD_LA_REBORN_PC_BANK_H
#define GUARD_LA_REBORN_PC_BANK_H
#include "global.h"
#include "pokemon.h"
#include "compact_pc_codec.h"
#define LA_PC_NORMAL_BOXES 14
#define LA_PC_NORMAL_MODE 0
#define LA_PC_COLLECTION_MODE 1
struct __attribute__((may_alias)) LaPcBank
{
    u8 currentBox;
    u8 mode;
    u16 version;
    union {
        struct BoxPokemon native[LA_PC_NORMAL_BOXES][30];
        u8 compact[60][30][LA_PC_RECORD_BYTES];
    } records;
    u8 names[60][9];
    u8 wallpapers[60];
    struct Pokemon fusions[4];
};
struct LaPcBankContext
{
    struct LaPcBank *bank;
    struct BoxPokemon cache[30];
    u8 cachedBox;
    bool8 cacheValid;
};
/* Bind only for initialization/validated reload; use Move for live relocation. */
void LaPcBankBind(struct LaPcBankContext *, struct LaPcBank *);
void LaPcBankClear(struct LaPcBankContext *, u32 mode);
/* Only the confirmed transition clears boxed records; party/fusions stay intact. */
bool32 LaPcBankChangeMode(struct LaPcBankContext *, u32 mode, bool32 confirmed);
u32 LaPcBankBoxCount(const struct LaPcBankContext *);
bool32 LaPcBankMove(struct LaPcBankContext *, struct LaPcBank *destination);
bool32 LaPcBankFlush(struct LaPcBankContext *);
/* Pointer remains valid only until the next access to a different box.
 * Direct mutations are captured by Flush. Failure never clears a specimen. */
struct BoxPokemon *LaPcBankGet(struct LaPcBankContext *, u32 box, u32 slot);
bool32 LaPcBankRead(struct LaPcBankContext *, u32 box, u32 slot, struct BoxPokemon *);
bool32 LaPcBankSet(struct LaPcBankContext *, u32 box, u32 slot, const struct BoxPokemon *);
#endif
