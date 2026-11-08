Kanto_FourIsland_LoreleisHouse_MapScripts::
	.byte 0

KantoAR_35_4_FourIsland_LoreleisHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_35_5_FOURISLAND_HARBOR, 8, 5
	goto KantoAR_InspectionFinish
