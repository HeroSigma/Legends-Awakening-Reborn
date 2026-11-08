Kanto_SevenIsland_Harbor_MapScripts::
	.byte 0

KantoAR_31_6_SevenIsland_Harbor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_32_0_ONEISLAND_POKEMONCENTER_1F, 9, 5
	goto KantoAR_InspectionFinish
