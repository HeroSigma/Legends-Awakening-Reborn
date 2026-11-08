Kanto_PowerPlant_Rift_MapScripts::
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PowerPlantRift_LegacyFrame
	.byte 0

PowerPlantRift_LegacyFrame:
	map_script_2 VAR_TEMP_0, 0, PowerPlantRift_LegacyRedirect
	.2byte 0

PowerPlantRift_LegacyRedirect::
	lockall
	warp MAP_KANTOAR_3_28_ROUTE10, 9, 44
	waitstate
	end

PowerPlantRift_RouteTransition:
	setflag FLAG_TEMP_1
	setflag FLAG_TEMP_2
	setvar VAR_TEMP_0, 1
	goto_if_ne VAR_LA_MAUVILLE_RIFT, 1, PowerPlantRift_RouteTransitionEnd
	clearflag FLAG_TEMP_1
	call_if_ge VAR_LA_POWERPLANT_STATE, 3, PowerPlantRift_ShowRouteWattson
	goto_if_set FLAG_LA_KANTO_RIFT_ARRIVAL, PowerPlantRift_RouteTransitionEnd
	setvar VAR_TEMP_0, 0
PowerPlantRift_RouteTransitionEnd:
	end

PowerPlantRift_ShowRouteWattson::
	clearflag FLAG_TEMP_2
	return

PowerPlantRift_RouteFrame:
	map_script_2 VAR_TEMP_0, 0, PowerPlantRift_Arrival
	.2byte 0

PowerPlantRift_PlantTransition:
	setflag FLAG_TEMP_5
	clearflag FLAG_TEMP_3
	goto_if_lt VAR_LA_POWERPLANT_STATE, 3, PowerPlantRift_PlantTransitionEnd
	setflag FLAG_TEMP_3
PowerPlantRift_PlantTransitionEnd:
	end

PowerPlantRift_OnLoad:
	@ The reactor's front is solid and is operated from the tile below.
	setmetatile 8, 11, 0x2f9, TRUE
	end

PowerPlantRift_Arrival::
	lockall
	setvar VAR_TEMP_0, 1
	setflag FLAG_LA_KANTO_RIFT_ARRIVAL
	applymovement LOCALID_PLAYER, PowerPlantRift_LookAround
	waitmovement 0
	setspeaker SP_NAME_PLAYER
	msgbox PowerPlantRift_Text_WhereAreWe, MSGBOX_DEFAULT
	closemessage
	setspeaker SP_NAME_NONE
	releaseall
	end

PowerPlantRift_LookAround:
	face_left
	delay_16
	face_right
	delay_16
	face_up
	step_end

PowerPlantRift_ReadSign::
	lockall
	setspeaker SP_NAME_NONE
	msgbox PowerPlantRift_Text_Sign, MSGBOX_DEFAULT
	goto_if_ne VAR_LA_MAUVILLE_RIFT, 1, PowerPlantRift_End
	goto_if_ne VAR_LA_POWERPLANT_STATE, 0, PowerPlantRift_End
	setspeaker SP_NAME_PLAYER
	msgbox PowerPlantRift_Text_Player, MSGBOX_DEFAULT
	setspeaker SP_NAME_WALLY
	msgbox PowerPlantRift_Text_FindWattson, MSGBOX_DEFAULT
	goto PowerPlantRift_End

PowerPlantRift_RouteWattson::
	lock
	faceplayer
	goto_if_lt VAR_LA_POWERPLANT_STATE, 4, PowerPlantRift_Unstable
	msgbox PowerPlantRift_Text_Ready, MSGBOX_DEFAULT
	goto PowerPlantRift_End

PowerPlantRift_Wally::
	lockall
	goto_if_eq VAR_LA_POWERPLANT_STATE, 3, PowerPlantRift_WallyAfterBattle
	goto_if_ge VAR_LA_POWERPLANT_STATE, 4, PowerPlantRift_Ready
	setspeaker SP_NAME_WALLY
	msgbox PowerPlantRift_Text_Wally, MSGBOX_DEFAULT
	goto PowerPlantRift_End

PowerPlantRift_Wattson::
	lock
	goto_if_eq VAR_LA_POWERPLANT_STATE, 2, PowerPlantRift_WattsonAfterBattle
	goto_if_ge VAR_LA_POWERPLANT_STATE, 3, PowerPlantRift_Ready
	turnobject LOCALID_PLANT_RIFT_WATTSON, DIR_NORTH
	msgbox PowerPlantRift_Text_Wattson, MSGBOX_DEFAULT
	goto_if_eq VAR_LA_POWERPLANT_STATE, 2, PowerPlantRift_End
	setvar VAR_LA_POWERPLANT_STATE, 1
	goto PowerPlantRift_End

PowerPlantRift_Console::
	lockall
	goto_if_eq VAR_LA_POWERPLANT_STATE, 0, PowerPlantRift_UnknownConsole
	goto_if_ge VAR_LA_POWERPLANT_STATE, 2, PowerPlantRift_StableConsole
	msgbox PowerPlantRift_Text_Console, MSGBOX_YESNO
	goto_if_ne VAR_RESULT, YES, PowerPlantRift_End
	closemessage
	playse SE_THUNDER
	msgbox PowerPlantRift_Text_Shutdown, MSGBOX_DEFAULT
	closemessage
	clearflag FLAG_TEMP_5
	addobject LOCALID_PLANT_RIFT_MIRAIDON
	playmoncry SPECIES_MIRAIDON, CRY_MODE_NORMAL
	applymovement LOCALID_PLANT_RIFT_MIRAIDON, PowerPlantRift_MiraidonApproach
	waitmovement 0
	setspeaker SP_NAME_PLAYER
	msgbox PowerPlantRift_Text_Miraidon, MSGBOX_DEFAULT
	closemessage
	setspeaker SP_NAME_NONE
	setflag FLAG_LA_MIRAIDON_BATTLE
	setwildbattle SPECIES_MIRAIDON, 70
	dowildbattle
	clearflag FLAG_LA_MIRAIDON_BATTLE
	special HealPlayerParty
	removeobject LOCALID_PLANT_RIFT_MIRAIDON
	setflag FLAG_TEMP_5
	setvar VAR_LA_POWERPLANT_STATE, 2
	setspeaker SP_NAME_PLAYER
	msgbox PowerPlantRift_Text_Outmatched, MSGBOX_DEFAULT
	goto PowerPlantRift_End

PowerPlantRift_StableConsole::
	msgbox PowerPlantRift_Text_Stable, MSGBOX_DEFAULT
	goto PowerPlantRift_End

PowerPlantRift_UnknownConsole::
	msgbox PowerPlantRift_Text_UnknownConsole, MSGBOX_DEFAULT
	goto PowerPlantRift_End

PowerPlantRift_Return::
	lockall
	goto_if_ne VAR_LA_POWERPLANT_STATE, 4, PowerPlantRift_Unstable
	msgbox PowerPlantRift_Text_Return, MSGBOX_YESNO
	goto_if_ne VAR_RESULT, YES, PowerPlantRift_End
	closemessage
	setspeaker SP_NAME_WALLY
	msgbox PowerPlantRift_Text_GoTogether, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_ROUTE10_RIFT_KIRLIA, PowerPlantRift_KirliaReturn
	waitmovement 0
	removeobject LOCALID_ROUTE10_RIFT_KIRLIA
	applymovement LOCALID_ROUTE10_RIFT_WALLY, PowerPlantRift_WallyReturn
	waitmovement 0
	removeobject LOCALID_ROUTE10_RIFT_WALLY
	applymovement LOCALID_ROUTE10_RIFT_WATTSON, PowerPlantRift_WattsonReturn
	waitmovement 0
	removeobject LOCALID_ROUTE10_RIFT_WATTSON
	setvar VAR_LA_MAUVILLE_RIFT, 2
	warp MAP_MAUVILLE_CITY_GYM, 5, 19
	waitstate
	end

PowerPlantRift_Unstable::
	msgbox PowerPlantRift_Text_Unstable, MSGBOX_DEFAULT
	goto PowerPlantRift_End

PowerPlantRift_End::
	closemessage
	setspeaker SP_NAME_NONE
	releaseall
	end

PowerPlantRift_Text_Sign:
	.string "KANTO REGION - ROUTE 10\nPOWER PLANT - NORTH$"
PowerPlantRift_Text_WhereAreWe:
	.string "Where are we? This isn't the Gym.\pThere's a sign by the building.\nI should read it.$"
PowerPlantRift_Text_FindWattson:
	.string "Kanto… That's a long way from\nMauville.\pKirlia senses someone inside.\nIt might be Wattson.\pI'll watch the rift with her\nwhile you check the Power Plant.$"
PowerPlantRift_Text_Player:
	.string "Kanto? We just crossed from\nHoenn in a single step…$"
PowerPlantRift_Text_Wally:
	.string "Kirlia, you hear someone?\nShow us where.$"
PowerPlantRift_Text_Wattson:
	.string "Wattson: Am I glad to see you!\pThis reactor is pulling power\nstraight through the rift.\pI'm holding the relay. Use the\nemergency switch to shut it down.\pIt's on the front of the reactor\nbeside me.$"
PowerPlantRift_Text_UnknownConsole:
	.string "The gauges are jumping too fast\nto read.$"
PowerPlantRift_Text_Console:
	.string "Shut down the reactor?$"
PowerPlantRift_Text_Stable:
	.string "The reactor is silent.\nThe rift is holding for now.$"
PowerPlantRift_Text_Unstable:
	.string "We need to check on Wattson and\nWally before we leave.$"
PowerPlantRift_Text_Return:
	.string "Bring Wattson, Wally, and Kirlia\nback through the rift?$"

PowerPlantRift_MiraidonApproach:
	walk_down
	walk_down
	walk_down
	walk_down
	walk_right
	walk_right
	walk_right
	step_end

PowerPlantRift_WattsonAfterBattle::
	faceplayer
	setspeaker SP_NAME_NONE
	msgbox PowerPlantRift_Text_WattsonAfter, MSGBOX_DEFAULT
	setvar VAR_LA_POWERPLANT_STATE, 3
	closemessage
	applymovement LOCALID_PLANT_RIFT_WATTSON, PowerPlantRift_WattsonLeftExit
	waitmovement 0
	playse SE_DOOR
	removeobject LOCALID_PLANT_RIFT_WATTSON
	setflag FLAG_TEMP_3
	goto PowerPlantRift_End

PowerPlantRift_WallyAfterBattle::
	setspeaker SP_NAME_WALLY
	msgbox PowerPlantRift_Text_WallyAfter, MSGBOX_DEFAULT
	setvar VAR_LA_POWERPLANT_STATE, 4
	goto PowerPlantRift_End

PowerPlantRift_Ready::
	msgbox PowerPlantRift_Text_Ready, MSGBOX_DEFAULT
	goto PowerPlantRift_End

PowerPlantRift_Text_Shutdown:
	.string "The reactor winds down.\pHeavy footsteps echo from the\nother side of the machinery.$"
PowerPlantRift_Text_Miraidon:
	.string "What is that?!\nIt's coming straight for us!$"
PowerPlantRift_Text_Outmatched:
	.string "We couldn't even slow it down…\pIt went after the reactor. I need\nto check on Wattson.$"
PowerPlantRift_Text_WattsonAfter:
	.string "Wattson: Are you hurt? I've never\nseen a Pokémon like that!\pThe reactor was drawing it here.\nIt left when the current died.\pThe rift outside is still holding.\pI'll take the exit on the left.\nFollow me back to the courtyard.\pCheck on Wally before we leave.$"
PowerPlantRift_Text_WallyAfter:
	.string "{PLAYER}! We heard the battle.\nAre you all right?\pKirlia felt it coming, but I\ncouldn't tell what she meant.\pLet's get everyone home. I'll\nstay right with you this time.$"
PowerPlantRift_Text_Ready:
	.string "Everyone is ready. Head back\nto the rift.$"
PowerPlantRift_Text_GoTogether:
	.string "Kirlia, stay close. Wattson,\ncome with us. We're going together!$"

PowerPlantRift_KirliaReturn:
	walk_down
	walk_right
	walk_right
	walk_right
	step_end

PowerPlantRift_WallyReturn:
	walk_right
	walk_right
	walk_right
	step_end

PowerPlantRift_WattsonReturn:
	walk_left
	step_end

PowerPlantRift_WattsonLeftExit:
	walk_left
	walk_down
	step_end
