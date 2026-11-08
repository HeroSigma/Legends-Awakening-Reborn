Kanto_MtEmber_RubyPath_B3F_MapScripts::
	.byte 0

KantoAR_1_106_MtEmber_RubyPath_B3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_107_MTEMBER_RUBYPATH_B1F_STAIRS, 3, 3
	goto KantoAR_InspectionFinish
