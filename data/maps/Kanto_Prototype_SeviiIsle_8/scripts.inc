Kanto_Prototype_SeviiIsle_8_MapScripts::
	.byte 0

KantoAR_3_52_Prototype_SeviiIsle_8_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_54_FIVEISLAND_RESORTGORGEOUS, 35, 10
	goto KantoAR_InspectionFinish
