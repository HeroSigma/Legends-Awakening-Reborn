Kanto_CeladonCity_DepartmentStore_2F_MapScripts::
	.byte 0

KantoAR_10_1_CeladonCity_DepartmentStore_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_2_CELADONCITY_DEPARTMENTSTORE_3F, 6, 7
	goto KantoAR_InspectionFinish
