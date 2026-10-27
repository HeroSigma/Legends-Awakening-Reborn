#ifndef GUARD_LA_REBORN_PC_ADAPTER_H
#define GUARD_LA_REBORN_PC_ADAPTER_H
#include "compact_pc_codec.h"
struct BoxPokemon;
/* Staged adapter: callers must check failure before modifying storage. */
int LaPcEncodeBoxMon(struct BoxPokemon *, unsigned char out[LA_PC_RECORD_BYTES]);
int LaPcDecodeBoxMon(const unsigned char in[LA_PC_RECORD_BYTES], struct BoxPokemon *);
#endif
