Kanto_MtEmber_RubyPath_B1F_MapScripts::
	.byte 0

KantoAR_1_104_MtEmber_RubyPath_B1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_105_MTEMBER_RUBYPATH_B2F, 8, 4
	goto KantoAR_InspectionFinish
