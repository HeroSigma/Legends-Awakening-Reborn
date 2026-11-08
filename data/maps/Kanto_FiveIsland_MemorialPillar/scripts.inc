Kanto_FiveIsland_MemorialPillar_MapScripts::
	.byte 0

KantoAR_3_57_FiveIsland_MemorialPillar_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_58_SIXISLAND_OUTCASTISLAND, 12, 28
	goto KantoAR_InspectionFinish
