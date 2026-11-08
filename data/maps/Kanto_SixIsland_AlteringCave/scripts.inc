Kanto_SixIsland_AlteringCave_MapScripts::
	.byte 0

KantoAR_1_122_SixIsland_AlteringCave_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_0_NAVELROCK_EXTERIOR, 10, 10
	goto KantoAR_InspectionFinish
