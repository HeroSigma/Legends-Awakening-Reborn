
@ Ashes and Echoes: shared villain research, then Hoopa's controlled past crossing.
LegendsAshes_End::
    closemessage
    setspeaker SP_NAME_NONE
    releaseall
    end
LegendsAshes_Return::
    return

LegendsAshes_WoodsDeparture::
    lockall
    goto_if_set FLAG_LA_ASHES_WOODS_DEPARTURE, LegendsAshes_End
    goto_if_lt VAR_LA_RIFT_TRACKER, 2, LegendsAshes_End
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_Residual, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox Ashes_Text_North, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_MayPlan, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox Ashes_Text_MayLeave, MSGBOX_DEFAULT
    closemessage
    applymovement LOCALID_TIMELESS_PARADIGM_MAY, Ashes_MayDepartWoods
    waitmovement 0
    removeobject LOCALID_TIMELESS_PARADIGM_MAY
    setflag FLAG_TEMP_3
    setflag FLAG_LA_ASHES_WOODS_DEPARTURE
    setvar VAR_LA_ASHES_STATE, 1
    goto LegendsAshes_End
Ashes_MayDepartWoods:
    walk_left
    walk_left
    walk_down
    step_end

LegendsAshes_CozmoTransition::
    setvar VAR_TEMP_3, 1
    setflag FLAG_TEMP_2
    setflag FLAG_TEMP_4
    goto_if_eq VAR_LA_ASHES_STATE, 0, LegendsAshes_MapEnd
    goto_if_set FLAG_LA_COZMO_BRIEFED, LegendsAshes_MapEnd
    clearflag FLAG_HIDE_FALLARBOR_HOUSE_PROF_COZMO
    clearflag FLAG_TEMP_2
    setvar VAR_TEMP_3, 0
LegendsAshes_MapEnd::
    end
LegendsAshes_CozmoFrame:
    map_script_2 VAR_TEMP_3, 0, LegendsAshes_CozmoBriefing
    .2byte 0
LegendsAshes_CozmoBriefing::
    lockall
    setvar VAR_TEMP_3, 1
    applymovement LOCALID_PLAYER, Ashes_PlayerToTable
    waitmovement 0
    applymovement 1, Ashes_CozmoToTable
    waitmovement 0
    setspeaker SP_NAME_MAY
    msgbox Ashes_Text_MayCozmo, MSGBOX_DEFAULT
    setspeaker SP_NAME_COZMO
    msgbox Ashes_Text_Resonance, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_Echo, MSGBOX_DEFAULT
    setspeaker SP_NAME_COZMO
    msgbox Ashes_Text_Meteorite, MSGBOX_DEFAULT
    closemessage
    playse SE_DOOR
    clearflag FLAG_TEMP_4
    addobject LOCALID_ASHES_COZMO_TABITHA
    addobject LOCALID_ASHES_COZMO_GRUNT
    applymovement LOCALID_ASHES_COZMO_GRUNT, Ashes_UpOne
    waitmovement 0
    setspeaker SP_NAME_MAGMA_TABITHA
    msgbox Ashes_Text_TabithaTheft, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_BlockTheft, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox Ashes_Text_MayProtectCozmo, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 11
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, Ashes_Text_GruntDefeat
    setspeaker SP_NAME_MAGMA_TABITHA
    msgbox Ashes_Text_TabithaEscape, MSGBOX_DEFAULT
    closemessage
    applymovement LOCALID_ASHES_COZMO_GRUNT, Ashes_DownTwo
    waitmovement 0
    removeobject LOCALID_ASHES_COZMO_GRUNT
    applymovement LOCALID_ASHES_COZMO_TABITHA, Ashes_TabithaOut
    waitmovement 0
    removeobject LOCALID_ASHES_COZMO_TABITHA
    setflag FLAG_TEMP_4
    setflag FLAG_MET_PROF_COZMO
    setflag FLAG_LA_COZMO_BRIEFED
    setvar VAR_LA_ASHES_STATE, 2
    setspeaker SP_NAME_COZMO
    msgbox Ashes_Text_Calibration, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox Ashes_Text_MayPursue, MSGBOX_DEFAULT
    closemessage
    applymovement LOCALID_ASHES_COZMO_MAY, Ashes_MayOut
    waitmovement 0
    removeobject LOCALID_ASHES_COZMO_MAY
    setflag FLAG_TEMP_2
    applymovement 1, Ashes_CozmoOut
    waitmovement 0
    removeobject 1
    setflag FLAG_HIDE_FALLARBOR_HOUSE_PROF_COZMO
    goto LegendsAshes_End
Ashes_CozmoOut:
    walk_down
    walk_down
    walk_left
    walk_left
    walk_left
    walk_down
    step_end
Ashes_PlayerToTable:
    walk_up
    walk_up
    face_right
    step_end
Ashes_CozmoToTable:
    walk_left
    walk_down
    face_left
    step_end
Ashes_TabithaOut:
    walk_left
    walk_left
    walk_left
    walk_down
    step_end
Ashes_MayOut:
    walk_left
    walk_left
    walk_left
    walk_down
    walk_down
    step_end
Ashes_UpOne:
    walk_up
    step_end
Ashes_DownTwo:
    walk_down
    walk_down
    step_end

LegendsAshes_ChimneyTransition::
    special LegendsAshes_SetGraphics
    setobjectxyperm LOCALID_ASHES_CHIMNEY_HOOPA, 10, 7
    setflag FLAG_TEMP_6
    setflag FLAG_TEMP_7
    goto_if_unset FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, LegendsAshes_Return
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsAshes_Return
    clearflag FLAG_TEMP_7
    return
LegendsAshes_ReactorPreview::
    setspeaker SP_NAME_MAXIE
    msgbox Ashes_Text_MaxieExpansion, MSGBOX_DEFAULT
    closemessage
    playse SE_THUNDER
    delay 20
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_SummitFlicker, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAXIE
    msgbox Ashes_Text_MaxieResponse, MSGBOX_DEFAULT
    return

LegendsAshes_ChimneyAftermath::
    special LegendsAshes_SetGraphics
    setflag FLAG_LA_CHIMNEY_RESONANCE
    setvar VAR_LA_ASHES_STATE, 3
    clearflag FLAG_TEMP_6
    addobject LOCALID_ASHES_CHIMNEY_MAY
    setspeaker SP_NAME_MAY
    msgbox Ashes_Text_WallyFragment, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_WeReachedHim, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox Ashes_Text_MaySummitWork, MSGBOX_DEFAULT
    closemessage
    special HealPlayerParty
    clearflag FLAG_TEMP_7
    addobject LOCALID_ASHES_CHIMNEY_HOOPA
    setvar VAR_0x8004, LOCALID_ASHES_CHIMNEY_HOOPA
    setvar VAR_0x8005, FALSE
    callnative PlayDewfordHoopaAnimation
    playse SE_WARP_IN
    delay 40
    playmoncry SPECIES_HOOPA, CRY_MODE_NORMAL
    waitmoncry
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_HoopaReturns, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox Ashes_Text_MayPortalChoice, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_PortalPlan, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox Ashes_Text_MayStay, MSGBOX_DEFAULT
    return

LegendsAshes_EnterPast::
    lockall
    goto_if_unset FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, LegendsAshes_End
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsAshes_End
    goto_if_set FLAG_LA_CHIMNEY_RESONANCE, LegendsAshes_EnterPastChoice
    call LegendsAshes_ChimneyAftermath
LegendsAshes_EnterPastChoice:
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_FollowHoopa, MSGBOX_YESNO
    goto_if_ne VAR_RESULT, YES, LegendsAshes_End
    closemessage
    special HealPlayerParty
    setvar VAR_LA_ASHES_STATE, 4
    playse SE_WARP_IN
    warp MAP_KANTOAR_3_10_SAFFRONCITY, 33, 32
    waitstate
    end

LegendsAshes_SaffronTransition:
    special LegendsAshes_SetGraphics
    setvar VAR_TEMP_0, 1
    goto_if_set FLAG_LA_PAST_SAFFRON_ARRIVED, LegendsAshes_MapEnd
    setvar VAR_TEMP_0, 0
    end
LegendsAshes_SaffronFrame:
    map_script_2 VAR_TEMP_0, 0, LegendsAshes_SaffronArrival
    .2byte 0
LegendsAshes_SaffronArrival::
    lockall
    setvar VAR_TEMP_0, 1
    setflag FLAG_LA_PAST_SAFFRON_ARRIVED
    turnobject LOCALID_PLAYER, DIR_NORTH
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_Saffron, MSGBOX_DEFAULT
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox Ashes_Text_LockdownShout, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_InsideSilph, MSGBOX_DEFAULT
    goto LegendsAshes_End
LegendsAshes_Lockdown::
    lockall
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_Lockdown, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsAshes_SilphTransition:
    special LegendsAshes_SetGraphics
    setflag FLAG_TEMP_4
    setflag FLAG_TEMP_5
    setflag FLAG_TEMP_6
    end

LegendsAshes_WallySilph::
    lockall
    faceplayer
    goto_if_set FLAG_LA_SILPH_WALLY_FOUND, LegendsAshes_WallyWait
    setspeaker SP_NAME_WALLY
    msgbox Ashes_Text_WallyReunion, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_WallyPastHints, MSGBOX_DEFAULT
    setspeaker SP_NAME_WALLY
    msgbox Ashes_Text_WallyCoverStairs, MSGBOX_DEFAULT
    setflag FLAG_LA_SILPH_WALLY_FOUND
    special HealPlayerParty
LegendsAshes_WallyWait:
    setspeaker SP_NAME_WALLY
    msgbox Ashes_Text_WallyWait, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsAshes_AdminGate::
    lockall
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_AdminGate, MSGBOX_DEFAULT
    goto LegendsAshes_End
LegendsAshes_Petrel::
    lockall
    faceplayer
    goto_if_set FLAG_LA_SILPH_PETREL_DEFEATED, LegendsAshes_AdminDone
    setspeaker SP_NAME_PETREL
    msgbox Ashes_Text_Petrel, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 9
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, Ashes_Text_PetrelDefeat
    setflag FLAG_LA_SILPH_PETREL_DEFEATED
    setspeaker SP_NAME_PETREL
    msgbox Ashes_Text_PetrelAfter, MSGBOX_DEFAULT
    special HealPlayerParty
    goto LegendsAshes_End
LegendsAshes_Ariana::
    lockall
    faceplayer
    goto_if_set FLAG_LA_SILPH_ARIANA_DEFEATED, LegendsAshes_AdminDone
    setspeaker SP_NAME_ARIANA
    msgbox Ashes_Text_Ariana, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 10
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, Ashes_Text_ArianaDefeat
    setflag FLAG_LA_SILPH_ARIANA_DEFEATED
    setspeaker SP_NAME_ARIANA
    msgbox Ashes_Text_ArianaAfter, MSGBOX_DEFAULT
    goto LegendsAshes_End
LegendsAshes_AdminDone:
    msgbox Ashes_Text_AdminDone, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsAshes_RoofTransition:
    special LegendsAshes_SetGraphics
    setflag FLAG_TEMP_4
    setflag FLAG_TEMP_5
    setflag FLAG_TEMP_6
    end
LegendsAshes_TwoGiovannis::
    goto_if_set FLAG_LA_SILPH_GIOVANNIS_FLED, LegendsAshes_End
    lockall
    goto_if_unset FLAG_LA_SILPH_PETREL_DEFEATED, LegendsAshes_AdminGate
    goto_if_unset FLAG_LA_SILPH_ARIANA_DEFEATED, LegendsAshes_AdminGate
    goto_if_unset FLAG_LA_SILPH_WALLY_FOUND, LegendsAshes_AdminGate
    turnobject LOCALID_PLAYER, DIR_NORTH
    setspeaker SP_NAME_PAST_GIOVANNI
    msgbox Ashes_Text_PastGiovanni, MSGBOX_DEFAULT
    setspeaker SP_NAME_RAINBOW_ROCKET_GIOVANNI
    msgbox Ashes_Text_PresentGiovanni, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_TwoGiovannis, MSGBOX_DEFAULT
    setspeaker SP_NAME_PAST_GIOVANNI
    msgbox Ashes_Text_PastIntruder, MSGBOX_DEFAULT
    setspeaker SP_NAME_RAINBOW_ROCKET_GIOVANNI
    msgbox Ashes_Text_PresentOrders, MSGBOX_DEFAULT
    closemessage
    playmoncry SPECIES_MEWTWO, CRY_MODE_NORMAL
    waitmoncry
    playse SE_THUNDER
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_ExitSealed, MSGBOX_DEFAULT
    clearflag FLAG_TEMP_4
    addobject LOCALID_ASHES_SILPH_RIFT
    playse SE_WARP_IN
    applymovement LOCALID_ASHES_GIOVANNI_PRESENT, Ashes_GiovanniPresentExit
    waitmovement 0
    removeobject LOCALID_ASHES_GIOVANNI_PRESENT
    applymovement LOCALID_ASHES_GIOVANNI_PAST, Ashes_GiovanniPastExit
    waitmovement 0
    removeobject LOCALID_ASHES_GIOVANNI_PAST
    applymovement LOCALID_ASHES_MEWTWO, Ashes_MewtwoExit
    waitmovement 0
    removeobject LOCALID_ASHES_MEWTWO
    playse SE_WARP_OUT
    removeobject LOCALID_ASHES_SILPH_RIFT
    setflag FLAG_TEMP_4
    setflag FLAG_LA_SILPH_GIOVANNIS_FLED
    setflag FLAG_LA_SILPH_TIME_REVEALED
    clearflag FLAG_TEMP_5
    addobject LOCALID_ASHES_ROOF_WALLY
    addobject LOCALID_ASHES_ROOF_KIRLIA
    setspeaker SP_NAME_WALLY
    msgbox Ashes_Text_WallyRoof, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_InThePast, MSGBOX_DEFAULT
    closemessage
    clearflag FLAG_TEMP_6
    addobject LOCALID_ASHES_ROOF_HOOPA
    playse SE_WARP_IN
    setvar VAR_0x8004, LOCALID_ASHES_ROOF_HOOPA
    setvar VAR_0x8005, FALSE
    callnative PlayDewfordHoopaAnimation
    delay 40
    playmoncry SPECIES_HOOPA, CRY_MODE_NORMAL
    waitmoncry
    setspeaker SP_NAME_WALLY
    msgbox Ashes_Text_HoopaRescue, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_AcceptHoopa, MSGBOX_DEFAULT
    setflag FLAG_LA_HOOPA_COMPANION
    call LegendsAshes_TryHoopaGift
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_EscapeTogether, MSGBOX_DEFAULT
    closemessage
    setflag FLAG_LA_WALLY_RESCUED
    clearflag FLAG_HIDE_VERDANTURF_TOWN_WANDAS_HOUSE_WALLY
    setvar VAR_LA_ASHES_STATE, 5
    playse SE_WARP_IN
    warp MAP_LAVARIDGE_TOWN, 9, 11
    waitstate
    end
Ashes_GiovanniPresentExit:
    walk_left
    walk_down
    step_end
Ashes_GiovanniPastExit:
    walk_right
    walk_down
    step_end
Ashes_MewtwoExit:
    walk_down
    walk_left
    walk_down
    step_end

LegendsAshes_LavaridgeTransition::
    special LegendsAshes_SetGraphics
    setvar VAR_TEMP_6, 1
    setflag FLAG_TEMP_5
    goto_if_unset FLAG_LA_WALLY_RESCUED, LegendsAshes_LavaCheckReturn
    goto_if_set FLAG_BADGE04_GET, LegendsAshes_LavaCheckReturn
    clearflag FLAG_TEMP_5
LegendsAshes_LavaCheckReturn:
    goto_if_ne VAR_LA_ASHES_STATE, 5, LegendsAshes_Return
    setvar VAR_TEMP_6, 0
    return
LegendsAshes_LavaridgeFrame:
    map_script_2 VAR_TEMP_6, 0, LegendsAshes_Returned
    .2byte 0
LegendsAshes_Returned::
    lockall
    setvar VAR_TEMP_6, 1
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_BackHoenn, MSGBOX_DEFAULT
    setspeaker SP_NAME_BIRCH
    playse SE_POKENAV_CALL
    msgbox Ashes_Text_BirchReturn, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_TellBirchTime, MSGBOX_DEFAULT
    setspeaker SP_NAME_BIRCH
    msgbox Ashes_Text_BirchNext, MSGBOX_DEFAULT
    closemessage
    playse SE_POKENAV_HANG_UP
    setspeaker SP_NAME_NONE
    msgbox Ashes_Text_FlanneryWelcome, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox Ashes_Text_FlanneryAnswer, MSGBOX_DEFAULT
    setspeaker SP_NAME_NONE
    msgbox Ashes_Text_FlanneryChallenge, MSGBOX_DEFAULT
    setvar VAR_LA_ASHES_STATE, 6
    goto LegendsAshes_End

LegendsAshes_HoopaInteract::
    lockall
    faceplayer
    special LegendsAshes_HoopaPrepare
    goto_if_eq VAR_RESULT, TRUE, LegendsAshes_HoopaJoin
    setspeaker SP_NAME_NONE
    playmoncry SPECIES_HOOPA, CRY_MODE_NORMAL
    msgbox Ashes_Text_HoopaWaiting, MSGBOX_DEFAULT
    goto LegendsAshes_End
LegendsAshes_HoopaJoin::
    lockall
    call LegendsAshes_TryHoopaGift
    goto LegendsAshes_End
LegendsAshes_TryHoopaGift::
    special LegendsAshes_HoopaPrepare
    goto_if_ne VAR_RESULT, TRUE, LegendsAshes_Return
    setflag FLAG_LA_HOOPA_JOIN_PROMPTED
    setspeaker SP_NAME_NONE
    msgbox Ashes_Text_HoopaReady, MSGBOX_DEFAULT
    givemon SPECIES_HOOPA, 50, ITEM_NONE
    special LegendsAshes_HoopaGranted
    goto_if_eq VAR_RESULT, 2, LegendsAshes_HoopaFull
    playfanfare MUS_OBTAIN_ITEM
    msgbox Ashes_Text_HoopaJoined, MSGBOX_DEFAULT
    waitfanfare
    return
LegendsAshes_HoopaFull:
    msgbox Ashes_Text_HoopaFull, MSGBOX_DEFAULT
    return
LegendsAshes_FamilySafe::
    setspeaker SP_NAME_NONE
    msgbox Ashes_Text_FamilySafe, MSGBOX_DEFAULT
    goto LegendsAshes_End
LegendsAshes_WallyHome::
    setspeaker SP_NAME_WALLY
    msgbox Ashes_Text_WallyHome, MSGBOX_DEFAULT
    goto LegendsAshes_End

Ashes_Text_Residual:
    .string "The device is gone, but its energy\nhasn't quite faded.\pThe Tracker found a matching pulse\nsomewhere north of Mauville.$"
Ashes_Text_North:
    .string "Then we follow the evidence.\pI'll check Cozmo's work in Fallarbor.\nHe studies unusual meteorites.$"
Ashes_Text_MayPlan:
    .string "I'll compare the readings on the way.\nWe still need to find Wally.$"
Ashes_Text_MayLeave:
    .string "And we're not entering that natural\nwormhole. Not without clearance.\pMeet me at Cozmo's house.$"
Ashes_Text_MayCozmo:
    .string "There you are! Cozmo found something\nthat reacts to our recorded signal.$"
Ashes_Text_Resonance:
    .string "This meteorite produces a different\nsignal. Heat makes the two resonate.\pThink of one note making another\nobject vibrate.$"
Ashes_Text_Echo:
    .string "Like an echo.\pCould that help us reach Wally?$"
Ashes_Text_Meteorite:
    .string "Perhaps. But an uncontrolled response\ncould make his situation worse.\pTeam Magma asked for these results.\nI refused to hand them over.$"
Ashes_Text_TabithaTheft:
    .string "Your assistant was more cooperative.\nThe sample is already on its way.\pWe'll take the calibration notes,\ntoo. Stand aside.$"
Ashes_Text_BlockTheft:
    .string "You stole them? You're not walking\nout while we just watch!$"
Ashes_Text_MayProtectCozmo:
    .string "I'll cover Cozmo. Stop that grunt!\nDon't let them split us up.$"
Ashes_Text_GruntDefeat:
    .string "That bought the commander enough time!$"
Ashes_Text_TabithaEscape:
    .string "Keep the victory. We have the data.\nMeteor Falls is our next stop.$"
Ashes_Text_Calibration:
    .string "The cavern contains matching mineral\nbeds. They can calibrate the sample.\pThen they'll take it to Mt. Chimney.\nPlease stop the experiment!$"
Ashes_Text_MayPursue:
    .string "I'll check the trail ahead.\nMeet me near the mountain.$"
Ashes_Text_MaxieExpansion:
    .string "Our partners have supplied the data.\nThe meteorite will provide the energy.\pWhy accept the boundaries of one\nworld when we could reach beyond it?$"
Ashes_Text_SummitFlicker:
    .string "Something moved inside that light!\nThere was another place beyond it…$"
Ashes_Text_MaxieResponse:
    .string "A response. Exactly as predicted.\pOr almost. Stand aside, Trainer.$"
Ashes_Text_WallyFragment:
    .string "The radio picked up a voice during\nthe surge. Wally's voice!\pI kept the remaining crew off the\nrelay while you stopped Maxie.$"
Ashes_Text_WeReachedHim:
    .string "Then the signal can reach him.\nWe need a safer way to follow it.$"
Ashes_Text_MaySummitWork:
    .string "I've copied the recording for Birch.\nYour team needs a rest first.$"
Ashes_Text_HoopaReturns:
    .string "That ring… The same kind we saw\nnear Dewford!\pIs it showing us where Wally went?$"
Ashes_Text_MayPortalChoice:
    .string "This signal is different from the\nnatural wormhole in the woods.\pBut we still don't know where\nit leads. You can prepare first.$"
Ashes_Text_PortalPlan:
    .string "I'll follow it. Keep our recording\nsafe and tell Paradigm where I went.$"
Ashes_Text_MayStay:
    .string "I will. And if it feels wrong,\nyou come straight back.$"
Ashes_Text_FollowHoopa:
    .string "Follow Hoopa through the golden ring?\nYour team will be healed first.$"
Ashes_Text_Saffron:
    .string "Saffron City… The Silph sign!\nThis must be where Wally called from.\pThe streets are so quiet.$"
Ashes_Text_LockdownShout:
    .string "All personnel remain indoors!\nSilph is under Rocket control!$"
Ashes_Text_InsideSilph:
    .string "Black uniforms. The R on their chests.\nWally described this.\pI need to find him inside.$"
Ashes_Text_Lockdown:
    .string "Rocket has the streets locked down.\nWally's lead points to Silph.$"
Ashes_Text_WallyReunion:
    .string "{PLAYER}! Kirlia felt you coming!\pWe've been hiding from those people.\nThey watched her every time\lshe sensed another opening.$"
Ashes_Text_WallyPastHints:
    .string "The equipment here looks older than\nthe Silph gear we saw in Hoenn.\pSomething about this place is wrong.$"
Ashes_Text_WallyCoverStairs:
    .string "Kirlia won't go near the top floor.\nThere's something powerful up there.\pI'll watch the stairs with her.\nBe careful. We still need a way home.$"
Ashes_Text_WallyWait:
    .string "Your team's healed. I'll keep watch.\nCall if you find a way out.$"
Ashes_Text_AdminGate:
    .string "I need to find Wally and get past\nboth Rocket admins before going up.$"
Ashes_Text_Petrel:
    .string "Petrel. Remember the name.\pYou embarrassed our people downstairs.\nNow let's see how long that lasts.$"
Ashes_Text_PetrelDefeat:
    .string "You're more trouble than you look!$"
Ashes_Text_PetrelAfter:
    .string "Fine. Take a breath. I'd rather you\nface Ariana without an excuse.$"
Ashes_Text_Ariana:
    .string "Petrel talks too much.\nI prefer results.\pThe meeting upstairs stays private.$"
Ashes_Text_ArianaDefeat:
    .string "Even this… wasn't enough?$"
Ashes_Text_ArianaAfter:
    .string "You don't understand what you're\nwalking into. Go and see for yourself.$"
Ashes_Text_AdminDone:
    .string "The others are waiting.\nDon't expect a welcome.$"
Ashes_Text_PastGiovanni:
    .string "You wear my face, but you expect me\nto take your orders?$"
Ashes_Text_PresentGiovanni:
    .string "I know what happens in this building.\nYou don't need to repeat my mistakes.\pThe boy's Kirlia felt the crossings\nbefore our instruments did.\pWe redirected his passage here.\nYour records will explain her response.$"
Ashes_Text_TwoGiovannis:
    .string "Giovanni…? There are two of you?!$"
Ashes_Text_PastIntruder:
    .string "And who is this child?$"
Ashes_Text_PresentOrders:
    .string "A complication from Hoenn.\pMewtwo. Seal the lower exits.\nWe're leaving.$"
Ashes_Text_ExitSealed:
    .string "The stairwell! He cut off our way out!$"
Ashes_Text_WallyRoof:
    .string "{PLAYER}! We can't get back down!\nKirlia won't go near that force.$"
Ashes_Text_InThePast:
    .string "Two Giovannis. The old equipment…\nWally, this isn't just Kanto.\pI think we're in its past.$"
Ashes_Text_HoopaRescue:
    .string "That little Pokémon!\nKirlia says the opening is safe!$"
Ashes_Text_AcceptHoopa:
    .string "You came back for us.\nYou knew we couldn't get out.$"
Ashes_Text_EscapeTogether:
    .string "Wally, Kirlia! Stay close.\nNobody gets left behind this time.$"
Ashes_Text_BackHoenn:
    .string "Lavaridge. We're back!\pHoopa took Wally and Kirlia straight\nto his family. They're home.$"
Ashes_Text_BirchReturn:
    .string "{PLAYER}! May told us you crossed.\nAre you all right?$"
Ashes_Text_TellBirchTime:
    .string "Wally's safe. But there were two\nGiovannis at Silph.\pOne spoke as if he'd been there\nbefore. The other didn't know him.\pHoopa got us out. I think that\nbuilding was in the past.$"
Ashes_Text_BirchNext:
    .string "Stay where you are. We'll compare\nyour account with Oak's records.\pKeep training while we investigate.\nFlannery can help you prepare.\pAnd check on Wally's family when\nyou can. They'll want to see you.$"
Ashes_Text_HoopaWaiting:
    .string "Hoopa stays close, watching the air.\pIt will battle beside you once your\nlevel cap reaches at least 50.$"
Ashes_Text_HoopaReady:
    .string "Hoopa senses that its help is needed.\nIt is ready to battle beside you.$"
Ashes_Text_HoopaJoined:
    .string "Hoopa joined the team!\pIf your party was full, Hoopa was\nsent safely to Pokémon storage.$"
Ashes_Text_HoopaFull:
    .string "Your party and storage are full.\pHoopa will keep following you.\nMake room, then speak to it again.$"
Ashes_Text_FamilySafe:
    .string "Wally and Kirlia are home!\pThank you for bringing them back.\nWe thought we'd never see them again.$"
Ashes_Text_WallyHome:
    .string "Kirlia finally slept without waking\nto every strange sound.\pThank you, {PLAYER}. We're home.\nI won't forget what you did.$"

LegendsAshes_Grunt_0::
    lockall
    faceplayer
    goto_if_set 0x290, LegendsAshes_GruntDone
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox Ashes_Text_RocketGuard, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 1
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, Ashes_Text_RocketDefeat
    setflag 0x290
    applymovement LOCALID_ASHES_SILPH_GRUNT_2, Ashes_GruntStepAside
    waitmovement 0
    goto LegendsAshes_End

LegendsAshes_Grunt_1::
    lockall
    faceplayer
    goto_if_set 0x291, LegendsAshes_GruntDone
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox Ashes_Text_RocketGuard, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 2
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, Ashes_Text_RocketDefeat
    setflag 0x291
    applymovement LOCALID_ASHES_SILPH_GRUNT_3, Ashes_GruntStepAside
    waitmovement 0
    goto LegendsAshes_End

LegendsAshes_Grunt_2::
    lockall
    faceplayer
    goto_if_set 0x292, LegendsAshes_GruntDone
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox Ashes_Text_RocketGuard, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 3
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, Ashes_Text_RocketDefeat
    setflag 0x292
    applymovement LOCALID_ASHES_SILPH_GRUNT_4, Ashes_GruntStepAside
    waitmovement 0
    goto LegendsAshes_End

LegendsAshes_Grunt_3::
    lockall
    faceplayer
    goto_if_set 0x293, LegendsAshes_GruntDone
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox Ashes_Text_RocketGuard, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 4
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, Ashes_Text_RocketDefeat
    setflag 0x293
    applymovement LOCALID_ASHES_SILPH_GRUNT_5, Ashes_GruntStepAside
    waitmovement 0
    goto LegendsAshes_End

LegendsAshes_Grunt_4::
    lockall
    faceplayer
    goto_if_set 0x294, LegendsAshes_GruntDone
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox Ashes_Text_RocketGuard, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 5
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, Ashes_Text_RocketDefeat
    setflag 0x294
    applymovement LOCALID_ASHES_SILPH_GRUNT_6, Ashes_GruntStepAside
    waitmovement 0
    goto LegendsAshes_End

LegendsAshes_Grunt_5::
    lockall
    faceplayer
    goto_if_set 0x295, LegendsAshes_GruntDone
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox Ashes_Text_RocketGuard, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 6
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, Ashes_Text_RocketDefeat
    setflag 0x295
    applymovement LOCALID_ASHES_SILPH_GRUNT_7, Ashes_GruntStepAside
    waitmovement 0
    goto LegendsAshes_End

LegendsAshes_Grunt_6::
    lockall
    faceplayer
    goto_if_set 0x296, LegendsAshes_GruntDone
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox Ashes_Text_RocketGuard, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 7
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, Ashes_Text_RocketDefeat
    setflag 0x296
    applymovement LOCALID_ASHES_SILPH_GRUNT_8, Ashes_GruntStepAside
    waitmovement 0
    goto LegendsAshes_End

LegendsAshes_Grunt_7::
    lockall
    faceplayer
    goto_if_set 0x297, LegendsAshes_GruntDone
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox Ashes_Text_RocketGuard, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 8
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, Ashes_Text_RocketDefeat
    setflag 0x297
    applymovement LOCALID_ASHES_SILPH_GRUNT_9, Ashes_GruntStepAside
    waitmovement 0
    goto LegendsAshes_End

LegendsAshes_GruntDone:
    msgbox Ashes_Text_RocketDone, MSGBOX_DEFAULT
    goto LegendsAshes_End
Ashes_Text_RocketGuard:
    .string "This floor is off limits!\nYou should have stayed outside.$"
Ashes_Text_RocketDefeat:
    .string "How did you get past our team?!$"
Ashes_Text_RocketDone:
    .string "The executives are upstairs.\nYou'll regret going any farther.$"

Ashes_Text_MountainNext:
    .string "Aqua and Magma. The same operation.\nI need to stop that relay.$"

LegendsAshes_FlanneryOutside::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox Ashes_Text_FlanneryChallenge, MSGBOX_DEFAULT
    goto LegendsAshes_End
Ashes_Text_FlanneryWelcome:
    .string "Flannery: May called ahead. Then\nWattson. What a day you've had.\pI'm glad your friend's safe.\nCome catch your breath inside.$"
Ashes_Text_FlanneryAnswer:
    .string "Thank you. But I still need to be\nready for whatever comes next.\pCan I challenge your Gym?$"
Ashes_Text_FlanneryChallenge:
    .string "Flannery: You can. I won't go easy\non you, and I won't expect you to.\pCome inside when you're ready.$"

Ashes_GruntStepAside:
    walk_left
    face_right
    step_end
