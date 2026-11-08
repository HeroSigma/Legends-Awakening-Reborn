Kanto_SaffronCity_CopycatsHouse_1F_MapScripts::
	.byte 0

KantoAR_14_0_SaffronCity_CopycatsHouse_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_14_1_SAFFRONCITY_COPYCATSHOUSE_2F, 6, 4
	goto KantoAR_InspectionFinish
