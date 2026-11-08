Kanto_SevenIsland_SevaultCanyon_MapScripts::
	.byte 0

KantoAR_3_64_SevenIsland_SevaultCanyon_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_65_SEVENISLAND_TANOBYRUINS, 85, 10
	goto KantoAR_InspectionFinish
