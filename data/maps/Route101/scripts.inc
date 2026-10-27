Route101_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, Route101_OnTransition
	map_script MAP_SCRIPT_ON_FRAME_TABLE, Route101_OnFrame
	.byte 0

Route101_OnTransition:
	setflag FLAG_HIDE_LA_BIRCH_RESCUE_RED
	call ProfBirch_EventScript_UpdateLocation
	end

Route101_OnFrame:
	map_script_2 VAR_ROUTE101_STATE, 0, Route101_EventScript_HideMapNamePopup
	.2byte 0

Route101_EventScript_HideMapNamePopup::
	setflag FLAG_HIDE_MAP_NAME_POPUP
	setvar VAR_ROUTE101_STATE, 1
	end

Route101_EventScript_StartBirchRescue::
	lockall
	playbgm MUS_HELP, TRUE
	setspeaker SP_NAME_BIRCH
	msgbox Route101_Text_HelpMe, MSGBOX_DEFAULT
	closemessage
	setobjectxy LOCALID_ROUTE101_BIRCH, 0, 15
	setobjectxy LOCALID_ROUTE101_ZIGZAGOON, 0, 16
	applymovement LOCALID_PLAYER, Route101_Movement_EnterScene
	applymovement LOCALID_ROUTE101_BIRCH, Route101_Movement_BirchRunAway1
	applymovement LOCALID_ROUTE101_ZIGZAGOON, Route101_Movement_ZigzagoonChase1
	waitmovement 0
	applymovement LOCALID_ROUTE101_ZIGZAGOON, Route101_Movement_ZigzagoonChaseInCircles
	applymovement LOCALID_ROUTE101_BIRCH, Route101_Movement_BirchRunInCircles
	waitmovement 0
	applymovement LOCALID_ROUTE101_BIRCH, Common_Movement_WalkInPlaceFasterRight
	waitmovement 0
	applymovement LOCALID_ROUTE101_ZIGZAGOON, Route101_Movement_ZigzagoonFaceBirch
	applymovement LOCALID_ROUTE101_BIRCH, Route101_Movement_BirchFaceZigzagoon
	waitmovement 0
	msgbox Route101_Text_PleaseHelp, MSGBOX_DEFAULT
	closemessage
	setvar VAR_ROUTE101_STATE, 2
	releaseall
	end

Route101_EventScript_PreventExitSouth::
	lockall
	msgbox Route101_Text_DontLeaveMe, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_PLAYER, Route101_Movement_PreventExitSouth
	waitmovement 0
	releaseall
	end

Route101_EventScript_PreventExitWest::
	lockall
	msgbox Route101_Text_DontLeaveMe, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_PLAYER, Route101_Movement_PreventExitWest
	waitmovement 0
	releaseall
	end

Route101_EventScript_PreventExitNorth::
	lockall
	msgbox Route101_Text_DontLeaveMe, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_PLAYER, Route101_Movement_PreventExitNorth
	waitmovement 0
	releaseall
	end

Route101_Movement_PreventExitSouth:
	walk_up
	step_end

Route101_Movement_PreventExitWest:
	walk_right
	step_end

Route101_Movement_PreventExitNorth:
	walk_down
	step_end

Route101_Movement_ZigzagoonChaseInCircles:
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_fast_right
	walk_fast_right
	walk_fast_right
	walk_fast_down
	walk_fast_down
	walk_fast_left
	walk_fast_left
	walk_fast_left
	walk_fast_up
	walk_fast_up
	walk_fast_right
	walk_fast_right
	walk_fast_right
	walk_fast_down
	walk_fast_down
	walk_fast_left
	walk_fast_left
	walk_fast_left
	walk_fast_up
	walk_fast_up
	walk_fast_right
	walk_fast_right
	walk_fast_right
	walk_fast_down
	walk_fast_down
	walk_fast_left
	walk_fast_left
	step_end

Route101_Movement_ZigzagoonChase1:
	walk_fast_up
	walk_fast_right
	walk_fast_right
	walk_fast_right
	walk_fast_right
	walk_fast_up
	step_end

@ Leftover data? This command is unused.
	step_end

Route101_Movement_ZigzagoonFaceBirch:
	walk_in_place_fast_left
	walk_in_place_fast_left
	walk_in_place_fast_left
	walk_in_place_fast_left
	step_end

Route101_Movement_EnterScene:
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_in_place_faster_left
	step_end

Route101_Movement_BirchRunInCircles:
	walk_fast_up
	walk_fast_up
	walk_fast_right
	walk_fast_right
	walk_fast_right
	walk_fast_down
	walk_fast_down
	walk_fast_left
	walk_fast_left
	walk_fast_left
	walk_fast_up
	walk_fast_up
	walk_fast_right
	walk_fast_right
	walk_fast_right
	walk_fast_down
	walk_fast_down
	walk_fast_left
	walk_fast_left
	walk_fast_left
	walk_fast_up
	walk_fast_up
	walk_fast_right
	walk_fast_right
	walk_fast_right
	walk_fast_down
	walk_fast_down
	walk_fast_left
	walk_fast_left
	walk_fast_left
	step_end

Route101_Movement_BirchRunAway1:
	walk_fast_right
	walk_fast_right
	walk_fast_right
	walk_fast_right
	walk_fast_up
	walk_fast_up
	step_end

@ Leftover data? This command is unused.
	step_end

Route101_Movement_BirchFaceZigzagoon:
	walk_in_place_fast_right
	walk_in_place_fast_right
	walk_in_place_fast_right
	walk_in_place_fast_right
	step_end

Route101_Movement_Unused1:
	walk_up
	walk_up
	step_end

Route101_Movement_Unused2:
	walk_up
	walk_left
	walk_up
	step_end

Route101_EventScript_Youngster::
	msgbox Route101_Text_TakeTiredPokemonToPokeCenter, MSGBOX_NPC
	end

Route101_EventScript_Boy::
	msgbox Route101_Text_WildPokemonInTallGrass, MSGBOX_NPC
	end

Route101_EventScript_RouteSign::
	msgbox Route101_Text_RouteSign, MSGBOX_SIGN
	end

Route101_EventScript_BirchsBag::
	lock
	faceplayer
	setflag FLAG_SYS_POKEMON_GET
	setflag FLAG_LA_BIRCH_RESCUE_BATTLE
	setvar VAR_LA_BIRCH_RESCUE_STATE, 1
	fadescreen FADE_TO_BLACK
	removeobject LOCALID_ROUTE101_ZIGZAGOON
	setobjectxy LOCALID_PLAYER, 6, 13
	applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterLeft
	waitmovement 0
	special ChooseStarter
	call Route101_RedRescue
	applymovement LOCALID_ROUTE101_BIRCH, Route101_Movement_BirchApproachPlayer
	waitmovement 0
	setspeaker SP_NAME_BIRCH
	msgbox Route101_Text_YouSavedMe, MSGBOX_DEFAULT
	special HealPlayerParty
	setflag FLAG_RESCUED_BIRCH
	setvar VAR_LA_BIRCH_RESCUE_STATE, 3
	setflag FLAG_HIDE_ROUTE_101_BIRCH_ZIGZAGOON_BATTLE
	clearflag FLAG_HIDE_LITTLEROOT_TOWN_BIRCHS_LAB_BIRCH
	setflag FLAG_HIDE_ROUTE_101_BIRCH_STARTERS_BAG
	setvar VAR_BIRCH_LAB_STATE, 2
	setvar VAR_ROUTE101_STATE, 3
	clearflag FLAG_HIDE_MAP_NAME_POPUP
	checkplayergender
	call_if_eq VAR_RESULT, MALE, Route101_EventScript_HideMayInBedroom
	call_if_eq VAR_RESULT, FEMALE, Route101_EventScript_HideBrendanInBedroom
	warp MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB, 6, 5
	waitstate
	release
	end

Route101_EventScript_HideMayInBedroom::
	setflag FLAG_HIDE_LITTLEROOT_TOWN_MAYS_HOUSE_RIVAL_BEDROOM
	return

Route101_EventScript_HideBrendanInBedroom::
	setflag FLAG_HIDE_LITTLEROOT_TOWN_BRENDANS_HOUSE_RIVAL_BEDROOM
	return

Route101_Movement_BirchApproachPlayer:
	walk_right
	step_end

Route101_Text_HelpMe:
	.string "H-help me!$"

Route101_Text_PleaseHelp:
	.string "Hello! You over there!\n"
	.string "Please! Help!\p"
	.string "In my BAG!\n"
	.string "There's a POKé BALL!$"

Route101_Text_DontLeaveMe:
	.string "Wh-Where are you going?!\n"
	.string "Don't leave me like this!$"

Route101_Text_YouSavedMe:
    .string "Whew… That was far beyond anything\nI expected to find on this route.\pYou tried to protect me, {PLAYER}.\nAnd Red arrived just in time.\pLet's get your partner somewhere safe.\nWe can talk at my lab.$"

Route101_Text_TakeTiredPokemonToPokeCenter:
	.string "If POKéMON get tired, take them to\n"
	.string "a POKéMON CENTER.\p"
	.string "There's a POKéMON CENTER in OLDALE\n"
	.string "TOWN right close by.$"

Route101_Text_WildPokemonInTallGrass:
	.string "Wild POKéMON will jump out at you in\n"
	.string "tall grass.\p"
	.string "If you want to catch POKéMON, you have\n"
	.string "to go into the tall grass and search.$"

Route101_Text_RouteSign:
	.string "ROUTE 101\n"
	.string "{UP_ARROW} OLDALE TOWN$"


@ The first-battle callback returns here on loss without blackout or money loss.
Route101_RedRescue:
    clearflag FLAG_LA_BIRCH_RESCUE_BATTLE
    setvar VAR_LA_BIRCH_RESCUE_STATE, 2
    addobject LOCALID_ROUTE101_ZIGZAGOON
    setobjectxy LOCALID_ROUTE101_ZIGZAGOON, 5, 13
    setobjectmovementtype LOCALID_ROUTE101_ZIGZAGOON, MOVEMENT_TYPE_FACE_RIGHT
    setspeaker SP_NAME_PLAYER
    msgbox Route101_Text_Outmatched, MSGBOX_DEFAULT
    setspeaker SP_NAME_NONE
    msgbox Route101_Text_RedOffscreen, MSGBOX_DEFAULT
    closemessage
    special LegendsBirchRescueThunderbolt
    waitstate
    applymovement LOCALID_ROUTE101_ZIGZAGOON, Route101_Movement_AttackerFaints
    waitmovement 0
    removeobject LOCALID_ROUTE101_ZIGZAGOON
    setflag FLAG_HIDE_ROUTE_101_ZIGZAGOON
    clearflag FLAG_HIDE_LA_BIRCH_RESCUE_RED
    addobject LOCALID_ROUTE101_RED
    addobject LOCALID_ROUTE101_RED_PIKACHU
    applymovement LOCALID_ROUTE101_RED, Route101_Movement_RedArrives
    applymovement LOCALID_ROUTE101_RED_PIKACHU, Route101_Movement_RedArrives
    waitmovement 0
    applymovement LOCALID_ROUTE101_RED, Common_Movement_FacePlayer
    applymovement LOCALID_ROUTE101_RED_PIKACHU, Common_Movement_FacePlayer
    waitmovement 0
    applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterUp
    waitmovement 0
    setspeaker SP_NAME_RED
    msgbox Route101_Text_RedIntroduces, MSGBOX_DEFAULT
    setspeaker SP_NAME_BIRCH
    msgbox Route101_Text_BirchThanksRed, MSGBOX_DEFAULT
    setspeaker SP_NAME_RED
    msgbox Route101_Text_RedReassures, MSGBOX_DEFAULT
    closemessage
    setflag FLAG_LA_MET_RED
    special HealPlayerParty
    applymovement LOCALID_ROUTE101_RED, Route101_Movement_RedLeavesSouth
    applymovement LOCALID_ROUTE101_RED_PIKACHU, Route101_Movement_PikachuLeavesSouth
    waitmovement 0
    removeobject LOCALID_ROUTE101_RED
    removeobject LOCALID_ROUTE101_RED_PIKACHU
    setflag FLAG_HIDE_LA_BIRCH_RESCUE_RED
    applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterLeft
    waitmovement 0
    return

Route101_Movement_AttackerFaints:
    delay_8
    set_invisible
    delay_8
    set_visible
    delay_8
    set_invisible
    step_end

@ Enter from the northern path, stopping just above the player and bag.
Route101_Movement_RedArrives:
    walk_down
    walk_down
    walk_left
    walk_left
    walk_left
    walk_left
    walk_left
    walk_down
    step_end

Route101_Text_Outmatched:
    .string "{COLOR LIGHT_BLUE}My partner can't keep fighting…\pI can't stop that thing!$"
Route101_Text_RedOffscreen:
    .string "{COLOR RED}Pikachu! Use Thunderbolt!$"
Route101_Text_RedIntroduces:
    .string "{COLOR RED}Stay back. Pikachu's got this.\pI'm Red. Are either of you hurt?$"
Route101_Text_BirchThanksRed:
    .string "We're all right, thanks to you.\pThat POKéMON… It doesn't belong\nanywhere near Littleroot.$"
Route101_Text_RedReassures:
    .string "{COLOR RED}You stepped in to help. That took\ncourage. But you were outmatched.\pLook after your partner first.\nProfessor, get them back to your lab.$"

Route101_Movement_RedLeavesSouth:
    walk_left
    walk_down
    walk_down
    walk_down
    walk_right
    walk_right
    walk_right
    walk_right
    walk_down
    walk_down
    walk_down
    walk_down
    set_invisible
    step_end

Route101_Movement_PikachuLeavesSouth:
    delay_16
    walk_left
    walk_left
    walk_down
    walk_down
    walk_down
    walk_right
    walk_right
    walk_right
    walk_right
    walk_down
    walk_down
    walk_down
    walk_down
    set_invisible
    step_end
