Kanto_CeladonCity_DepartmentStore_5F_MapScripts::
	.byte 0

KantoAR_10_4_CeladonCity_DepartmentStore_5F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_5_CELADONCITY_DEPARTMENTSTORE_ROOF, 9, 7
	goto KantoAR_InspectionFinish
