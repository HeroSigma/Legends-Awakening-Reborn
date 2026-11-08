Kanto_FiveIsland_ResortGorgeous_House_MapScripts::
	.byte 0

KantoAR_39_0_FiveIsland_ResortGorgeous_House_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_40_0_TWOISLAND_CAPEBRINK_HOUSE, 4, 3
	goto KantoAR_InspectionFinish
