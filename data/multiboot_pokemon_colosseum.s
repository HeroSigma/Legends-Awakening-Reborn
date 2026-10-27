#include "config/free_space.h"
	.section .rodata

gMultiBootProgram_PokemonColosseum_Start::
#if !LA_FREE_SPACE
	.incbin "data/mb_colosseum.gba"
#endif
gMultiBootProgram_PokemonColosseum_End::
