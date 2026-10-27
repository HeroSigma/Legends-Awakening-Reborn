@ Project-owned Devon Tera laboratory. No donor scripts or save-layout changes.
LegendsTera_Scientist::
    lock
    faceplayer
    goto_if_unset FLAG_RETURNED_DEVON_GOODS, LegendsTera_Locked
    goto_if_unset FLAG_RECEIVED_POKENAV, LegendsTera_Locked
    msgbox LegendsTera_Text_Welcome, MSGBOX_DEFAULT
    closemessage
LegendsTera_Page1:
    multichoice 0, 0, MULTI_LA_TERA_PAGE1, FALSE
    goto_if_eq VAR_RESULT, 6, LegendsTera_Page2
    goto_if_ge VAR_RESULT, 6, LegendsTera_End
    copyvar VAR_0x8005, VAR_RESULT
    goto LegendsTera_ChooseMon
LegendsTera_Page2:
    multichoice 0, 0, MULTI_LA_TERA_PAGE2, FALSE
    goto_if_eq VAR_RESULT, 6, LegendsTera_Page3
    goto_if_ge VAR_RESULT, 6, LegendsTera_End
    copyvar VAR_0x8005, VAR_RESULT
    addvar VAR_0x8005, 6
    goto LegendsTera_ChooseMon
LegendsTera_Page3:
    multichoice 0, 0, MULTI_LA_TERA_PAGE3, FALSE
    goto_if_eq VAR_RESULT, 7, LegendsTera_Page1
    goto_if_ge VAR_RESULT, 7, LegendsTera_End
    copyvar VAR_0x8005, VAR_RESULT
    addvar VAR_0x8005, 12
LegendsTera_ChooseMon:
    special ChoosePartyMon
    goto_if_ge VAR_0x8004, PARTY_SIZE, LegendsTera_End
    special LegendsPrepareTeraChange
    call LegendsTera_CheckResult
    goto_if_ne VAR_RESULT, 0, LegendsTera_End
    bufferitemname STR_VAR_2, VAR_0x8006
    buffernumberstring STR_VAR_3, VAR_0x8007
    msgbox LegendsTera_Text_Confirm, MSGBOX_YESNO
    goto_if_ne VAR_RESULT, YES, LegendsTera_End
    special LegendsCommitTeraChange
    call LegendsTera_CheckResult
    goto_if_ne VAR_RESULT, 0, LegendsTera_End
    playse SE_SUCCESS
    msgbox LegendsTera_Text_Done, MSGBOX_DEFAULT
LegendsTera_End:
    release
    end
LegendsTera_CheckResult:
    goto_if_eq VAR_RESULT, 1, LegendsTera_Short
    goto_if_eq VAR_RESULT, 2, LegendsTera_Egg
    goto_if_eq VAR_RESULT, 3, LegendsTera_Same
    goto_if_eq VAR_RESULT, 4, LegendsTera_NotOpen
    return
LegendsTera_Short:
    msgbox LegendsTera_Text_Short, MSGBOX_DEFAULT
    setvar VAR_RESULT, 1
    return
LegendsTera_Egg:
    msgbox LegendsTera_Text_Egg, MSGBOX_DEFAULT
    setvar VAR_RESULT, 2
    return
LegendsTera_Same:
    msgbox LegendsTera_Text_Same, MSGBOX_DEFAULT
    setvar VAR_RESULT, 3
    return
LegendsTera_NotOpen:
    msgbox LegendsTera_Text_Locked, MSGBOX_DEFAULT
    setvar VAR_RESULT, 4
    return
LegendsTera_Locked:
    msgbox LegendsTera_Text_Locked, MSGBOX_DEFAULT
    goto LegendsTera_End
LegendsTera_Text_Entrance:
    .string "The Tera laboratory is downstairs.\pOur scientist can change Tera Types.$"
LegendsTera_Text_Welcome:
    .string "I can change your partner's Tera Type.\pBring 50 shards of the chosen type.\nStellar requires 150 Stellar Shards.\pWhich Tera Type would you like?$"
LegendsTera_Text_Confirm:
    .string "Change {STR_VAR_1}'s Tera Type?\pCost: {STR_VAR_3} {STR_VAR_2}.$"
LegendsTera_Text_Done:
    .string "The treatment is complete!\pYour partner's Tera Type has changed.$"
LegendsTera_Text_Short:
    .string "You do not have enough matching\nTera Shards for that treatment.$"
LegendsTera_Text_Egg:
    .string "Please choose a hatched POKéMON.$"
LegendsTera_Text_Same:
    .string "Your partner already has that\nTera Type. No shards were used.$"
LegendsTera_Text_Locked:
    .string "The laboratory is not open yet.$"
