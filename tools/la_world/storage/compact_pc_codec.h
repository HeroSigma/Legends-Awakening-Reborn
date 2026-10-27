#ifndef LA_COMPACT_PC_CODEC_H
#define LA_COMPACT_PC_CODEC_H
#include <stdint.h>
#define LA_PC_BOXES 60
#define LA_PC_SLOTS_PER_BOX 30
#define LA_PC_SLOTS (LA_PC_BOXES * LA_PC_SLOTS_PER_BOX)
#define LA_PC_RECORD_BYTES 31
#define LA_PC_EV_COMBINATIONS UINT64_C(23033206414848)
/* Collection profile v2. Preserve functional traits, including Beauty for
 * Feebas, Pokerus, Dynamax/Gigantamax traits, and personality evolution rules.
 * Names, full OT/met history and cosmetic personality patterns are regenerated.
 * This portable codec is not yet connected to a player save. */
struct LaPcTraits {
 uint16_t species, item, moves[4], evolution_tracker;
 uint32_t experience;
 uint8_t tera_type, pp_bonuses, evs[6], ivs[6], ability;
 uint8_t mint_nature, original_nature, female, shiny, friendship;
 uint8_t hyper_trained, egg, ball, foreign_ot, wurmple_branch;
 uint8_t shadow, fateful, champion_ribbon;
 uint8_t pokerus, beauty, personality_mod100_quotient;
 uint8_t dynamax_level, gigantamax_factor, foreign_language, markings;
};
uint16_t LaPcPeekSpecies(const uint8_t in[LA_PC_RECORD_BYTES]);
uint8_t LaPcPeekEgg(const uint8_t in[LA_PC_RECORD_BYTES]);
uint16_t LaPcPeekMove(const uint8_t in[LA_PC_RECORD_BYTES], unsigned slot);
uint16_t LaPcPeekItem(const uint8_t in[LA_PC_RECORD_BYTES]);
int LaPcEncode(const struct LaPcTraits *, uint8_t out[LA_PC_RECORD_BYTES]);
int LaPcDecode(const uint8_t in[LA_PC_RECORD_BYTES], struct LaPcTraits *);
int LaPcRankEvs(const uint8_t evs[6], uint64_t *rank);
int LaPcUnrankEvs(uint64_t rank, uint8_t evs[6]);
#endif
