Kanto_FiveIsland_Harbor_MapScripts::
	.byte 0

KantoAR_36_2_FiveIsland_Harbor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_36_3_FIVEISLAND_HOUSE1, 4, 3
	goto KantoAR_InspectionFinish
