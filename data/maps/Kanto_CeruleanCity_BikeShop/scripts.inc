Kanto_CeruleanCity_BikeShop_MapScripts::
	.byte 0

KantoAR_7_6_CeruleanCity_BikeShop_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_7_7_CERULEANCITY_MART, 5, 4
	goto KantoAR_InspectionFinish
