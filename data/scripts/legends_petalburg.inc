@ Project-owned Petalburg chapter. Native gym/badge and tutorial state remain authoritative.
LegendsPetalburg_CheckWoodsExit:
    setvar VAR_TEMP_3, 0
    goto_if_unset FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN, LegendsPetalburg_Return
    goto_if_set FLAG_LA_WOODS_EXIT_THOUGHT, LegendsPetalburg_Return
    goto_if_set FLAG_LA_REPORTED_WOODS_TO_NORMAN, LegendsPetalburg_Return
    getplayerxy VAR_0x8004, VAR_0x8005
    goto_if_gt VAR_0x8005, 4, LegendsPetalburg_Return
    goto_if_lt VAR_0x8004, 6, LegendsPetalburg_Return
    goto_if_gt VAR_0x8004, 7, LegendsPetalburg_Return
    setvar VAR_TEMP_3, 1
LegendsPetalburg_Return:
    return
LegendsPetalburg_Route102Frame:
    map_script_2 VAR_TEMP_3, 1, LegendsPetalburg_WoodsExit
    .2byte 0
LegendsPetalburg_WoodsExit::
    lockall
    setvar VAR_TEMP_3, 0
    goto_if_set FLAG_LA_WOODS_EXIT_THOUGHT, LegendsPetalburg_ExitEnd
    setspeaker SP_NAME_PLAYER
    msgbox LegendsPetalburg_Text_Exit, MSGBOX_DEFAULT
    setflag FLAG_LA_WOODS_EXIT_THOUGHT
    setspeaker SP_NAME_NONE
LegendsPetalburg_ExitEnd:
    releaseall
    end

LegendsPetalburg_Report:
    goto_if_unset FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN, LegendsPetalburg_Return
    goto_if_set FLAG_LA_REPORTED_WOODS_TO_NORMAN, LegendsPetalburg_Return
    setspeaker SP_NAME_PLAYER
    msgbox LegendsPetalburg_Text_Report, MSGBOX_DEFAULT
    setspeaker SP_NAME_NORMAN
    msgbox LegendsPetalburg_Text_Listen, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsPetalburg_Text_Descriptions, MSGBOX_DEFAULT
    setspeaker SP_NAME_NORMAN
    msgbox LegendsPetalburg_Text_Recognizes, MSGBOX_DEFAULT
    closemessage
    setflag FLAG_LA_REPORTED_WOODS_TO_NORMAN
    setvar VAR_LA_PETALBURG_ARC, 1
    return
LegendsPetalburg_LateReport:
    call LegendsPetalburg_Report
    call LegendsPetalburg_RelayToBirch
    return
LegendsPetalburg_RelayToBirch:
    goto_if_unset FLAG_LA_REPORTED_WOODS_TO_NORMAN, LegendsPetalburg_Return
    goto_if_set FLAG_LA_NORMAN_CONTACTED_BIRCH, LegendsPetalburg_Return
    setspeaker SP_NAME_NORMAN
    msgbox LegendsPetalburg_Text_Relay, MSGBOX_DEFAULT
    setflag FLAG_LA_NORMAN_CONTACTED_BIRCH
    setvar VAR_LA_PETALBURG_ARC, 3
    return

LegendsPetalburg_RaltsApproach:
    clearflag FLAG_TEMP_9
    addobject LOCALID_LA_PETALBURG_RALTS
    playmoncry SPECIES_RALTS, CRY_MODE_NORMAL
    waitmoncry
    setspeaker SP_NAME_PLAYER
    msgbox LegendsPetalburg_Text_RaltsUnease, MSGBOX_DEFAULT
    setspeaker SP_NAME_WALLY
    msgbox LegendsPetalburg_Text_Reassure, MSGBOX_DEFAULT
    closemessage
    applymovement LOCALID_LA_PETALBURG_RALTS, LegendsPetalburg_RaltsStep
    waitmovement 0
    delay 24
    setspeaker SP_NAME_WALLY
    msgbox LegendsPetalburg_Text_RaltsTrust, MSGBOX_DEFAULT
    closemessage
    removeobject LOCALID_LA_PETALBURG_RALTS
    setflag FLAG_TEMP_9
    setspeaker SP_NAME_NONE
    return
LegendsPetalburg_RaltsCaught:
    setflag FLAG_LA_WALLY_RALTS_BOND
    goto_if_unset FLAG_LA_REPORTED_WOODS_TO_NORMAN, LegendsPetalburg_CaughtReturn
    goto_if_set FLAG_LA_NORMAN_CONTACTED_BIRCH, LegendsPetalburg_CaughtReturn
    setvar VAR_LA_PETALBURG_ARC, 2
LegendsPetalburg_CaughtReturn:
    setspeaker SP_NAME_WALLY
    return
LegendsPetalburg_RaltsStep:
    walk_left
    face_left
    step_end

LegendsPetalburg_Text_Exit:
    .string "{COLOR LIGHT_BLUE}I can't just keep this to myself.\pProfessor Birch needs to know.\pPetalburg is close. Maybe Norman\ncan help me reach him.$"
LegendsPetalburg_Text_Report:
    .string "{COLOR LIGHT_BLUE}Something happened in the woods.\pI heard two men talking about\nthe rifts. They took something.\pThey said it could keep a portal\nopen and let them control it.\pThey didn't want the professors\nor any of us finding out.$"
LegendsPetalburg_Text_Listen:
    .string "Take a breath. You're safe here.\pTell me what they looked like.$"
LegendsPetalburg_Text_Descriptions:
    .string "{COLOR LIGHT_BLUE}One had dark hair and a suit.\nHe did most of the talking.\pThe other had blue hair,\nand wore a gray uniform.\pI felt like I'd seen them before.\nBut I can't remember where.$"
LegendsPetalburg_Text_Recognizes:
    .string "A dark suit… Blue hair…\pThose descriptions…\nIf they're who I think they are…$"
LegendsPetalburg_Text_Relay:
    .string "Now, about those men.\pI've relayed your account to Birch.\nHe'll contact you soon.\pYou did the right thing coming here.\nLeave the investigation to us.\pDon't follow those men alone.\nIf you see them, find help.\pAnd let Wally enjoy meeting his\npartner. He needn't worry about this.$"
LegendsPetalburg_Text_RaltsUnease:
    .string "{COLOR LIGHT_BLUE}A Ralts… It's watching me.\pCan it feel what I'm feeling?\nI still can't shake those woods.$"
LegendsPetalburg_Text_Reassure:
    .string "It's all right. We're not going\nto hurt you.\pI'm a little nervous, too.\nWe can take this slowly.$"
LegendsPetalburg_Text_RaltsTrust:
    .string "It came closer…\pMaybe it's as lonely as I am.\nI'd really like to be its friend.$"
