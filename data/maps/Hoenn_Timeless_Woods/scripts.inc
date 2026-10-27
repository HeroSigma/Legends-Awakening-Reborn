Hoenn_Timeless_Woods_MapScripts::
    map_script MAP_SCRIPT_ON_TRANSITION, TimelessWoods_OnTransition
    map_script MAP_SCRIPT_ON_FRAME_TABLE, TimelessWoods_OnFrame
    .byte 0

TimelessWoods_OnTransition:
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
    setspeaker SP_NAME_GIOVANNI
    msgbox TimelessWoods_Text_Discovery, MSGBOX_DEFAULT
    setspeaker SP_NAME_CYRUS
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
    setspeaker SP_NAME_GIOVANNI
    msgbox TimelessWoods_Text_Stabilize, MSGBOX_DEFAULT
    setspeaker SP_NAME_CYRUS
    msgbox TimelessWoods_Text_Plan, MSGBOX_DEFAULT
    setspeaker SP_NAME_GIOVANNI
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
    .string "Stable passage would let us\nmove between worlds at will.\pFirst, we must learn how to\ncontrol the destination.$"
TimelessWoods_Text_Secrecy:
    .string "The professors must not find it.\pAnd keep those children out of\nour way. All of them.\pBy the time anyone understands,\nwe'll control the crossings.$"
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
