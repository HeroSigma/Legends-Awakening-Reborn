Kanto_OneIsland_Harbor_MapScripts::
	.byte 0

KantoAR_32_4_OneIsland_Harbor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_33_0_TWOISLAND_JOYFULGAMECORNER, 6, 5
	goto KantoAR_InspectionFinish
