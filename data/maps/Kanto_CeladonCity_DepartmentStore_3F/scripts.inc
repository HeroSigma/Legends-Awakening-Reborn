Kanto_CeladonCity_DepartmentStore_3F_MapScripts::
	.byte 0

KantoAR_10_2_CeladonCity_DepartmentStore_3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_3_CELADONCITY_DEPARTMENTSTORE_4F, 6, 5
	goto KantoAR_InspectionFinish
