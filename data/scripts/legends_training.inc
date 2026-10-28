@ Free preparation service. Summary-screen move relearning stays unchanged.
LegendsTraining_Scientist::
    lock
    faceplayer
    getpartysize
    goto_if_eq VAR_RESULT, 0, LegendsTraining_NoParty
    msgbox LegendsTraining_Text_Welcome, MSGBOX_DEFAULT
LegendsTraining_ChooseMon:
    closemessage
    special ChoosePartyMon
    goto_if_ge VAR_0x8004, PARTY_SIZE, LegendsTraining_End
    copyvar VAR_0x8009, VAR_0x8004
    special LegendsTraining_Inspect
    goto_if_eq VAR_RESULT, 1, LegendsTraining_Egg
LegendsTraining_Main:
    closemessage
    setvar VAR_0x8005, 0
    special LegendsTraining_Menu
    goto_if_ge VAR_RESULT, 8, LegendsTraining_End
    copyvar VAR_0x8008, VAR_RESULT
    goto_if_eq VAR_RESULT, 7, LegendsTraining_PresetsStart
    goto_if_eq VAR_RESULT, 0, LegendsTraining_InspectBuild
    goto_if_eq VAR_RESULT, 2, LegendsTraining_Reset
    goto_if_eq VAR_RESULT, 4, LegendsTraining_Nature
    goto_if_eq VAR_RESULT, 5, LegendsTraining_Ability
    goto_if_eq VAR_RESULT, 6, LegendsTraining_Level
    setvar VAR_0x8006, 0
LegendsTraining_Stats:
    call_if_eq VAR_0x8008, 1, LegendsTraining_ShowEVBudget
    setvar VAR_0x8005, 1
    special LegendsTraining_Menu
    goto_if_eq VAR_RESULT, 6, LegendsTraining_AllIVs
    goto_if_ge VAR_RESULT, 6, LegendsTraining_Main
    copyvar VAR_0x8006, VAR_RESULT
    goto_if_eq VAR_0x8008, 3, LegendsTraining_IV
    setvar VAR_0x8005, 2
    special LegendsTraining_Menu
    goto_if_ge VAR_RESULT, 4, LegendsTraining_Stats
    goto_if_eq VAR_RESULT, 3, LegendsTraining_ExactEV
    setvar VAR_0x8007, 252
    goto_if_eq VAR_RESULT, 0, LegendsTraining_Confirm
    setvar VAR_0x8007, 4
    goto_if_eq VAR_RESULT, 1, LegendsTraining_Confirm
    setvar VAR_0x8007, 0
    goto LegendsTraining_Confirm
LegendsTraining_ShowEVBudget:
    special LegendsTraining_EVBudget
    message gStringVar4
    waitmessage
    return
LegendsTraining_ExactEV:
    setvar VAR_0x8005, 5
    goto LegendsTraining_Number
LegendsTraining_PresetsStart:
    setvar VAR_0x8007, 0
LegendsTraining_Presets:
    setvar VAR_0x8005, 8
    special LegendsTraining_Menu
    goto_if_ge VAR_RESULT, 4, LegendsTraining_Main
    setvar VAR_0x8008, 8
    copyvar VAR_0x8007, VAR_RESULT
    goto LegendsTraining_Confirm
LegendsTraining_AllIVs:
    setvar VAR_0x8006, 6
    setvar VAR_0x8008, 7
    setvar VAR_0x8007, 31
    goto LegendsTraining_Confirm
LegendsTraining_IV:
    setvar VAR_0x8005, 6
    goto LegendsTraining_Number
LegendsTraining_Level:
    setvar VAR_0x8005, 7
LegendsTraining_Number:
    special LegendsTraining_Menu
    goto_if_lt VAR_RESULT, 256, LegendsTraining_Return
    copyvar VAR_0x8007, VAR_RESULT
    subvar VAR_0x8007, 256
    goto LegendsTraining_Confirm
LegendsTraining_Reset:
    setvar VAR_0x8007, 0
    goto LegendsTraining_Confirm
LegendsTraining_Nature:
    setvar VAR_0x8005, 3
    special LegendsTraining_Menu
    goto_if_ge VAR_RESULT, NUM_NATURES, LegendsTraining_Main
    copyvar VAR_0x8007, VAR_RESULT
    goto LegendsTraining_Confirm
LegendsTraining_Ability:
    setvar VAR_0x8005, 4
    special LegendsTraining_Menu
    goto_if_ge VAR_RESULT, NUM_ABILITY_SLOTS, LegendsTraining_Main
    copyvar VAR_0x8007, VAR_RESULT
LegendsTraining_Confirm:
    special LegendsTraining_Prepare
    goto_if_eq VAR_RESULT, 1, LegendsTraining_Egg
    goto_if_eq VAR_RESULT, 2, LegendsTraining_EVLimit
    goto_if_eq VAR_RESULT, 3, LegendsTraining_Illegal
    goto_if_eq VAR_RESULT, 4, LegendsTraining_Same
    msgbox gStringVar4, MSGBOX_YESNO
    goto_if_ne VAR_RESULT, YES, LegendsTraining_Return
    special LegendsTraining_Commit
    goto_if_ne VAR_RESULT, 0, LegendsTraining_Illegal
    playse SE_SUCCESS
    msgbox LegendsTraining_Text_Done, MSGBOX_DEFAULT
    goto_if_ne VAR_0x8008, 6, LegendsTraining_Return
    msgbox LegendsTraining_Text_Level, MSGBOX_DEFAULT
    closemessage
    special LegendsTraining_Evolve
    goto LegendsTraining_Main
LegendsTraining_Return:
    closemessage
    goto_if_eq VAR_0x8008, 1, LegendsTraining_Stats
    goto_if_eq VAR_0x8008, 3, LegendsTraining_Stats
    goto_if_eq VAR_0x8008, 7, LegendsTraining_ReturnIVs
    goto_if_eq VAR_0x8008, 4, LegendsTraining_Nature
    goto_if_eq VAR_0x8008, 5, LegendsTraining_Ability
    goto_if_eq VAR_0x8008, 8, LegendsTraining_Presets
    goto LegendsTraining_Main
LegendsTraining_ReturnIVs:
    setvar VAR_0x8008, 3
    goto LegendsTraining_Stats
LegendsTraining_InspectBuild:
    special LegendsTraining_Inspect
    goto_if_ne VAR_RESULT, 0, LegendsTraining_Egg
    msgbox gStringVar4, MSGBOX_DEFAULT
    goto LegendsTraining_Main
LegendsTraining_EVLimit:
    msgbox LegendsTraining_Text_EVLimit, MSGBOX_DEFAULT
    goto LegendsTraining_Return
LegendsTraining_Illegal:
    msgbox LegendsTraining_Text_Illegal, MSGBOX_DEFAULT
    goto LegendsTraining_Return
LegendsTraining_Same:
    msgbox LegendsTraining_Text_Same, MSGBOX_DEFAULT
    goto LegendsTraining_Return
LegendsTraining_Egg:
    msgbox LegendsTraining_Text_Egg, MSGBOX_DEFAULT
    goto LegendsTraining_ChooseMon
LegendsTraining_NoParty:
    msgbox LegendsTraining_Text_NoParty, MSGBOX_DEFAULT
LegendsTraining_End:
    release
    end
LegendsTraining_Text_Welcome:
    .string "I help partners reach their potential.\nAll training here is free.\pChoose a POKéMON to get started.$"
LegendsTraining_Text_Done:
    .string "Your partner's training is complete!$"
LegendsTraining_Text_Level:
    .string "Review new moves in the summary.\nYour partner may also evolve now.$"
LegendsTraining_Text_EVLimit:
    .string "That would exceed 510 total EVs.\pLower another stat or reset all EVs,\nthen try that training again.$"
LegendsTraining_Text_Illegal:
    .string "That change isn't available.\pTraining respects the level cap\nand your partner's legal Abilities.$"
LegendsTraining_Text_Same:
    .string "Your partner already has that setting.\nNo change is needed.$"
LegendsTraining_Text_Egg:
    .string "Please choose a hatched POKéMON.$"

LegendsTraining_Text_NoParty:
    .string "Bring a POKéMON partner with you.\nI will be happy to help you train.$"
