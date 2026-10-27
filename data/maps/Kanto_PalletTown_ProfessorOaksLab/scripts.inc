Kanto_PalletTown_ProfessorOaksLab_MapScripts::
	.byte 0

KantoAR_4_3_PalletTown_ProfessorOaksLab_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_5_0_VIRIDIANCITY_HOUSE, 4, 3
	goto KantoAR_InspectionFinish
