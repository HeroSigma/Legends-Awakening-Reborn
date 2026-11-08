@ Pokémon Center training and Egg Move tutor.
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
    goto_if_ge VAR_RESULT, 10, LegendsTraining_End
    copyvar VAR_0x8008, VAR_RESULT
    goto_if_eq VAR_RESULT, 9, LegendsTraining_EggMoves
    goto_if_eq VAR_RESULT, 7, LegendsTraining_Friendship
    goto_if_eq VAR_RESULT, 6, LegendsTraining_Level
    goto LegendsTraining_End
LegendsTraining_Friendship:
    setvar VAR_0x8008, 8
    goto LegendsTraining_Confirm
LegendsTraining_Level:
    setvar VAR_0x8005, 7
LegendsTraining_Number:
    special LegendsTraining_Menu
    goto_if_lt VAR_RESULT, 256, LegendsTraining_Return
    copyvar VAR_0x8007, VAR_RESULT
    subvar VAR_0x8007, 256
    goto LegendsTraining_Confirm
LegendsTraining_EggMoves:
    setvar VAR_0x8005, 8
    special LegendsTraining_Menu
    goto_if_eq VAR_RESULT, 254, LegendsTraining_NoEggMoves
    goto_if_lt VAR_RESULT, 256, LegendsTraining_Return
    copyvar VAR_0x8007, VAR_RESULT
    subvar VAR_0x8007, 256
    setvar VAR_0x8006, MAX_MON_MOVES
    goto LegendsTraining_Confirm
LegendsTraining_ReplaceMove:
    msgbox LegendsTraining_Text_ReplaceMove, MSGBOX_DEFAULT
    closemessage
    setvar VAR_0x8005, 9
    special LegendsTraining_Menu
    goto_if_ge VAR_RESULT, MAX_MON_MOVES, LegendsTraining_Return
    copyvar VAR_0x8006, VAR_RESULT
    goto LegendsTraining_Confirm
LegendsTraining_NoEggMoves:
    msgbox LegendsTraining_Text_NoEggMoves, MSGBOX_DEFAULT
    goto LegendsTraining_Return
LegendsTraining_NoMoney:
    msgbox LegendsTraining_Text_NoMoney, MSGBOX_DEFAULT
    goto LegendsTraining_Return
LegendsTraining_Confirm:
    special LegendsTraining_Prepare
    goto_if_eq VAR_RESULT, 1, LegendsTraining_Egg
    goto_if_eq VAR_RESULT, 2, LegendsTraining_EVLimit
    goto_if_eq VAR_RESULT, 3, LegendsTraining_Illegal
    goto_if_eq VAR_RESULT, 4, LegendsTraining_Same
    goto_if_eq VAR_RESULT, 5, LegendsTraining_NoMoney
    goto_if_eq VAR_RESULT, 6, LegendsTraining_ReplaceMove
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
    .string "I offer free level catch-up and\nfriendship training.\pI also teach Egg Moves for\n¥2,000 each.\pFor individual stats, press START\non the summary's Stats page.\pChoose a POKéMON to train.$"
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

LegendsTraining_Text_ReplaceMove:
    .string "Which move should your partner\nforget?$"
LegendsTraining_Text_NoEggMoves:
    .string "I have no new Egg Moves to teach\nthis POKéMON.$"
LegendsTraining_Text_NoMoney:
    .string "You need ¥2,000 to learn that move.$"
