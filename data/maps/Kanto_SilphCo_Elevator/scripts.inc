Kanto_SilphCo_Elevator_MapScripts::
	.byte 0

KantoAR_1_58_SilphCo_Elevator_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_59_POKEMONMANSION_1F, 19, 15
	goto KantoAR_InspectionFinish
