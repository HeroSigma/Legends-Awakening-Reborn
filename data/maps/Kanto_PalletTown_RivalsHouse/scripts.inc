Kanto_PalletTown_RivalsHouse_MapScripts::
	.byte 0

KantoAR_4_2_PalletTown_RivalsHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_4_3_PALLETTOWN_PROFESSOROAKSLAB, 6, 7
	goto KantoAR_InspectionFinish
