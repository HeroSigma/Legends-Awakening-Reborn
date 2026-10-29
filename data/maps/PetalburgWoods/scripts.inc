PetalburgWoods_MapScripts::
	map_script MAP_SCRIPT_ON_LOAD, LegendsWoods_OnLoad
	.byte 0

LegendsWoods_OnLoad:
	setflag FLAG_HIDE_LA_WOODS_TRIAD_BACKUP
	goto_if_ge VAR_PETALBURG_WOODS_STATE, 1, LegendsWoods_HideFinished
	end
LegendsWoods_HideFinished:
	setflag FLAG_HIDE_PETALBURG_WOODS_AQUA_GRUNT
	setflag FLAG_HIDE_PETALBURG_WOODS_DEVON_EMPLOYEE
	end

PetalburgWoods_EventScript_DevonResearcherRight::
	lockall
	applymovement LOCALID_PLAYER, LegendsWoods_PlayerLeft
	waitmovement 0
	goto LegendsWoods_Begin

PetalburgWoods_EventScript_DevonResearcherLeft::
	lockall
LegendsWoods_Begin:
	applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterUp
	waitmovement 0
	setspeaker SP_NAME_DEVON_RESEARCHER
	msgbox LegendsWoods_Text_Readings, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_WOODS_SILPH, LegendsWoods_SilphCheckScope
	waitmovement 0
	setspeaker SP_NAME_SILPH_RESEARCHER
	msgbox LegendsWoods_Text_Scope, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_PETALBURG_WOODS_DEVON_EMPLOYEE, LegendsWoods_DevonApproach
	waitmovement 0
	applymovement LOCALID_WOODS_SILPH, LegendsWoods_SilphJoinPlayer
	waitmovement 0
	setspeaker SP_NAME_DEVON_RESEARCHER
	msgbox LegendsWoods_Text_Greeting, MSGBOX_DEFAULT
	closemessage
	playbgm MUS_ENCOUNTER_AQUA, FALSE
	applymovement LOCALID_PETALBURG_WOODS_GRUNT, LegendsWoods_TriadApproach
	waitmovement 0
	applymovement LOCALID_WOODS_SILPH, LegendsWoods_SilphReactToThreat
	applymovement LOCALID_PETALBURG_WOODS_DEVON_EMPLOYEE, Common_Movement_WalkInPlaceFasterUp
	waitmovement 0
	setspeaker SP_NAME_SHADOW_TRIAD
	msgbox LegendsWoods_Text_Demand, MSGBOX_DEFAULT
	setspeaker SP_NAME_SILPH_RESEARCHER
	msgbox LegendsWoods_Text_Refusal, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_PETALBURG_WOODS_DEVON_EMPLOYEE, LegendsWoods_DevonAside
	applymovement LOCALID_PETALBURG_WOODS_GRUNT, LegendsWoods_TriadOneDown
	waitmovement 0
	setspeaker SP_NAME_DEVON_RESEARCHER
	msgbox LegendsWoods_Text_Help, MSGBOX_DEFAULT
	setspeaker SP_NAME_SHADOW_TRIAD
	msgbox LegendsWoods_Text_Challenge, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	trainerbattle_no_intro TRAINER_GRUNT_PETALBURG_WOODS, LegendsWoods_Text_Defeat
	closemessage
	applymovement LOCALID_PETALBURG_WOODS_GRUNT, LegendsWoods_TriadBack
	waitmovement 0
	setspeaker SP_NAME_SHADOW_TRIAD
	msgbox LegendsWoods_Text_Delay, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_WOODS_SILPH, LegendsWoods_SilphProtectRecording
	waitmovement 0
	playse SE_M_TELEPORT
	addobject LOCALID_WOODS_TRIAD_2
	addobject LOCALID_WOODS_TRIAD_3
	delay 20
	applymovement LOCALID_WOODS_TRIAD_2, LegendsWoods_TriadBackupApproach
	waitmovement 0
	setspeaker SP_NAME_SILPH_RESEARCHER
	msgbox LegendsWoods_Text_Three, MSGBOX_DEFAULT
	setspeaker SP_NAME_SHADOW_TRIAD
	msgbox LegendsWoods_Text_Confirmed, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_WOODS_SILPH, Common_Movement_WalkInPlaceFasterLeft
	waitmovement 0
	setspeaker SP_NAME_SILPH_RESEARCHER
	msgbox LegendsWoods_Text_Stolen, MSGBOX_DEFAULT
	setflag FLAG_LA_WOODS_RIFT_RECORD_STOLEN
	setspeaker SP_NAME_SHADOW_TRIAD
	msgbox LegendsWoods_Text_Withdraw, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_PETALBURG_WOODS_GRUNT, LegendsWoods_TriadExitLead
	applymovement LOCALID_WOODS_TRIAD_2, LegendsWoods_TriadExitBackup
	applymovement LOCALID_WOODS_TRIAD_3, LegendsWoods_TriadExitBackup
	waitmovement 0
	playse SE_M_TELEPORT
	removeobject LOCALID_PETALBURG_WOODS_GRUNT
	removeobject LOCALID_WOODS_TRIAD_2
	removeobject LOCALID_WOODS_TRIAD_3
	setflag FLAG_HIDE_PETALBURG_WOODS_AQUA_GRUNT
	setflag FLAG_HIDE_LA_WOODS_TRIAD_BACKUP
	fadedefaultbgm
	applymovement LOCALID_PETALBURG_WOODS_DEVON_EMPLOYEE, Common_Movement_WalkInPlaceFasterLeft
	applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterRight
	waitmovement 0
	applymovement LOCALID_WOODS_SILPH, LegendsWoods_SilphAfterTheft
	waitmovement 0
	setspeaker SP_NAME_DEVON_RESEARCHER
	msgbox LegendsWoods_Text_Thanks, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	giveitem ITEM_GREAT_BALL
	goto_if_eq VAR_RESULT, FALSE, LegendsWoods_NoRoom
LegendsWoods_AfterReward:
	call LegendsPokevial_GiveReward
	applymovement LOCALID_WOODS_SILPH, Common_Movement_WalkInPlaceFasterDown
	waitmovement 0
	setspeaker SP_NAME_SILPH_RESEARCHER
	msgbox LegendsWoods_Text_Damage, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	goto_if_unset FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN, LegendsWoods_NoRecognition
	msgbox LegendsWoods_Text_Thought, MSGBOX_DEFAULT
	goto LegendsWoods_Report
LegendsWoods_NoRecognition:
	msgbox LegendsWoods_Text_ThoughtUnknown, MSGBOX_DEFAULT
LegendsWoods_Report:
	setspeaker SP_NAME_DEVON_RESEARCHER
	msgbox LegendsWoods_Text_Report, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_WOODS_SILPH, LegendsWoods_SilphExit
	waitmovement 0
	removeobject LOCALID_WOODS_SILPH
	applymovement LOCALID_PETALBURG_WOODS_DEVON_EMPLOYEE, LegendsWoods_DevonExit
	applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterUp
	waitmovement 0
	removeobject LOCALID_PETALBURG_WOODS_DEVON_EMPLOYEE
	setflag FLAG_HIDE_PETALBURG_WOODS_DEVON_EMPLOYEE
	setflag FLAG_LA_WOODS_TRIAD_COMPLETE
	setvar VAR_PETALBURG_WOODS_STATE, 1
	setspeaker SP_NAME_NONE
	releaseall
	end
LegendsWoods_NoRoom:
	setspeaker SP_NAME_DEVON_RESEARCHER
	msgbox LegendsWoods_Text_NoRoom, MSGBOX_DEFAULT
	goto LegendsWoods_AfterReward

LegendsWoods_PlayerLeft:
	walk_left
	step_end
LegendsWoods_DevonApproach:
	walk_down
	walk_down
	face_down
	step_end
LegendsWoods_DevonAside:
	walk_fast_right
	walk_fast_down
	face_left
	step_end
LegendsWoods_TriadApproach:
	walk_down
	walk_down
	walk_down
	walk_down
	step_end
LegendsWoods_TriadOneDown:
	delay_16
	walk_down
	step_end
LegendsWoods_TriadBackupApproach:
	walk_down
	face_right
	step_end
LegendsWoods_TriadBack:
	walk_up
	face_down
	step_end
LegendsWoods_TriadExitLead:
	delay_16
	delay_16
	walk_fast_up
	walk_fast_up
	walk_fast_up
	step_end
LegendsWoods_TriadExitBackup:
	walk_fast_up
	walk_fast_up
	walk_fast_up
	step_end
LegendsWoods_SilphExit:
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_fast_left
	walk_fast_left
	walk_fast_left
	walk_fast_up
	walk_fast_up
	walk_fast_up
	step_end
LegendsWoods_DevonExit:
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_fast_left
	walk_fast_left
	walk_fast_left
	walk_fast_up
	walk_fast_up
	walk_fast_up
	step_end

PetalburgWoods_EventScript_Boy1::
	msgbox PetalburgWoods_Text_StayOutOfTallGrass, MSGBOX_NPC
	end

PetalburgWoods_EventScript_Boy2::
	msgbox PetalburgWoods_Text_HiddenItemsExplanation, MSGBOX_NPC
	end

PetalburgWoods_EventScript_Girl::
	lock
	faceplayer
	goto_if_set FLAG_RECEIVED_MIRACLE_SEED, PetalburgWoods_EventScript_ExplainMiracleSeed
	msgbox PetalburgWoods_Text_TryUsingThisItem, MSGBOX_DEFAULT
	giveitem ITEM_MIRACLE_SEED
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_ShowBagIsFull
	setflag FLAG_RECEIVED_MIRACLE_SEED
	release
	end

PetalburgWoods_EventScript_ExplainMiracleSeed::
	msgbox PetalburgWoods_Text_MiracleSeedExplanation, MSGBOX_DEFAULT
	release
	end

PetalburgWoods_EventScript_Sign1::
	msgbox PetalburgWoods_Text_TrainerTipsExperience, MSGBOX_SIGN
	end

PetalburgWoods_EventScript_Sign2::
	msgbox PetalburgWoods_Text_TrainerTipsPP, MSGBOX_SIGN
	end

PetalburgWoods_EventScript_Lyle::
	trainerbattle_single TRAINER_LYLE, PetalburgWoods_Text_GoBugPokemonTeam, PetalburgWoods_Text_ICouldntWin
	msgbox PetalburgWoods_Text_ImOutOfPokeBalls, MSGBOX_AUTOCLOSE
	end

PetalburgWoods_EventScript_James::
	trainerbattle_single TRAINER_JAMES_1, PetalburgWoods_Text_InstantlyPopularWithBugPokemon, PetalburgWoods_Text_CantBePopularIfILose, PetalburgWoods_EventScript_TryRegisterJames
	specialvar VAR_RESULT, ShouldTryRematchBattle
	goto_if_eq VAR_RESULT, TRUE, PetalburgWoods_EventScript_JamesRematch
	setvar VAR_0x8004, TRAINER_JAMES_1
	specialvar VAR_RESULT, IsTrainerRegistered
	goto_if_eq VAR_RESULT, FALSE, PetalburgWoods_EventScript_TryRegisterJames2
	msgbox PetalburgWoods_Text_PeopleRespectYou, MSGBOX_DEFAULT
	release
	end

PetalburgWoods_EventScript_TryRegisterJames::
	special PlayerFaceTrainerAfterBattle
	waitmovement 0
	goto_if_set FLAG_HAS_MATCH_CALL, PetalburgWoods_EventScript_RegisterJames
	release
	end

PetalburgWoods_EventScript_RegisterJames::
	msgbox PetalburgWoods_Text_IWantRematch1, MSGBOX_DEFAULT
	register_matchcall TRAINER_JAMES_1
	release
	end

PetalburgWoods_EventScript_TryRegisterJames2::
	goto_if_set FLAG_HAS_MATCH_CALL, PetalburgWoods_EventScript_RegisterJames2
	msgbox PetalburgWoods_Text_PeopleRespectYou, MSGBOX_DEFAULT
	release
	end

PetalburgWoods_EventScript_RegisterJames2::
	msgbox PetalburgWoods_Text_IWantRematch2, MSGBOX_DEFAULT
	register_matchcall TRAINER_JAMES_1
	release
	end

PetalburgWoods_EventScript_JamesRematch::
	trainerbattle_rematch TRAINER_JAMES_1, PetalburgWoods_Text_MyPokemonHaveGrown, PetalburgWoods_Text_CantBePopularIfLose
	msgbox PetalburgWoods_Text_IveBeenTrainingHard, MSGBOX_AUTOCLOSE
	end

PetalburgWoods_Text_GoBugPokemonTeam:
	.string "I caught a whole bunch of POKéMON!\p"
	.string "Go, go, go!\n"
	.string "My BUG POKéMON team!$"

PetalburgWoods_Text_ICouldntWin:
	.string "I have all these POKéMON,\n"
	.string "but I couldn't win…$"

PetalburgWoods_Text_ImOutOfPokeBalls:
	.string "I caught a bunch of POKéMON.\n"
	.string "Now I'm out of POKé BALLS.$"

PetalburgWoods_Text_InstantlyPopularWithBugPokemon:
	.string "If you take BUG POKéMON to school,\n"
	.string "you get to be instantly popular!$"

PetalburgWoods_Text_CantBePopularIfILose:
	.string "I can't be popular if I lose.$"

PetalburgWoods_Text_PeopleRespectYou:
	.string "If you have a big BUG POKéMON,\n"
	.string "people respect you for it.$"

PetalburgWoods_Text_IWantRematch1:
	.string "I want a rematch when my BUG\n"
	.string "POKéMON grow up!\p"
	.string "I'm registering you in my POKéNAV!$"

PetalburgWoods_Text_IWantRematch2:
	.string "I want a rematch when my BUG \n"
	.string "POKéMON grow up!\p"
	.string "I'm registering you in my POKéNAV!$"

PetalburgWoods_Text_MyPokemonHaveGrown:
	.string "My BUG POKéMON have grown.\n"
	.string "I'll be popular again.$"

PetalburgWoods_Text_CantBePopularIfLose:
	.string "I can't be popular if I lose.$"

PetalburgWoods_Text_IveBeenTrainingHard:
	.string "You get to be popular if you have\n"
	.string "strong POKéMON, right?\l"
	.string "So, I've been training hard.$"

PetalburgWoods_Text_StayOutOfTallGrass:
	.string "Yo, there!\n"
	.string "Your POKéMON doing okay?\p"
	.string "If your POKéMON are weak and you want\n"
	.string "to avoid battles, you should stay out\l"
	.string "of tall grass.$"

PetalburgWoods_Text_HiddenItemsExplanation:
	.string "Sometimes, there are things on the\n"
	.string "ground even if you can't see them.\p"
	.string "That's why I always check where I'm\n"
	.string "walking.$"

PetalburgWoods_Text_TryUsingThisItem:
	.string "Oh, neat!\n"
	.string "That's the BADGE from RUSTBORO GYM!\p"
	.string "You must be a TRAINER.\n"
	.string "You should try using this item.$"

PetalburgWoods_Text_MiracleSeedExplanation:
	.string "It's a MIRACLE SEED.\n"
	.string "If a POKéMON holds that item, its\l"
	.string "GRASS-type moves become stronger.\p"
	.string "Besides MIRACLE SEED, I think there are\n"
	.string "other convenient items for POKéMON\l"
	.string "to hold.$"

PetalburgWoods_Text_TrainerTipsExperience:
	.string "TRAINER TIPS\p"
	.string "Any POKéMON that appears even once\n"
	.string "in a battle is awarded EXP Points.\p"
	.string "To raise a weak POKéMON, put it at the\n"
	.string "left of the team list.\p"
	.string "As soon as a battle starts, switch it\n"
	.string "out. It will earn EXP Points without\l"
	.string "being exposed to any harm.$"

PetalburgWoods_Text_TrainerTipsPP:
	.string "TRAINER TIPS\p"
	.string "In addition to Hit Points (HP), POKéMON\n"
	.string "have Power Points (PP) that are used to\l"
	.string "make moves during battle.\p"
	.string "If a POKéMON runs out of PP, it must be\n"
	.string "taken to a POKéMON CENTER.$"


@ Project-owned reservation; no donor gameplay, flags or warp destination.
PetalburgWoods_EventScript_HyperConstruction_1::
	lock
	faceplayer
	msgbox PetalburgWoods_Text_HyperConstruction_1, MSGBOX_DEFAULT
	release
	end

PetalburgWoods_Text_HyperConstruction_1:
	.string "Flower Paradise is\n"
	.string "under construction.\p"
	.string "Please check back later!$"

@ Project-owned reservation; no donor gameplay, flags or warp destination.
PetalburgWoods_EventScript_HyperConstruction_2::
	lock
	faceplayer
	msgbox PetalburgWoods_Text_HyperConstruction_2, MSGBOX_DEFAULT
	release
	end

PetalburgWoods_Text_HyperConstruction_2:
	.string "Flower Paradise is\n"
	.string "under construction.\p"
	.string "Please check back later!$"

@ Project-owned reservation; no donor gameplay, flags or warp destination.
PetalburgWoods_EventScript_HyperConstruction_3::
	lock
	faceplayer
	msgbox PetalburgWoods_Text_HyperConstruction_3, MSGBOX_DEFAULT
	release
	end

PetalburgWoods_Text_HyperConstruction_3:
	.string "Allearth Forest is\n"
	.string "under construction.\p"
	.string "Please check back later!$"

LegendsWoods_Text_Readings:
	.string "The energy spike came from here.\p"
	.string "Devon and Silph registered it\n"
	.string "at exactly the same moment.$"

LegendsWoods_Text_Scope:
	.string "The modified Silph Scope caught\n"
	.string "an image inside the opening.\p"
	.string "Buildings. People. A different sky.\p"
	.string "It collapsed before I could\n"
	.string "identify the location.$"

LegendsWoods_Text_Greeting:
	.string "Oh! A Trainer. Please be careful.\p"
	.string "We are investigating the rifts.\n"
	.string "I work for Devon in Rustboro.\p"
	.string "My colleague is visiting from\n"
	.string "Silph in Kanto.$"

LegendsWoods_Text_Demand:
	.string "Your recording. Hand it over.$"

LegendsWoods_Text_Refusal:
	.string "Who are you? This is joint research\n"
	.string "between Devon and Silph!$"

LegendsWoods_Text_Help:
	.string "Please, help us! We cannot let\n"
	.string "someone take these findings.$"

LegendsWoods_Text_Challenge:
	.string "You felt the disturbance too.\n"
	.string "That is why you stopped.\p"
	.string "Step aside. Or show me how far\n"
	.string "that curiosity will take you.$"

LegendsWoods_Text_Defeat:
	.string "Enough. You have made your point.$"

LegendsWoods_Text_Delay:
	.string "You have strength.\p"
	.string "But you were watching only me.$"

LegendsWoods_Text_Three:
	.string "Two more?!\n"
	.string "Where did they come from?$"

LegendsWoods_Text_Confirmed:
	.string "The signatures match.\n"
	.string "Take the Scope recording.\p"
	.string "The device they recovered needs\n"
	.string "a stable point of reference.$"

LegendsWoods_Text_Stolen:
	.string "The backup drive!\n"
	.string "You took the only clear images!$"

LegendsWoods_Text_Withdraw:
	.string "Our task is complete.\n"
	.string "Do not follow us, Trainer.$"

LegendsWoods_Text_Thanks:
	.string "You kept him away from us.\n"
	.string "Thank you.\p"
	.string "This is a small gift,\n"
	.string "but you have more than earned it.$"

LegendsWoods_Text_Damage:
	.string "The readings are still here.\n"
	.string "Only the Scope images are gone.\p"
	.string "They knew exactly what to take.$"

LegendsWoods_Text_Thought:
	.string "That device... Could they mean\n"
	.string "the object from Timeless Woods?\p"
	.string "I need to get this news to Birch.$"

LegendsWoods_Text_ThoughtUnknown:
	.string "What device were they talking about?\p"
	.string "Birch needs to hear about this.$"

LegendsWoods_Text_Report:
	.string "We will warn Devon right away.\p"
	.string "If you reach Rustboro, ask for us\n"
	.string "at the Devon building.\p"
	.string "Tell them you helped in the woods.\p"
	.string "We must compare what you saw, too.$"

LegendsWoods_Text_NoRoom:
	.string "Your Bag is full. Please do not\n"
	.string "worry about the gift right now.$"

@ Silph stays in the eastern lane, clear of the player and Devon.
LegendsWoods_SilphCheckScope:
	face_up
	delay_16
	face_left
	step_end
LegendsWoods_SilphJoinPlayer:
	walk_down
	face_down
	step_end
LegendsWoods_SilphReactToThreat:
	face_left
	delay_16
	step_end
LegendsWoods_SilphProtectRecording:
	walk_up
	face_left
	step_end
LegendsWoods_SilphAfterTheft:
	walk_down
	face_down
	step_end
