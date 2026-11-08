Kanto_PalletTown_PlayersHouse_1F_MapScripts::
	.byte 0

KantoAR_4_0_PalletTown_PlayersHouse_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_4_1_PALLETTOWN_PLAYERSHOUSE_2F, 5, 3
	goto KantoAR_InspectionFinish
