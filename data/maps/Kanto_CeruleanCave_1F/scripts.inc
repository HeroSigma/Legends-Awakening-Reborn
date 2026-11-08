Kanto_CeruleanCave_1F_MapScripts::
	.byte 0

KantoAR_1_72_CeruleanCave_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_73_CERULEANCAVE_2F, 17, 11
	goto KantoAR_InspectionFinish
