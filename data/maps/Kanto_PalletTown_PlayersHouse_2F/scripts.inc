Kanto_PalletTown_PlayersHouse_2F_MapScripts::
	.byte 0

KantoAR_4_1_PalletTown_PlayersHouse_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_4_2_PALLETTOWN_RIVALSHOUSE, 4, 5
	goto KantoAR_InspectionFinish
