Kanto_NavelRock_Fork_MapScripts::
	.byte 0

KantoAR_2_55_NavelRock_Fork_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_56_BIRTHISLAND_EXTERIOR, 15, 20
	goto KantoAR_InspectionFinish
