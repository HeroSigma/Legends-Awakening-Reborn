Kanto_TwoIsland_JoyfulGameCorner_MapScripts::
	.byte 0

KantoAR_33_0_TwoIsland_JoyfulGameCorner_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_33_1_TWOISLAND_HOUSE, 4, 3
	goto KantoAR_InspectionFinish
