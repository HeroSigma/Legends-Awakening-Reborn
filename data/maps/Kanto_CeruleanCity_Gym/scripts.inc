Kanto_CeruleanCity_Gym_MapScripts::
	.byte 0

KantoAR_7_5_CeruleanCity_Gym_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_7_6_CERULEANCITY_BIKESHOP, 6, 5
	goto KantoAR_InspectionFinish
