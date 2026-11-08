
RiftResearch_QueueExistingSave::
	goto_if_ne VAR_LA_RIFT_TRACKER, 0, RiftResearch_Return
	goto_if_ne VAR_LA_MAUVILLE_RIFT, 3, RiftResearch_Return
	setvar VAR_TEMP_6, 1
RiftResearch_Return::
	return

RiftResearch_InviteExistingSave::
	lockall
	setvar VAR_TEMP_6, 0
	call RiftResearch_Invite
	releaseall
	end

RiftResearch_Invite::
	goto_if_ne VAR_LA_RIFT_TRACKER, 0, RiftResearch_Return
	closemessage
	playse SE_POKENAV_CALL
	delay 30
	setspeaker SP_NAME_BIRCH
	pokenavcall RiftResearch_Text_Invite
	waitmessage
	closemessage
	setspeaker SP_NAME_PLAYER
	msgbox RiftResearch_Text_Answer, MSGBOX_DEFAULT
	setspeaker SP_NAME_BIRCH
	msgbox RiftResearch_Text_Priority, MSGBOX_DEFAULT
	closemessage
	playse SE_POKENAV_HANG_UP
	setvar VAR_LA_RIFT_TRACKER, 1
	setspeaker SP_NAME_NONE
	return

RiftResearch_Briefing::
	lockall
	faceplayer
	call RiftResearch_OakIntroduction
	setspeaker SP_NAME_BIRCH
	msgbox RiftResearch_Text_Welcome, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox RiftResearch_Text_Question, MSGBOX_DEFAULT
	setspeaker SP_NAME_BIRCH
	msgbox RiftResearch_Text_Signatures, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox RiftResearch_Text_Strength, MSGBOX_DEFAULT
	setspeaker SP_NAME_BIRCH
	msgbox RiftResearch_Text_Explain, MSGBOX_DEFAULT
	closemessage
	playfanfare MUS_OBTAIN_ITEM
	setspeaker SP_NAME_NONE
	msgbox RiftResearch_Text_Upgrade, MSGBOX_DEFAULT
	waitfanfare
	setvar VAR_LA_RIFT_TRACKER, 2
	call LegendsQuest_EnsureTracker
	setspeaker SP_NAME_PLAYER
	msgbox RiftResearch_Text_Resolve, MSGBOX_DEFAULT
	setspeaker SP_NAME_BIRCH
	msgbox RiftResearch_Text_LastAdvice, MSGBOX_DEFAULT
	call RiftResearch_OakGift
	closemessage
	setspeaker SP_NAME_NONE
	releaseall
	end

RiftResearch_NoDetector::
	msgbox RiftResearch_Text_NoDetector, MSGBOX_DEFAULT
	goto RiftResearch_End
RiftResearch_Repelled::
	msgbox RiftResearch_Text_Repelled, MSGBOX_DEFAULT
	goto RiftResearch_End
RiftResearch_Sealed::
	msgbox RiftResearch_Text_Sealed, MSGBOX_DEFAULT
	goto RiftResearch_End
RiftResearch_Quiet::
	msgbox RiftResearch_Text_Quiet, MSGBOX_DEFAULT
	goto RiftResearch_End
RiftResearch_End::
	closemessage
	setspeaker SP_NAME_NONE
	releaseall
	end

RiftResearch_Text_Invite:
	.string "{PLAYER}, it's Birch. Wattson sent\nhis readings. You've earned his Badge!\pRowan and I have found two\ndifferent rift signatures.\pCome to my lab in Littleroot.\nI have something that may help us."
	.string "\pBring your PokéNav. We'll explain\nour findings in person.$"
RiftResearch_Text_Answer:
	.string "A way to find Wally?\nI'll come and hear what you found.$"
RiftResearch_Text_Priority:
	.string "A way to follow the evidence.\nI don't want to promise more yet.\pIf Wally calls, help his family\nfirst. This can wait until then.$"
RiftResearch_Text_Welcome:
	.string "Good to see you, {PLAYER}.\nRowan helped compare the readings.\pDevon's engineers built this\nsensor to work with your PokéNav.$"
RiftResearch_Text_Question:
	.string "Will it tell us where a rift\nleads before we step through?$"
RiftResearch_Text_Signatures:
	.string "It can distinguish two kinds.\nThe oval wormholes carry\pstrong signs of Pokémon life.\nThey are far more dangerous.\pStay clear until you have beaten\nthe Hoenn Pokémon League.\pEven then, we must study each one.\pThe rifts you saw in the Gym\nconnect places.\pHoopa's golden rings have their\nown signature. Don't confuse them.$"
RiftResearch_Text_Strength:
	.string "Then why do some openings\npush me away when I get close?$"
RiftResearch_Text_Explain:
	.string "Your partners must withstand\nthe energy with you. Gym training\phelps them handle stronger rifts.\nThe detector uses your Badges\pas a safety guide. Even then,\na passage may still be unstable.\pThis is your Rift Tracker.\nIt will show signals,\psafety checks, our findings,\nand your current investigation.\pA signal is a lead, {PLAYER}.\nIt isn't a promise of safe travel.$"
RiftResearch_Text_Upgrade:
	.string "{PLAYER} received the Rift Tracker!\nThe detector is ready to use.$"
RiftResearch_Text_Resolve:
	.string "Then I'll keep a record of what\nwe find. Wally isn't just a reading.\pWe're bringing him and Kirlia home.$"
RiftResearch_Text_LastAdvice:
	.string "Exactly. Follow the evidence and\nkeep speaking with the others.\pCheck your Rift Tracker from the\nStart menu whenever you need a lead.$"
RiftResearch_Text_NoDetector:
	.string "The opening gives off a strange hum.\nI need a way to read its energy.$"
RiftResearch_Text_Repelled:
	.string "You feel a strange energy\npushing you away.\pYour partners cannot withstand\nthis rift yet. More Gym training\pmay help you approach safely.$"
RiftResearch_Text_Sealed:
	.string "The detector recognizes a passage,\nbut its far end is unstable.\pSurvey it after the League, then\nreturn to Birch for its own permit.$"
RiftResearch_Text_Quiet:
	.string "The wormhole is quiet.\nIts Pokémon signal has faded.$"
RiftResearch_Text_Encounter:
	.string "A Pokémon signal pulses inside.\nApproach the wormhole?$"
RiftResearch_Text_Travel:
	.string "The detector confirms a stable\npassage to {STR_VAR_1}.\pStep through?$"

RiftResearch_BlockNoDetector::
	lockall
	goto RiftResearch_NoDetector
RiftResearch_BlockRepelled::
	lockall
	goto RiftResearch_Repelled
RiftResearch_BlockSealed::
	lockall
	goto RiftResearch_Sealed

RiftResearch_BlockLeague::
	lockall
	msgbox RiftResearch_Text_League, MSGBOX_DEFAULT
	goto RiftResearch_End

RiftResearch_Text_League:
	.string "You feel a fierce energy\npushing you away.\pThis natural wormhole is too\ndangerous for your partners.\pReturn after you have beaten\nthe Hoenn Pokémon League.$"

RiftResearch_Natural_0::
	lockall
	setvar VAR_0x8004, 0
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_1::
	lockall
	setvar VAR_0x8004, 1
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_2::
	lockall
	setvar VAR_0x8004, 2
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_3::
	lockall
	setvar VAR_0x8004, 3
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_4::
	lockall
	setvar VAR_0x8004, 4
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_5::
	lockall
	setvar VAR_0x8004, 5
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_6::
	lockall
	setvar VAR_0x8004, 6
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_7::
	lockall
	setvar VAR_0x8004, 7
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_8::
	lockall
	setvar VAR_0x8004, 8
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_9::
	lockall
	setvar VAR_0x8004, 9
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_10::
	lockall
	setvar VAR_0x8004, 10
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_11::
	lockall
	setvar VAR_0x8004, 11
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_12::
	lockall
	setvar VAR_0x8004, 12
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_13::
	lockall
	setvar VAR_0x8004, 13
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_14::
	lockall
	setvar VAR_0x8004, 14
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_15::
	lockall
	setvar VAR_0x8004, 15
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_16::
	lockall
	setvar VAR_0x8004, 16
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_17::
	lockall
	setvar VAR_0x8004, 17
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_18::
	lockall
	setvar VAR_0x8004, 18
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_19::
	lockall
	setvar VAR_0x8004, 19
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_20::
	lockall
	setvar VAR_0x8004, 20
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_21::
	lockall
	setvar VAR_0x8004, 21
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_22::
	lockall
	setvar VAR_0x8004, 22
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_Natural_23::
	lockall
	setvar VAR_0x8004, 23
	special RiftTracker_Check
	goto_if_eq VAR_RESULT, 0, RiftResearch_NoDetector
	goto_if_eq VAR_RESULT, 3, RiftResearch_PermitReady
	goto_if_eq VAR_RESULT, 5, RiftResearch_BlockLeague
	goto RiftResearch_Sealed

RiftResearch_SetupOak::
	setflag FLAG_TEMP_7
	goto_if_unset FLAG_BADGE03_GET, RiftResearch_Return
	clearflag FLAG_TEMP_7
	return

RiftResearch_OakTalk::
	goto_if_lt VAR_LA_RIFT_TRACKER, 2, RiftResearch_Briefing
	goto RiftResearch_OakCatchUp

RiftResearch_OakCatchUp::
	lockall
	faceplayer
	call_if_eq VAR_LA_OAK_STARTER, 0, RiftResearch_OakIntroduction
	call RiftResearch_OakGift
	goto RiftResearch_End

RiftResearch_OakIntroduction::
	goto_if_ne VAR_LA_OAK_STARTER, 0, RiftResearch_Return
	clearflag FLAG_TEMP_7
	addobject LOCALID_LA_TRACKER_OAK
	turnobject LOCALID_LA_TRACKER_OAK, DIR_SOUTH
	setspeaker SP_NAME_BIRCH
	msgbox RiftResearch_Text_OakIntroduction, MSGBOX_DEFAULT
	setspeaker SP_NAME_OAK
	msgbox RiftResearch_Text_OakGreeting, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox RiftResearch_Text_PlayerOak, MSGBOX_DEFAULT
	setspeaker SP_NAME_OAK
	msgbox RiftResearch_Text_OakReply, MSGBOX_DEFAULT
	setvar VAR_LA_OAK_STARTER, 1
	setspeaker SP_NAME_BIRCH
	return

RiftResearch_OakGift::
	setspeaker SP_NAME_OAK
	goto_if_ge VAR_LA_OAK_STARTER, 2, RiftResearch_OakReminder
	msgbox RiftResearch_Text_Offer, MSGBOX_DEFAULT
RiftResearch_OakChoose::
	closemessage
	multichoice 0, 0, MULTI_LA_OAK_STARTER, FALSE
	goto_if_eq VAR_RESULT, 0, RiftResearch_PreviewBulbasaur
	goto_if_eq VAR_RESULT, 1, RiftResearch_PreviewCharmander
	goto_if_eq VAR_RESULT, 2, RiftResearch_PreviewSquirtle
	msgbox RiftResearch_Text_Later, MSGBOX_DEFAULT
	return

RiftResearch_PreviewBulbasaur::
	setvar VAR_0x8007, 2
	setvar VAR_TEMP_TRANSFERRED_SPECIES, SPECIES_BULBASAUR
	showmonpic SPECIES_BULBASAUR, 10, 3
	goto RiftResearch_ConfirmStarter
RiftResearch_PreviewCharmander::
	setvar VAR_0x8007, 3
	setvar VAR_TEMP_TRANSFERRED_SPECIES, SPECIES_CHARMANDER
	showmonpic SPECIES_CHARMANDER, 10, 3
	goto RiftResearch_ConfirmStarter
RiftResearch_PreviewSquirtle::
	setvar VAR_0x8007, 4
	setvar VAR_TEMP_TRANSFERRED_SPECIES, SPECIES_SQUIRTLE
	showmonpic SPECIES_SQUIRTLE, 10, 3
RiftResearch_ConfirmStarter::
	bufferspeciesname STR_VAR_1, VAR_TEMP_TRANSFERRED_SPECIES
	msgbox RiftResearch_Text_ConfirmStarter, MSGBOX_YESNO
	hidemonpic
	goto_if_ne VAR_RESULT, YES, RiftResearch_OakChoose
	goto_if_eq VAR_0x8007, 2, RiftResearch_GiveBulbasaur
	goto_if_eq VAR_0x8007, 3, RiftResearch_GiveCharmander
	givemon SPECIES_SQUIRTLE, 5
	goto RiftResearch_StarterGiven
RiftResearch_GiveBulbasaur::
	givemon SPECIES_BULBASAUR, 5
	goto RiftResearch_StarterGiven
RiftResearch_GiveCharmander::
	givemon SPECIES_CHARMANDER, 5
RiftResearch_StarterGiven::
	goto_if_eq VAR_RESULT, MON_GIVEN_TO_PARTY, RiftResearch_GiftSuccess
	goto_if_eq VAR_RESULT, MON_GIVEN_TO_PC, RiftResearch_GiftToPC
	msgbox RiftResearch_Text_NoRoom, MSGBOX_DEFAULT
	return
RiftResearch_GiftToPC::
	setspeaker SP_NAME_NONE
	msgbox RiftResearch_Text_SentToPC, MSGBOX_DEFAULT
RiftResearch_GiftSuccess::
	copyvar VAR_LA_OAK_STARTER, VAR_0x8007
	bufferspeciesname STR_VAR_1, VAR_TEMP_TRANSFERRED_SPECIES
	playfanfare MUS_OBTAIN_ITEM
	setspeaker SP_NAME_NONE
	msgbox RiftResearch_Text_ReceivedStarter, MSGBOX_DEFAULT
	waitfanfare
	setspeaker SP_NAME_PLAYER
	msgbox RiftResearch_Text_ThanksOak, MSGBOX_DEFAULT
	setspeaker SP_NAME_OAK
	msgbox RiftResearch_Text_Grandson, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox RiftResearch_Text_FindBlue, MSGBOX_DEFAULT
	return

RiftResearch_OakReminder::
	goto_if_ge VAR_LA_OAK_STARTER, 10, RiftResearch_OakAfterBlue
	msgbox RiftResearch_Text_Grandson, MSGBOX_DEFAULT
	return
RiftResearch_OakAfterBlue::
	msgbox RiftResearch_Text_OakAfterBlue, MSGBOX_DEFAULT
	return

RiftResearch_Text_OakIntroduction:
	.string "{PLAYER}, I'd like you to meet\nProfessor Oak, from Kanto.\pHe's one of the voices you heard\non the Paradigm call.$"
RiftResearch_Text_OakGreeting:
	.string "So this is the young Trainer who\nhelped Wattson in our Power Plant!\pI'm Samuel Oak. Birch has told me\nhow determined you are to find Wally.$"
RiftResearch_Text_PlayerOak:
	.string "Glad to meet you, Professor.\nThat voice does sound familiar.\pWally and Kirlia are still out\nthere. I want to bring them home.$"
RiftResearch_Text_OakReply:
	.string "And you shall have our help.\nA careful observer can find clues\pthat even experienced researchers\nmiss. Now, let's hear Birch out.$"
RiftResearch_Text_Offer:
	.string "Before you go, I brought three\nyoung Pokémon from Kanto.\pI'd like one to travel with you.\nChoose the partner you want to raise.$"
RiftResearch_Text_ConfirmStarter:
	.string "Would you like {STR_VAR_1}\nto join you? It is level 5.$"
RiftResearch_Text_Later:
	.string "Take your time. I'll keep them\nsafe here until you're ready.$"
RiftResearch_Text_NoRoom:
	.string "Your party and storage are full.\nMake room, then come back to me.\pI'll keep your choice safe.$"
RiftResearch_Text_SentToPC:
	.string "Your party is full. The Pokémon\nwas transferred to your PC.$"
RiftResearch_Text_ReceivedStarter:
	.string "{PLAYER} received {STR_VAR_1}\nfrom Professor Oak!$"
RiftResearch_Text_ThanksOak:
	.string "Thank you, Professor. I'll take\ngood care of our new partner.$"
RiftResearch_Text_Grandson:
	.string "There's someone else I'd like\nyou to meet: my grandson, Blue.\pHe's in Fallarbor Town, comparing\nreports of unusual Pokémon.\pHe can be rather sure of himself,\nbut he's an excellent Trainer.\pTell him I sent you. You may have\nmore to learn from each other\pthan either of you expects.$"
RiftResearch_Text_FindBlue:
	.string "Blue, in Fallarbor. I'll look\nfor him when I get there.\pIf he's found anything about the\nrifts, we should compare notes.$"
RiftResearch_Text_OakAfterBlue:
	.string "Blue told me you met in Fallarbor.\nSharing evidence is a good start.\pI hope you'll keep looking out\nfor one another on your journeys.$"

RiftResearch_ShowBlue::
	goto_if_set FLAG_LA_BLUE_CHIMNEY_BRIEFED, RiftResearch_ShowBlueDone
	clearflag FLAG_TEMP_7
	return
RiftResearch_ShowBlueDone::
	return
RiftResearch_Blue::
	lockall
	faceplayer
	setspeaker SP_NAME_BLUE
	goto_if_ge VAR_LA_OAK_STARTER, 10, RiftResearch_BlueRepeat
	msgbox RiftResearch_Text_BlueFirst, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox RiftResearch_Text_PlayerBlue, MSGBOX_DEFAULT
	setspeaker SP_NAME_BLUE
	msgbox RiftResearch_Text_BlueReply, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox RiftResearch_Text_PlayerEvidence, MSGBOX_DEFAULT
	setspeaker SP_NAME_BLUE
	msgbox RiftResearch_Text_BlueEvidence, MSGBOX_DEFAULT
	addvar VAR_LA_OAK_STARTER, 8
	goto LegendsBlue_Briefing
RiftResearch_BlueRepeat::
	goto_if_set FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY, RiftResearch_BlueLegacyRepeat
	goto_if_unset FLAG_LA_BLUE_CHIMNEY_BRIEFED, LegendsBlue_Briefing
RiftResearch_BlueLegacyRepeat:
	msgbox RiftResearch_Text_BlueRepeat, MSGBOX_DEFAULT
	goto RiftResearch_End
RiftResearch_Text_BlueFirst:
	.string "Need something? I'm comparing\nthese reports before the ash\pburies the tracks. Wait, you\ncame looking for me?$"
RiftResearch_Text_PlayerBlue:
	.string "I'm {PLAYER}. Professor Oak said\nI'd find his grandson in Fallarbor.\pHe gave me a Kanto Pokémon and\nasked me to introduce myself.$"
RiftResearch_Text_BlueReply:
	.string "Gramps sent you? I'm Blue.\nYou must be working with Birch.\pI heard Red was here too.\nFigures he'd get a head start.$"
RiftResearch_Text_PlayerEvidence:
	.string "We're looking for Wally and Kirlia.\nA rift left them stranded in Kanto.\pHave you seen anything here that\ncould help us find a way back?$"
RiftResearch_Text_BlueEvidence:
	.string "Different tracks after every\nashfall. Pokémon that don't\pbelong here. I'm checking which\nreports have evidence behind them.\pIf we're going to help your friend,\nwe need a route we can trust.\pKeep your tracker handy. I'll\ncompare what I find with Paradigm.$"
RiftResearch_Text_BlueRepeat:
	.string "A strange sighting isn't proof\nof a stable passage.\pCheck the tracks, the time and\nthe weather. Then compare reports.$"

RiftResearch_PermitReady::
    msgbox RiftResearch_Text_PermitReady, MSGBOX_DEFAULT
    goto RiftResearch_End
RiftResearch_Text_PermitReady:
    .string "The passage is stable.\nYour permit matches this wormhole.\pStep into it when you are ready.$"
