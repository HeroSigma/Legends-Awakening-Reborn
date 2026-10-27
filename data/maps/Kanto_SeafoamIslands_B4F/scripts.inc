Kanto_SeafoamIslands_B4F_MapScripts::
	.byte 0

KantoAR_1_87_SeafoamIslands_B4F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_88_POKEMONTOWER_1F, 12, 10
	goto KantoAR_InspectionFinish
