VerdanturfTown_WandasHouse_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, LegendsParadigm_FamilyTransition
	.byte 0

VerdanturfTown_WandasHouse_EventScript_Wally::
	lock
	faceplayer
	goto_if_set FLAG_WALLY_SPEECH, VerdanturfTown_WandasHouse_EventScript_WallyShortSpeech
	msgbox VerdanturfTown_WandasHouse_Text_StrongerSpeech, MSGBOX_DEFAULT
	setflag FLAG_WALLY_SPEECH
	release
	end

VerdanturfTown_WandasHouse_EventScript_WallyShortSpeech::
	msgbox VerdanturfTown_WandasHouse_Text_StrongerSpeechShort, MSGBOX_DEFAULT
	release
	end

VerdanturfTown_WandasHouse_EventScript_WallysUncle::
	lock
	faceplayer
	goto_if_eq VAR_LA_PARADIGM_ARC, 3, LegendsParadigm_TellFamily
	goto_if_ge VAR_LA_PARADIGM_ARC, 4, LegendsParadigm_UncleInformed
	goto_if_eq VAR_LA_MAUVILLE_RIFT, 3, LegendsParadigm_UncleWaiting
	goto_if_set FLAG_DEFEATED_WALLY_VICTORY_ROAD, VerdanturfTown_WandasHouse_EventScript_WallysUncleEverGrande
	goto_if_set FLAG_DEFEATED_LAVARIDGE_GYM, VerdanturfTown_WandasHouse_EventScript_WallysUncleSlippedOff
	msgbox VerdanturfTown_WandasHouse_Text_WallysNextDoor, MSGBOX_DEFAULT
	release
	end

VerdanturfTown_WandasHouse_EventScript_WallysUncleSlippedOff::
	msgbox VerdanturfTown_WandasHouse_Text_WallySlippedOff, MSGBOX_DEFAULT
	release
	end

VerdanturfTown_WandasHouse_EventScript_WallysUncleEverGrande::
	msgbox VerdanturfTown_WandasHouse_Text_WallyGoneThatFar, MSGBOX_DEFAULT
	release
	end

VerdanturfTown_WandasHouse_EventScript_WandasBoyfriend::
	msgbox VerdanturfTown_WandasHouse_Text_CanSeeGirlfriendEveryDay, MSGBOX_NPC
	end

VerdanturfTown_WandasHouse_EventScript_Wanda::
	lock
	faceplayer
	goto_if_ge VAR_LA_PARADIGM_ARC, 4, LegendsParadigm_FamilyInformed
	goto_if_eq VAR_LA_MAUVILLE_RIFT, 3, LegendsParadigm_FamilyWaiting
	goto_if_set FLAG_DEFEATED_LAVARIDGE_GYM, VerdanturfTown_WandasHouse_EventScript_WandaDontWorry
	goto_if_set FLAG_DEFEATED_WALLY_MAUVILLE, VerdanturfTown_WandasHouse_EventScript_MeetWanda
	msgbox VerdanturfTown_WandasHouse_Text_DontWorryAboutWally, MSGBOX_DEFAULT
	release
	end

VerdanturfTown_WandasHouse_EventScript_MeetWanda::
	msgbox VerdanturfTown_WandasHouse_Text_MeetWanda, MSGBOX_DEFAULT
	release
	end

VerdanturfTown_WandasHouse_EventScript_WandaDontWorry::
	msgbox VerdanturfTown_WandasHouse_Text_DontWorryAboutWally, MSGBOX_DEFAULT
	release
	end

VerdanturfTown_WandasHouse_EventScript_WallysAunt::
	lock
	faceplayer
	goto_if_ge VAR_LA_PARADIGM_ARC, 4, LegendsParadigm_FamilyInformed
	goto_if_eq VAR_LA_MAUVILLE_RIFT, 3, LegendsParadigm_FamilyWaiting
	goto_if_set FLAG_DEFEATED_WALLY_VICTORY_ROAD, VerdanturfTown_WandasHouse_EventScript_WallysAuntEverGrande
	goto_if_set FLAG_DEFEATED_LAVARIDGE_GYM, VerdanturfTown_WandasHouse_EventScript_WallysAuntAnythingHappened
	goto_if_set FLAG_RUSTURF_TUNNEL_OPENED, VerdanturfTown_WandasHouse_EventScript_WallysAuntTunnelOpen
	msgbox VerdanturfTown_WandasHouse_Text_DaughtersBoyfriendDriven, MSGBOX_DEFAULT
	release
	end

VerdanturfTown_WandasHouse_EventScript_WallysAuntTunnelOpen::
	msgbox VerdanturfTown_WandasHouse_Text_DaughtersBoyfriendWasDigging, MSGBOX_DEFAULT
	release
	end

VerdanturfTown_WandasHouse_EventScript_WallysAuntAnythingHappened::
	msgbox VerdanturfTown_WandasHouse_Text_IfAnythingHappenedToWally, MSGBOX_DEFAULT
	release
	end

VerdanturfTown_WandasHouse_EventScript_WallysAuntEverGrande::
	msgbox VerdanturfTown_WandasHouse_Text_WallyWasInEverGrande, MSGBOX_DEFAULT
	release
	end

VerdanturfTown_WandasHouse_Text_StrongerSpeech:
	.string "WALLY: I lost to you, {PLAYER}, but I'm\n"
	.string "not feeling down anymore.\p"
	.string "Because I have a new purpose in life.\n"
	.string "Together with my RALTS, I'm going\l"
	.string "to challenge POKéMON GYMS and become\l"
	.string "a great TRAINER.\p"
	.string "Please watch me, {PLAYER}.\n"
	.string "I'm going to be stronger than you.\p"
	.string "When I do, I'm going to challenge you\n"
	.string "to another battle.$"

VerdanturfTown_WandasHouse_Text_StrongerSpeechShort:
	.string "WALLY: Please watch me, {PLAYER}.\n"
	.string "I'm going to get stronger than you.\p"
	.string "When I do, I'm going to challenge you\n"
	.string "to another battle.$"

VerdanturfTown_WandasHouse_Text_WallysNextDoor:
	.string "UNCLE: Oh! {PLAYER}{KUN}!\n"
	.string "WALLY's next door.\p"
	.string "But, boy, there's something I have to\n"
	.string "tell you.\p"
	.string "This natural environment is doing\n"
	.string "wonders for WALLY's health.\p"
	.string "Maybe it's not just the environment.\n"
	.string "It could be POKéMON that are giving\l"
	.string "the boy hope.$"

VerdanturfTown_WandasHouse_Text_WallySlippedOff:
	.string "WALLY's gone away…\n"
	.string "He slipped off on his own…$"

VerdanturfTown_WandasHouse_Text_WallyGoneThatFar:
	.string "UNCLE: Is that right?\n"
	.string "WALLY's gone away that far all by\l"
	.string "himself…\p"
	.string "Well, I have to give him credit--he is\n"
	.string "my little brother's son.$"

VerdanturfTown_WandasHouse_Text_MeetWanda:
	.string "WANDA: You are?\n"
	.string "Oh, right, I get it!\p"
	.string "You're the {PLAYER} who WALLY was\n"
	.string "telling me about.\p"
	.string "I'm WALLY's cousin.\n"
	.string "Glad to meet you!\p"
	.string "I think WALLY's become a lot more lively\n"
	.string "and healthy since he came here.$"

VerdanturfTown_WandasHouse_Text_DontWorryAboutWally:
	.string "WANDA: Don't worry about WALLY.\n"
	.string "He'll be just fine.\p"
	.string "I know my little cousin, and he has\n"
	.string "POKéMON with him, too.$"

VerdanturfTown_WandasHouse_Text_CanSeeGirlfriendEveryDay:
	.string "Thanks to you, I can see my girlfriend\n"
	.string "every day.\l"
	.string "Happy? You bet I am!$"

VerdanturfTown_WandasHouse_Text_DaughtersBoyfriendDriven:
	.string "My daughter's boyfriend is a very\n"
	.string "driven and passionate sort of person.\p"
	.string "He's been digging a tunnel nonstop\n"
	.string "just so he can see my daughter.\p"
	.string "My daughter's a little concerned,\n"
	.string "so she goes out to the tunnel a lot.$"

VerdanturfTown_WandasHouse_Text_DaughtersBoyfriendWasDigging:
	.string "It's amazing. My daughter's boyfriend\n"
	.string "was digging the tunnel by hand!\p"
	.string "It's so incredible!$"

VerdanturfTown_WandasHouse_Text_IfAnythingHappenedToWally:
	.string "If anything were to happen to WALLY,\n"
	.string "I would never be able to look his\l"
	.string "parents in PETALBURG in the eye…$"

VerdanturfTown_WandasHouse_Text_WallyWasInEverGrande:
	.string "WALLY was in EVER GRANDE?\p"
	.string "His parents in PETALBURG would be\n"
	.string "astonished to hear that!$"


@ Project-owned reservation; registered asset map, no donor gameplay.
VerdanturfTown_WandasHouse_EventScript_HyperConstruction_Registered1::
	lock
	faceplayer
	msgbox VerdanturfTown_WandasHouse_Text_HyperConstruction_Registered1, MSGBOX_DEFAULT
	release
	end

VerdanturfTown_WandasHouse_Text_HyperConstruction_Registered1:
	.string "This area is under construction.\p"
	.string "Please check back later!$"

LegendsParadigm_FamilyTransition::
	setflag FLAG_TEMP_1
	goto_if_ne VAR_LA_MAUVILLE_RIFT, 3, LegendsParadigm_FamilyTransitionEnd
	setflag FLAG_HIDE_VERDANTURF_TOWN_WANDAS_HOUSE_WALLY
	clearflag FLAG_HIDE_VERDANTURF_TOWN_WANDAS_HOUSE_WALLYS_UNCLE
LegendsParadigm_FamilyTransitionEnd::
	end

LegendsParadigm_TellFamily::
	lockall
	setspeaker SP_NAME_PLAYER
	msgbox LegendsParadigm_Text_TellUncle, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	msgbox LegendsParadigm_Text_UncleRelief, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox LegendsParadigm_Text_PromiseFamily, MSGBOX_DEFAULT
	closemessage
	playse SE_DOOR
	clearflag FLAG_TEMP_1
	addobject LOCALID_VERDANTURF_PARADIGM_MAY
	applymovement LOCALID_VERDANTURF_PARADIGM_MAY, LegendsParadigm_MayApproach
	waitmovement 0
	turnobject LOCALID_PLAYER, DIR_SOUTH
	setspeaker SP_NAME_MAY
	msgbox LegendsParadigm_Text_MaySearch, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox LegendsParadigm_Text_RecallVillains, MSGBOX_DEFAULT
	setspeaker SP_NAME_MAY
	msgbox LegendsParadigm_Text_WoodsLead, MSGBOX_DEFAULT
	closemessage
	setspeaker SP_NAME_NONE
	applymovement LOCALID_VERDANTURF_PARADIGM_MAY, LegendsParadigm_MayLeave
	waitmovement 0
	removeobject LOCALID_VERDANTURF_PARADIGM_MAY
	setflag FLAG_TEMP_1
	setvar VAR_LA_PARADIGM_ARC, 4
	releaseall
	end

LegendsParadigm_MayApproach:
	walk_up
	walk_up
	step_end

LegendsParadigm_MayLeave:
	walk_down
	walk_down
	step_end

LegendsParadigm_UncleInformed::
	msgbox LegendsParadigm_Text_UncleInformed, MSGBOX_DEFAULT
	goto LegendsParadigm_FamilyEnd

LegendsParadigm_UncleWaiting::
	msgbox LegendsParadigm_Text_UncleWaiting, MSGBOX_DEFAULT
	goto LegendsParadigm_FamilyEnd

LegendsParadigm_FamilyInformed::
	msgbox LegendsParadigm_Text_FamilyInformed, MSGBOX_DEFAULT
	goto LegendsParadigm_FamilyEnd

LegendsParadigm_FamilyWaiting::
	msgbox LegendsParadigm_Text_FamilyWaiting, MSGBOX_DEFAULT
LegendsParadigm_FamilyEnd::
	closemessage
	setspeaker SP_NAME_NONE
	releaseall
	end

LegendsParadigm_Text_TellUncle:
	.string "I heard from Wally. He's safe.\nKirlia is with him.\pThe rift sent them to Kanto.\nShe's helping him find a way back.$"
LegendsParadigm_Text_UncleRelief:
	.string "Kanto… So far from home?\pThank you for coming to tell us.\nWe've been waiting for news.\pIf he calls again, tell him he\nhas nothing to prove.\pTell him to come home when\nit's safe to travel.$"
LegendsParadigm_Text_PromiseFamily:
	.string "I will. Professor Birch and the\nothers are helping us look too.$"
LegendsParadigm_Text_MaySearch:
	.string "{PLAYER}! Dad told us about Wally.\nRed and Brendan are helping search.\pI came to check on his family.\nI'm glad he managed to call.$"
LegendsParadigm_Text_RecallVillains:
	.string "Those men in Timeless Woods had\nsomething that could steady rifts.\pOne had an R on his clothes.\nThe other had a G.\pIf they can control a crossing,\nmaybe they know where Wally went.$"
LegendsParadigm_Text_WoodsLead:
	.string "Then we should check where you\nsaw them. I'll meet you there.\pDad's sharing the descriptions\nwith Paradigm.\pWe need a clue they can follow.$"
LegendsParadigm_Text_UncleInformed:
	.string "May went to Timeless Woods.\pThank you for telling us about\nWally. Please keep us informed.$"
LegendsParadigm_Text_UncleWaiting:
	.string "Birch told us Wally went missing.\nHave you heard anything from him?$"
LegendsParadigm_Text_FamilyWaiting:
	.string "We keep listening for the phone.\nPlease tell us if Wally calls.$"
LegendsParadigm_Text_FamilyInformed:
	.string "At least he has Kirlia with him.\nThank you for bringing us news.$"
