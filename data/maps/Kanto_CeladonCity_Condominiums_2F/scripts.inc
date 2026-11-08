Kanto_CeladonCity_Condominiums_2F_MapScripts::
	.byte 0

KantoAR_10_8_CeladonCity_Condominiums_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_9_CELADONCITY_CONDOMINIUMS_3F, 10, 10
	goto KantoAR_InspectionFinish
