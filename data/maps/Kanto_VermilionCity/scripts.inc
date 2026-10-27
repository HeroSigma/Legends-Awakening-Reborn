Kanto_VermilionCity_MapScripts::
	.byte 0

KantoAR_3_5_VermilionCity_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_6_CELADONCITY, 30, 15
	goto KantoAR_InspectionFinish
