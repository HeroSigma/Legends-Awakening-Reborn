Kanto_VermilionCity_House3_MapScripts::
	.byte 0

KantoAR_9_7_VermilionCity_House3_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_0_CELADONCITY_DEPARTMENTSTORE_1F, 6, 6
	goto KantoAR_InspectionFinish
