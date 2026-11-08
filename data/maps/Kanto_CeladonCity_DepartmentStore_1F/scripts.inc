Kanto_CeladonCity_DepartmentStore_1F_MapScripts::
	.byte 0

KantoAR_10_0_CeladonCity_DepartmentStore_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_1_CELADONCITY_DEPARTMENTSTORE_2F, 6, 7
	goto KantoAR_InspectionFinish
