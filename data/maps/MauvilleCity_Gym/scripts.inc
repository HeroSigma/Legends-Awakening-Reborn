MauvilleCity_Gym_MapScripts::
	map_script MAP_SCRIPT_ON_LOAD, MauvilleCity_Gym_OnLoad
	map_script MAP_SCRIPT_ON_TRANSITION, MauvilleRift_GymTransition
	map_script MAP_SCRIPT_ON_FRAME_TABLE, MauvilleRift_GymFrame
	.byte 0

MauvilleCity_Gym_OnLoad:
	goto_if_set FLAG_DEFEATED_MAUVILLE_GYM, MauvilleCity_Gym_EventScript_DeactivatePuzzle
	switch VAR_MAUVILLE_GYM_STATE
	case 0, MauvilleCity_Gym_EventScript_UpdateBarriers
	case 1, MauvilleCity_Gym_EventScript_Switch1Pressed
	case 2, MauvilleCity_Gym_EventScript_Switch2Pressed
	case 3, MauvilleCity_Gym_EventScript_Switch3Pressed
	case 4, MauvilleCity_Gym_EventScript_Switch4Pressed
	end

MauvilleCity_Gym_EventScript_UpdateBarriers::
	goto_if_set FLAG_MAUVILLE_GYM_BARRIERS_STATE, MauvilleCity_Gym_EventScript_SetAltBarriers
	end

MauvilleCity_Gym_EventScript_SetAltBarriers::
	setmetatile 3, 11, METATILE_MauvilleGym_RedBeamV1_On, TRUE
	setmetatile 3, 12, METATILE_MauvilleGym_RedBeamV2_On, TRUE
	setmetatile 3, 13, METATILE_MauvilleGym_PoleTop_On, TRUE
	setmetatile 4, 10, METATILE_MauvilleGym_RedBeamH1_On, FALSE
	setmetatile 5, 10, METATILE_MauvilleGym_RedBeamH2_On, FALSE
	setmetatile 4, 11, METATILE_MauvilleGym_RedBeamH3_On, TRUE
	setmetatile 5, 11, METATILE_MauvilleGym_RedBeamH4_On, TRUE
	setmetatile 7, 10, METATILE_MauvilleGym_RedBeamH1_On, FALSE
	setmetatile 8, 10, METATILE_MauvilleGym_RedBeamH2_On, FALSE
	setmetatile 7, 11, METATILE_MauvilleGym_RedBeamH3_On, TRUE
	setmetatile 8, 11, METATILE_MauvilleGym_RedBeamH4_On, TRUE
	setmetatile 4, 13, METATILE_MauvilleGym_GreenBeamH1_Off, FALSE
	setmetatile 5, 13, METATILE_MauvilleGym_GreenBeamH2_Off, FALSE
	setmetatile 4, 14, METATILE_MauvilleGym_GreenBeamH3_Off, FALSE
	setmetatile 5, 14, METATILE_MauvilleGym_GreenBeamH4_Off, FALSE
	setmetatile 1, 10, METATILE_MauvilleGym_GreenBeamH1_Off, FALSE
	setmetatile 2, 10, METATILE_MauvilleGym_GreenBeamH2_Off, FALSE
	setmetatile 1, 11, METATILE_MauvilleGym_GreenBeamH3_Off, FALSE
	setmetatile 2, 11, METATILE_MauvilleGym_GreenBeamH4_Off, FALSE
	setmetatile 6, 8, METATILE_MauvilleGym_PoleBottom_On, TRUE
	setmetatile 6, 9, METATILE_MauvilleGym_FloorTile, FALSE
	setmetatile 6, 10, METATILE_MauvilleGym_PoleTop_Off, FALSE
	setmetatile 4, 6, METATILE_MauvilleGym_GreenBeamH1_Off, FALSE
	setmetatile 5, 6, METATILE_MauvilleGym_GreenBeamH2_Off, FALSE
	setmetatile 4, 7, METATILE_MauvilleGym_GreenBeamH3_Off, FALSE
	setmetatile 5, 7, METATILE_MauvilleGym_GreenBeamH4_Off, FALSE
	end

MauvilleCity_Gym_EventScript_Switch1Pressed::
	setvar VAR_0x8004, 0
	special MauvilleGymPressSwitch
	goto MauvilleCity_Gym_EventScript_UpdateBarriers
	end

MauvilleCity_Gym_EventScript_Switch2Pressed::
	setvar VAR_0x8004, 1
	special MauvilleGymPressSwitch
	goto MauvilleCity_Gym_EventScript_UpdateBarriers
	end

MauvilleCity_Gym_EventScript_Switch3Pressed::
	setvar VAR_0x8004, 2
	special MauvilleGymPressSwitch
	goto MauvilleCity_Gym_EventScript_UpdateBarriers
	end

MauvilleCity_Gym_EventScript_Switch4Pressed::
	setvar VAR_0x8004, 3
	special MauvilleGymPressSwitch
	goto MauvilleCity_Gym_EventScript_UpdateBarriers
	end

MauvilleCity_Gym_EventScript_DeactivatePuzzle::
	special MauvilleGymDeactivatePuzzle
	end

MauvilleCity_Gym_EventScript_Wattson::
	goto_if_set FLAG_DEFEATED_MAUVILLE_GYM, MauvilleRift_WattsonBattle
	goto_if_ne VAR_LA_MAUVILLE_RIFT, 3, MauvilleCity_Gym_EventScript_GymGuide
MauvilleRift_WattsonBattle::
	call_if_eq VAR_LA_PARADIGM_ARC, 0, MauvilleRift_WattsonExplains
	trainerbattle_single TRAINER_WATTSON_1, MauvilleCity_Gym_Text_WattsonIntro, MauvilleCity_Gym_Text_WattsonDefeat, MauvilleCity_Gym_EventScript_WattsonDefeated, NO_MUSIC
	specialvar VAR_RESULT, ShouldTryRematchBattle
	goto_if_eq VAR_RESULT, TRUE, MauvilleCity_Gym_EventScript_WattsonRematch
	goto_if_unset FLAG_RECEIVED_TM_SHOCK_WAVE, MauvilleCity_Gym_EventScript_GiveShockWave2
	goto_if_eq VAR_NEW_MAUVILLE_STATE, 2, MauvilleCity_Gym_EventScript_CompletedNewMauville
	msgbox MauvilleCity_Gym_Text_WattsonPostBattle, MSGBOX_DEFAULT
	release
	end

MauvilleCity_Gym_EventScript_WattsonDefeated::
	message MauvilleCity_Gym_Text_ReceivedDynamoBadge
	waitmessage
	call Common_EventScript_PlayGymBadgeFanfare
	msgbox MauvilleCity_Gym_Text_ExplainDynamoBadgeTakeThis, MSGBOX_DEFAULT
	setvar VAR_SLATEPORT_OUTSIDE_MUSEUM_STATE, 3
	setflag FLAG_HIDE_VERDANTURF_TOWN_SCOTT
	setflag FLAG_DEFEATED_MAUVILLE_GYM
	setflag FLAG_BADGE03_GET
	addvar VAR_PETALBURG_GYM_STATE, 1
	call_if_eq VAR_PETALBURG_GYM_STATE, 6, Common_EventScript_ReadyPetalburgGymForBattle
	setvar VAR_0x8008, 3
	call Common_EventScript_SetGymTrainers
	special MauvilleGymDeactivatePuzzle
	special DrawWholeMapView
	playse SE_UNLOCK
	call MauvilleCity_Gym_EventScript_GiveShockWave
	closemessage
	delay 30
	playfanfare MUS_REGISTER_MATCH_CALL
	msgbox MauvilleCity_Gym_Text_RegisteredWattson, MSGBOX_DEFAULT
	waitfanfare
	closemessage
	delay 30
	setflag FLAG_ENABLE_WATTSON_MATCH_CALL
	call LegendsParadigm_QueueWallyCall
	call RiftResearch_Invite
	release
	end

MauvilleCity_Gym_EventScript_GiveShockWave2::
	giveitem ITEM_TM_SHOCK_WAVE
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_ShowBagIsFull
	msgbox MauvilleCity_Gym_Text_ExplainShockWave, MSGBOX_DEFAULT
	setflag FLAG_RECEIVED_TM_SHOCK_WAVE
	release
	end

MauvilleCity_Gym_EventScript_GiveShockWave::
	giveitem ITEM_TM_SHOCK_WAVE
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_BagIsFull
	msgbox MauvilleCity_Gym_Text_ExplainShockWave, MSGBOX_DEFAULT
	setflag FLAG_RECEIVED_TM_SHOCK_WAVE
	return

MauvilleCity_Gym_EventScript_CompletedNewMauville::
	msgbox MauvilleCity_Gym_Text_WattsonGoForthAndEndeavor, MSGBOX_DEFAULT
	release
	end

MauvilleCity_Gym_EventScript_WattsonRematch::
	trainerbattle_rematch_double TRAINER_WATTSON_1, MauvilleCity_Gym_Text_WattsonPreRematch, MauvilleCity_Gym_Text_WattsonRematchDefeat, MauvilleCity_Gym_Text_WattsonRematchNeedTwoMons
	msgbox MauvilleCity_Gym_Text_WattsonPostRematch, MSGBOX_AUTOCLOSE
	end

MauvilleCity_Gym_EventScript_Switch1::
	lockall
	goto_if_set FLAG_DEFEATED_MAUVILLE_GYM, MauvilleCity_Gym_EventScript_SwitchDoNothing
	goto_if_eq VAR_MAUVILLE_GYM_STATE, 1, MauvilleCity_Gym_EventScript_SwitchDoNothing
	setvar VAR_MAUVILLE_GYM_STATE, 1
	setvar VAR_0x8004, 0
	goto MauvilleCity_Gym_EventScript_PressFloorSwitch
	end

MauvilleCity_Gym_EventScript_Switch2::
	lockall
	goto_if_set FLAG_DEFEATED_MAUVILLE_GYM, MauvilleCity_Gym_EventScript_SwitchDoNothing
	goto_if_eq VAR_MAUVILLE_GYM_STATE, 2, MauvilleCity_Gym_EventScript_SwitchDoNothing
	setvar VAR_MAUVILLE_GYM_STATE, 2
	setvar VAR_0x8004, 1
	goto MauvilleCity_Gym_EventScript_PressFloorSwitch
	end

MauvilleCity_Gym_EventScript_Switch3::
	lockall
	goto_if_set FLAG_DEFEATED_MAUVILLE_GYM, MauvilleCity_Gym_EventScript_SwitchDoNothing
	goto_if_eq VAR_MAUVILLE_GYM_STATE, 3, MauvilleCity_Gym_EventScript_SwitchDoNothing
	setvar VAR_MAUVILLE_GYM_STATE, 3
	setvar VAR_0x8004, 2
	goto MauvilleCity_Gym_EventScript_PressFloorSwitch
	end

MauvilleCity_Gym_EventScript_Switch4::
	lockall
	goto_if_set FLAG_DEFEATED_MAUVILLE_GYM, MauvilleCity_Gym_EventScript_SwitchDoNothing
	goto_if_eq VAR_MAUVILLE_GYM_STATE, 4, MauvilleCity_Gym_EventScript_SwitchDoNothing
	setvar VAR_MAUVILLE_GYM_STATE, 4
	setvar VAR_0x8004, 3
	goto MauvilleCity_Gym_EventScript_PressFloorSwitch
	end

MauvilleCity_Gym_EventScript_PressFloorSwitch::
	special MauvilleGymSetDefaultBarriers
	special MauvilleGymPressSwitch
	special DrawWholeMapView
	playse SE_UNLOCK
	goto_if_set FLAG_MAUVILLE_GYM_BARRIERS_STATE, MauvilleCity_Gym_EventScript_ClearBarriersAltState
	goto_if_unset FLAG_MAUVILLE_GYM_BARRIERS_STATE, MauvilleCity_Gym_EventScript_SetBarriersAltState
	releaseall
	end

MauvilleCity_Gym_EventScript_SwitchDoNothing::
	releaseall
	end

MauvilleCity_Gym_EventScript_SetBarriersAltState::
	setflag FLAG_MAUVILLE_GYM_BARRIERS_STATE
	releaseall
	end

MauvilleCity_Gym_EventScript_ClearBarriersAltState::
	clearflag FLAG_MAUVILLE_GYM_BARRIERS_STATE
	releaseall
	end

MauvilleCity_Gym_EventScript_Kirk::
	trainerbattle_single TRAINER_KIRK, MauvilleCity_Gym_Text_KirkIntro, MauvilleCity_Gym_Text_KirkDefeat
	msgbox MauvilleCity_Gym_Text_KirkPostBattle, MSGBOX_AUTOCLOSE
	end

MauvilleCity_Gym_EventScript_Shawn::
	trainerbattle_single TRAINER_SHAWN, MauvilleCity_Gym_Text_ShawnIntro, MauvilleCity_Gym_Text_ShawnDefeat
	msgbox MauvilleCity_Gym_Text_ShawnPostBattle, MSGBOX_AUTOCLOSE
	end

MauvilleCity_Gym_EventScript_Ben::
	trainerbattle_single TRAINER_BEN, MauvilleCity_Gym_Text_BenIntro, MauvilleCity_Gym_Text_BenDefeat
	msgbox MauvilleCity_Gym_Text_BenPostBattle, MSGBOX_AUTOCLOSE
	end

MauvilleCity_Gym_EventScript_Vivian::
	trainerbattle_single TRAINER_VIVIAN, MauvilleCity_Gym_Text_VivianIntro, MauvilleCity_Gym_Text_VivianDefeat
	msgbox MauvilleCity_Gym_Text_VivianPostBattle, MSGBOX_AUTOCLOSE
	end

MauvilleCity_Gym_EventScript_Angelo::
	trainerbattle_single TRAINER_ANGELO, MauvilleCity_Gym_Text_AngeloIntro, MauvilleCity_Gym_Text_AngeloDefeat
	msgbox MauvilleCity_Gym_Text_AngeloPostBattle, MSGBOX_AUTOCLOSE
	end

MauvilleCity_Gym_EventScript_GymGuide::
	lock
	faceplayer
	goto_if_set FLAG_DEFEATED_MAUVILLE_GYM, MauvilleCity_Gym_EventScript_GymGuidePostVictory
	goto_if_eq VAR_LA_MAUVILLE_RIFT, 0, MauvilleRift_Guide
	goto_if_eq VAR_LA_MAUVILLE_RIFT, 1, MauvilleRift_Wally
	msgbox MauvilleCity_Gym_Text_GymGuideAdvice, MSGBOX_DEFAULT
	release
	end

MauvilleCity_Gym_EventScript_GymGuidePostVictory::
	msgbox MauvilleCity_Gym_Text_GymGuidePostVictory, MSGBOX_DEFAULT
	release
	end

MauvilleCity_Gym_EventScript_LeftGymStatue::
	lockall
	goto_if_set FLAG_BADGE03_GET, MauvilleCity_Gym_EventScript_GymStatueCertified
	goto MauvilleCity_Gym_EventScript_GymStatue
	end

MauvilleCity_Gym_EventScript_RightGymStatue::
	lockall
	goto_if_set FLAG_BADGE03_GET, MauvilleCity_Gym_EventScript_GymStatueCertified
	goto MauvilleCity_Gym_EventScript_GymStatue
	end

MauvilleCity_Gym_EventScript_GymStatueCertified::
	msgbox MauvilleCity_Gym_Text_GymStatueCertified, MSGBOX_DEFAULT
	releaseall
	end

MauvilleCity_Gym_EventScript_GymStatue::
	msgbox MauvilleCity_Gym_Text_GymStatue, MSGBOX_DEFAULT
	releaseall
	end

MauvilleCity_Gym_Text_GymGuideAdvice:
	.string "Hey, how's it going, CHAMPION-\n"
	.string "bound {PLAYER}?\p"
	.string "WATTSON, the LEADER of MAUVILLE\n"
	.string "GYM, uses ELECTRIC-type POKéMON.\p"
	.string "If you challenge him with WATER-type\n"
	.string "POKéMON, he'll zap them! Bzzt!\p"
	.string "And, he's put in switch-controlled\n"
	.string "doors all over his GYM! Eccentric!\p"
	.string "Hey, go for it!$"

MauvilleCity_Gym_Text_GymGuidePostVictory:
	.string "Whoa, you're electrifying!\n"
	.string "You've powered the door open!$"

MauvilleCity_Gym_Text_KirkIntro:
	.string "My electric soul, it'll shatter your\n"
	.string "dreams whole, whoa-yeahah!$"

MauvilleCity_Gym_Text_KirkDefeat:
	.string "That was plugged in, amped up,\n"
	.string "over-driven electric, man!$"

MauvilleCity_Gym_Text_KirkPostBattle:
	.string "POKéMON and rock, it's all about heart,\n"
	.string "whoa-yeah!$"

MauvilleCity_Gym_Text_ShawnIntro:
	.string "I trained under WATTSON!\n"
	.string "There ain't no way I'll lose easily!$"

MauvilleCity_Gym_Text_ShawnDefeat:
	.string "Unplugged and turned off…$"

MauvilleCity_Gym_Text_ShawnPostBattle:
	.string "WATTSON, our GYM LEADER, has been\n"
	.string "around for a long, long time.\p"
	.string "He was battling even before your\n"
	.string "daddy was born, that tough coot.$"

MauvilleCity_Gym_Text_BenIntro:
	.string "This GYM's got puzzles!\n"
	.string "Isn't it fun?$"

MauvilleCity_Gym_Text_BenDefeat:
	.string "It's no fun to lose…$"

MauvilleCity_Gym_Text_BenPostBattle:
	.string "WATTSON says he likes setting up\n"
	.string "little traps with switches.$"

MauvilleCity_Gym_Text_VivianIntro:
	.string "With my charm and my POKéMON's moves,\n"
	.string "you'll be shocked!$"

MauvilleCity_Gym_Text_VivianDefeat:
	.string "I'm shocked by your power!$"

MauvilleCity_Gym_Text_VivianPostBattle:
	.string "I've heard that MAUVILLE was founded\n"
	.string "by WATTSON.\p"
	.string "He was a TRAINER long before we\n"
	.string "became TRAINERS.\l"
	.string "He must know all sorts of things!$"

MauvilleCity_Gym_Text_AngeloIntro:
	.string "I love shiny things!$"

MauvilleCity_Gym_Text_AngeloDefeat:
	.string "Oh…\n"
	.string "My eyes are frazzled…$"

MauvilleCity_Gym_Text_AngeloPostBattle:
	.string "MAUVILLE GYM's WATTSON has a shiny\n"
	.string "forehead. It makes me happy!$"

MauvilleCity_Gym_Text_WattsonIntro:
	.string "Show me what you and your partners\ncan do, {PLAYER}!$"

MauvilleCity_Gym_Text_WattsonDefeat:
	.string "Wahahahah!\n"
	.string "Fine, I lost!\p"
	.string "You ended up giving me a thrill!\n"
	.string "Take this BADGE!$"

MauvilleCity_Gym_Text_ReceivedDynamoBadge:
	.string "{PLAYER} received the DYNAMO BADGE\n"
	.string "from WATTSON.$"

MauvilleCity_Gym_Text_ExplainDynamoBadgeTakeThis:
	.string "With the DYNAMO BADGE, POKéMON can\n"
	.string "use ROCK SMASH out of battle.\p"
	.string "And, it will make your POKéMON a little\n"
	.string "bit faster, too.\p"
	.string "Hmm…\n"
	.string "You should take this, too!$"

MauvilleCity_Gym_Text_ExplainShockWave:
	.string "That TM34 there contains SHOCK WAVE.\p"
	.string "It's a trustworthy move that never\n"
	.string "misses! You can count on it!\p"
	.string "… … … … … …$"

MauvilleCity_Gym_Text_RegisteredWattson:
	.string "Registered GYM LEADER WATTSON\n"
	.string "in the POKéNAV.$"

MauvilleCity_Gym_Text_WattsonPostBattle:
	.string "I'll keep watching the power lines.\nKeep your PokéNav close, {PLAYER}.$"

MauvilleCity_Gym_Text_WattsonGoForthAndEndeavor:
	.string "Wahahahah!\n"
	.string "Go forth and endeavor, youngster!$"

MauvilleCity_Gym_Text_GymStatue:
	.string "MAUVILLE CITY POKéMON GYM$"

MauvilleCity_Gym_Text_GymStatueCertified:
	.string "MAUVILLE CITY POKéMON GYM\p"
	.string "WATTSON'S CERTIFIED TRAINERS:\n"
	.string "{PLAYER}$"

MauvilleCity_Gym_Text_WattsonPreRematch:
	.string "WATTSON: Ah-ha! Here at last!\n"
	.string "I know what you want.\l"
	.string "You want to battle my POKéMON!\p"
	.string "Wahahahaha!\p"
	.string "I'll make sparks fly from you!\n"
	.string "Don't say I didn't warn you!$"

MauvilleCity_Gym_Text_WattsonRematchDefeat:
	.string "Oof…\n"
	.string "Our batteries ran dry…$"

MauvilleCity_Gym_Text_WattsonPostRematch:
	.string "WATTSON: We'll have to recharge our\n"
	.string "batteries again.\p"
	.string "When we're fully charged up, we'll\n"
	.string "gladly accept your challenge.\p"
	.string "So, come back again sometime,\n"
	.string "won't you?$"

MauvilleCity_Gym_Text_WattsonRematchNeedTwoMons:
	.string "WATTSON: Ah-ha! Here at last!\n"
	.string "I know what you want.\l"
	.string "You want to battle my POKéMON!\p"
	.string "Wahahahaha!\p"
	.string "Oops! Wait!\n"
	.string "You've only one POKéMON with you!\p"
	.string "Come see me with two or more\n"
	.string "POKéMON, all right?$"


MauvilleRift_GymTransition::
	setflag FLAG_TEMP_1
	setflag FLAG_TEMP_2
	setflag FLAG_TEMP_3
	setvar VAR_TEMP_4, 0
	setvar VAR_TEMP_6, 0
	call_if_set FLAG_BADGE03_GET, RiftResearch_QueueExistingSave
	goto_if_set FLAG_DEFEATED_MAUVILLE_GYM, MauvilleRift_TransitionDone
	goto_if_eq VAR_LA_MAUVILLE_RIFT, 3, MauvilleRift_ShowWattson
	setflag FLAG_HIDE_MAUVILLE_GYM_WATTSON
	call_if_eq VAR_LA_MAUVILLE_RIFT, 0, MauvilleRift_QueueEntrance
	goto_if_ne VAR_LA_MAUVILLE_RIFT, 1, MauvilleRift_TransitionDone
	clearflag FLAG_TEMP_1
	clearflag FLAG_TEMP_2
MauvilleRift_TransitionDone::
	end

MauvilleRift_QueueEntrance::
	goto_if_unset FLAG_DEFEATED_WALLY_MAUVILLE, MauvilleRift_QueueEntranceDone
	setvar VAR_TEMP_4, 1
MauvilleRift_QueueEntranceDone::
	return

MauvilleRift_ShowWattson::
	clearflag FLAG_HIDE_MAUVILLE_GYM_WATTSON
	end

MauvilleRift_GymFrame:
	map_script_2 VAR_TEMP_6, 1, RiftResearch_InviteExistingSave
	map_script_2 VAR_LA_MAUVILLE_RIFT, 2, MauvilleRift_AfterReturn
	map_script_2 VAR_TEMP_4, 1, MauvilleRift_AutoEntrance
	.2byte 0

MauvilleRift_AutoEntrance::
	lockall
	setvar VAR_TEMP_4, 0
	turnobject LOCALID_PLAYER, DIR_EAST
	msgbox MauvilleRift_Text_Guide, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_PLAYER, MauvilleRift_Movement_PlayerApproach
	waitmovement 0
	goto MauvilleRift_Open

MauvilleRift_Movement_PlayerApproach:
	walk_up
	walk_up
	step_end

MauvilleRift_Guide::
	goto_if_unset FLAG_DEFEATED_WALLY_MAUVILLE, MauvilleRift_WaitForWally
	msgbox MauvilleRift_Text_Guide, MSGBOX_DEFAULT
	closemessage
MauvilleRift_Open::
	turnobject LOCALID_PLAYER, DIR_NORTH
	clearflag FLAG_TEMP_2
	addobject LOCALID_MAUVILLE_RIFT_WALLY
	addobject LOCALID_MAUVILLE_RIFT_KIRLIA
	playmoncry SPECIES_KIRLIA, CRY_MODE_NORMAL
	setspeaker SP_NAME_WALLY
	msgbox MauvilleRift_Text_KirliaFoundIt, MSGBOX_DEFAULT
	closemessage
	playse SE_THUNDER
	clearflag FLAG_TEMP_1
	addobject LOCALID_MAUVILLE_RIFT_GATE
	setspeaker SP_NAME_PLAYER
	msgbox MauvilleRift_Text_PlayerConnectsSurge, MSGBOX_DEFAULT
	setvar VAR_LA_MAUVILLE_RIFT, 1
	goto MauvilleRift_End

MauvilleRift_WaitForWally::
	msgbox MauvilleRift_Text_WaitForWally, MSGBOX_DEFAULT
	goto MauvilleRift_End

MauvilleRift_Wally::
	lockall
	setspeaker SP_NAME_WALLY
	msgbox MauvilleRift_Text_KirliaFoundIt, MSGBOX_DEFAULT
	goto MauvilleRift_End

MauvilleRift_Enter::
	lockall
	msgbox MauvilleRift_Text_Enter, MSGBOX_YESNO
	goto_if_ne VAR_RESULT, YES, MauvilleRift_End
	closemessage
	applymovement LOCALID_MAUVILLE_RIFT_KIRLIA, MauvilleRift_Movement_KirliaEnter
	waitmovement 0
	removeobject LOCALID_MAUVILLE_RIFT_KIRLIA
	applymovement LOCALID_MAUVILLE_RIFT_WALLY, MauvilleRift_Movement_WallyEnter
	waitmovement 0
	removeobject LOCALID_MAUVILLE_RIFT_WALLY
	warp MAP_KANTOAR_3_28_ROUTE10, 9, 44
	waitstate
	end

MauvilleRift_Movement_KirliaEnter:
	walk_left
	walk_left
	step_end

MauvilleRift_Movement_WallyEnter:
	walk_up
	walk_left
	walk_left
	walk_left
	step_end

MauvilleRift_AfterReturn::
	lockall
	setflag FLAG_TEMP_2
	clearflag FLAG_TEMP_3
	addobject LOCALID_MAUVILLE_RIFT_WATTSON
	setobjectxy LOCALID_MAUVILLE_RIFT_WATTSON, 4, 19
	setspeaker SP_NAME_PLAYER
	msgbox MauvilleRift_Text_WallyMissing, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	msgbox MauvilleRift_Text_WattsonMissing, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox MauvilleRift_Text_CallBirch, MSGBOX_DEFAULT
	closemessage
	playse SE_POKENAV_CALL
	delay 30
	setspeaker SP_NAME_BIRCH
	msgbox MauvilleRift_Text_BirchReport, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox MauvilleRift_Text_ReportMissing, MSGBOX_DEFAULT
	setspeaker SP_NAME_BIRCH
	msgbox MauvilleRift_Text_BirchConnects, MSGBOX_DEFAULT
	setspeaker SP_NAME_ROWAN
	msgbox MauvilleRift_Text_RowanQuestion, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox MauvilleRift_Text_ReportMiraidon, MSGBOX_DEFAULT
	@ Burnet is unfamiliar to the player. Keep her name and portrait hidden.
	setspeaker SP_NAME_NONE
	msgbox MauvilleRift_Text_BurnetRift, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox MauvilleRift_Text_KirliaReport, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	msgbox MauvilleRift_Text_WattsonEvidence, MSGBOX_DEFAULT
	@ The remaining Paradigm members are unfamiliar voices.
	setspeaker SP_NAME_NONE
	msgbox MauvilleRift_Text_ElmKirlia, MSGBOX_DEFAULT
	msgbox MauvilleRift_Text_JuniperReadings, MSGBOX_DEFAULT
	msgbox MauvilleRift_Text_SycamoreDetails, MSGBOX_DEFAULT
	msgbox MauvilleRift_Text_KukuiHelp, MSGBOX_DEFAULT
	msgbox MauvilleRift_Text_OakSearch, MSGBOX_DEFAULT
	setspeaker SP_NAME_BIRCH
	msgbox MauvilleRift_Text_BirchSearch, MSGBOX_DEFAULT
	closemessage
	playse SE_POKENAV_HANG_UP
	delay 20
	turnobject LOCALID_PLAYER, DIR_WEST
	setspeaker SP_NAME_NONE
	msgbox MauvilleRift_Text_WattsonClue, MSGBOX_DEFAULT
	closemessage
	turnobject LOCALID_PLAYER, DIR_NORTH
	applymovement LOCALID_MAUVILLE_RIFT_WATTSON, MauvilleRift_Movement_WattsonNorth
	waitmovement 0
	removeobject LOCALID_MAUVILLE_RIFT_WATTSON
	setflag FLAG_TEMP_3
	setflag FLAG_HIDE_VERDANTURF_TOWN_WANDAS_HOUSE_WALLY
	clearflag FLAG_ENABLE_FIRST_WALLY_POKENAV_CALL
	clearflag FLAG_HIDE_MAUVILLE_GYM_WATTSON
	addobject LOCALID_MAUVILLE_GYM_WATTSON
	setvar VAR_LA_MAUVILLE_RIFT, 3
	goto MauvilleRift_End

MauvilleRift_End::
	closemessage
	setspeaker SP_NAME_NONE
	releaseall
	end

MauvilleRift_Text_Guide:
	.string "Wattson went to check a surge by\nthe maintenance door.\pThe lights haven't stopped\nflickering since he left.$"
MauvilleRift_Text_WaitForWally:
	.string "Wattson's checking a power surge.\pYour friend Wally is waiting just\noutside if you're looking for him.$"
MauvilleRift_Text_KirliaFoundIt:
	.string "Kirlia, is that where the sound\nwas coming from?$"
MauvilleRift_Text_PlayerConnectsSurge:
	.string "The lights are pulsing with it.\nIs this what Rowan picked up?$"
MauvilleRift_Text_Enter:
	.string "Step through the rift with\nWally and Kirlia?$"
MauvilleRift_Text_WallyMissing:
	.string "Wally? Kirlia?\pThey went through right ahead of\nus. Where did they go?$"
MauvilleRift_Text_WattsonMissing:
	.string "Wattson: Stay back. The opening\nhas closed.\pI saw them enter too. They should\nhave come out here with us.$"
MauvilleRift_Text_ReportMissing:
	.string "We're back in Mauville Gym.\nBut Wally and Kirlia are missing.\pThey entered the rift together,\nright ahead of us.\pWattson and I followed them.\nThey never came out here.$"
MauvilleRift_Text_BirchSearch:
	.string "We'll check the readings and\nlet Wally's family know.\pKeep your PokéNav close, {PLAYER}.\nWe'll call as soon as we know more.\pIf Wally contacts you, tell us\nwhere he is immediately.$"
MauvilleRift_Text_BirchReport:
	.string "{PLAYER}? Birch speaking.\nAre you with Wattson?$"
MauvilleRift_Text_WattsonClue:
	.string "Wattson: I'll send those readings\nfrom the control desk.\pCome find me when you're ready.\nWe'll work out what to do next.$"

MauvilleRift_Text_CallBirch:
	.string "Birch needs to know they're missing.\nI'm calling him now.$"

MauvilleRift_Text_RowanQuestion:
	.string "It's Rowan, {PLAYER}. Where did\nyou find yourselves?$"

MauvilleRift_Text_ReportMiraidon:
	.string "Route 10, near Kanto's Power Plant.\nWattson was holding a relay inside.\pThe reactor was running with\nits main breaker switched off.\pWhen I shut it down, a huge\nviolet Pokémon approached us.\pMy Pokédex identified Miraidon.\nElectricity covered its body.\pI tried to hold it off, but my\nteam didn't stand a chance.$"

MauvilleRift_Text_BurnetRift:
	.string "A voice on the call:\nDid Kirlia sense a change?$"

MauvilleRift_Text_WattsonEvidence:
	.string "Wattson: They went through together.\nWe followed seconds later.\pOnly {PLAYER} and I came out here.\nThen the opening closed.$"

MauvilleRift_Text_OakSearch:
	.string "Another voice:\nWe'll trace both ends together.\pWe should contact the Trainers\nwe've worked with as well.\pTheir friends and rivals can\nhelp search across the regions.$"

MauvilleRift_Text_ElmKirlia:
	.string "Another voice:\nThen those two may still be together.$"

MauvilleRift_Text_JuniperReadings:
	.string "A voice on the call:\nSend us the times and readings.\pWe'll check for a matching surge\nin our own regions.$"

MauvilleRift_Text_SycamoreDetails:
	.string "Another voice:\nKeep the details about Miraidon.\pIts reaction to the reactor\nmay help explain the disturbance.$"

MauvilleRift_Text_KukuiHelp:
	.string "A voice on the call:\nYou got yourself and Wattson home.\pTake a breath. We'll help you\nfind your friend.$"

MauvilleRift_WattsonExplains::
	lock
	faceplayer
	setspeaker SP_NAME_PLAYER
	msgbox MauvilleRift_Text_AskWattson, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	msgbox MauvilleRift_Text_WattsonAccount, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox MauvilleRift_Text_PlayerResolve, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	msgbox MauvilleRift_Text_WattsonChallenge, MSGBOX_DEFAULT
	closemessage
	setvar VAR_LA_PARADIGM_ARC, 1
	return

MauvilleRift_Text_AskWattson:
	.string "Before we battle… How did you\nend up at that Power Plant?$"
MauvilleRift_Text_WattsonAccount:
	.string "Wattson: I traced a surge to the\nmaintenance room behind the Gym.\pThe air split open. Beyond it\nwas a place I didn't recognize.\pI stepped through to investigate.\nThe hum led me into that plant.\pIts reactor was running with\nthe main breaker switched off.\pBy the time I found the way back,\nthe opening was shrinking.\pThat's when you and Wally arrived.\nI wish I'd kept him closer.$"
MauvilleRift_Text_PlayerResolve:
	.string "He chose to help us. So did Kirlia.\pWe'll find them. I need to be\nready for whatever's out there.$"
MauvilleRift_Text_WattsonChallenge:
	.string "Wattson: Then let's see how you\nand your partners work together.\pTake your time, clear your head,\nand give me your best battle.$"

MauvilleRift_Text_BirchConnects:
	.string "Stay with Wattson. Rowan and I\nare on a call with six colleagues.\pWe're The Paradigm Society.\nParadigm, for short.\pI'm putting you on with everyone.\nTell us where the rift took you.$"

MauvilleRift_Text_KirliaReport:
	.string "Wally said she felt something\nbefore Miraidon appeared.\pShe was still beside him when\nthey stepped through the rift.$"

MauvilleRift_Movement_WattsonNorth:
	walk_up
	walk_up
	walk_up
	walk_up
	walk_left
	walk_left
	walk_up
	walk_up
	walk_up
	step_end
