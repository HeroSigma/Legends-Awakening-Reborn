Kanto_SaffronCity_CopycatsHouse_2F_MapScripts::
	.byte 0

KantoAR_14_1_SaffronCity_CopycatsHouse_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_14_2_SAFFRONCITY_DOJO, 6, 8
	goto KantoAR_InspectionFinish
