Kanto_SeafoamIslands_B3F_MapScripts::
	.byte 0

KantoAR_1_86_SeafoamIslands_B3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_87_SEAFOAMISLANDS_B4F, 13, 12
	goto KantoAR_InspectionFinish
