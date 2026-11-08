Kanto_CeladonCity_Condominiums_1F_MapScripts::
	.byte 0

KantoAR_10_7_CeladonCity_Condominiums_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_8_CELADONCITY_CONDOMINIUMS_2F, 10, 10
	goto KantoAR_InspectionFinish
