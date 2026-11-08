Kanto_SeafoamIslands_B2F_MapScripts::
	.byte 0

KantoAR_1_85_SeafoamIslands_B2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_86_SEAFOAMISLANDS_B3F, 20, 18
	goto KantoAR_InspectionFinish
