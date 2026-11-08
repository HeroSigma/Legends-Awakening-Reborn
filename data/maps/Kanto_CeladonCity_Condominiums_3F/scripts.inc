Kanto_CeladonCity_Condominiums_3F_MapScripts::
	.byte 0

KantoAR_10_9_CeladonCity_Condominiums_3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_10_CELADONCITY_CONDOMINIUMS_ROOF, 9, 11
	goto KantoAR_InspectionFinish
