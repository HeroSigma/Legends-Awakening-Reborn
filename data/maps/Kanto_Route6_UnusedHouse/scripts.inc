Kanto_Route6_UnusedHouse_MapScripts::
	.byte 0

KantoAR_18_1_Route6_UnusedHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_19_0_ROUTE7_EASTENTRANCE, 6, 5
	goto KantoAR_InspectionFinish
