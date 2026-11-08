@ Legends Awakening: A Strange Delivery. Expansion owns all story state.
LegendsBedroom_Initialize::
    setflag FLAG_LA_INTRO_ACTIVE
    setvar VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_WAKE_UP
    setflag FLAG_HIDE_LITTLEROOT_TOWN_MOM_OUTSIDE
    setflag FLAG_HIDE_LITTLEROOT_TOWN_BRENDANS_HOUSE_TRUCK
    setflag FLAG_HIDE_LITTLEROOT_TOWN_MAYS_HOUSE_TRUCK
    setflag FLAG_HIDE_LITTLEROOT_TOWN_PLAYERS_HOUSE_VIGOROTH_1
    setflag FLAG_HIDE_LITTLEROOT_TOWN_PLAYERS_HOUSE_VIGOROTH_2
    setflag FLAG_HIDE_LITTLEROOT_TOWN_PLAYERS_BEDROOM_MOM
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsBedroom_InitializeFemale
    setrespawn HEAL_LOCATION_LITTLEROOT_TOWN_BRENDANS_HOUSE_2F
    setflag FLAG_HIDE_LITTLEROOT_TOWN_MAYS_HOUSE_MOM
    setflag FLAG_HIDE_LITTLEROOT_TOWN_BRENDANS_HOUSE_RIVAL_MOM
    setflag FLAG_HIDE_LITTLEROOT_TOWN_BRENDANS_HOUSE_RIVAL_SIBLING
    setflag FLAG_HIDE_LITTLEROOT_TOWN_BRENDANS_HOUSE_2F_POKE_BALL
    setvar VAR_LITTLEROOT_HOUSES_STATE_BRENDAN, 1
    end

LegendsBedroom_InitializeFemale:
    setrespawn HEAL_LOCATION_LITTLEROOT_TOWN_MAYS_HOUSE_2F
    setflag FLAG_HIDE_LITTLEROOT_TOWN_BRENDANS_HOUSE_MOM
    setflag FLAG_HIDE_LITTLEROOT_TOWN_MAYS_HOUSE_RIVAL_MOM
    setflag FLAG_HIDE_LITTLEROOT_TOWN_MAYS_HOUSE_RIVAL_SIBLING
    setflag FLAG_HIDE_LITTLEROOT_TOWN_MAYS_HOUSE_2F_POKE_BALL
    setvar VAR_LITTLEROOT_HOUSES_STATE_MAY, 1
    end

LegendsBedroom_OnTransition::
    @ No coordinate/tileset edits: the existing Hyper rooms stay authoritative.
    goto_if_ne VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_WAKE_UP, LegendsBedroom_Return
    setflag FLAG_HIDE_LITTLEROOT_TOWN_PLAYERS_BEDROOM_MOM
    return

LegendsBedroom_Return:
    return

LegendsBedroom_OnFrame:
    map_script_2 VAR_TEMP_3, 2, LegendsNextDoor_RoomToPC
    map_script_2 VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_WAKE_UP, LegendsBedroom_Wake
    map_script_2 VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_PACKAGE, LegendsBedroom_Package
    .2byte 0

LegendsBedroom_Wake::
    lockall
    fadeoutbgm 1
    applymovement LOCALID_PLAYER, LegendsBedroom_Hide
    waitmovement 0
    delay 45
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_Dream, MSGBOX_DEFAULT
    closemessage
    delay 30
    playse SE_M_THUNDERBOLT
    fadescreenswapbuffers FADE_TO_WHITE
    applymovement LOCALID_PLAYER, LegendsBedroom_Show
    waitmovement 0
    fadescreenswapbuffers FADE_FROM_WHITE
    fadescreen FADE_FROM_BLACK
    delay 45
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_Wake, MSGBOX_DEFAULT
    closemessage
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsBedroom_GetUpFemale
    applymovement LOCALID_PLAYER, LegendsBedroom_GetUpMale
    waitmovement 0
    goto LegendsBedroom_Chime

LegendsBedroom_GetUpFemale:
    applymovement LOCALID_PLAYER, LegendsBedroom_GetUpFemaleMovement
    waitmovement 0

LegendsBedroom_Chime:
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsBedroom_NotificationFemale
    setvar VAR_0x8004, PC_LOCATION_BRENDANS_HOUSE
    goto LegendsBedroom_NotificationOn
LegendsBedroom_NotificationFemale:
    setvar VAR_0x8004, PC_LOCATION_MAYS_HOUSE
LegendsBedroom_NotificationOn:
    special DoPCTurnOnEffect
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_DreamAftermath, MSGBOX_DEFAULT
    closemessage
    delay 25
    playse SE_PC_ON
    waitse
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_Huh, MSGBOX_DEFAULT
    closemessage
    delay 15
    playse SE_PC_ON
    waitse
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_CheckPC, MSGBOX_DEFAULT
    closemessage
    setspeaker SP_NAME_NONE
    setvar VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_CHECK_PC
    fadedefaultbgm
    releaseall
    end

LegendsBedroom_ReadDelivery::
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsBedroom_PCIsFemale
    setvar VAR_0x8004, PC_LOCATION_BRENDANS_HOUSE
    goto LegendsBedroom_PCOn
LegendsBedroom_PCIsFemale:
    setvar VAR_0x8004, PC_LOCATION_MAYS_HOUSE
LegendsBedroom_PCOn:
    special DoPCTurnOnEffect
    playse SE_PC_ON
    setspeaker SP_NAME_NONE
    msgbox LegendsBedroom_Text_Delivery, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_OrderReaction, MSGBOX_DEFAULT
    closemessage
    playse SE_PC_OFF
    special DoPCTurnOffEffect
    setflag FLAG_LA_PC_DELIVERY_MESSAGE_READ
    setvar VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_SET_CLOCK
    setspeaker SP_NAME_NONE
    releaseall
    end

LegendsBedroom_BlockStairs::
    lockall
    setspeaker SP_NAME_PLAYER
    goto_if_set FLAG_LA_PC_DELIVERY_MESSAGE_READ, LegendsBedroom_ClockFirst
    msgbox LegendsBedroom_Text_PCFirst, MSGBOX_DEFAULT
    goto LegendsBedroom_PushFromStairs
LegendsBedroom_ClockFirst:
    msgbox LegendsBedroom_Text_ClockFirst, MSGBOX_DEFAULT
LegendsBedroom_PushFromStairs:
    closemessage
    applymovement LOCALID_PLAYER, LegendsBedroom_StepAway
    waitmovement 0
    setspeaker SP_NAME_NONE
    releaseall
    end

LegendsBedroom_ClockBeforePC::
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_PCFirst, MSGBOX_DEFAULT
    setspeaker SP_NAME_NONE
    releaseall
    end

LegendsBedroom_SetClock::
    setspeaker SP_NAME_PLAYER
    msgbox PlayersHouse_2F_Text_ClockIsStopped, MSGBOX_DEFAULT
    closemessage
    setspeaker SP_NAME_NONE
    call PlayersHouse_2F_EventScript_SetWallClock
    setflag FLAG_SET_WALL_CLOCK
    setvar VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_PACKAGE
    goto LegendsBedroom_Package

LegendsBedroom_Package::
    lockall
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_ClockDone, MSGBOX_DEFAULT
    closemessage
    delay 25
    playse SE_EXIT
    setvar VAR_0x8008, LOCALID_PLAYERS_HOUSE_2F_MOM
    clearflag FLAG_HIDE_LITTLEROOT_TOWN_PLAYERS_BEDROOM_MOM
    addobject LOCALID_PLAYERS_HOUSE_2F_MOM
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsBedroom_ElaraEnterFemale
    applymovement LOCALID_PLAYERS_HOUSE_2F_MOM, PlayersHouse_2F_Movement_MomEntersMale
    waitmovement 0
    applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterRight
    waitmovement 0
    goto LegendsBedroom_Conversation
LegendsBedroom_ElaraEnterFemale:
    applymovement LOCALID_PLAYERS_HOUSE_2F_MOM, PlayersHouse_2F_Movement_MomEntersFemale
    waitmovement 0
    applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterLeft
    waitmovement 0

LegendsBedroom_Conversation:
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_Talk0, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_Talk1, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_Talk2, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_Talk3, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_Talk4, MSGBOX_DEFAULT
    closemessage
    delay 20
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_Talk5, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_Talk6, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_Talk7, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_Talk8, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_Talk9, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_Talk10, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_Talk11, MSGBOX_DEFAULT
    closemessage
    delay 20
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_Talk12, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_Talk13, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_Talk14, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_Talk15, MSGBOX_DEFAULT
    closemessage
    delay 20
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_Talk16, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_Talk17, MSGBOX_DEFAULT
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_RECEIVED_TERA_ORB, LegendsBedroom_AfterItem
    checkitem ITEM_TERA_ORB
    goto_if_eq VAR_RESULT, TRUE, LegendsBedroom_ItemAlreadyPresent
    giveitem ITEM_TERA_ORB
    goto_if_eq VAR_RESULT, FALSE, LegendsBedroom_ItemFull
LegendsBedroom_ItemAlreadyPresent:
    setflag FLAG_LA_RECEIVED_TERA_ORB
    setvar VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_TERA_ORB_RECEIVED
LegendsBedroom_AfterItem:
    setflag FLAG_LA_TERA_ORB_ACTIVATED
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_After0, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_After1, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_After2, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_After3, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_After4, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_After5, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_After6, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsBedroom_Text_After7, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_After8, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsBedroom_Text_After9, MSGBOX_DEFAULT
    closemessage
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsBedroom_ElaraExitFemale
    applymovement LOCALID_PLAYERS_HOUSE_2F_MOM, PlayersHouse_2F_Movement_MomExitsMale
    waitmovement 0
    goto LegendsBedroom_Finish
LegendsBedroom_ElaraExitFemale:
    applymovement LOCALID_PLAYERS_HOUSE_2F_MOM, PlayersHouse_2F_Movement_MomExitsFemale
    waitmovement 0
LegendsBedroom_Finish:
    playse SE_EXIT
    removeobject LOCALID_PLAYERS_HOUSE_2F_MOM
    setflag FLAG_HIDE_LITTLEROOT_TOWN_PLAYERS_BEDROOM_MOM
    setflag FLAG_LA_ELARA_PACKAGE_SCENE_COMPLETE
    setvar VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_COMPLETE
    setspeaker SP_NAME_NONE
    releaseall
    end

LegendsBedroom_ItemFull:
    @ Retry through the room on-frame hook; never mark an unsuccessful gift received.
    msgbox LegendsBedroom_Text_BagFull, MSGBOX_DEFAULT
    removeobject LOCALID_PLAYERS_HOUSE_2F_MOM
    setflag FLAG_HIDE_LITTLEROOT_TOWN_PLAYERS_BEDROOM_MOM
    setspeaker SP_NAME_NONE
    releaseall
    end

LegendsBedroom_Hide:
    set_invisible
    step_end
LegendsBedroom_Show:
    set_visible
    face_down
    step_end
LegendsBedroom_GetUpMale:
    walk_down
    walk_right
    face_up
    step_end
LegendsBedroom_GetUpFemaleMovement:
    walk_down
    walk_left
    face_up
    step_end
LegendsBedroom_StepAway:
    walk_down
    step_end

LegendsBedroom_Text_Dream:
    .string "{COLOR LIGHT_BLUE}No...\nDon't send me away...\pPlease...\pNo!$"

LegendsBedroom_Text_Wake:
    .string "{COLOR LIGHT_BLUE}...!$"

LegendsBedroom_Text_DreamAftermath:
    .string "{COLOR LIGHT_BLUE}That dream again...\p“Don't send me away...”\pWhy would I say that?\pI can barely remember any of it.$"

LegendsBedroom_Text_Huh:
    .string "{COLOR LIGHT_BLUE}Huh?$"

LegendsBedroom_Text_CheckPC:
    .string "{COLOR LIGHT_BLUE}That's my PC.\nI should check it.$"

LegendsBedroom_Text_Delivery:
    .string "DELIVERY NOTICE\pYour order has been processed.\pDelivery is scheduled to arrive\nshortly.\pThank you for your purchase.$"

LegendsBedroom_Text_OrderReaction:
    .string "{COLOR LIGHT_BLUE}My order?\pI didn't order anything.\pThat's weird...\pAnd the clock still isn't set.\pI should probably fix that before I go\ndownstairs.$"

LegendsBedroom_Text_PCFirst:
    .string "{COLOR LIGHT_BLUE}I should check the PC first.$"

LegendsBedroom_Text_ClockFirst:
    .string "{COLOR LIGHT_BLUE}Clock first.\pElara will definitely say something if I\nleave it like that.$"

LegendsBedroom_Text_ClockDone:
    .string "{COLOR LIGHT_BLUE}There.\nMuch better.\pNow the clock's set.$"

LegendsBedroom_Text_Talk0:
    .string "Hey, sleepyhead.\nFinally awake?$"

LegendsBedroom_Text_Talk1:
    .string "{COLOR LIGHT_BLUE}Barely.$"

LegendsBedroom_Text_Talk2:
    .string "You okay?$"

LegendsBedroom_Text_Talk3:
    .string "{COLOR LIGHT_BLUE}Yeah.\nJust had a weird dream.$"

LegendsBedroom_Text_Talk4:
    .string "Bad one?$"

LegendsBedroom_Text_Talk5:
    .string "{COLOR LIGHT_BLUE}I think so.\nI can't really remember it.$"

LegendsBedroom_Text_Talk6:
    .string "Probably for the best.$"

LegendsBedroom_Text_Talk7:
    .string "Actually...\nA package just arrived for you.$"

LegendsBedroom_Text_Talk8:
    .string "{COLOR LIGHT_BLUE}For me?$"

LegendsBedroom_Text_Talk9:
    .string "That's what it says.\nYour name and everything.$"

LegendsBedroom_Text_Talk10:
    .string "When did you order something?$"

LegendsBedroom_Text_Talk11:
    .string "{COLOR LIGHT_BLUE}I didn't.$"

LegendsBedroom_Text_Talk12:
    .string "...\nThat's strange.$"

LegendsBedroom_Text_Talk13:
    .string "{COLOR LIGHT_BLUE}My PC said an order was arriving too.$"

LegendsBedroom_Text_Talk14:
    .string "Your PC knew about it?$"

LegendsBedroom_Text_Talk15:
    .string "{COLOR LIGHT_BLUE}Apparently.$"

LegendsBedroom_Text_Talk16:
    .string "Well...\nit's addressed to you.$"

LegendsBedroom_Text_Talk17:
    .string "Let's at least see what's inside.$"

LegendsBedroom_Text_After0:
    .string "{COLOR LIGHT_BLUE}A Tera Orb...?$"

LegendsBedroom_Text_After1:
    .string "That's definitely not something I'd\nexpect to arrive in the mail.$"

LegendsBedroom_Text_After2:
    .string "{COLOR LIGHT_BLUE}You know what it is?$"

LegendsBedroom_Text_After3:
    .string "I've heard of them.\nThey're used by Trainers in other\lregions.$"

LegendsBedroom_Text_After4:
    .string "But why someone sent one to you...\nI have no idea.$"

LegendsBedroom_Text_After5:
    .string "Keep it with you for now.$"

LegendsBedroom_Text_After6:
    .string "Just don't start pressing buttons\nuntil we know where it came from.$"

LegendsBedroom_Text_After7:
    .string "{COLOR LIGHT_BLUE}That's oddly specific.$"

LegendsBedroom_Text_After8:
    .string "I'm your mother.\nBeing oddly specific is part of the job.$"

LegendsBedroom_Text_After9:
    .string "Come downstairs when you're ready.\nThere's something else I need to tell\lyou.$"

LegendsBedroom_Text_BagFull:
    .string "Make room for the package first.$"
