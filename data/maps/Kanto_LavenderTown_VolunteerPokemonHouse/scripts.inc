Kanto_LavenderTown_VolunteerPokemonHouse_MapScripts::
	.byte 0

KantoAR_8_2_LavenderTown_VolunteerPokemonHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_8_3_LAVENDERTOWN_HOUSE1, 4, 3
	goto KantoAR_InspectionFinish
