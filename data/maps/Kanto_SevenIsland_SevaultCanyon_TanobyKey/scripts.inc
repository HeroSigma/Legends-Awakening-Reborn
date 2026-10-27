Kanto_SevenIsland_SevaultCanyon_TanobyKey_MapScripts::
	.byte 0

KantoAR_2_35_SevenIsland_SevaultCanyon_TanobyKey_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_36_NAVELROCK_1F, 8, 13
	goto KantoAR_InspectionFinish
