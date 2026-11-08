Kanto_MtEmber_RubyPath_1F_MapScripts::
	.byte 0

KantoAR_1_103_MtEmber_RubyPath_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_104_MTEMBER_RUBYPATH_B1F, 3, 12
	goto KantoAR_InspectionFinish
