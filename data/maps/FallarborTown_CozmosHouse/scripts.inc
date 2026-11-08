FallarborTown_CozmosHouse_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, LegendsAshes_CozmoTransition
	map_script MAP_SCRIPT_ON_FRAME_TABLE, LegendsAshes_CozmoFrame
	.byte 0

FallarborTown_CozmosHouse_EventScript_ProfCozmo::
	setspeaker SP_NAME_COZMO
	lock
	faceplayer
	goto_if_set FLAG_RECEIVED_TM_RETURN, FallarborTown_CozmosHouse_EventScript_GaveMeteorite
	checkitem ITEM_METEORITE
	goto_if_eq VAR_RESULT, TRUE, FallarborTown_CozmosHouse_EventScript_PlayerHasMeteorite
	msgbox FallarborTown_CozmosHouse_Text_MeteoriteWillNeverBeMineNow, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	release
	end

FallarborTown_CozmosHouse_EventScript_PlayerHasMeteorite::
	call_if_unset FLAG_TEMP_2, FallarborTown_CozmosHouse_EventScript_NoticeMeteorite
	call_if_set FLAG_TEMP_2, FallarborTown_CozmosHouse_EventScript_AskForMeteorite
	goto_if_eq VAR_RESULT, NO, FallarborTown_CozmosHouse_EventScript_DeclineGiveMeteorite
	msgbox FallarborTown_CozmosHouse_Text_PleaseUseThisTM, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	giveitem ITEM_TM_RETURN
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_ShowBagIsFull
	setvar VAR_0x8004, ITEM_METEORITE
	call Common_EventScript_PlayerHandedOverTheItem
	setflag FLAG_RECEIVED_TM_RETURN
	setspeaker SP_NAME_COZMO
	msgbox FallarborTown_CozmosHouse_Text_ReallyGoingToHelpMyResearch, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	release
	end

FallarborTown_CozmosHouse_EventScript_NoticeMeteorite::
	setspeaker SP_NAME_PLAYER
	msgbox BlueChimney_Text_PlayerReturnsMeteorite, MSGBOX_DEFAULT
	setspeaker SP_NAME_COZMO
	msgbox FallarborTown_CozmosHouse_Text_MeteoriteWillNeverBeMineNow, MSGBOX_DEFAULT
	msgbox FallarborTown_CozmosHouse_Text_IsThatMeteoriteMayIHaveIt, MSGBOX_YESNO
	return

FallarborTown_CozmosHouse_EventScript_AskForMeteorite::
	msgbox FallarborTown_CozmosHouse_Text_MayIHaveMeteorite, MSGBOX_YESNO
	return

FallarborTown_CozmosHouse_EventScript_DeclineGiveMeteorite::
	setflag FLAG_TEMP_2
	msgbox FallarborTown_CozmosHouse_Text_CrushedWithDisappointment, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	release
	end

FallarborTown_CozmosHouse_EventScript_GaveMeteorite::
	setspeaker SP_NAME_COZMO
	msgbox FallarborTown_CozmosHouse_Text_ReallyGoingToHelpMyResearch, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	release
	end

FallarborTown_CozmosHouse_EventScript_CozmosWife::
	lock
	faceplayer
	goto_if_set FLAG_RECEIVED_TM_RETURN, FallarborTown_CozmosHouse_EventScript_CozmoIsHappy
	goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, FallarborTown_CozmosHouse_EventScript_CozmoIsSad
	msgbox FallarborTown_CozmosHouse_Text_CozmoWentToMeteorFalls, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	release
	end

FallarborTown_CozmosHouse_EventScript_CozmoIsSad::
	msgbox FallarborTown_CozmosHouse_Text_FeelSorryForCozmo, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	release
	end

FallarborTown_CozmosHouse_EventScript_CozmoIsHappy::
	msgbox FallarborTown_CozmosHouse_Text_CozmoIsSoHappy, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	release
	end

FallarborTown_CozmosHouse_Text_MeteoriteWillNeverBeMineNow:
	.string "They took the sample and the notes.\nI should have secured them sooner.\pThe relay readings may tell us what\nthey opened. We must preserve them.$"

FallarborTown_CozmosHouse_Text_IsThatMeteoriteMayIHaveIt:
	.string "You recovered the meteorite!\nMay I examine it here?\pI can compare it with our earlier\nreadings and send Birch the results.\pI'll give you a TM for your help.$"

FallarborTown_CozmosHouse_Text_PleaseUseThisTM:
	.string "Thank you. Take this TM.\nYou protected more than my research.$"

FallarborTown_CozmosHouse_Text_ReallyGoingToHelpMyResearch:
	.string "The stone still carries traces of\nthe reaction. I'll document them.\pBirch needs evidence he can test,\nnot another guess about the rifts.$"

FallarborTown_CozmosHouse_Text_CrushedWithDisappointment:
	.string "All right. Keep it safe.\nPlease bring it back when you're ready.$"

FallarborTown_CozmosHouse_Text_MayIHaveMeteorite:
	.string "May I examine that meteorite?\nI'll exchange a TM for it.\pThe evidence could help us understand\nwhat happened at the relay.$"

FallarborTown_CozmosHouse_Text_CozmoWentToMeteorFalls:
	.string "Cozmo went to Meteor Falls to check\nwhat they did with his research.\pMay said you were following the trail.\nPlease be careful.$"

FallarborTown_CozmosHouse_Text_FeelSorryForCozmo:
	.string "He's comparing his old notes with\nwhat happened at the mountain.\pHe wants to help put this right.$"

FallarborTown_CozmosHouse_Text_CozmoIsSoHappy:
	.string "He's preparing a report for Birch.\nThank you for bringing the sample back.$"

