Kanto_SeafoamIslands_B1F_MapScripts::
	.byte 0

KantoAR_1_84_SeafoamIslands_B1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_85_SEAFOAMISLANDS_B2F, 18, 16
	goto KantoAR_InspectionFinish
