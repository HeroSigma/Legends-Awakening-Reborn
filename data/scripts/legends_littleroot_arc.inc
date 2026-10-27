@ Project-owned Littleroot chapter. No donor story state or save-layout changes.
LegendsArc_SetupLab:
    setflag FLAG_LA_HIDE_RED_IN_LAB
    setflag FLAG_LA_HIDE_ARC_LAB_RIVALS
    goto_if_unset FLAG_LA_MET_RED, LegendsArc_Return
    goto_if_eq VAR_BIRCH_LAB_STATE, 2, LegendsArc_ShowLabRed
    goto_if_eq VAR_LA_LITTLEROOT_ARC, 1, LegendsArc_ShowLabRed
    goto_if_unset FLAG_LA_RED_ROUTE103_COMPLETE, LegendsArc_Return
    goto_if_eq VAR_LA_LITTLEROOT_ARC, 3, LegendsArc_ShowLabReturn
    goto_if_ne VAR_BIRCH_LAB_STATE, 4, LegendsArc_Return
LegendsArc_ShowLabReturn:
    setflag FLAG_HIDE_LITTLEROOT_TOWN_BIRCHS_LAB_RIVAL
    clearflag FLAG_LA_HIDE_ARC_LAB_RIVALS
LegendsArc_ShowLabRed:
    clearflag FLAG_LA_HIDE_RED_IN_LAB
    goto_if_ne VAR_BIRCH_LAB_STATE, 2, LegendsArc_Return
    setobjectxyperm LOCALID_LA_LAB_RED, 5, 4
LegendsArc_Return:
    return

LegendsArc_SetupRoute103:
    setflag FLAG_LA_HIDE_ARC_ROUTE103_ACTORS
    goto_if_unset FLAG_LA_RED_LAB_COMPLETE, LegendsArc_Return
    setflag FLAG_HIDE_ROUTE_103_RIVAL
    goto_if_set FLAG_LA_RED_ROUTE103_COMPLETE, LegendsArc_Return
    clearflag FLAG_LA_HIDE_ARC_ROUTE103_ACTORS
    return

LegendsArc_LabIntro::
    lockall
    turnobject LOCALID_LA_LAB_RED, DIR_EAST
    turnobject LOCALID_LA_LAB_PIKACHU, DIR_EAST
    goto_if_set FLAG_LA_RED_LAB_COMPLETE, LegendsArc_LabDispatch
    turnobject LOCALID_BIRCHS_LAB_BIRCH, DIR_WEST
    setspeaker SP_NAME_BIRCH
    msgbox LegendsArc_Text_BirchRecognizes, MSGBOX_DEFAULT
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_PortalArrival, MSGBOX_DEFAULT
    turnobject LOCALID_BIRCHS_LAB_BIRCH, DIR_SOUTH
    setspeaker SP_NAME_BIRCH
    msgbox LegendsArc_Text_KeepStarter, MSGBOX_DEFAULT
    bufferleadmonspeciesname STR_VAR_1
    msgbox LittlerootTown_ProfessorBirchsLab_Text_WhyNotGiveNicknameToMon, MSGBOX_YESNO
    call_if_eq VAR_RESULT, YES, LegendsArc_NameStarter
    closemessage
    applymovement LOCALID_LA_LAB_RED, LegendsArc_LabRedStepDown
    waitmovement 0
    call LegendsArc_LabFaceEachOther
    setspeaker SP_NAME_PLAYER
    msgbox LegendsArc_Text_PlayerIntroduction, MSGBOX_DEFAULT
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_RedIntroduction, MSGBOX_DEFAULT
    turnobject LOCALID_LA_LAB_RED, DIR_NORTH
    turnobject LOCALID_LA_LAB_PIKACHU, DIR_EAST
    turnobject LOCALID_BIRCHS_LAB_BIRCH, DIR_WEST
    setspeaker SP_NAME_BIRCH
    msgbox LegendsArc_Text_RioluGift, MSGBOX_DEFAULT
    call LegendsArc_LabFaceEachOther
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_RedChallenge, MSGBOX_DEFAULT
    closemessage
    special HealPlayerParty
    setflag FLAG_LA_RED_LAB_BATTLE
    setvar VAR_LA_LITTLEROOT_ARC, 1
    trainerbattle_earlyrival TRAINER_LA_RED_FRESH_START, RIVAL_BATTLE_HEAL_AFTER, LegendsArc_Text_RedDefeated, LegendsArc_Text_RedVictory
    clearflag FLAG_LA_RED_LAB_BATTLE
    special HealPlayerParty
    call LegendsArc_LabFaceEachOther
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_RedCongratulates, MSGBOX_DEFAULT
    goto_if_set FLAG_LA_RECEIVED_RED_MEGA_RING, LegendsArc_AfterMegaRing
    giveitem ITEM_MEGA_RING
    goto_if_eq VAR_RESULT, FALSE, LegendsArc_RingBagFull
    setflag FLAG_LA_RECEIVED_RED_MEGA_RING
LegendsArc_AfterMegaRing:
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_MegaRingFuture, MSGBOX_DEFAULT
    setflag FLAG_LA_RED_LAB_COMPLETE
LegendsArc_LabDispatch:
    turnobject LOCALID_PLAYER, DIR_NORTH
    turnobject LOCALID_LA_LAB_RED, DIR_NORTH
    turnobject LOCALID_LA_LAB_PIKACHU, DIR_EAST
    turnobject LOCALID_BIRCHS_LAB_BIRCH, DIR_SOUTH
    setspeaker SP_NAME_BIRCH
    msgbox LegendsArc_Text_FindBothRivals, MSGBOX_DEFAULT
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_RedHeadsAhead, MSGBOX_DEFAULT
    closemessage
    applymovement LOCALID_LA_LAB_RED, LegendsArc_LabRedExit
    applymovement LOCALID_LA_LAB_PIKACHU, LegendsArc_LabPikachuExit
    waitmovement 0
    removeobject LOCALID_LA_LAB_RED
    removeobject LOCALID_LA_LAB_PIKACHU
    setflag FLAG_LA_HIDE_RED_IN_LAB
    clearflag FLAG_HIDE_ROUTE_101_BOY
    setvar VAR_BIRCH_LAB_STATE, 3
    setvar VAR_LA_LITTLEROOT_ARC, 2
    releaseall
    end
LegendsArc_NameStarter:
    setvar VAR_0x8004, 0
    call Common_EventScript_NameReceivedPartyMon
    return
LegendsArc_RingBagFull:
    setvar VAR_BIRCH_LAB_STATE, 3
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_RingBagFull, MSGBOX_DEFAULT
    releaseall
    end

LegendsArc_Route103Meeting::
    lockall
    goto_if_unset FLAG_LA_RED_LAB_COMPLETE, LegendsArc_NotReady
    goto_if_set FLAG_LA_RED_ROUTE103_COMPLETE, LegendsArc_NotReady
    getplayerxy VAR_0x8004, VAR_0x8005
    call_if_eq VAR_0x8005, 5, LegendsArc_Route103Approach
    turnobject LOCALID_PLAYER, DIR_NORTH
    turnobject LOCALID_LA_ROUTE103_RED, DIR_NORTH
    turnobject LOCALID_LA_ROUTE103_PIKACHU, DIR_WEST
    turnobject LOCALID_LA_ROUTE103_BRENDAN, DIR_SOUTH
    turnobject LOCALID_LA_ROUTE103_MAY, DIR_SOUTH
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsArc_Text_BrendanRecognizes, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsArc_Text_MayRecognizes, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsArc_Text_PlayerChampionQuestion, MSGBOX_DEFAULT
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_RedExplains, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsArc_Text_MayRiftQuestion, MSGBOX_DEFAULT
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_RedFreshStart, MSGBOX_DEFAULT
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsArc_Text_BrendanDoubleChallenge, MSGBOX_DEFAULT
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_RedPartnerAdvice, MSGBOX_DEFAULT
    closemessage
    special HealPlayerParty
    setflag FLAG_LA_ROUTE103_PARTNER_BATTLE
    switch VAR_STARTER_MON
    case 0, LegendsArc_Double0
    case 1, LegendsArc_Double1
    case 2, LegendsArc_Double2
    goto LegendsArc_Double0
LegendsArc_Double0:
    multi_fixed_2_vs_2 TRAINER_LA_BRENDAN_ROUTE103_0, LegendsArc_Text_BrendanDefeat, TRAINER_LA_MAY_ROUTE103_0, LegendsArc_Text_MayDefeat, PARTNER_LA_RED_FRESH_START
    goto LegendsArc_AfterDouble
LegendsArc_Double1:
    multi_fixed_2_vs_2 TRAINER_LA_BRENDAN_ROUTE103_1, LegendsArc_Text_BrendanDefeat, TRAINER_LA_MAY_ROUTE103_1, LegendsArc_Text_MayDefeat, PARTNER_LA_RED_FRESH_START
    goto LegendsArc_AfterDouble
LegendsArc_Double2:
    multi_fixed_2_vs_2 TRAINER_LA_BRENDAN_ROUTE103_2, LegendsArc_Text_BrendanDefeat, TRAINER_LA_MAY_ROUTE103_2, LegendsArc_Text_MayDefeat, PARTNER_LA_RED_FRESH_START
LegendsArc_AfterDouble:
    clearflag FLAG_LA_ROUTE103_PARTNER_BATTLE
    special HealPlayerParty
    goto_if_ne VAR_RESULT, B_OUTCOME_WON, LegendsArc_DoubleRetry
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsArc_Text_BrendanAfterDouble, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsArc_Text_MayAfterDouble, MSGBOX_DEFAULT
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_RedAfterDouble, MSGBOX_DEFAULT
    closemessage
    setflag FLAG_LA_RED_ROUTE103_COMPLETE
    setflag FLAG_DEFEATED_RIVAL_ROUTE103
    setflag FLAG_HIDE_ROUTE_103_RIVAL
    setvar VAR_BIRCH_LAB_STATE, 4
    setvar VAR_LA_LITTLEROOT_ARC, 3
    fadescreen FADE_TO_BLACK
    removeobject LOCALID_LA_ROUTE103_RED
    removeobject LOCALID_LA_ROUTE103_PIKACHU
    removeobject LOCALID_LA_ROUTE103_BRENDAN
    removeobject LOCALID_LA_ROUTE103_MAY
    setflag FLAG_LA_HIDE_ARC_ROUTE103_ACTORS
    fadescreen FADE_FROM_BLACK
    releaseall
    end
LegendsArc_DoubleRetry:
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_DoubleRetry, MSGBOX_DEFAULT
LegendsArc_NotReady:
    releaseall
    end

LegendsArc_DexGifts::
    closemessage
    applymovement LOCALID_LA_LAB_RED, LegendsArc_LabRedApproach
    waitmovement 0
    goto_if_set FLAG_LA_RED_DEX_GIFTS, LegendsArc_DexFinish
    turnobject LOCALID_BIRCHS_LAB_BIRCH, DIR_SOUTH
    setspeaker SP_NAME_BIRCH
    msgbox LegendsArc_Text_BirchResearch, MSGBOX_DEFAULT
    turnobject LOCALID_BIRCHS_LAB_BIRCH, DIR_WEST
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_RedResearch, MSGBOX_DEFAULT
    turnobject LOCALID_BIRCHS_LAB_BIRCH, DIR_SOUTH
    setspeaker SP_NAME_BIRCH
    msgbox LegendsArc_Text_NationalDexGift, MSGBOX_DEFAULT
    call LittlerootTown_ProfessorBirchsLab_EventScript_ReceivePokedex
    setflag FLAG_SYS_NATIONAL_DEX
    special EnableNationalPokedex
    setflag FLAG_LA_DEXNAV_RECEIVED
    setspeaker SP_NAME_BIRCH
    msgbox LegendsArc_Text_DexNavGift, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsArc_Text_MayPokeBalls, MSGBOX_DEFAULT
    giveitem ITEM_POKE_BALL, 5
    goto_if_eq VAR_RESULT, FALSE, LegendsArc_DexBagFull
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsArc_Text_BrendanResearch, MSGBOX_DEFAULT
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_RedFarewell, MSGBOX_DEFAULT
    closemessage
    setflag FLAG_LA_RED_DEX_GIFTS
    applymovement LOCALID_LA_LAB_RED, LegendsArc_LabRedExit
    applymovement LOCALID_LA_LAB_PIKACHU, LegendsArc_LabPikachuExit
    waitmovement 0
    removeobject LOCALID_LA_LAB_RED
    removeobject LOCALID_LA_LAB_PIKACHU
    setflag FLAG_LA_HIDE_RED_IN_LAB
LegendsArc_DexFinish:
    setvar VAR_BIRCH_LAB_STATE, 5
    setflag FLAG_ADVENTURE_STARTED
    setvar VAR_OLDALE_TOWN_STATE, 1
    setvar VAR_LITTLEROOT_RIVAL_STATE, 4
    setvar VAR_LITTLEROOT_TOWN_STATE, 3
    setvar VAR_LA_LITTLEROOT_ARC, 4
    releaseall
    end
LegendsArc_DexBagFull:
    setvar VAR_BIRCH_LAB_STATE, 3
    setspeaker SP_NAME_MAY
    msgbox LegendsArc_Text_DexBagFull, MSGBOX_DEFAULT
    releaseall
    end

LegendsArc_ElaraShoes::
    setspeaker SP_NAME_MOM
    msgbox LegendsArc_Text_ElaraAsk, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsArc_Text_PlayerTellsElara, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsArc_Text_ElaraAbsorbs, MSGBOX_DEFAULT
    setspeaker SP_NAME_NONE
    msgbox LegendsArc_Text_ElaraThought, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsArc_Text_ElaraShoes, MSGBOX_DEFAULT
    playfanfare MUS_OBTAIN_ITEM
    message LittlerootTown_Text_SwitchShoesWithRunningShoes
    waitfanfare
    setflag FLAG_RECEIVED_RUNNING_SHOES
    msgbox LegendsArc_Text_ElaraTakeCare, MSGBOX_DEFAULT
    setflag FLAG_LA_ELARA_CAELUM_FAREWELL
    setvar VAR_LA_LITTLEROOT_ARC, 5
    closemessage
    return

LegendsArc_CompanionTalk::
    goto_if_unset FLAG_LA_RED_LAB_COMPLETE, LegendsArc_ClaimRing
    lock
    faceplayer
    setspeaker SP_NAME_RED
    msgbox LegendsArc_Text_Companion, MSGBOX_DEFAULT
    release
    end

@ Both paths stay in the lab's central aisle; Pikachu follows one step behind.
LegendsArc_LabRedExit:
    walk_down
    walk_right
    walk_down
    walk_down
    walk_down
    walk_down
    walk_down
    walk_down
    set_invisible
    step_end
LegendsArc_LabPikachuExit:
    walk_down
    walk_down
    walk_right
    walk_right
    walk_down
    walk_down
    walk_down
    walk_down
    walk_down
    walk_down
    set_invisible
    step_end

LegendsArc_Text_BirchRecognizes:
    .string "Red?! I know that face anywhere!\pBut how did you get to Hoenn?$"

LegendsArc_Text_PortalArrival:
    .string "{COLOR RED}Pikachu and I came through a portal.\pOne moment we were travelling.\pThe next, we were here.\pI travelled through Hoenn before.\pI remembered the road to your lab.$"

LegendsArc_Text_KeepStarter:
    .string "Then the rifts carry people too…\pFor now, both of you are safe.\p{PLAYER}, keep the partner you\nchose.\pYou stood together when it mattered.$"

LegendsArc_Text_PlayerIntroduction:
    .string "{COLOR LIGHT_BLUE}We never introduced ourselves.\pMy name is {PLAYER}.\pThank you for saving us.$"

LegendsArc_Text_RedIntroduction:
    .string "{COLOR RED}Red. Glad to meet you properly.\pHow about a battle?\pPikachu would be too much right now.\pProfessor, may I raise a new\npartner?$"

LegendsArc_Text_RioluGift:
    .string "This Riolu was found near a rift.\pIts species is native to Sinnoh.\nFinding one here was quite a surprise.\pAn aide brought it to my lab.\nI have been helping it settle in.\pIt needs more than observation.\nIt needs someone it can trust.\pIf it is willing, Red, I would like\nyou to travel together.$"

LegendsArc_Text_RedChallenge:
    .string "{COLOR RED}All right, Riolu. A fresh start.\p{PLAYER}, show me how you and your\ppartner work together.$"

LegendsArc_Text_RedDefeated:
    .string "{COLOR RED}You surprised me. Well battled!$"

LegendsArc_Text_RedVictory:
    .string "{COLOR RED}You held your ground. Well done.$"

LegendsArc_Text_RedCongratulates:
    .string "{COLOR RED}You held your own for a new trainer.\pYou watched, and you kept trying.\pExperience makes a difference.\pKeep building trust with your\npartner.$"

LegendsArc_Text_MegaRingFuture:
    .string "{COLOR RED}That is a Mega Ring.\pIt will come in handy in the future.\pWhen you find a matching Mega Stone,\pyour bond can unlock more power.$"

LegendsArc_Text_FindBothRivals:
    .string "Brendan and May are on Route 103.\pPlease call them back to the lab.\pI have research equipment for you.$"

LegendsArc_Text_RedHeadsAhead:
    .string "{COLOR RED}I will go on ahead and find them.\pCome on, Pikachu. Stay close.$"

LegendsArc_Text_RingBagFull:
    .string "{COLOR RED}Make room for this ring first.\pI will keep it safe until you do.$"

LegendsArc_Text_BrendanRecognizes:
    .string "{COLOR GREEN}Wait… Red?!\pThe Champion from Kanto?!$"

LegendsArc_Text_MayRecognizes:
    .string "{COLOR RED}It really is you! And Pikachu!\pDad never said you were visiting!$"

LegendsArc_Text_PlayerChampionQuestion:
    .string "{COLOR LIGHT_BLUE}Champion…?\pYou are Kanto's Champion?$"

LegendsArc_Text_RedExplains:
    .string "{COLOR RED}That is where my journey began.\pBut a title does not explain a rift.\pI came through one with Pikachu.\pNow I want to understand why.$"

LegendsArc_Text_MayRiftQuestion:
    .string "{COLOR RED}You came through a rift yourself?\pThen the sightings are only part of\nit.$"

LegendsArc_Text_RedFreshStart:
    .string "{COLOR RED}I know my way around Hoenn.\pThis time, I am starting fresh.\pNew partners. New things to learn.\pPikachu is still coming with me.$"

LegendsArc_Text_BrendanDoubleChallenge:
    .string "{COLOR GREEN}Then let us help with that!\pMay and me against you two.\pA double battle!$"

LegendsArc_Text_RedPartnerAdvice:
    .string "{COLOR RED}Ready, {PLAYER}? Watch both\nopponents.\pRiolu and I will back you up.\pPikachu, stay here and watch.$"

LegendsArc_Text_BrendanDefeat:
    .string "{COLOR GREEN}So that is fighting a Champion…$"

LegendsArc_Text_MayDefeat:
    .string "{COLOR RED}You two made a good team!$"

LegendsArc_Text_BrendanAfterDouble:
    .string "{COLOR GREEN}Even with a new partner… Wow.\p{PLAYER}, you kept up with him!$"

LegendsArc_Text_MayAfterDouble:
    .string "{COLOR RED}Dad wants us back at the lab?\pLet us go. We have plenty to tell\nhim.$"

LegendsArc_Text_RedAfterDouble:
    .string "{COLOR RED}Well battled, all of you.\pA new team still learns every day.\pLet us bring the Professor his\nnotes.$"

LegendsArc_Text_DoubleRetry:
    .string "{COLOR RED}Everyone needs practice together.\pI have healed your partners.\pSpeak to us when you want to try\nagain.$"

LegendsArc_Text_BirchResearch:
    .string "You have all seen what is happening.\pPOKéMON from distant places…\pAnd now, people crossing the rifts.\pWe need careful records, not\nguesses.$"

LegendsArc_Text_RedResearch:
    .string "{COLOR RED}I will investigate what I can.\pThere may be other travellers.\pIf we share what we learn, it helps.$"

LegendsArc_Text_NationalDexGift:
    .string "{PLAYER}, this is your POKéDEX.\pI have enabled its National records.\pA Hoenn-only list is no longer\nenough.$"

LegendsArc_Text_DexNavGift:
    .string "I have also installed the DexNav.\pIt helps you find and study POKéMON.\pSearch the habitats around you.\pDifferent times bring different\nsights.$"

LegendsArc_Text_MayPokeBalls:
    .string "{COLOR RED}Here. Take these POKé BALLS too.\pLet your new partner make some\nfriends!$"

LegendsArc_Text_BrendanResearch:
    .string "{COLOR GREEN}And remember, we are rivals now.\pResearch does not cancel our\nbattles!$"

LegendsArc_Text_RedFarewell:
    .string "{COLOR RED}I will look for signs of the rifts.\pThere is still a lot we do not know.\pWe will meet again, {PLAYER}.\pCome on, Pikachu.$"

LegendsArc_Text_DexBagFull:
    .string "{COLOR RED}Your bag is full.\pMake room, then come back for these.$"

LegendsArc_Text_ElaraAsk:
    .string "There you are, {PLAYER}.\pYou have been gone quite a while.\pHow did meeting the Professor go?$"

LegendsArc_Text_PlayerTellsElara:
    .string "{COLOR LIGHT_BLUE}There was a strange POKéMON.\pRed and Pikachu saved us.\pHe said he came through a portal.\pHe is a Champion from Kanto.\pWe battled, and he gave me this\nring.\pBirch asked us to study the\nsightings.$"

LegendsArc_Text_ElaraAbsorbs:
    .string "A portal… And Red is here too…\pThat is a lot for your first outing.$"

LegendsArc_Text_ElaraThought:
    .string "Elara falls quiet for a moment.\pHer thoughts turn to Caelum.\p(Is this what you planned?)$"

LegendsArc_Text_ElaraShoes:
    .string "Then you will need these shoes.\pThey are made for a long journey.$"

LegendsArc_Text_ElaraTakeCare:
    .string "Hold B outside to run.\pCome home whenever you need to.\pTake care of yourself, {PLAYER}.\pAnd take care of your partner too.$"

LegendsArc_Text_Companion:
    .string "{COLOR RED}There is always something new to\nlearn.\pPikachu and I are taking our time.$"

LegendsArc_ClaimRing:
    lockall
    giveitem ITEM_MEGA_RING
    goto_if_eq VAR_RESULT, FALSE, LegendsArc_RingBagFull
    setflag FLAG_LA_RECEIVED_RED_MEGA_RING
    goto LegendsArc_AfterMegaRing
LegendsArc_ResumeDex::
    lockall
    setvar VAR_BIRCH_LAB_STATE, 4
    goto LegendsArc_DexGifts
LegendsArc_PikachuTalk::
    lock
    faceplayer
    playmoncry SPECIES_PIKACHU, CRY_MODE_NORMAL
    waitmoncry
    release
    end
LegendsArc_BrendanTalk::
    lock
    faceplayer
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsArc_Text_BrendanResearch, MSGBOX_DEFAULT
    release
    end
LegendsArc_MayTalk::
    lock
    faceplayer
    setspeaker SP_NAME_MAY
    msgbox LegendsArc_Text_MayAfterDouble, MSGBOX_DEFAULT
    release
    end

@ Red steps beside the player before their introductions and spar.
LegendsArc_LabFaceEachOther:
    turnobject LOCALID_LA_LAB_RED, DIR_EAST
    turnobject LOCALID_PLAYER, DIR_WEST
    turnobject LOCALID_LA_LAB_PIKACHU, DIR_EAST
    return

@ All saved Route 103 trigger positions converge on the same conversation cell.
LegendsArc_Route103Auto7::
LegendsArc_Route103Auto8::
LegendsArc_Route103Auto9::
    goto LegendsArc_Route103Meeting

LegendsArc_Route103Approach:
    switch VAR_0x8004
    case 1, LegendsArc_Route103From1
    case 2, LegendsArc_Route103From2
    case 3, LegendsArc_Route103From3
    case 4, LegendsArc_Route103From4
    case 5, LegendsArc_Route103From5
    case 6, LegendsArc_Route103From6
    case 7, LegendsArc_Route103From7
    return
LegendsArc_Route103From1:
    applymovement LOCALID_PLAYER, LegendsArc_Route103Path1
    waitmovement 0
    return
LegendsArc_Route103From2:
    applymovement LOCALID_PLAYER, LegendsArc_Route103Path2
    waitmovement 0
    return
LegendsArc_Route103From3:
    applymovement LOCALID_PLAYER, LegendsArc_Route103Path3
    waitmovement 0
    return
LegendsArc_Route103From4:
    applymovement LOCALID_PLAYER, LegendsArc_Route103Path4
    waitmovement 0
    return
LegendsArc_Route103From5:
    applymovement LOCALID_PLAYER, LegendsArc_Route103Path5
    waitmovement 0
    return
LegendsArc_Route103From6:
    applymovement LOCALID_PLAYER, LegendsArc_Route103Path6
    waitmovement 0
    return
LegendsArc_Route103From7:
    applymovement LOCALID_PLAYER, LegendsArc_Route103Path7
    waitmovement 0
    return
LegendsArc_Route103Path1:
    walk_right
    walk_up
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    face_up
    step_end
LegendsArc_Route103Path2:
    walk_up
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    face_up
    step_end
LegendsArc_Route103Path3:
    walk_up
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    face_up
    step_end
LegendsArc_Route103Path4:
    walk_up
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    face_up
    step_end
LegendsArc_Route103Path5:
    walk_up
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    face_up
    step_end
LegendsArc_Route103Path6:
    walk_up
    walk_right
    walk_right
    walk_right
    walk_right
    face_up
    step_end
LegendsArc_Route103Path7:
    walk_up
    walk_right
    walk_right
    walk_right
    face_up
    step_end

LegendsArc_LabRedApproach:
    walk_right
    face_right
    step_end

LegendsArc_LabRedStepDown:
    walk_down
    face_right
    step_end
