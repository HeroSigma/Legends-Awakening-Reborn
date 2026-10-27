Kanto_TradeCenter_MapScripts::
	.byte 0

KantoAR_0_1_TradeCenter_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_0_2_RECORDCORNER, 13, 5
	goto KantoAR_InspectionFinish
