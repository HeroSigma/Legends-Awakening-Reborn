Kanto_FiveIsland_LostCave_Room14_MapScripts::
	.byte 0

KantoAR_2_26_FiveIsland_LostCave_Room14_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_27_SEVENISLAND_TANOBYRUINS_MONEANCHAMBER, 11, 8
	goto KantoAR_InspectionFinish
