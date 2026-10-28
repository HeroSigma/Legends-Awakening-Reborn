Route102_MapScripts::
	map_script MAP_SCRIPT_ON_FRAME_TABLE, LegendsPetalburg_Route102Frame
	map_script MAP_SCRIPT_ON_TRANSITION, Route102_TimelessCallOnTransition
	.byte 0

Route102_EventScript_LittleBoy::
	msgbox Route102_Text_ImNotVeryTall, MSGBOX_NPC
	end

Route102_EventScript_RouteSignOldale::
	msgbox Route102_Text_RouteSignOldale, MSGBOX_SIGN
	end

Route102_EventScript_RouteSignPetalburg::
	msgbox Route102_Text_RouteSignPetalburg, MSGBOX_SIGN
	end

Route102_EventScript_Boy::
	msgbox Route102_Text_CatchWholeBunchOfPokemon, MSGBOX_NPC
	end

Route102_EventScript_Calvin::
	trainerbattle_single TRAINER_CALVIN_1, Route102_Text_CalvinIntro, Route102_Text_CalvinDefeated, Route102_EventScript_CalvinRegisterMatchCallAfterBattle
	specialvar VAR_RESULT, ShouldTryRematchBattle
	goto_if_eq VAR_RESULT, TRUE, Route102_EventScript_CalvinRematch
	setvar VAR_0x8004, TRAINER_CALVIN_1
	specialvar VAR_RESULT, IsTrainerRegistered
	goto_if_eq VAR_RESULT, FALSE, Route102_EventScript_CalvinTryRegister
	msgbox Route102_Text_CalvinPostBattle, MSGBOX_DEFAULT
	release
	end

Route102_EventScript_CalvinRegisterMatchCallAfterBattle::
	special PlayerFaceTrainerAfterBattle
	waitmovement 0
	goto_if_set FLAG_HAS_MATCH_CALL, Route102_EventScript_CalvinRegisterMatchCall
	release
	end

Route102_EventScript_CalvinRegisterMatchCall::
	msgbox Route102_Text_CalvinRegisterShort, MSGBOX_DEFAULT
	register_matchcall TRAINER_CALVIN_1
	release
	end

Route102_EventScript_CalvinTryRegister::
	goto_if_set FLAG_HAS_MATCH_CALL, Route102_EventScript_CalvinRegister
	msgbox Route102_Text_CalvinPostBattle, MSGBOX_DEFAULT
	release
	end

Route102_EventScript_CalvinRegister::
	msgbox Route102_Text_CalvinRegister, MSGBOX_DEFAULT
	register_matchcall TRAINER_CALVIN_1
	release
	end

Route102_EventScript_CalvinRematch::
	trainerbattle_rematch TRAINER_CALVIN_1, Route102_Text_CalvinRematchIntro, Route102_Text_CalvinRematchDefeated
	msgbox Route102_Text_CalvinRematchPostBattle, MSGBOX_AUTOCLOSE
	end

Route102_EventScript_Rick::
	trainerbattle_single TRAINER_RICK, Route102_Text_RickIntro, Route102_Text_RickDefeated
	msgbox Route102_Text_RickPostBattle, MSGBOX_AUTOCLOSE
	end

Route102_EventScript_Tiana::
	trainerbattle_single TRAINER_TIANA, Route102_Text_TianaIntro, Route102_Text_TianaDefeated
	msgbox Route102_Text_TianaPostBattle, MSGBOX_AUTOCLOSE
	end

Route102_EventScript_Allen::
	trainerbattle_single TRAINER_ALLEN, Route102_Text_AllenIntro, Route102_Text_AllenDefeated, Route102_EventScript_AllenAfterBattle
Route102_EventScript_AllenAfterBattle::
	msgbox Route102_Text_AllenPostBattle, MSGBOX_DEFAULT
	closemessage
	call Route102_CheckTimelessCallAfterBattle
	release
	end

Route102_Text_WatchMeCatchPokemon:
	.string "Wally: POKéMON hide in grass like\nthis, don't they?\pPlease stay with me.\nI want to try catching a partner.$"

Route102_Text_WallyIDidIt:
	.string "I did it!\nRalts… My very first partner!\pThank you for trusting me.\nI promise to take care of you.$"

Route102_Text_LetsGoBack:
	.string "{PLAYER}, thank you!\n"
	.string "Let's go back to the GYM!$"

Route102_Text_ImNotVeryTall:
	.string "I'm…not very tall, so I sink right\n"
	.string "into tall grass.\p"
	.string "The grass goes up my nose and…\n"
	.string "Fwafwafwafwafwa…\p"
	.string "Fwatchoo!$"

Route102_Text_CatchWholeBunchOfPokemon:
	.string "I'm going to catch a whole bunch of\n"
	.string "POKéMON!$"

Route102_Text_RouteSignOldale:
	.string "ROUTE 102\n"
	.string "{RIGHT_ARROW} OLDALE TOWN$"

Route102_Text_RouteSignPetalburg:
	.string "ROUTE 102\n"
	.string "{LEFT_ARROW} PETALBURG CITY$"

@ Project-owned reservation; no donor gameplay, flags or warp destination.
Route102_EventScript_HyperConstruction_1::
	lock
	faceplayer
	msgbox Route102_Text_HyperConstruction_1, MSGBOX_DEFAULT
	release
	end

Route102_Text_HyperConstruction_1:
	.string "Timeless Woods is\n"
	.string "under construction.\p"
	.string "Please check back later!$"

@ Project-owned reservation; no donor gameplay, flags or warp destination.
Route102_EventScript_HyperConstruction_2::
	lock
	faceplayer
	msgbox Route102_Text_HyperConstruction_2, MSGBOX_DEFAULT
	release
	end

Route102_Text_HyperConstruction_2:
	.string "Timeless Woods is\n"
	.string "under construction.\p"
	.string "Please check back later!$"

@ Project-owned reservation; no donor gameplay, flags or warp destination.
Route102_EventScript_HyperConstruction_3::
	lock
	faceplayer
	msgbox Route102_Text_HyperConstruction_3, MSGBOX_DEFAULT
	release
	end

Route102_Text_HyperConstruction_3:
	.string "Timeless Woods is\n"
	.string "under construction.\p"
	.string "Please check back later!$"

@ Project-owned reservation; no donor gameplay, flags or warp destination.
Route102_EventScript_HyperConstruction_4::
	lock
	faceplayer
	msgbox Route102_Text_HyperConstruction_4, MSGBOX_DEFAULT
	release
	end

Route102_Text_HyperConstruction_4:
	.string "Timeless Woods is\n"
	.string "under construction.\p"
	.string "Please check back later!$"

@ Saved once-only story state; no trainer defeat or Woods access requirement.
Route102_TimelessCallOnTransition:
    call LegendsPetalburg_CheckWoodsExit
    goto_if_set FLAG_LA_TIMELESS_WOODS_CALL_HEARD, Route102_TimelessCallAlreadyHeard
    setvar VAR_LA_TIMELESS_WOODS_CALL_STATE, 0
    end
Route102_TimelessCallAlreadyHeard:
    setvar VAR_LA_TIMELESS_WOODS_CALL_STATE, 2
    end

Route102_CheckTimelessCallAfterBattle:
    goto_if_set FLAG_LA_TIMELESS_WOODS_CALL_HEARD, Route102_TimelessCallReturn
    getplayerxy VAR_0x8004, VAR_0x8005
    goto_if_ne VAR_0x8005, 8, Route102_TimelessCallReturn
    goto_if_lt VAR_0x8004, 12, Route102_TimelessCallReturn
    goto_if_gt VAR_0x8004, 14, Route102_TimelessCallReturn
    call Route102_TimelessCallScene
Route102_TimelessCallReturn:
    return

Route102_EventScript_TimelessCall::
    call Route102_TimelessCallScene
    end
Route102_TimelessCallScene:
    goto_if_set FLAG_LA_TIMELESS_WOODS_CALL_HEARD, Route102_TimelessCallReturn
    lockall
    setvar VAR_LA_TIMELESS_WOODS_CALL_STATE, 1
    applymovement LOCALID_PLAYER, Route102_TimelessNotice
    waitmovement 0
    playse SE_M_PSYBEAM2
    waitse
    setspeaker SP_NAME_NONE
    msgbox Route102_Text_TimelessName, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Route102_Text_TimelessCalling, MSGBOX_DEFAULT
    closemessage
    getplayerxy VAR_0x8004, VAR_0x8005
    special SpawnCameraObject
    switch VAR_0x8004
    case 12, Route102_TimelessPan12
    case 13, Route102_TimelessPan13
    case 14, Route102_TimelessPan14
Route102_TimelessPan12:
    applymovement LOCALID_CAMERA, Route102_TimelessCameraLeft6
    goto Route102_TimelessPanUp
Route102_TimelessPan13:
    applymovement LOCALID_CAMERA, Route102_TimelessCameraLeft7
    goto Route102_TimelessPanUp
Route102_TimelessPan14:
    applymovement LOCALID_CAMERA, Route102_TimelessCameraLeft8
Route102_TimelessPanUp:
    waitmovement 0
    applymovement LOCALID_CAMERA, Route102_TimelessCameraUp
    waitmovement 0
    delay 30
    playse SE_M_PSYBEAM2
    waitse
    setspeaker SP_NAME_NONE
    msgbox Route102_Text_TimelessName, MSGBOX_DEFAULT
    closemessage
    applymovement LOCALID_CAMERA, Route102_TimelessCameraDown
    waitmovement 0
    switch VAR_0x8004
    case 12, Route102_TimelessReturn12
    case 13, Route102_TimelessReturn13
    case 14, Route102_TimelessReturn14
Route102_TimelessReturn12:
    applymovement LOCALID_CAMERA, Route102_TimelessCameraRight6
    goto Route102_TimelessCameraReturned
Route102_TimelessReturn13:
    applymovement LOCALID_CAMERA, Route102_TimelessCameraRight7
    goto Route102_TimelessCameraReturned
Route102_TimelessReturn14:
    applymovement LOCALID_CAMERA, Route102_TimelessCameraRight8
Route102_TimelessCameraReturned:
    waitmovement 0
    special RemoveCameraObject
    setspeaker SP_NAME_PLAYER
    msgbox Route102_Text_TimelessKnowsMe, MSGBOX_DEFAULT
    closemessage
    setflag FLAG_LA_TIMELESS_WOODS_CALL_HEARD
    setvar VAR_LA_TIMELESS_WOODS_CALL_STATE, 2
    releaseall
    return

Route102_TimelessNotice:
    face_up
    delay_16
    face_left
    delay_16
    face_up
    step_end
Route102_TimelessCameraLeft8:
    walk_left
Route102_TimelessCameraLeft7:
    walk_left
Route102_TimelessCameraLeft6:
    walk_left
    walk_left
    walk_left
    walk_left
    walk_left
    walk_left
    step_end
Route102_TimelessCameraRight8:
    walk_right
Route102_TimelessCameraRight7:
    walk_right
Route102_TimelessCameraRight6:
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    step_end
Route102_TimelessCameraUp:
    walk_up
    walk_up
    walk_up
    walk_up
    walk_up
    step_end
Route102_TimelessCameraDown:
    walk_down
    walk_down
    walk_down
    walk_down
    walk_down
    step_end
Route102_Text_TimelessName:
    .string "{COLOR LIGHT_BLUE}{PLAYER}…$"
Route102_Text_TimelessCalling:
    .string "{COLOR LIGHT_BLUE}What is calling me?\pThat opening in the trees…\nThe voice is coming from there.$"
Route102_Text_TimelessKnowsMe:
    .string "{COLOR LIGHT_BLUE}I heard it again.\pIt knows my name…\pThat trainer is blocking\nthe path on the left.\pThere must be another way\nto get in there.$"
