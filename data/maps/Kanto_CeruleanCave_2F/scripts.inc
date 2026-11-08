Kanto_CeruleanCave_2F_MapScripts::
	.byte 0

KantoAR_1_73_CeruleanCave_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_74_CERULEANCAVE_B1F, 20, 13
	goto KantoAR_InspectionFinish
