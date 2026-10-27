Kanto_PalletTown_MapScripts::
	.byte 0

KantoAR_3_0_PalletTown_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_0_0_BATTLECOLOSSEUM_2P, 7, 4
	goto KantoAR_InspectionFinish

KantoAR_TravelHub::
	lock
	faceplayer
	multichoice 4, 0, MULTI_UNUSED_21, FALSE
	goto_if_eq VAR_RESULT, 0, KantoAR_HubStay
	goto_if_eq VAR_RESULT, 1, KantoAR_HubSevii
	goto_if_eq VAR_RESULT, 2, KantoAR_HubTour
	goto_if_eq VAR_RESULT, 3, KantoAR_HubHome
KantoAR_HubStay::
	closemessage
	release
	end
KantoAR_HubSevii::
	closemessage
	warp MAP_KANTOAR_3_12_ONEISLAND, 13, 10
	waitstate
	release
	end
KantoAR_HubTour::
	closemessage
	setdynamicwarp MAP_KANTOAR_3_0_PALLETTOWN, 12, 9
	warp MAP_KANTOAR_0_0_BATTLECOLOSSEUM_2P, 7, 4
	waitstate
	release
	end
KantoAR_HubHome::
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end

KantoAR_InspectionText:
	.string "Visit the next Kanto map?\p"
	.string "YES: next. NO: Littleroot.$"

KantoAR_InspectionPrompt::
	lock
	faceplayer
	msgbox KantoAR_InspectionText, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoAR_InspectionHome
	closemessage
	setdynamicwarp MAP_KANTOAR_3_0_PALLETTOWN, 12, 9
	return
KantoAR_InspectionHome::
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
KantoAR_InspectionFinish::
	waitstate
	release
	end
