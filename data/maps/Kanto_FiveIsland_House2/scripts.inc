Kanto_FiveIsland_House2_MapScripts::
	.byte 0

KantoAR_36_4_FiveIsland_House2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_37_0_SIXISLAND_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
