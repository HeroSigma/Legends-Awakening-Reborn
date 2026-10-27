Kanto_SeafoamIslands_1F_MapScripts::
	.byte 0

KantoAR_1_83_SeafoamIslands_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_84_SEAFOAMISLANDS_B1F, 21, 10
	goto KantoAR_InspectionFinish
