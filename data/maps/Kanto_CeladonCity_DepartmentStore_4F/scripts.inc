Kanto_CeladonCity_DepartmentStore_4F_MapScripts::
	.byte 0

KantoAR_10_3_CeladonCity_DepartmentStore_4F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_4_CELADONCITY_DEPARTMENTSTORE_5F, 6, 7
	goto KantoAR_InspectionFinish
