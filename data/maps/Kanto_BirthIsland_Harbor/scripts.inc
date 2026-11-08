Kanto_BirthIsland_Harbor_MapScripts::
	.byte 0

KantoAR_2_58_BirthIsland_Harbor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_59_NAVELROCK_HARBOR, 8, 5
	goto KantoAR_InspectionFinish
