Kanto_SevenIsland_SevaultCanyon_House_MapScripts::
	.byte 0

KantoAR_42_0_SevenIsland_SevaultCanyon_House_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_0_PALLETTOWN, 12, 9
	goto KantoAR_InspectionFinish
