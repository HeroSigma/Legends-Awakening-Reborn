#include "config/free_space.h"
	.equiv LA_AUDIO_GC, LA_FREE_SPACE
	.section .rodata

	.include "asm/macros.inc"
	.include "constants/constants.inc"

	.include "asm/macros/m4a.inc"
	.include "asm/macros/music_voice.inc"
	.include "include/config/general.h"
	.include "include/config/pokemon.h"
	.include "sound/voice_groups.inc"
	.include "sound/keysplit_tables.inc"
	.include "sound/programmable_wave_data.inc"
	.section .rodata.audio.player_table, "a", %progbits
	.include "sound/music_player_table.inc"
	.section .rodata.audio.song_table, "a", %progbits
	.include "sound/song_table.inc"
	.include "sound/direct_sound_data.inc"

	.align 2
