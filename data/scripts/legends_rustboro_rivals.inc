@ May appears for both protagonists; Silver's loss checkpoint is independent.
LegendsRustboro_SetupSilver:
    setflag FLAG_LA_HIDE_RUSTBORO_SILVER
    goto_if_unset FLAG_LA_MET_SILVER, LegendsRustboro_Return
    goto_if_set FLAG_LA_DEFEATED_SILVER_RUSTBORO, LegendsRustboro_Return
    clearflag FLAG_LA_HIDE_RUSTBORO_SILVER
    setobjectxyperm LOCALID_LA_RUSTBORO_SILVER, 18, 54
LegendsRustboro_Return:
    return

LegendsRustboro_CheckSilverRetry:
    goto_if_unset FLAG_LA_DEFEATED_SILVER_RUSTBORO, LegendsRustboro_SilverRetry
    goto RustboroCity_EventScript_MayEncounter

LegendsRustboro_SilverInteract::
    lockall
    goto_if_set FLAG_LA_DEFEATED_SILVER_RUSTBORO, LegendsRustboro_Release
    goto LegendsRustboro_SilverRetry

LegendsRustboro_SilverScene::
    lockall
    goto_if_set FLAG_LA_MET_SILVER, LegendsRustboro_CheckSilverRetry
    setspeaker SP_NAME_MAY
    msgbox LegendsRustboroRivals_Text_MayHeal, MSGBOX_DEFAULT
    closemessage
    special HealPlayerParty
    fadescreen FADE_TO_BLACK
    setobjectxy LOCALID_PLAYER, 18, 55
    setobjectxy LOCALID_RUSTBORO_RIVAL, 17, 54
    clearflag FLAG_LA_HIDE_RUSTBORO_SILVER
    setobjectxyperm LOCALID_LA_RUSTBORO_SILVER, 18, 48
    addobject LOCALID_LA_RUSTBORO_SILVER
    turnobject LOCALID_PLAYER, DIR_NORTH
    turnobject LOCALID_RUSTBORO_RIVAL, DIR_NORTH
    fadescreen FADE_FROM_BLACK
    setspeaker SP_NAME_NONE
    msgbox LegendsRustboroRivals_Text_Offscreen, MSGBOX_DEFAULT
    closemessage
    applymovement LOCALID_LA_RUSTBORO_SILVER, LegendsRustboro_SilverApproach
    waitmovement 0
    turnobject LOCALID_RUSTBORO_RIVAL, DIR_EAST
    setspeaker SP_NAME_MAY
    msgbox LegendsRustboroRivals_Text_MayStartled, MSGBOX_DEFAULT
    setspeaker SP_NAME_SILVER
    msgbox LegendsRustboroRivals_Text_Where, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsRustboroRivals_Text_Hoenn, MSGBOX_DEFAULT
    setspeaker SP_NAME_SILVER
    msgbox LegendsRustboroRivals_Text_Johto, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsRustboroRivals_Text_Rift, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsRustboroRivals_Text_Introduce, MSGBOX_DEFAULT
    setspeaker SP_NAME_SILVER
    msgbox LegendsRustboroRivals_Text_Name, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsRustboroRivals_Text_Partner, MSGBOX_DEFAULT
    setspeaker SP_NAME_SILVER
    msgbox LegendsRustboroRivals_Text_Challenge, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsRustboroRivals_Text_Accept, MSGBOX_DEFAULT
    setspeaker SP_NAME_SILVER
    msgbox LegendsRustboroRivals_Text_Totodile, MSGBOX_DEFAULT
    setflag FLAG_LA_MET_SILVER
    goto LegendsRustboro_SilverBattle

LegendsRustboro_SilverRetry:
    lockall
    setspeaker SP_NAME_MAY
    msgbox LegendsRustboroRivals_Text_RetryHeal, MSGBOX_DEFAULT
    closemessage
    fadescreen FADE_TO_BLACK
    setobjectxy LOCALID_PLAYER, 18, 55
    setobjectxy LOCALID_RUSTBORO_RIVAL, 17, 54
    setobjectxy LOCALID_LA_RUSTBORO_SILVER, 18, 54
    turnobject LOCALID_PLAYER, DIR_NORTH
    turnobject LOCALID_RUSTBORO_RIVAL, DIR_EAST
    turnobject LOCALID_LA_RUSTBORO_SILVER, DIR_SOUTH
    special HealPlayerParty
    fadescreen FADE_FROM_BLACK
    setspeaker SP_NAME_SILVER
    msgbox LegendsRustboroRivals_Text_Retry, MSGBOX_DEFAULT
LegendsRustboro_SilverBattle:
    setspeaker SP_NAME_NONE
    closemessage
    special HealPlayerParty
    trainerbattle_no_intro TRAINER_SILVER_RUSTBORO, LegendsRustboroRivals_Text_Defeat
    setflag FLAG_LA_DEFEATED_SILVER_RUSTBORO
    special HealPlayerParty
    setspeaker SP_NAME_SILVER
    msgbox LegendsRustboroRivals_Text_Admission, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsRustboroRivals_Text_Offer, MSGBOX_DEFAULT
    setspeaker SP_NAME_SILVER
    msgbox LegendsRustboroRivals_Text_Leave, MSGBOX_DEFAULT
    closemessage
    applymovement LOCALID_LA_RUSTBORO_SILVER, LegendsRustboro_SilverExit
    waitmovement 0
    removeobject LOCALID_LA_RUSTBORO_SILVER
    setflag FLAG_LA_HIDE_RUSTBORO_SILVER
    setspeaker SP_NAME_MAY
    msgbox LegendsRustboroRivals_Text_After, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsRustboroRivals_Text_Report, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsRustboroRivals_Text_Briney, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsRustboroRivals_Text_Farewell, MSGBOX_DEFAULT
    closemessage
    applymovement LOCALID_RUSTBORO_RIVAL, LegendsRustboro_MayReturn
    waitmovement 0
    call RustboroCity_EventScript_RestoreBgm
LegendsRustboro_Release:
    setspeaker SP_NAME_NONE
    releaseall
    end

LegendsRustboro_SilverApproach:
    walk_down
    walk_down
    walk_down
    walk_down
    walk_down
    walk_down
    face_down
    step_end
LegendsRustboro_SilverExit:
    walk_up
    walk_up
    walk_up
    walk_up
    walk_up
    walk_up
    step_end
LegendsRustboro_MayReturn:
    walk_up
    walk_up
    walk_left
    face_down
    step_end

LegendsRustboroRivals_Text_PlayerNav:
    .string "Mr. Stone gave it to me. I've got\nsome deliveries to make for Devon.$"
LegendsRustboroRivals_Text_MayHeal:
    .string "That was a good battle!\pHere, let me look after your team.\nYou've still got a journey ahead.$"
LegendsRustboroRivals_Text_Offscreen:
    .string "{COLOR RED}You two. Hold on.$"
LegendsRustboroRivals_Text_MayStartled:
    .string "Oh! Did you need something?$"
LegendsRustboroRivals_Text_Where:
    .string "You looked like you knew what you\nwere doing. So tell me.\pWhat town is this?$"
LegendsRustboroRivals_Text_Hoenn:
    .string "Rustboro City. You're in Hoenn.\pAre you lost?$"
LegendsRustboroRivals_Text_Johto:
    .string "Hoenn…?\pI was heading toward Ecruteak.\nThat's in Johto.\pHow did I end up across the sea?$"
LegendsRustboroRivals_Text_Rift:
    .string "You might have come through a rift.\nYou're not the first person we've met\lwho's arrived that way.$"
LegendsRustboroRivals_Text_Introduce:
    .string "I'm {PLAYER}. This is May.\nWhat's your name?$"
LegendsRustboroRivals_Text_Name:
    .string "Silver. Remember it.\pIf I'm stuck here, I won't sit around\nwaiting for someone to sort it out.$"
LegendsRustboroRivals_Text_Partner:
    .string "And you've got a Totodile!\nDid your team come through with you?$"
LegendsRustboroRivals_Text_Challenge:
    .string "They're with me. I can look after\nmy own Pokémon.\pYou held your own against her.\nLet's see if you can beat me.$"
LegendsRustboroRivals_Text_Accept:
    .string "I'll battle. But afterward, tell us\nwhat happened before you got here.$"
LegendsRustboroRivals_Text_Totodile:
    .string "If you can win.\pTotodile, we'll show them.$"
LegendsRustboroRivals_Text_RetryHeal:
    .string "I'll get your team ready again.\pSilver's still waiting. You won't\nhave to battle me again first.$"
LegendsRustboroRivals_Text_Retry:
    .string "Back already? Good.\nLet's finish this.$"
LegendsRustboroRivals_Text_Defeat:
    .string "Tch… Don't get used to winning.$"
LegendsRustboroRivals_Text_Admission:
    .string "Fine. You won.\pThere was an opening ahead of me.\nRed light. Cold air.\pI stepped through, and suddenly I\nwas on the cliffs north of here.$"
LegendsRustboroRivals_Text_Offer:
    .string "Professor Birch is investigating\nthe rifts. You could talk to him.\pYou don't have to figure this out\non your own.$"
LegendsRustboroRivals_Text_Leave:
    .string "I'll find my own answers.\pKeep training. Next time,\ndon't expect the same result.$"
LegendsRustboroRivals_Text_After:
    .string "He didn't even wait for directions.\pI hope he finds someone to talk to.$"
LegendsRustboroRivals_Text_Report:
    .string "Another traveler from a rift…\nI'll tell the Professor about him.$"
LegendsRustboroRivals_Text_Briney:
    .string "I'll let Dad know too.\pI passed Mr. Briney in the woods.\nHe was heading home to his cottage.\pIf you need to get across the sea,\nhe's the person to ask.$"
LegendsRustboroRivals_Text_Farewell:
    .string "Then that's my next stop.\nTake care, May.$"
