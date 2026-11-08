Kanto_ThreeIsland_Port_MapScripts::
	.byte 0

KantoAR_3_49_ThreeIsland_Port_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_52_PROTOTYPE_SEVIIISLE_8, 49, 11
	goto KantoAR_InspectionFinish
