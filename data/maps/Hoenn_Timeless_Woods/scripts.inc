Hoenn_Timeless_Woods_MapScripts::
    map_script MAP_SCRIPT_ON_TRANSITION, TimelessWoods_OnTransition
    map_script MAP_SCRIPT_ON_FRAME_TABLE, TimelessWoods_OnFrame
    .byte 0

TimelessWoods_OnTransition:
    setflag FLAG_TEMP_3
    setflag FLAG_TEMP_4
    call_if_ge VAR_LA_PARADIGM_ARC, 4, LegendsParadigm_ShowWoodsSearch
    setvar VAR_TEMP_1, 0
    setvar VAR_TEMP_2, 0
    goto_if_unset FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN, TimelessWoods_CheckArrival
    setvar VAR_TEMP_1, 1
TimelessWoods_CheckArrival:
    goto_if_unset FLAG_LA_TIMELESS_WOODS_ENTERED, TimelessWoods_TransitionEnd
    setvar VAR_TEMP_2, 1
TimelessWoods_TransitionEnd:
    end

TimelessWoods_OnFrame:
    map_script_2 VAR_TEMP_2, 0, TimelessWoods_FirstArrival
    .2byte 0

TimelessWoods_FirstArrival:
    lockall
    setvar VAR_TEMP_2, 1
    setspeaker SP_NAME_PLAYER
    msgbox TimelessWoods_Text_Familiar, MSGBOX_DEFAULT
    closemessage
    setflag FLAG_LA_TIMELESS_WOODS_ENTERED
    setspeaker SP_NAME_NONE
    releaseall
    end

TimelessWoods_EventScript_Waiting::
    lock
    faceplayer
    msgbox TimelessWoods_Text_Distant, MSGBOX_DEFAULT
    release
    end

TimelessWoods_EventScript_Conspiracy::
    goto_if_set FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN, TimelessWoods_SceneEnd
    lockall
    setvar VAR_TEMP_1, 1
    applymovement LOCALID_PLAYER, TimelessWoods_FaceRight
    waitmovement 0
    setspeaker SP_NAME_PLAYER
    msgbox TimelessWoods_Text_Voices, MSGBOX_DEFAULT
    closemessage
    special SpawnCameraObject
    applymovement LOCALID_CAMERA, TimelessWoods_CameraRight
    waitmovement 0
    applymovement LOCALID_CAMERA, TimelessWoods_FaceUpStep
    waitmovement 0
    delay 24
    setspeaker SP_NAME_MAN_IN_SUIT
    msgbox TimelessWoods_Text_Discovery, MSGBOX_DEFAULT
    setspeaker SP_NAME_BLUE_HAIRED_MAN
    msgbox TimelessWoods_Text_Resonance, MSGBOX_DEFAULT
    closemessage
    applymovement 1, TimelessWoods_FaceLeft
    waitmovement 0
    delay 20
    removeobject 3
    setflag FLAG_LA_TIMELESS_WOODS_ORB_TAKEN
    playse SE_SELECT
    waitse
    applymovement 1, TimelessWoods_PickUp
    waitmovement 0
    setspeaker SP_NAME_MAN_IN_SUIT
    msgbox TimelessWoods_Text_Stabilize, MSGBOX_DEFAULT
    setspeaker SP_NAME_BLUE_HAIRED_MAN
    msgbox TimelessWoods_Text_Plan, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAN_IN_SUIT
    msgbox TimelessWoods_Text_Secrecy, MSGBOX_DEFAULT
    closemessage
    applymovement 1, TimelessWoods_LeaveGiovanni
    applymovement 2, TimelessWoods_LeaveCyrus
    waitmovement 0
    removeobject 1
    applymovement 2, TimelessWoods_LastSteps
    waitmovement 0
    removeobject 2
    setflag FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN
    delay 20
    applymovement LOCALID_CAMERA, TimelessWoods_FaceDownStep
    waitmovement 0
    applymovement LOCALID_CAMERA, TimelessWoods_CameraLeft
    waitmovement 0
    special RemoveCameraObject
    setspeaker SP_NAME_PLAYER
    msgbox TimelessWoods_Text_Recognition, MSGBOX_DEFAULT
    closemessage
    setspeaker SP_NAME_NONE
    releaseall
TimelessWoods_SceneEnd:
    end

TimelessWoods_FaceRight:
    face_right
    step_end
TimelessWoods_FaceLeft:
    face_left
    step_end
TimelessWoods_FaceUpStep:
    walk_up
    step_end
TimelessWoods_FaceDownStep:
    walk_down
    step_end
TimelessWoods_PickUp:
    walk_left
    face_left
    delay_16
    step_end
TimelessWoods_CameraRight:
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    step_end
TimelessWoods_CameraLeft:
    walk_left
    walk_left
    walk_left
    walk_left
    walk_left
    walk_left
    walk_left
    walk_left
    step_end
TimelessWoods_LeaveGiovanni:
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    step_end
TimelessWoods_LeaveCyrus:
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    step_end
TimelessWoods_LastSteps:
    walk_right
    walk_right
    step_end

TimelessWoods_Text_Familiar:
    .string "{COLOR LIGHT_BLUE}This place…\nIt feels familiar.\pBut why?$"
TimelessWoods_Text_Voices:
    .string "{COLOR LIGHT_BLUE}Voices…\nSomeone's up ahead.$"
TimelessWoods_Text_Discovery:
    .string "So this is what the readings\nled us to.$"
TimelessWoods_Text_Resonance:
    .string "Its energy holds the distortion\nin a fixed state.\pWith it, a rift could remain open.$"
TimelessWoods_Text_Stabilize:
    .string "Then this little item may be the\nkey to stabilizing the rifts.\pNo more waiting for a portal\nto open by chance.$"
TimelessWoods_Text_Plan:
    .string "Each team will supply its data.\nI will resolve the destination.\pOnce the device is calibrated,\nwe can choose where to cross.$"
TimelessWoods_Text_Secrecy:
    .string "Tell the others to keep their\noperations quiet.\pThe professors must not find it.\nKeep those children away, too.\pBy the time anyone understands,\nwe'll control the crossings.$"
TimelessWoods_Text_Recognition:
    .string "{COLOR LIGHT_BLUE}Those two…\nI've seen them before.\pBut where?\pI need to tell Professor Birch\nwhat I heard.\pWhere did they go?\nI need to know more.$"
TimelessWoods_Text_Distant:
    .string "They seem absorbed in\ntheir conversation.$"

@ Project-owned reservation; registered asset map, no donor gameplay.
HyperHoenn_34_67_Timeless_Woods_EventScript_HyperConstruction_Registered1::
	lock
	faceplayer
	msgbox HyperHoenn_34_67_Timeless_Woods_Text_HyperConstruction_Registered1, MSGBOX_DEFAULT
	release
	end

HyperHoenn_34_67_Timeless_Woods_Text_HyperConstruction_Registered1:
	.string "This area is under construction.\p"
	.string "Please check back later!$"

LegendsParadigm_ShowWoodsSearch::
	goto_if_set FLAG_LA_ASHES_WOODS_DEPARTURE, LegendsParadigm_WoodsSearchShown
	clearflag FLAG_TEMP_3
	goto_if_ne VAR_LA_PARADIGM_ARC, 4, LegendsParadigm_WoodsSearchShown
	clearflag FLAG_TEMP_4
LegendsParadigm_WoodsSearchShown::
	return

LegendsParadigm_WoodsApproach::
	lockall
	applymovement LOCALID_PLAYER, LegendsParadigm_StepToClearing
	waitmovement 0
	goto LegendsParadigm_WoodsLead

LegendsParadigm_StepToClearing:
	walk_up
	step_end

LegendsParadigm_WoodsLead::
	lockall
	goto_if_ge VAR_LA_PARADIGM_ARC, 5, LegendsParadigm_WoodsRepeat
	turnobject LOCALID_PLAYER, DIR_EAST
	setspeaker SP_NAME_MAY
	msgbox LegendsParadigm_Text_MayTracks, MSGBOX_DEFAULT
	setspeaker SP_NAME_SHADOW_TRIAD
	msgbox LegendsParadigm_Text_Scout, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	call LegendsParadigm_AskScout
	setspeaker SP_NAME_SHADOW_TRIAD
	msgbox LegendsParadigm_Text_ScoutWarning, MSGBOX_DEFAULT
	closemessage
	playse SE_M_TELEPORT
	removeobject LOCALID_TIMELESS_PARADIGM_TRIAD
	setflag FLAG_TEMP_4
	setspeaker SP_NAME_MAY
	msgbox LegendsParadigm_Text_NorthernLead, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox LegendsParadigm_Text_ReportBeforeCrossing, MSGBOX_DEFAULT
	closemessage
	setspeaker SP_NAME_NONE
	setvar VAR_LA_PARADIGM_ARC, 5
	releaseall
	end

LegendsParadigm_WoodsRepeat::
	goto_if_lt VAR_LA_RIFT_TRACKER, 2, LegendsParadigm_WoodsRepeatLegacy
	goto_if_unset FLAG_LA_ASHES_WOODS_DEPARTURE, LegendsAshes_WoodsDeparture
LegendsParadigm_WoodsRepeatLegacy:
	setspeaker SP_NAME_MAY
	msgbox LegendsParadigm_Text_NorthernLead, MSGBOX_DEFAULT
	closemessage
	setspeaker SP_NAME_NONE
	releaseall
	end

LegendsParadigm_Text_MayTracks:
	.string "Fresh footprints, {PLAYER}.\nSomeone came back after those men.\pThat outfit… The attackers in\nPetalburg Woods dressed like that.$"
LegendsParadigm_Text_Scout:
	.string "The boy reached Kanto alive.\nYou already know that much.\pYet here you are, looking for a\ndevice you don't understand.$"
LegendsParadigm_Text_AskScout:
	.string "How do you know about Wally?\pWhere are the men with the\nR and G on their clothes?$"
LegendsParadigm_Text_ScoutWarning:
	.string "The device is already in transit.\nWe are securing their route.\pThe northern opening is restricted.\nTurn back while you still can.\pYour friend's crossing was\nrecorded. So was yours.$"
LegendsParadigm_Text_NorthernLead:
	.string "He knew about Wally before we\nsaid anything. Dad needs to hear.\pI'll watch the northern opening.\nLet's find out what they left.$"
LegendsParadigm_Text_ReportBeforeCrossing:
	.string "We tell Paradigm before anyone\nsteps through another rift.$"

LegendsParadigm_AskScout::
    goto_if_set FLAG_LA_HEARD_GIOVANNI, LegendsParadigm_AskScoutByName
    msgbox LegendsParadigm_Text_AskScout, MSGBOX_DEFAULT
    return
LegendsParadigm_AskScoutByName:
    msgbox LegendsParadigm_Text_AskGiovanni, MSGBOX_DEFAULT
    return
LegendsParadigm_Text_AskGiovanni:
    .string "How do you know about Wally?\pIs Giovanni the man in the suit?\nWhere did you take that device?$"
