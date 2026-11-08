Kanto_FourIsland_Harbor_MapScripts::
	.byte 0

KantoAR_35_5_FourIsland_Harbor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_35_6_FOURISLAND_HOUSE2, 4, 3
	goto KantoAR_InspectionFinish
