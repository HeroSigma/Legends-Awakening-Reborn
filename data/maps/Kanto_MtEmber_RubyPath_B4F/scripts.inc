Kanto_MtEmber_RubyPath_B4F_MapScripts::
	.byte 0

KantoAR_1_96_MtEmber_RubyPath_B4F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_97_MTEMBER_EXTERIOR, 28, 28
	goto KantoAR_InspectionFinish
