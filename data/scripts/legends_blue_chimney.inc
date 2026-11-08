@ Blue joins the investigation without changing the fixed story battle format.
LegendsBlue_FallarborTransition::
    goto_if_lt VAR_LA_OAK_STARTER, 2, LegendsBlue_Return
    goto_if_set FLAG_LA_BLUE_CHIMNEY_BRIEFED, LegendsBlue_Return
    clearflag FLAG_TEMP_7
LegendsBlue_Return:
    return

LegendsBlue_Briefing::
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, RiftResearch_BlueRepeat
    setspeaker SP_NAME_PLAYER
    goto_if_unset FLAG_LA_HEARD_GIOVANNI, LegendsBlue_UnnamedReport
    msgbox BlueChimney_Text_GiovanniReport, MSGBOX_DEFAULT
    goto LegendsBlue_CommonReport
LegendsBlue_UnnamedReport:
    msgbox BlueChimney_Text_WallyReport, MSGBOX_DEFAULT
LegendsBlue_CommonReport:
    setspeaker SP_NAME_BLUE
    msgbox BlueChimney_Text_TakeSeriously, MSGBOX_DEFAULT
    goto_if_unset FLAG_LA_COZMO_BRIEFED, LegendsBlue_BeforeCozmo
    setspeaker SP_NAME_PLAYER
    msgbox BlueChimney_Text_StolenSample, MSGBOX_DEFAULT
    goto LegendsBlue_Plan
LegendsBlue_BeforeCozmo:
    setspeaker SP_NAME_PLAYER
    msgbox BlueChimney_Text_CozmoLead, MSGBOX_DEFAULT
LegendsBlue_Plan:
    setspeaker SP_NAME_BLUE
    msgbox BlueChimney_Text_Plan, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox BlueChimney_Text_PlayerAgrees, MSGBOX_DEFAULT
    setspeaker SP_NAME_BLUE
    msgbox BlueChimney_Text_Station, MSGBOX_DEFAULT
    setflag FLAG_LA_BLUE_CHIMNEY_BRIEFED
    closemessage
    fadescreenswapbuffers FADE_TO_BLACK
    removeobject LOCALID_LA_FALLARBOR_BLUE
    setflag FLAG_TEMP_7
    fadescreenswapbuffers FADE_FROM_BLACK
    goto LegendsAshes_End

LegendsBlue_LeaveWest::
    getobjectfacingdirection LOCALID_PLAYER, VAR_0x8009
    goto_if_ne VAR_0x8009, DIR_WEST, LegendsBlue_End
    setvar VAR_0x8008, DIR_WEST
    goto LegendsBlue_LeaveCheck
LegendsBlue_LeaveEast::
    getobjectfacingdirection LOCALID_PLAYER, VAR_0x8009
    goto_if_ne VAR_0x8009, DIR_EAST, LegendsBlue_End
    setvar VAR_0x8008, DIR_EAST
LegendsBlue_LeaveCheck:
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, LegendsBlue_End
    goto_if_set FLAG_LA_BLUE_CHIMNEY_BRIEFED, LegendsBlue_End
    goto_if_lt VAR_LA_OAK_STARTER, 2, LegendsBlue_End
    lockall
    setspeaker SP_NAME_PLAYER
    msgbox BlueChimney_Text_BeforeLeaving, MSGBOX_DEFAULT
    closemessage
    goto_if_eq VAR_0x8008, DIR_WEST, LegendsBlue_PushEast
    applymovement LOCALID_PLAYER, BlueChimney_Left
    waitmovement 0
    goto LegendsAshes_End
LegendsBlue_PushEast:
    applymovement LOCALID_PLAYER, BlueChimney_Right
    waitmovement 0
    goto LegendsAshes_End
LegendsBlue_End:
    end
BlueChimney_Left:
    walk_left
    step_end
BlueChimney_Right:
    walk_right
    step_end

LegendsBlue_CableTransition::
    setflag FLAG_TEMP_5
    goto_if_unset FLAG_LA_BLUE_CHIMNEY_BRIEFED, LegendsBlue_Return
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, LegendsBlue_Return
    goto_if_set FLAG_LA_BLUE_CHIMNEY_BOARDED, LegendsBlue_Return
    clearflag FLAG_TEMP_5
    return
LegendsBlue_CheckCableBriefing::
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, LegendsBlue_Return
    goto_if_lt VAR_LA_ASHES_STATE, 1, LegendsBlue_Return
    goto_if_unset FLAG_LA_BLUE_CHIMNEY_BRIEFED, LegendsBlue_CableNeedBrief
    goto_if_set FLAG_LA_BLUE_CABLE_MET, LegendsBlue_Return
    goto LegendsBlue_StationMeet
LegendsBlue_CableNeedBrief:
    setspeaker SP_NAME_PLAYER
    msgbox BlueChimney_Text_BeforeLeaving, MSGBOX_DEFAULT
    goto LegendsAshes_End
LegendsBlue_StationMeet::
    goto_if_unset FLAG_LA_BLUE_CHIMNEY_BRIEFED, LegendsBlue_End
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, LegendsBlue_End
    goto_if_set FLAG_LA_BLUE_CHIMNEY_BOARDED, LegendsBlue_End
    lockall
    turnobject LOCALID_PLAYER, DIR_WEST
    turnobject LOCALID_LA_BLUE_CABLE, DIR_EAST
    setspeaker SP_NAME_BLUE
    goto_if_set FLAG_LA_BLUE_CABLE_MET, LegendsBlue_StationRepeat
    msgbox BlueChimney_Text_StationEvidence, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox BlueChimney_Text_CavernReport, MSGBOX_DEFAULT
    setspeaker SP_NAME_BLUE
    msgbox BlueChimney_Text_TeamUp, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox BlueChimney_Text_SummitSplit, MSGBOX_DEFAULT
    setspeaker SP_NAME_BLUE
    msgbox BlueChimney_Text_Ready, MSGBOX_DEFAULT
    setflag FLAG_LA_BLUE_CABLE_MET
    goto LegendsAshes_End
LegendsBlue_StationRepeat:
    msgbox BlueChimney_Text_Ready, MSGBOX_DEFAULT
    goto LegendsAshes_End
LegendsBlue_Board::
    goto_if_unset FLAG_LA_BLUE_CHIMNEY_BRIEFED, LegendsBlue_Return
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, LegendsBlue_Return
    goto_if_set FLAG_LA_BLUE_CHIMNEY_BOARDED, LegendsBlue_Return
    applymovement LOCALID_LA_BLUE_CABLE, BlueChimney_Board
    waitmovement 0
    removeobject LOCALID_LA_BLUE_CABLE
    setflag FLAG_TEMP_5
    setflag FLAG_LA_BLUE_CHIMNEY_BOARDED
    return
BlueChimney_Board:
    walk_up
    walk_up
    walk_right
    walk_up
    walk_up
    step_end

LegendsBlue_SummitTransition::
    setflag FLAG_TEMP_5
    goto_if_unset FLAG_LA_BLUE_CHIMNEY_BOARDED, LegendsBlue_Return
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsBlue_Return
    clearflag FLAG_TEMP_5
    goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, LegendsBlue_SummitReposition
    setobjectxyperm LOCALID_LA_BLUE_CHIMNEY, 24, 20
    return
LegendsBlue_SummitReposition::
    goto_if_unset FLAG_LA_BLUE_CHIMNEY_BOARDED, LegendsBlue_Return
    setobjectxyperm LOCALID_LA_BLUE_CHIMNEY, 12, 8
    setobjectxy LOCALID_LA_BLUE_CHIMNEY, 12, 8
    addobject LOCALID_LA_BLUE_CHIMNEY
    return
LegendsBlue_Perimeter::
    lockall
    faceplayer
    setspeaker SP_NAME_BLUE
    msgbox BlueChimney_Text_Perimeter, MSGBOX_DEFAULT
    goto LegendsAshes_End
LegendsBlue_SummitReport::
    goto_if_unset FLAG_LA_BLUE_CHIMNEY_BOARDED, LegendsBlue_Return
    applymovement LOCALID_LA_BLUE_CHIMNEY, Ashes_UpOne
    waitmovement 0
    turnobject LOCALID_LA_BLUE_CHIMNEY, DIR_EAST
    turnobject LOCALID_PLAYER, DIR_WEST
    setspeaker SP_NAME_BLUE
    msgbox BlueChimney_Text_SummitReport, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox BlueChimney_Text_PlayerReport, MSGBOX_DEFAULT
    return

BlueChimney_Text_GiovanniReport:
    .string "I heard the name Giovanni at the\nPower Plant. Someone was giving orders.\pWally called from Silph in Saffron.\nBlack uniforms, with an R on them.$"
BlueChimney_Text_WallyReport:
    .string "Wally called from Silph in Saffron.\nHe saw people in black uniforms.\pThere was an R on their clothes.\nHe and Kirlia are still trapped there.$"
BlueChimney_Text_TakeSeriously:
    .string "Rocket? And a crossing into Kanto?\pThat's serious. But we need evidence\nbefore we charge into another rift.$"
BlueChimney_Text_StolenSample:
    .string "Magma stole Cozmo's sample and notes.\nThey're taking them through the cavern.\pThen they plan a test on Mt. Chimney.\nMay is following their trail.$"
BlueChimney_Text_CozmoLead:
    .string "May is checking Cozmo's research.\nA meteorite reacts to our recording.\pThat could give us a lead on Wally.$"
BlueChimney_Text_Plan:
    .string "I'll watch the cable-car station.\nKeep following their trail.\pIf anyone moves equipment uphill,\nI'll find out who's helping them.$"
BlueChimney_Text_PlayerAgrees:
    .string "I'll bring you what we find.\nWe do this together.$"
BlueChimney_Text_Station:
    .string "Good. Meet me at the lower station.\nAnd keep that recording safe.$"
BlueChimney_Text_BeforeLeaving:
    .string "Before I leave, I need to brief Blue.\nHe's outside the Pokémon Center.$"
BlueChimney_Text_StationEvidence:
    .string "You're here. Magma sent equipment up.\nAqua cleared the way for them.\pThey're working together.\nWhat did Cozmo find?$"
BlueChimney_Text_CavernReport:
    .string "The meteorite amplifies the signal.\nThey calibrated it at Meteor Falls.\pNow they're using the summit's heat.\nWe have to stop that relay.$"
BlueChimney_Text_TeamUp:
    .string "Then we ride up together.\nI'll hold Aqua at the lower checkpoint.\pYou get through Magma to the machine.\nOne operation, two sides to stop.$"
BlueChimney_Text_SummitSplit:
    .string "Keep our way back clear.\nI'll stop the relay and find May.$"
BlueChimney_Text_Ready:
    .string "Ready when you are.\nTell the attendant we're going up.$"
BlueChimney_Text_Perimeter:
    .string "I've got this approach.\nThey won't close the trail behind you.\pGo! Maxie is at the relay.$"
BlueChimney_Text_SummitReport:
    .string "Aqua pulled back when the relay fell.\nTheir crews were sharing orders.\pI've recorded the equipment markings.\nParadigm needs to see these.$"
BlueChimney_Text_PlayerReport:
    .string "Maxie said they transmitted readings.\nStopping the machine wasn't enough.$"

LegendsBlue_StayWithMay::
    goto_if_unset FLAG_LA_BLUE_CHIMNEY_BOARDED, LegendsBlue_Return
    setspeaker SP_NAME_BLUE
    msgbox BlueChimney_Text_StayWithMay, MSGBOX_DEFAULT
    return
BlueChimney_Text_StayWithMay:
    .string "I'll secure the relay with May\nand contact Paradigm.\pFind Wally. If that passage changes,\nget out of there.$"

BlueChimney_Text_PlayerReturnsMeteorite:
    .string "I recovered the meteorite from the\nrelay. Can you learn what it did?$"
