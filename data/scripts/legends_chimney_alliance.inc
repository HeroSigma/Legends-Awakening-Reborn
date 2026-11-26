@ Mt. Chimney: allied blockade, backup call and three consecutive single battles.
ChimneyAlliance_Transition::
    callnative LegendsChimney_SetGraphics
    setflag FLAG_TEMP_3
    clearflag FLAG_TEMP_2
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, ChimneyAlliance_CompletedMap
    setobjectxyperm LOCALID_MT_CHIMNEY_MAGMA_GRUNT_2, 20, 18
    setobjectxyperm LOCALID_LA_CHIMNEY_AQUA, 21, 17
    setobjectxyperm LOCALID_LA_CHIMNEY_ROCKET, 18, 18
    setobjectxyperm LOCALID_LA_CHIMNEY_RESERVE, 29, 18
    goto_if_lt VAR_LA_CHIMNEY_GAUNTLET, 1, ChimneyAlliance_Return
    setobjectxyperm LOCALID_LA_BLUE_CHIMNEY, 20, 20
    setobjectxyperm LOCALID_LA_CHIMNEY_CHARIZARD, 21, 20
    setobjectxyperm LOCALID_LA_CHIMNEY_SHARPEDO, 23, 20
    setobjectxyperm LOCALID_MT_CHIMNEY_ARCHIE, 24, 20
    goto_if_lt VAR_LA_CHIMNEY_GAUNTLET, 2, ChimneyAlliance_Return
    setflag FLAG_LA_CHIMNEY_MAGMA_BEATEN
    goto_if_lt VAR_LA_CHIMNEY_GAUNTLET, 3, ChimneyAlliance_Return
    setflag FLAG_LA_CHIMNEY_AQUA_BEATEN
    goto_if_lt VAR_LA_CHIMNEY_GAUNTLET, 4, ChimneyAlliance_Return
    setflag FLAG_LA_CHIMNEY_ROCKET_BEATEN
    goto_if_lt VAR_LA_CHIMNEY_GAUNTLET, 5, ChimneyAlliance_Return
    clearflag FLAG_TEMP_3
    clearflag FLAG_TEMP_6
    setobjectxyperm LOCALID_LA_CHIMNEY_RED, 26, 20
    setobjectxyperm LOCALID_LA_CHIMNEY_PIKACHU, 27, 20
    setobjectxyperm LOCALID_ASHES_CHIMNEY_MAY, 23, 21
    setobjectxyperm LOCALID_LA_CHIMNEY_MAY_PARTNER, 24, 21
    setobjectxyperm LOCALID_LA_CHIMNEY_RESERVE, 25, 20
    return
ChimneyAlliance_CompletedMap:
    setflag FLAG_TEMP_2
    setflag FLAG_LA_CHIMNEY_MAGMA_BEATEN
    setflag FLAG_LA_CHIMNEY_AQUA_BEATEN
    setflag FLAG_LA_CHIMNEY_ROCKET_BEATEN
    goto_if_lt VAR_LA_CHIMNEY_GAUNTLET, 5, ChimneyAlliance_Return
    goto_if_set FLAG_LA_WALLY_RESCUED, ChimneyAlliance_PartyGone
    clearflag FLAG_TEMP_2
    clearflag FLAG_TEMP_3
    clearflag FLAG_TEMP_6
    setobjectxyperm LOCALID_LA_CHIMNEY_CHARIZARD, 8, 8
    setobjectxyperm LOCALID_LA_CHIMNEY_MAY_PARTNER, 12, 8
    setobjectxyperm LOCALID_LA_CHIMNEY_RED, 14, 7
    setobjectxyperm LOCALID_LA_CHIMNEY_PIKACHU, 15, 7
    setobjectxyperm LOCALID_ASHES_CHIMNEY_MAY, 13, 8
    return
ChimneyAlliance_PartyGone:
    setflag FLAG_TEMP_6
    return
ChimneyAlliance_Return:
    return
ChimneyAlliance_Frame:
    map_script_2 VAR_LA_CHIMNEY_GAUNTLET, 4, ChimneyAlliance_BackupArrives
    .2byte 0

ChimneyAlliance_BriefSouth::
    lockall
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, ChimneyAlliance_End
    getplayerxy VAR_0x8008, VAR_0x8009
    call_if_eq VAR_0x8008, 20, ChimneyAlliance_AlignSouth20
    call_if_eq VAR_0x8008, 21, ChimneyAlliance_AlignSouth21
    call_if_eq VAR_0x8008, 22, ChimneyAlliance_AlignSouth22
    call_if_eq VAR_0x8008, 23, ChimneyAlliance_AlignSouth23
    call_if_eq VAR_0x8008, 24, ChimneyAlliance_AlignSouth24
    goto ChimneyAlliance_Briefing
ChimneyAlliance_BriefWest::
    lockall
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, ChimneyAlliance_End
    getplayerxy VAR_0x8008, VAR_0x8009
    call_if_eq VAR_0x8008, 17, ChimneyAlliance_AlignWest17
    call_if_eq VAR_0x8008, 18, ChimneyAlliance_AlignWest18
    goto ChimneyAlliance_Briefing
ChimneyAlliance_Briefing:
    applymovement LOCALID_LA_BLUE_CHIMNEY, ChimneyAlliance_BlueApproach
    applymovement LOCALID_LA_CHIMNEY_CHARIZARD, ChimneyAlliance_CharizardApproach
    waitmovement LOCALID_LA_BLUE_CHIMNEY
    waitmovement LOCALID_LA_CHIMNEY_CHARIZARD
    turnobject LOCALID_PLAYER, DIR_NORTH
    turnobject LOCALID_LA_BLUE_CHIMNEY, DIR_WEST
    playse SE_PIN
    applymovement LOCALID_LA_BLUE_CHIMNEY, Common_Movement_ExclamationMark
    waitmovement 0
    setspeaker SP_NAME_BLUE
    msgbox ChimneyAlliance_Text_RocketRecognition, MSGBOX_DEFAULT
    turnobject LOCALID_LA_BLUE_CHIMNEY, DIR_SOUTH
    setspeaker SP_NAME_PLAYER
    msgbox ChimneyAlliance_Text_ThreeTeams, MSGBOX_DEFAULT
    setspeaker SP_NAME_BLUE
    msgbox ChimneyAlliance_Text_CallBackup, MSGBOX_DEFAULT
    closemessage
    playse SE_POKENAV_CALL
    setspeaker SP_NAME_PLAYER
    msgbox ChimneyAlliance_Text_PlayerCall, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox ChimneyAlliance_Text_MayCall, MSGBOX_DEFAULT
    setspeaker SP_NAME_RED
    msgbox ChimneyAlliance_Text_RedCall, MSGBOX_DEFAULT
    closemessage
    playse SE_POKENAV_HANG_UP
    applymovement LOCALID_LA_BLUE_CHIMNEY, ChimneyAlliance_BlueHolds
    applymovement LOCALID_LA_CHIMNEY_CHARIZARD, ChimneyAlliance_CharizardHolds
    waitmovement LOCALID_LA_BLUE_CHIMNEY
    waitmovement LOCALID_LA_CHIMNEY_CHARIZARD
    applymovement LOCALID_MT_CHIMNEY_ARCHIE, ChimneyAlliance_ArchieHolds
    applymovement LOCALID_LA_CHIMNEY_SHARPEDO, ChimneyAlliance_SharpedoHolds
    waitmovement LOCALID_MT_CHIMNEY_ARCHIE
    waitmovement LOCALID_LA_CHIMNEY_SHARPEDO
    turnobject LOCALID_MT_CHIMNEY_ARCHIE, DIR_WEST
    setspeaker SP_NAME_ARCHIE
    msgbox ChimneyAlliance_Text_ArchieBlue, MSGBOX_DEFAULT
    setspeaker SP_NAME_BLUE
    msgbox ChimneyAlliance_Text_BlueChallenge, MSGBOX_DEFAULT
    setvar VAR_LA_CHIMNEY_GAUNTLET, 1
    goto ChimneyAlliance_End

ChimneyAlliance_GauntletWest::
    lockall
    getplayerxy VAR_0x8008, VAR_0x8009
    call_if_eq VAR_0x8008, 17, ChimneyAlliance_AlignFight17
    call_if_eq VAR_0x8008, 18, ChimneyAlliance_AlignFight18
    goto ChimneyAlliance_Gauntlet
ChimneyAlliance_Gauntlet::
    lockall
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, ChimneyAlliance_End
    turnobject LOCALID_PLAYER, DIR_NORTH
    goto_if_ge VAR_LA_CHIMNEY_GAUNTLET, 4, ChimneyAlliance_BackupArrives
    goto_if_ge VAR_LA_CHIMNEY_GAUNTLET, 3, ChimneyAlliance_RocketBattle
    goto_if_ge VAR_LA_CHIMNEY_GAUNTLET, 2, ChimneyAlliance_AquaBattle
    applymovement LOCALID_MT_CHIMNEY_MAGMA_GRUNT_2, ChimneyAlliance_MagmaApproach
    waitmovement 0
    setspeaker SP_NAME_TEAM_MAGMA
    msgbox ChimneyAlliance_Text_MagmaIntro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 34
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, ChimneyAlliance_Text_MagmaDefeat
    setflag FLAG_LA_CHIMNEY_MAGMA_BEATEN
    setvar VAR_LA_CHIMNEY_GAUNTLET, 2
    applymovement LOCALID_MT_CHIMNEY_MAGMA_GRUNT_2, ChimneyAlliance_GruntRetreat
    waitmovement 0
    removeobject LOCALID_MT_CHIMNEY_MAGMA_GRUNT_2
ChimneyAlliance_AquaBattle:
    applymovement LOCALID_LA_CHIMNEY_AQUA, ChimneyAlliance_AquaApproach
    waitmovement 0
    setspeaker SP_NAME_TEAM_AQUA
    msgbox ChimneyAlliance_Text_AquaIntro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 35
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, ChimneyAlliance_Text_AquaDefeat
    setflag FLAG_LA_CHIMNEY_AQUA_BEATEN
    setvar VAR_LA_CHIMNEY_GAUNTLET, 3
    applymovement LOCALID_LA_CHIMNEY_AQUA, ChimneyAlliance_GruntRetreat
    waitmovement 0
    removeobject LOCALID_LA_CHIMNEY_AQUA
ChimneyAlliance_RocketBattle:
    applymovement LOCALID_LA_CHIMNEY_ROCKET, ChimneyAlliance_RocketApproach
    waitmovement 0
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox ChimneyAlliance_Text_RocketIntro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 36
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, ChimneyAlliance_Text_RocketDefeat
    setflag FLAG_LA_CHIMNEY_ROCKET_BEATEN
    setvar VAR_LA_CHIMNEY_GAUNTLET, 4
    applymovement LOCALID_LA_CHIMNEY_ROCKET, ChimneyAlliance_GruntRetreat
    waitmovement 0
    removeobject LOCALID_LA_CHIMNEY_ROCKET
    goto ChimneyAlliance_BackupArrives

ChimneyAlliance_BackupArrives::
    lockall
    goto_if_ge VAR_LA_CHIMNEY_GAUNTLET, 5, ChimneyAlliance_End
    applymovement LOCALID_LA_CHIMNEY_RESERVE, ChimneyAlliance_ReserveApproach
    waitmovement 0
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox ChimneyAlliance_Text_Reserve, MSGBOX_DEFAULT
    setspeaker SP_NAME_RED
    msgbox ChimneyAlliance_Text_RedOffscreen, MSGBOX_DEFAULT
    closemessage
    applymovement LOCALID_PLAYER, ChimneyAlliance_PlayerAside
    waitmovement 0
    clearflag FLAG_TEMP_3
    clearflag FLAG_TEMP_6
    setobjectxyperm LOCALID_LA_CHIMNEY_RED, 25, 23
    setobjectxyperm LOCALID_LA_CHIMNEY_PIKACHU, 24, 23
    setobjectxyperm LOCALID_ASHES_CHIMNEY_MAY, 23, 23
    setobjectxyperm LOCALID_LA_CHIMNEY_MAY_PARTNER, 22, 23
    addobject LOCALID_LA_CHIMNEY_RED
    addobject LOCALID_LA_CHIMNEY_PIKACHU
    addobject LOCALID_ASHES_CHIMNEY_MAY
    addobject LOCALID_LA_CHIMNEY_MAY_PARTNER
    applymovement LOCALID_LA_CHIMNEY_RED, ChimneyAlliance_RedArrive
    applymovement LOCALID_LA_CHIMNEY_PIKACHU, ChimneyAlliance_PikachuArrive
    waitmovement LOCALID_LA_CHIMNEY_RED
    waitmovement LOCALID_LA_CHIMNEY_PIKACHU
    applymovement LOCALID_ASHES_CHIMNEY_MAY, ChimneyAlliance_MayArrive
    applymovement LOCALID_LA_CHIMNEY_MAY_PARTNER, ChimneyAlliance_MayPartnerArrive
    waitmovement LOCALID_ASHES_CHIMNEY_MAY
    waitmovement LOCALID_LA_CHIMNEY_MAY_PARTNER
    turnobject LOCALID_LA_CHIMNEY_RESERVE, DIR_EAST
    turnobject LOCALID_PLAYER, DIR_WEST
    setspeaker SP_NAME_MAY
    msgbox ChimneyAlliance_Text_MayArrives, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox ChimneyAlliance_Text_PlayerArrival, MSGBOX_DEFAULT
    setspeaker SP_NAME_RED
    msgbox ChimneyAlliance_Text_RedAssignment, MSGBOX_DEFAULT
    playmoncry SPECIES_PIKACHU, CRY_MODE_NORMAL
    waitmoncry
    setspeaker SP_NAME_BLUE
    msgbox ChimneyAlliance_Text_BlueSend, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox ChimneyAlliance_Text_MayHeal, MSGBOX_DEFAULT
    special HealPlayerParty
    setobjectxyperm LOCALID_LA_CHIMNEY_RED, 26, 20
    setobjectxyperm LOCALID_LA_CHIMNEY_PIKACHU, 27, 20
    setobjectxyperm LOCALID_ASHES_CHIMNEY_MAY, 23, 21
    setobjectxyperm LOCALID_LA_CHIMNEY_MAY_PARTNER, 24, 21
    setobjectxyperm LOCALID_LA_CHIMNEY_RESERVE, 25, 20
    setvar VAR_LA_CHIMNEY_GAUNTLET, 5
    goto ChimneyAlliance_End

ChimneyAlliance_SupportToSummit::
    goto_if_lt VAR_LA_CHIMNEY_GAUNTLET, 5, ChimneyAlliance_Return
    removeobject LOCALID_LA_CHIMNEY_RESERVE
    removeobject LOCALID_LA_CHIMNEY_AQUA_LOWER
    removeobject LOCALID_LA_CHIMNEY_ROCKET_UPPER
    removeobject LOCALID_LA_CHIMNEY_CAMERUPT
    removeobject LOCALID_LA_CHIMNEY_SHARPEDO
    clearflag FLAG_TEMP_3
    clearflag FLAG_TEMP_6
    setobjectxyperm LOCALID_LA_CHIMNEY_RED, 14, 7
    setobjectxy LOCALID_LA_CHIMNEY_RED, 14, 7
    addobject LOCALID_LA_CHIMNEY_RED
    setobjectxyperm LOCALID_LA_CHIMNEY_PIKACHU, 15, 7
    setobjectxy LOCALID_LA_CHIMNEY_PIKACHU, 15, 7
    addobject LOCALID_LA_CHIMNEY_PIKACHU
    setobjectxyperm LOCALID_ASHES_CHIMNEY_MAY, 13, 8
    setobjectxy LOCALID_ASHES_CHIMNEY_MAY, 13, 8
    setobjectxyperm LOCALID_LA_CHIMNEY_MAY_PARTNER, 12, 8
    setobjectxy LOCALID_LA_CHIMNEY_MAY_PARTNER, 12, 8
    addobject LOCALID_LA_CHIMNEY_MAY_PARTNER
    setobjectxyperm LOCALID_LA_CHIMNEY_CHARIZARD, 8, 8
    setobjectxy LOCALID_LA_CHIMNEY_CHARIZARD, 8, 8
    addobject LOCALID_LA_CHIMNEY_CHARIZARD
    addobject LOCALID_ASHES_CHIMNEY_MAY
    turnobject LOCALID_LA_CHIMNEY_RED, DIR_WEST
    turnobject LOCALID_LA_CHIMNEY_PIKACHU, DIR_WEST
    turnobject LOCALID_ASHES_CHIMNEY_MAY, DIR_NORTH
    return
ChimneyAlliance_RedReport::
    goto_if_lt VAR_LA_CHIMNEY_GAUNTLET, 5, ChimneyAlliance_Return
    applymovement LOCALID_LA_BLUE_CHIMNEY, ChimneyAlliance_BlueMakesRoom
    waitmovement 0
    turnobject LOCALID_LA_BLUE_CHIMNEY, DIR_EAST
    turnobject LOCALID_PLAYER, DIR_EAST
    turnobject LOCALID_LA_CHIMNEY_RED, DIR_WEST
    setspeaker SP_NAME_RED
    msgbox ChimneyAlliance_Text_RedReport, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox ChimneyAlliance_Text_PlayerReport, MSGBOX_DEFAULT
    turnobject LOCALID_PLAYER, DIR_SOUTH
    return
ChimneyAlliance_RedPlan::
    goto_if_lt VAR_LA_CHIMNEY_GAUNTLET, 5, ChimneyAlliance_Return
    turnobject LOCALID_PLAYER, DIR_EAST
    turnobject LOCALID_LA_CHIMNEY_RED, DIR_WEST
    setspeaker SP_NAME_RED
    msgbox ChimneyAlliance_Text_RedPlan, MSGBOX_DEFAULT
    return
ChimneyAlliance_NeedBackup::
    lockall
    setspeaker SP_NAME_PLAYER
    msgbox ChimneyAlliance_Text_NeedBackup, MSGBOX_DEFAULT
    goto ChimneyAlliance_End
ChimneyAlliance_MayTalk::
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, LegendsAshes_EnterPast
    lockall
    faceplayer
    setspeaker SP_NAME_MAY
    msgbox ChimneyAlliance_Text_MayReady, MSGBOX_DEFAULT
    goto ChimneyAlliance_End
ChimneyAlliance_BlueTalk::
    lockall
    faceplayer
    setspeaker SP_NAME_BLUE
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, ChimneyAlliance_BlueAfter
    goto_if_ge VAR_LA_CHIMNEY_GAUNTLET, 1, ChimneyAlliance_BlueHolding
    msgbox ChimneyAlliance_Text_MeetStairs, MSGBOX_DEFAULT
    goto ChimneyAlliance_End
ChimneyAlliance_BlueHolding:
    msgbox ChimneyAlliance_Text_BlueHolding, MSGBOX_DEFAULT
    goto ChimneyAlliance_End
ChimneyAlliance_BlueAfter:
    msgbox ChimneyAlliance_Text_BlueAfter, MSGBOX_DEFAULT
    goto ChimneyAlliance_End
ChimneyAlliance_RedTalk::
    lockall
    faceplayer
    setspeaker SP_NAME_RED
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, ChimneyAlliance_RedAfter
    msgbox ChimneyAlliance_Text_RedReady, MSGBOX_DEFAULT
    goto ChimneyAlliance_End
ChimneyAlliance_RedAfter:
    msgbox ChimneyAlliance_Text_RedPlan, MSGBOX_DEFAULT
    goto ChimneyAlliance_End
ChimneyAlliance_PikachuTalk::
    lockall
    faceplayer
    playmoncry SPECIES_PIKACHU, CRY_MODE_NORMAL
    waitmoncry
    goto ChimneyAlliance_End
ChimneyAlliance_GuardTalk::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_MAGMA
    goto_if_ne VAR_LAST_TALKED, LOCALID_LA_CHIMNEY_AQUA, ChimneyAlliance_GuardLine
    setspeaker SP_NAME_TEAM_AQUA
ChimneyAlliance_GuardLine:
    msgbox ChimneyAlliance_Text_Guard, MSGBOX_DEFAULT
    goto ChimneyAlliance_End
ChimneyAlliance_RocketTalk::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox ChimneyAlliance_Text_RocketReady, MSGBOX_DEFAULT
    goto ChimneyAlliance_End
ChimneyAlliance_ReserveTalk::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox ChimneyAlliance_Text_ReserveReady, MSGBOX_DEFAULT
    goto ChimneyAlliance_End
ChimneyAlliance_AquaSupply::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_AQUA
    msgbox ChimneyAlliance_Text_Supply, MSGBOX_DEFAULT
    goto ChimneyAlliance_End
ChimneyAlliance_Receiver::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox ChimneyAlliance_Text_Receiver, MSGBOX_DEFAULT
ChimneyAlliance_End:
    closemessage
    setspeaker SP_NAME_NONE
    releaseall
    end

ChimneyAlliance_AlignSouth20:
    applymovement LOCALID_PLAYER, ChimneyAlliance_Right5
    waitmovement 0
    return

ChimneyAlliance_AlignSouth21:
    applymovement LOCALID_PLAYER, ChimneyAlliance_Right4
    waitmovement 0
    return

ChimneyAlliance_AlignSouth22:
    applymovement LOCALID_PLAYER, ChimneyAlliance_Right3
    waitmovement 0
    return

ChimneyAlliance_AlignSouth23:
    applymovement LOCALID_PLAYER, ChimneyAlliance_Right2
    waitmovement 0
    return

ChimneyAlliance_AlignSouth24:
    applymovement LOCALID_PLAYER, ChimneyAlliance_Right1
    waitmovement 0
    return

ChimneyAlliance_AlignWest17:
    applymovement LOCALID_PLAYER, ChimneyAlliance_WestBrief17
    waitmovement 0
    return

ChimneyAlliance_AlignFight17:
    applymovement LOCALID_PLAYER, ChimneyAlliance_WestFight17
    waitmovement 0
    return

ChimneyAlliance_AlignWest18:
    applymovement LOCALID_PLAYER, ChimneyAlliance_WestBrief18
    waitmovement 0
    return

ChimneyAlliance_AlignFight18:
    applymovement LOCALID_PLAYER, ChimneyAlliance_WestFight18
    waitmovement 0
    return

ChimneyAlliance_Right1:
    walk_right
    step_end

ChimneyAlliance_Right2:
    walk_right
    walk_right
    step_end

ChimneyAlliance_Right3:
    walk_right
    walk_right
    walk_right
    step_end

ChimneyAlliance_Right4:
    walk_right
    walk_right
    walk_right
    walk_right
    step_end

ChimneyAlliance_Right5:
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    step_end

ChimneyAlliance_WestBrief17:
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_down
    walk_down
    step_end

ChimneyAlliance_WestFight17:
    walk_right
    walk_right
    walk_up
    walk_up
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_down
    walk_down
    step_end

ChimneyAlliance_WestBrief18:
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_down
    walk_down
    step_end

ChimneyAlliance_WestFight18:
    walk_right
    walk_up
    walk_up
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_down
    walk_down
    step_end

ChimneyAlliance_BlueApproach:
    walk_right
    walk_down
    walk_down
    face_down
    step_end

ChimneyAlliance_BlueHolds:
    walk_up
    walk_left
    walk_left
    walk_left
    walk_left
    walk_left
    walk_up
    face_right
    step_end

ChimneyAlliance_MagmaApproach:
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_down
    walk_down
    face_down
    step_end

ChimneyAlliance_AquaApproach:
    walk_down
    walk_down
    walk_right
    walk_right
    walk_right
    walk_right
    walk_down
    face_down
    step_end

ChimneyAlliance_RocketApproach:
    walk_down
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_down
    face_down
    step_end

ChimneyAlliance_GruntRetreat:
    walk_right
    walk_right
    walk_up
    walk_up
    walk_up
    step_end

ChimneyAlliance_ReserveApproach:
    walk_down
    walk_left
    walk_left
    walk_left
    walk_left
    walk_down
    face_down
    step_end

ChimneyAlliance_PlayerAside:
    walk_right
    walk_right
    walk_up
    walk_up
    face_down
    step_end

ChimneyAlliance_RedArrive:
    walk_up
    walk_up
    walk_right
    walk_up
    face_left
    step_end

ChimneyAlliance_PikachuArrive:
    walk_right
    walk_up
    walk_up
    walk_right
    walk_right
    walk_up
    face_left
    step_end

ChimneyAlliance_MayArrive:
    walk_right
    walk_right
    walk_up
    walk_up
    walk_left
    walk_left
    face_up
    step_end

ChimneyAlliance_BlueMakesRoom:
    walk_left
    step_end

Ashes_DownOne:
    walk_down
    step_end

ChimneyAlliance_Text_RocketRecognition:
    .string "I know those uniforms. Team Rocket!\nWhat are they doing here?$"

ChimneyAlliance_Text_ThreeTeams:
    .string "Magma, Aqua, and Rocket…\nThey're guarding the same operation.$"

ChimneyAlliance_Text_CallBackup:
    .string "We'll be boxed in if we split up now.\nCall May and Red. We need backup.\pI'll keep Archie busy.\nYou take the guards at the stairs.$"

ChimneyAlliance_Text_PlayerCall:
    .string "May? Red? We're on Mt. Chimney.\nAqua, Magma and Rocket are here.\pBlue's holding Archie.\nWe need help getting to the summit!$"

ChimneyAlliance_Text_MayCall:
    .string "I'm close! I'm coming up the trail.\nKeep that recording safe!$"

ChimneyAlliance_Text_RedCall:
    .string "Pikachu and I are on our way.\nHold your ground.$"

ChimneyAlliance_Text_ArchieBlue:
    .string "Oak's grandson? You've picked\na busy day to play Champion, kid.$"

ChimneyAlliance_Text_BlueChallenge:
    .string "Then you can try getting past me.\n{PLAYER}, go. I've got this.$"

ChimneyAlliance_Text_MagmaIntro:
    .string "The stairs are closed!\nMagma's summit team stays undisturbed.$"

ChimneyAlliance_Text_MagmaDefeat:
    .string "Aqua! Stop that Trainer!$"

ChimneyAlliance_Text_AquaIntro:
    .string "Our turn. You don't get a clear run\njust because you beat their guard!$"

ChimneyAlliance_Text_AquaDefeat:
    .string "Rocket, where are you?!$"

ChimneyAlliance_Text_RocketIntro:
    .string "Right here. Thanks for wearing\nyourself out on the others.\pOur people are expecting a signal.\nYou're not going to interrupt it!$"

ChimneyAlliance_Text_RocketDefeat:
    .string "Three teams… and you kept going?$"

ChimneyAlliance_Text_Reserve:
    .string "You fought the lookouts.\nWe're the recovery team.\pHand over the recording. Now.$"

ChimneyAlliance_Text_RedOffscreen:
    .string "That's enough.\nPikachu, with me!$"

ChimneyAlliance_Text_MayArrives:
    .string "{PLAYER}! Sorry we're late!\nAre you and your Pokémon all right?$"

ChimneyAlliance_Text_PlayerArrival:
    .string "They're trying to surround us.\nMaxie's still at the machine!$"

ChimneyAlliance_Text_RedAssignment:
    .string "I'll take Rocket. May, hold the path.\nPikachu, stay close.$"

ChimneyAlliance_Text_BlueSend:
    .string "About time! {PLAYER}, get up there.\nArchie's still mine.$"

ChimneyAlliance_Text_MayHeal:
    .string "Let me patch your team up.\nThere! Now go stop Maxie!$"

ChimneyAlliance_Text_RedReport:
    .string "Rocket knew when to pull back.\nSomeone was waiting for that signal.\pThey'd already sent what they\ncame here to collect.$"

ChimneyAlliance_Text_PlayerReport:
    .string "Then even with all of us here,\nwe only stopped one part of it.$"

ChimneyAlliance_Text_RedPlan:
    .string "Pikachu and I will follow Rocket's\ntrail and send Birch what we find.\pFind Wally. Bring him home.$"

ChimneyAlliance_Text_MayRecording:
    .string "Red and I held the stairway while\nyou stopped Maxie.\pThe radio caught a voice in the surge.\n{PLAYER}, it was Wally!$"

ChimneyAlliance_Text_NeedBackup:
    .string "I need backup at the stairs before\nthey close the trail behind us.\pBlue is waiting down there.$"

ChimneyAlliance_Text_MayReady:
    .string "Red and I have the path covered.\nYou go after Maxie!$"

ChimneyAlliance_Text_MeetStairs:
    .string "Meet me by the upper stairs.\nYou need to see those uniforms.$"

ChimneyAlliance_Text_BlueHolding:
    .string "Archie's mine. Take the guards\nand get to the summit!$"

ChimneyAlliance_Text_BlueAfter:
    .string "We'll keep this equipment safe\nand contact Paradigm. Find Wally.$"

ChimneyAlliance_Text_RedReady:
    .string "We'll keep the trail clear.\nGo stop that machine.$"

ChimneyAlliance_Text_Guard:
    .string "Back to the trail.\nThe summit is off limits!$"

ChimneyAlliance_Text_RocketReady:
    .string "Keep your hands off our equipment.\nThis is a restricted operation.$"

ChimneyAlliance_Text_ReserveReady:
    .string "Recovery team. Stay out of our way.$"

ChimneyAlliance_Text_Supply:
    .string "We get these cases up the mountain.\nRocket handles the receiver.$"

ChimneyAlliance_Text_Receiver:
    .string "Aqua's feed is stable.\nMagma just needs to finish the test.$"

ChimneyAlliance_CharizardApproach:
    delay_16
    walk_right
    walk_right
    walk_down
    face_down
    step_end

ChimneyAlliance_CharizardHolds:
    walk_left
    walk_left
    walk_left
    walk_left
    walk_up
    face_right
    step_end

ChimneyAlliance_ArchieHolds:
    walk_down
    face_left
    step_end

ChimneyAlliance_SharpedoHolds:
    delay_16
    walk_down
    walk_left
    walk_down
    face_left
    step_end

ChimneyAlliance_MayPartnerArrive:
    delay_16
    walk_right
    walk_right
    walk_right
    walk_up
    walk_up
    walk_left
    face_up
    step_end

ChimneyAlliance_AceTalk::
    lockall
    faceplayer
    goto_if_eq VAR_LAST_TALKED, LOCALID_LA_CHIMNEY_CHARIZARD, ChimneyAlliance_CharizardCry
    goto_if_eq VAR_LAST_TALKED, LOCALID_LA_CHIMNEY_SHARPEDO, ChimneyAlliance_SharpedoCry
    goto_if_eq VAR_LAST_TALKED, LOCALID_LA_CHIMNEY_CAMERUPT, ChimneyAlliance_CameruptCry
    waitmoncry
    goto ChimneyAlliance_End
ChimneyAlliance_CharizardCry:
    playmoncry SPECIES_CHARIZARD, CRY_MODE_NORMAL
    waitmoncry
    goto ChimneyAlliance_End
ChimneyAlliance_SharpedoCry:
    playmoncry SPECIES_SHARPEDO, CRY_MODE_NORMAL
    waitmoncry
    goto ChimneyAlliance_End
ChimneyAlliance_CameruptCry:
    playmoncry SPECIES_CAMERUPT, CRY_MODE_NORMAL
    waitmoncry
    goto ChimneyAlliance_End
