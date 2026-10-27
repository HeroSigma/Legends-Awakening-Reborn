Kanto_ThreeIsland_Harbor_MapScripts::
	.byte 0

KantoAR_38_0_ThreeIsland_Harbor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_39_0_FIVEISLAND_RESORTGORGEOUS_HOUSE, 4, 3
	goto KantoAR_InspectionFinish
