@ FireRed occupation adapted to project-owned state.

LegendsPastSaffron_Guard_0::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSaffron_Guard_0_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Guard_0_Text:
    .string "What do you want?\nGet lost!$"

LegendsPastSaffron_Guard_1::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSaffron_Guard_1_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Guard_1_Text:
    .string "Boss said he'll take this town\nin the name of Team Rocket!$"

LegendsPastSaffron_Guard_2::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSaffron_Guard_2_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Guard_2_Text:
    .string "Don't get defiant!\nOr I'll have to hurt you!$"

LegendsPastSaffron_Guard_3::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSaffron_Guard_3_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Guard_3_Text:
    .string "Saffron belongs to Team Rocket!$"

LegendsPastSaffron_Guard_4::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSaffron_Guard_4_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Guard_4_Text:
    .string "My life as a criminal makes me feel\nso alive!$"

LegendsPastSaffron_Guard_5::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSaffron_Guard_5_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Guard_5_Text:
    .string "Zzz… The Boss said no visitors…\nNo visitors…$"

LegendsPastSaffron_Guard_6::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSaffron_Guard_6_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Guard_6_Text:
    .string "With Silph under control, we can\nexploit Pokémon around the world!\pWe'll get stinking rich, yeahah!$"

LegendsPastSaffron_Guard_7::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSaffron_Guard_7_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Guard_7_Text:
    .string "Ow!\nWatch where you're walking!$"

LegendsPastSaffron_Sign_0::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSaffron_Sign_0_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Sign_0_Text:
    .string "Saffron CITY\nShining, Golden Land of Commerce$"

LegendsPastSaffron_Sign_1::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSaffron_Sign_1_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Sign_1_Text:
    .string "FIGHTING DOJO$"

LegendsPastSaffron_Sign_2::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSaffron_Sign_2_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Sign_2_Text:
    .string "Silph's latest product!\nRelease to be determined…$"

LegendsPastSaffron_Sign_3::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSaffron_Sign_3_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Sign_3_Text:
    .string "TRAINER TIPS\pThe new GREAT BALL offers improved\ncatching rates.\pTry it on those hard-to-catch\nPokémon.$"

LegendsPastSaffron_Sign_4::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSaffron_Sign_4_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Sign_4_Text:
    .string "Silph Co. OFFICE BUILDING$"

LegendsPastSaffron_Sign_5::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSaffron_Sign_5_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Sign_5_Text:
    .string "TRAINER TIPS\pFULL HEAL cures all ailments like\nburns, paralysis, poisoning,\lfreezing, and sleep.\pIt costs a bit more, but it's more\nconvenient than buying other items.$"

LegendsPastSaffron_Sign_6::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSaffron_Sign_6_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Sign_6_Text:
    .string "Saffron CITY Pokémon GYM\nLEADER: SABRINA\lThe Master of PSYCHIC Pokémon!$"

LegendsPastSaffron_Sign_7::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSaffron_Sign_7_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Sign_7_Text:
    .string "MR. PSYCHIC'S HOUSE$"

LegendsPastSaffron_Sign_8::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSaffron_Sign_8_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSaffron_Sign_8_Text:
    .string "Pokémon TRAINER FAN CLUB\pMany TRAINERS have scribbled their\nnames on this sign.$"

LegendsPastSilph_F1_NPC0::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F1_NPC0_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F1_NPC0_Text:
    .string "Please keep your voice down.\nThey've taken the upper floors.\pThe President is still upstairs.\nI couldn't leave the others.$"

LegendsPastSilph_FloorSign_1::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_FloorSign_1_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_FloorSign_1_Text:
    .string "Silph Co. Head Office\n1F$"

LegendsAshes_Grunt_0::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x290, LegendsAshes_Grunt_0_After
    setvar VAR_LA_SILPH_OPPONENT, 1
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsAshes_Grunt_0_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsAshes_Grunt_0_Intro, LegendsAshes_Grunt_0_Defeat, LegendsAshes_Grunt_0_Victory
LegendsAshes_Grunt_0_After:
    setflag 0x290
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsAshes_Grunt_0_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsAshes_Grunt_0_Intro:
    .string "Hey, kid!\nWhat are you wandering here for?$"

LegendsAshes_Grunt_0_Defeat:
    .string "I goofed!$"

LegendsAshes_Grunt_0_Post:
    .string "Silph Co. will be associated with\nTeam Rocket!$"

LegendsPastSilph_F2_NPC1::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x281, LegendsPastSilph_F2_NPC1_After
    msgbox LegendsPastSilph_F2_NPC1_Intro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 12
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, LegendsPastSilph_F2_NPC1_Defeat
    setflag 0x281
LegendsPastSilph_F2_NPC1_After:
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F2_NPC1_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F2_NPC1_Intro:
    .string "It's off-limits here!\nGo home!$"

LegendsPastSilph_F2_NPC1_Defeat:
    .string "You're good.$"

LegendsPastSilph_F2_NPC1_Post:
    .string "Can you solve the maze in here?\nIt's not easy, I tell you!$"

LegendsPastSilph_F2_NPC2::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x282, LegendsPastSilph_F2_NPC2_After
    setvar VAR_LA_SILPH_OPPONENT, 13
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsPastSilph_F2_NPC2_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsPastSilph_F2_NPC2_Intro, LegendsPastSilph_F2_NPC2_Defeat, LegendsPastSilph_F2_NPC2_Victory
LegendsPastSilph_F2_NPC2_After:
    setflag 0x282
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F2_NPC2_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F2_NPC2_Intro:
    .string "No kids are allowed in here!$"

LegendsPastSilph_F2_NPC2_Defeat:
    .string "Tough!$"

LegendsPastSilph_F2_NPC2_Post:
    .string "Diamond-shaped tiles are teleport\nblocks.\pThey're transporters for this\nhigh-tech building.$"

LegendsPastSilph_F2_NPC3::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x283, LegendsPastSilph_F2_NPC3_After
    msgbox LegendsPastSilph_F2_NPC3_Intro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 14
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, LegendsPastSilph_F2_NPC3_Defeat
    setflag 0x283
LegendsPastSilph_F2_NPC3_After:
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F2_NPC3_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F2_NPC3_Intro:
    .string "Help!\nI'm a Silph employee.$"

LegendsPastSilph_F2_NPC3_Defeat:
    .string "How did you know\nI was a ROCKET?$"

LegendsPastSilph_F2_NPC3_Post:
    .string "I work for both Silph and TEAM\nROCKET.$"

LegendsPastSilph_F2_NPC4::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F2_NPC4_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F2_NPC4_Text:
    .string "I hid when the Rockets came.\nThey brought their own scientists.\pTry the beds on the ninth floor\nif your Pokémon need a rest.$"

LegendsPastSilph_FloorSign_2::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_FloorSign_2_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_FloorSign_2_Text:
    .string "Silph Co. Head Office\n2F$"

LegendsAshes_Grunt_1::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x291, LegendsAshes_Grunt_1_After
    setvar VAR_LA_SILPH_OPPONENT, 2
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsAshes_Grunt_1_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsAshes_Grunt_1_Intro, LegendsAshes_Grunt_1_Defeat, LegendsAshes_Grunt_1_Victory
LegendsAshes_Grunt_1_After:
    setflag 0x291
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsAshes_Grunt_1_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsAshes_Grunt_1_Intro:
    .string "Quit messing with us, kid!$"

LegendsAshes_Grunt_1_Defeat:
    .string "I give up!$"

LegendsAshes_Grunt_1_Post:
    .string "A Card Key opens those doors.\nSomeone lost one near the beds.$"

LegendsPastSilph_F3_NPC1::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F3_NPC1_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F3_NPC1_Text:
    .string "I work for Silph Co.\nWhat am I to do?$"

LegendsPastSilph_F3_NPC2::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x284, LegendsPastSilph_F3_NPC2_After
    msgbox LegendsPastSilph_F3_NPC2_Intro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 15
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, LegendsPastSilph_F3_NPC2_Defeat
    setflag 0x284
LegendsPastSilph_F3_NPC2_After:
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F3_NPC2_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F3_NPC2_Intro:
    .string "I support Team Rocket more than\nI support Silph Co.!$"

LegendsPastSilph_F3_NPC2_Defeat:
    .string "You really got me!$"

LegendsPastSilph_F3_NPC2_Post:
    .string "Humph…\pTeam Rocket said that if I helped\nthem, they'd let me study Pokémon.$"

LegendsPastSilph_FloorSign_3::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_FloorSign_3_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_FloorSign_3_Text:
    .string "Silph Co. Head Office\n3F$"

LegendsAshes_Grunt_2::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x292, LegendsAshes_Grunt_2_After
    setvar VAR_LA_SILPH_OPPONENT, 3
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsAshes_Grunt_2_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsAshes_Grunt_2_Intro, LegendsAshes_Grunt_2_Defeat, LegendsAshes_Grunt_2_Victory
LegendsAshes_Grunt_2_After:
    setflag 0x292
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsAshes_Grunt_2_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsAshes_Grunt_2_Intro:
    .string "Intruder spotted!$"

LegendsAshes_Grunt_2_Defeat:
    .string "Who are you?$"

LegendsAshes_Grunt_2_Post:
    .string "I better tell the Boss on 11F!$"

LegendsPastSilph_F4_NPC1::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x285, LegendsPastSilph_F4_NPC1_After
    setvar VAR_LA_SILPH_OPPONENT, 16
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsPastSilph_F4_NPC1_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsPastSilph_F4_NPC1_Intro, LegendsPastSilph_F4_NPC1_Defeat, LegendsPastSilph_F4_NPC1_Victory
LegendsPastSilph_F4_NPC1_After:
    setflag 0x285
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F4_NPC1_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F4_NPC1_Intro:
    .string "Team Rocket has taken control\nof Silph Co.!$"

LegendsPastSilph_F4_NPC1_Defeat:
    .string "Arrgh!$"

LegendsPastSilph_F4_NPC1_Post:
    .string "Fwahahaha!\nMy Boss has been after this place!$"

LegendsPastSilph_F4_NPC2::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x286, LegendsPastSilph_F4_NPC2_After
    msgbox LegendsPastSilph_F4_NPC2_Intro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 17
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, LegendsPastSilph_F4_NPC2_Defeat
    setflag 0x286
LegendsPastSilph_F4_NPC2_After:
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F4_NPC2_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F4_NPC2_Intro:
    .string "My Pokémon is my loyal servant.$"

LegendsPastSilph_F4_NPC2_Defeat:
    .string "Darn!\nYou weak Pokémon!$"

LegendsPastSilph_F4_NPC2_Post:
    .string "A Card Key opens those doors.\nSomeone lost one near the beds.$"

LegendsPastSilph_F4_NPC3::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F4_NPC3_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F4_NPC3_Text:
    .string "Sssh!\nCan't you see I'm hiding?$"

LegendsPastSilph_FloorSign_4::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_FloorSign_4_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_FloorSign_4_Text:
    .string "Silph Co. Head Office\n4F$"

LegendsAshes_Grunt_3::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x293, LegendsAshes_Grunt_3_After
    setvar VAR_LA_SILPH_OPPONENT, 4
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsAshes_Grunt_3_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsAshes_Grunt_3_Intro, LegendsAshes_Grunt_3_Defeat, LegendsAshes_Grunt_3_Victory
LegendsAshes_Grunt_3_After:
    setflag 0x293
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsAshes_Grunt_3_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsAshes_Grunt_3_Intro:
    .string "Show Team Rocket a little respect!$"

LegendsAshes_Grunt_3_Defeat:
    .string "Cough…\nCough…$"

LegendsAshes_Grunt_3_Post:
    .string "Which reminds me.\pKOFFING evolves into WEEZING!$"

LegendsPastSilph_F5_NPC1::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x287, LegendsPastSilph_F5_NPC1_After
    msgbox LegendsPastSilph_F5_NPC1_Intro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 18
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, LegendsPastSilph_F5_NPC1_Defeat
    setflag 0x287
LegendsPastSilph_F5_NPC1_After:
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F5_NPC1_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F5_NPC1_Intro:
    .string "Whaaat?\pThere shouldn't be any children\nhere!$"

LegendsPastSilph_F5_NPC1_Defeat:
    .string "Oh, goodness!$"

LegendsPastSilph_F5_NPC1_Post:
    .string "You're only on 5F.\nIt's a long way to my Boss!$"

LegendsPastSilph_F5_NPC2::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F5_NPC2_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F5_NPC2_Text:
    .string "Team Rocket is in an uproar over\nsome intruder.\pThat's you, right?$"

LegendsPastSilph_F5_NPC3::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x288, LegendsPastSilph_F5_NPC3_After
    msgbox LegendsPastSilph_F5_NPC3_Intro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 19
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, LegendsPastSilph_F5_NPC3_Defeat
    setflag 0x288
LegendsPastSilph_F5_NPC3_After:
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F5_NPC3_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F5_NPC3_Intro:
    .string "We study POKé BALL technology on\nthis floor.$"

LegendsPastSilph_F5_NPC3_Defeat:
    .string "Dang!\nBlast it!$"

LegendsPastSilph_F5_NPC3_Post:
    .string "We worked on the ultimate POKé\nBALL which would catch anything.$"

LegendsPastSilph_F5_NPC4::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x289, LegendsPastSilph_F5_NPC4_After
    setvar VAR_LA_SILPH_OPPONENT, 20
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsPastSilph_F5_NPC4_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsPastSilph_F5_NPC4_Intro, LegendsPastSilph_F5_NPC4_Defeat, LegendsPastSilph_F5_NPC4_Victory
LegendsPastSilph_F5_NPC4_After:
    setflag 0x289
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F5_NPC4_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F5_NPC4_Intro:
    .string "I heard a kid was wandering\naround.$"

LegendsPastSilph_F5_NPC4_Defeat:
    .string "Boom!$"

LegendsPastSilph_F5_NPC4_Post:
    .string "It's not smart to pick a fight with\nTeam Rocket!$"

LegendsPastSilph_F5_NPC8::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F5_NPC8_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F5_NPC8_Text:
    .string "Those thugs took over our building…\pTheir Boss said he was looking\nfor strong Pokémon.\pI hope our President managed\nto avoid trouble…$"

LegendsPastSilph_FloorSign_5::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_FloorSign_5_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_FloorSign_5_Text:
    .string "Silph Co. Head Office\n5F$"

LegendsAshes_Grunt_4::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x294, LegendsAshes_Grunt_4_After
    setvar VAR_LA_SILPH_OPPONENT, 5
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsAshes_Grunt_4_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsAshes_Grunt_4_Intro, LegendsAshes_Grunt_4_Defeat, LegendsAshes_Grunt_4_Victory
LegendsAshes_Grunt_4_After:
    setflag 0x294
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsAshes_Grunt_4_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsAshes_Grunt_4_Intro:
    .string "I am one of the four ROCKET\nBROTHERS!$"

LegendsAshes_Grunt_4_Defeat:
    .string "Flame out!$"

LegendsAshes_Grunt_4_Post:
    .string "No matter!\nMy brothers will avenge me!$"

LegendsPastSilph_F6_NPC1::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F6_NPC1_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F6_NPC1_Text:
    .string "Oh dear, oh dear.\nHelp me, please!$"

LegendsPastSilph_F6_NPC2::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F6_NPC2_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F6_NPC2_Text:
    .string "That man next to me…\nHe's such a coward!$"

LegendsPastSilph_F6_NPC3::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F6_NPC3_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F6_NPC3_Text:
    .string "They must have targeted Silph for\nour Pokémon products.$"

LegendsPastSilph_F6_NPC4::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F6_NPC4_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F6_NPC4_Text:
    .string "The ROCKETS came and took over\nthe building!$"

LegendsPastSilph_F6_NPC5::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F6_NPC5_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F6_NPC5_Text:
    .string "Team Rocket is trying to conquer\nthe world with Pokémon.$"

LegendsPastSilph_F6_NPC6::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x28A, LegendsPastSilph_F6_NPC6_After
    msgbox LegendsPastSilph_F6_NPC6_Intro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 21
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, LegendsPastSilph_F6_NPC6_Defeat
    setflag 0x28A
LegendsPastSilph_F6_NPC6_After:
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F6_NPC6_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F6_NPC6_Intro:
    .string "That rotten PRESIDENT!\pServes him right for shipping me\noff to the TIKSI BRANCH!\pThat's why Team Rocket came after\nus, I'm sure of it!$"

LegendsPastSilph_F6_NPC6_Defeat:
    .string "Shoot!$"

LegendsPastSilph_F6_NPC6_Post:
    .string "TIKSI BRANCH?\nIt's in Russian no-man's-land!$"

LegendsPastSilph_F6_NPC9::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x28B, LegendsPastSilph_F6_NPC9_After
    setvar VAR_LA_SILPH_OPPONENT, 22
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsPastSilph_F6_NPC9_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsPastSilph_F6_NPC9_Intro, LegendsPastSilph_F6_NPC9_Defeat, LegendsPastSilph_F6_NPC9_Victory
LegendsPastSilph_F6_NPC9_After:
    setflag 0x28B
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F6_NPC9_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F6_NPC9_Intro:
    .string "You dare betray Team Rocket?$"

LegendsPastSilph_F6_NPC9_Defeat:
    .string "You traitor!$"

LegendsPastSilph_F6_NPC9_Post:
    .string "If you stand for justice, you\nbetray us bad guys!$"

LegendsPastSilph_FloorSign_6::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_FloorSign_6_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_FloorSign_6_Text:
    .string "Silph Co. Head Office\n6F$"

LegendsPastSilph_F7_NPC1::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F7_NPC1_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F7_NPC1_Text:
    .string "Rocket is holding our staff here.\nEven the Pokémon are frightened.\pA boy with a Kirlia went upstairs.\nI hope he found somewhere safe.$"

LegendsAshes_Grunt_5::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x295, LegendsAshes_Grunt_5_After
    setvar VAR_LA_SILPH_OPPONENT, 6
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsAshes_Grunt_5_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsAshes_Grunt_5_Intro, LegendsAshes_Grunt_5_Defeat, LegendsAshes_Grunt_5_Victory
LegendsAshes_Grunt_5_After:
    setflag 0x295
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsAshes_Grunt_5_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsAshes_Grunt_5_Intro:
    .string "I am one of the four ROCKET\nBROTHERS!$"

LegendsAshes_Grunt_5_Defeat:
    .string "Aack!\nBrothers, I lost!$"

LegendsAshes_Grunt_5_Post:
    .string "Doesn't matter.\nMy brothers will repay the favor!$"

LegendsPastSilph_F7_NPC3::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x28C, LegendsPastSilph_F7_NPC3_After
    setvar VAR_LA_SILPH_OPPONENT, 23
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsPastSilph_F7_NPC3_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsPastSilph_F7_NPC3_Intro, LegendsPastSilph_F7_NPC3_Defeat, LegendsPastSilph_F7_NPC3_Victory
LegendsPastSilph_F7_NPC3_After:
    setflag 0x28C
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F7_NPC3_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F7_NPC3_Intro:
    .string "A child intruder?\nThat must be you!$"

LegendsPastSilph_F7_NPC3_Defeat:
    .string "Fine!\nI lost!$"

LegendsPastSilph_F7_NPC3_Post:
    .string "Go on home before my Boss gets\nticked off!$"

LegendsPastSilph_F7_NPC4::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x28D, LegendsPastSilph_F7_NPC4_After
    setvar VAR_LA_SILPH_OPPONENT, 24
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsPastSilph_F7_NPC4_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsPastSilph_F7_NPC4_Intro, LegendsPastSilph_F7_NPC4_Defeat, LegendsPastSilph_F7_NPC4_Victory
LegendsPastSilph_F7_NPC4_After:
    setflag 0x28D
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F7_NPC4_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F7_NPC4_Intro:
    .string "Uh-oh!\nI smell a little mouse!$"

LegendsPastSilph_F7_NPC4_Defeat:
    .string "Lights out!$"

LegendsPastSilph_F7_NPC4_Post:
    .string "You won't find my Boss by just\nscurrying around!$"

LegendsPastSilph_F7_NPC5::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F7_NPC5_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F7_NPC5_Text:
    .string "You!\nIt's really dangerous here!\pYou came to save me?\nYou can't!$"

LegendsPastSilph_F7_NPC6::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F7_NPC6_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F7_NPC6_Text:
    .string "Team Rocket was after the MASTER\nBALL, which catches any Pokémon.$"

LegendsPastSilph_F7_NPC7::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F7_NPC7_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F7_NPC7_Text:
    .string "It would be bad if Team Rocket\ntook over Silph or our Pokémon.$"

LegendsPastSilph_F7_NPC8::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x28E, LegendsPastSilph_F7_NPC8_After
    msgbox LegendsPastSilph_F7_NPC8_Intro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 25
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, LegendsPastSilph_F7_NPC8_Defeat
    setflag 0x28E
LegendsPastSilph_F7_NPC8_After:
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F7_NPC8_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F7_NPC8_Intro:
    .string "Heheh!\pYou mistook me for a Silph worker?$"

LegendsPastSilph_F7_NPC8_Defeat:
    .string "I'm done!$"

LegendsPastSilph_F7_NPC8_Post:
    .string "Despite your age, you are a\nskilled TRAINER!$"

LegendsPastSilph_FloorSign_7::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_FloorSign_7_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_FloorSign_7_Text:
    .string "Silph Co. Head Office\n7F$"

LegendsAshes_Grunt_6::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x296, LegendsAshes_Grunt_6_After
    setvar VAR_LA_SILPH_OPPONENT, 7
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsAshes_Grunt_6_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsAshes_Grunt_6_Intro, LegendsAshes_Grunt_6_Defeat, LegendsAshes_Grunt_6_Victory
LegendsAshes_Grunt_6_After:
    setflag 0x296
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsAshes_Grunt_6_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsAshes_Grunt_6_Intro:
    .string "That's as far as you'll go!$"

LegendsAshes_Grunt_6_Defeat:
    .string "Not enough grit!$"

LegendsAshes_Grunt_6_Post:
    .string "If you don't turn back…\nI'll call for backup!$"

LegendsPastSilph_F8_NPC1::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x28F, LegendsPastSilph_F8_NPC1_After
    setvar VAR_LA_SILPH_OPPONENT, 26
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsPastSilph_F8_NPC1_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsPastSilph_F8_NPC1_Intro, LegendsPastSilph_F8_NPC1_Defeat, LegendsPastSilph_F8_NPC1_Victory
LegendsPastSilph_F8_NPC1_After:
    setflag 0x28F
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F8_NPC1_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F8_NPC1_Intro:
    .string "I am one of the four ROCKET\nBROTHERS!$"

LegendsPastSilph_F8_NPC1_Defeat:
    .string "Whoo!\nOh, Brothers!$"

LegendsPastSilph_F8_NPC1_Post:
    .string "I'll leave you up to my brothers.$"

LegendsPastSilph_F8_NPC2::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x298, LegendsPastSilph_F8_NPC2_After
    msgbox LegendsPastSilph_F8_NPC2_Intro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 27
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, LegendsPastSilph_F8_NPC2_Defeat
    setflag 0x298
LegendsPastSilph_F8_NPC2_After:
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F8_NPC2_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F8_NPC2_Intro:
    .string "You're causing us problems!$"

LegendsPastSilph_F8_NPC2_Defeat:
    .string "Huh?\nI lost?$"

LegendsPastSilph_F8_NPC2_Post:
    .string "So, what do you think of Silph\nBUILDING's maze?$"

LegendsPastSilph_F8_NPC3::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F8_NPC3_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F8_NPC3_Text:
    .string "I wonder if Silph is finished…$"

LegendsPastSilph_F8_NPC5::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F8_NPC5_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F8_NPC5_Text:
    .string "Team Rocket's Boss is cruel!\pTo him, Pokémon are just tools.\pWhat will happen if he\ntakes over our company?$"

LegendsPastSilph_FloorSign_8::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_FloorSign_8_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_FloorSign_8_Text:
    .string "Silph Co. Head Office\n8F$"

LegendsPastSilph_F9_NPC0::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x299, LegendsPastSilph_F9_NPC0_After
    msgbox LegendsPastSilph_F9_NPC0_Intro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 28
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, LegendsPastSilph_F9_NPC0_Defeat
    setflag 0x299
LegendsPastSilph_F9_NPC0_After:
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F9_NPC0_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F9_NPC0_Intro:
    .string "Your Pokémon have weak points!\nI can nail them!$"

LegendsPastSilph_F9_NPC0_Defeat:
    .string "You hammered me!$"

LegendsPastSilph_F9_NPC0_Post:
    .string "Exploiting weak spots does work.\nThink about type advantages.$"

LegendsAshes_Grunt_7::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x297, LegendsAshes_Grunt_7_After
    setvar VAR_LA_SILPH_OPPONENT, 8
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsAshes_Grunt_7_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsAshes_Grunt_7_Intro, LegendsAshes_Grunt_7_Defeat, LegendsAshes_Grunt_7_Victory
LegendsAshes_Grunt_7_After:
    setflag 0x297
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsAshes_Grunt_7_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsAshes_Grunt_7_Intro:
    .string "I am one of the four ROCKET\nBROTHERS!$"

LegendsAshes_Grunt_7_Defeat:
    .string "Warg!\nBrothers, I lost!$"

LegendsAshes_Grunt_7_Post:
    .string "My brothers will avenge me!$"

LegendsPastSilph_F9_NPC2::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_F9_NPC2_Text, MSGBOX_DEFAULT
    special HealPlayerParty
    goto LegendsAshes_End

LegendsPastSilph_F9_NPC2_Text:
    .string "You look exhausted. Rest here.\nI'll watch while your team heals.$"

LegendsPastSilph_F9_NPC3::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x29A, LegendsPastSilph_F9_NPC3_After
    setvar VAR_LA_SILPH_OPPONENT, 29
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsPastSilph_F9_NPC3_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsPastSilph_F9_NPC3_Intro, LegendsPastSilph_F9_NPC3_Defeat, LegendsPastSilph_F9_NPC3_Victory
LegendsPastSilph_F9_NPC3_After:
    setflag 0x29A
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F9_NPC3_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F9_NPC3_Intro:
    .string "Your Pokémon seem to adore you,\nkid!$"

LegendsPastSilph_F9_NPC3_Defeat:
    .string "Ghaaah!$"

LegendsPastSilph_F9_NPC3_Post:
    .string "If I had started as a TRAINER at\nyour age…$"

LegendsPastSilph_FloorSign_9::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_FloorSign_9_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_FloorSign_9_Text:
    .string "Silph Co. Head Office\n9F$"

LegendsPastSilph_F10_NPC0::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x29B, LegendsPastSilph_F10_NPC0_After
    msgbox LegendsPastSilph_F10_NPC0_Intro, MSGBOX_DEFAULT
    closemessage
    setvar VAR_LA_SILPH_OPPONENT, 30
    cleartrainerflag TRAINER_GRUNT_UNUSED
    trainerbattle_no_intro TRAINER_GRUNT_UNUSED, LegendsPastSilph_F10_NPC0_Defeat
    setflag 0x29B
LegendsPastSilph_F10_NPC0_After:
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F10_NPC0_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F10_NPC0_Intro:
    .string "Enough of your silly games!$"

LegendsPastSilph_F10_NPC0_Defeat:
    .string "No continues left!$"

LegendsPastSilph_F10_NPC0_Post:
    .string "Are you satisfied with beating me?\nThen go on home!$"

LegendsPastSilph_F10_NPC1::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_WALLY_RESCUED, LegendsPastSilph_StaffSafe
    msgbox LegendsPastSilph_F10_NPC1_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F10_NPC1_Text:
    .string "Waaaaa!\nI'm scared!$"

LegendsPastSilph_F10_NPC2::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x29C, LegendsPastSilph_F10_NPC2_After
    setvar VAR_LA_SILPH_OPPONENT, 31
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsPastSilph_F10_NPC2_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsPastSilph_F10_NPC2_Intro, LegendsPastSilph_F10_NPC2_Defeat, LegendsPastSilph_F10_NPC2_Victory
LegendsPastSilph_F10_NPC2_After:
    setflag 0x29C
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F10_NPC2_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F10_NPC2_Intro:
    .string "Welcome to 10F!\nSo good of you to join me!$"

LegendsPastSilph_F10_NPC2_Defeat:
    .string "I'm stunned!$"

LegendsPastSilph_F10_NPC2_Post:
    .string "Nice try, but the boardroom is up\none more floor.$"

LegendsPastSilph_FloorSign_10::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_FloorSign_10_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_FloorSign_10_Text:
    .string "Silph Co. Head Office\n10F$"

LegendsPastSilph_F11_NPC3::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x29D, LegendsPastSilph_F11_NPC3_After
    setvar VAR_LA_SILPH_OPPONENT, 32
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsPastSilph_F11_NPC3_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsPastSilph_F11_NPC3_Intro, LegendsPastSilph_F11_NPC3_Defeat, LegendsPastSilph_F11_NPC3_Victory
LegendsPastSilph_F11_NPC3_After:
    setflag 0x29D
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F11_NPC3_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F11_NPC3_Intro:
    .string "Halt! Do you have an appointment\nwith my Boss?$"

LegendsPastSilph_F11_NPC3_Defeat:
    .string "Gaah!\nDemolished!$"

LegendsPastSilph_F11_NPC3_Post:
    .string "Watch your step…\nMy Boss likes his Pokémon tough!$"

LegendsPastSilph_F11_NPC5::
    lockall
    faceplayer
    setspeaker SP_NAME_TEAM_ROCKET
    goto_if_set 0x29E, LegendsPastSilph_F11_NPC5_After
    setvar VAR_LA_SILPH_OPPONENT, 33
    cleartrainerflag TRAINER_GRUNT_UNUSED
LegendsPastSilph_F11_NPC5_Battle::
    trainerbattle_single TRAINER_GRUNT_UNUSED, LegendsPastSilph_F11_NPC5_Intro, LegendsPastSilph_F11_NPC5_Defeat, LegendsPastSilph_F11_NPC5_Victory
LegendsPastSilph_F11_NPC5_After:
    setflag 0x29E
    setspeaker SP_NAME_TEAM_ROCKET
    msgbox LegendsPastSilph_F11_NPC5_Post, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_F11_NPC5_Intro:
    .string "Stop right there!\nDon't you move!$"

LegendsPastSilph_F11_NPC5_Defeat:
    .string "Don't…\nPlease!$"

LegendsPastSilph_F11_NPC5_Post:
    .string "So, you want to see my Boss?$"

LegendsPastSilph_FloorSign_11::
    lockall
    faceplayer
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_FloorSign_11_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End

LegendsPastSilph_FloorSign_11_Text:
    .string "Silph Co. Head Office\n11F$"

LegendsPastSilph_Kirlia::
    lockall
    faceplayer
    playmoncry SPECIES_KIRLIA, CRY_MODE_NORMAL
    waitmoncry
    setvar VAR_LAST_TALKED, LOCALID_ASHES_SILPH_WALLY
    goto LegendsAshes_WallySilph

LegendsPastSilph_StaffSafe::
    setspeaker SP_NAME_NONE
    msgbox LegendsPastSilph_StaffSafe_Text, MSGBOX_DEFAULT
    goto LegendsAshes_End
LegendsPastSilph_StaffSafe_Text:
    .string "The Rockets have gone…\nWe can finally leave these rooms.\pThank you for helping us.\nPlease take care of your friends.$"

LegendsAshes_Grunt_0_Victory::
    setflag 0x290
    goto LegendsAshes_End

LegendsPastSilph_F2_NPC2_Victory::
    setflag 0x282
    goto LegendsAshes_End

LegendsAshes_Grunt_1_Victory::
    setflag 0x291
    goto LegendsAshes_End

LegendsAshes_Grunt_2_Victory::
    setflag 0x292
    goto LegendsAshes_End

LegendsPastSilph_F4_NPC1_Victory::
    setflag 0x285
    goto LegendsAshes_End

LegendsAshes_Grunt_3_Victory::
    setflag 0x293
    goto LegendsAshes_End

LegendsPastSilph_F5_NPC4_Victory::
    setflag 0x289
    goto LegendsAshes_End

LegendsAshes_Grunt_4_Victory::
    setflag 0x294
    goto LegendsAshes_End

LegendsPastSilph_F6_NPC9_Victory::
    setflag 0x28B
    goto LegendsAshes_End

LegendsAshes_Grunt_5_Victory::
    setflag 0x295
    goto LegendsAshes_End

LegendsPastSilph_F7_NPC3_Victory::
    setflag 0x28C
    goto LegendsAshes_End

LegendsPastSilph_F7_NPC4_Victory::
    setflag 0x28D
    goto LegendsAshes_End

LegendsAshes_Grunt_6_Victory::
    setflag 0x296
    goto LegendsAshes_End

LegendsPastSilph_F8_NPC1_Victory::
    setflag 0x28F
    goto LegendsAshes_End

LegendsAshes_Grunt_7_Victory::
    setflag 0x297
    goto LegendsAshes_End

LegendsPastSilph_F9_NPC3_Victory::
    setflag 0x29A
    goto LegendsAshes_End

LegendsPastSilph_F10_NPC2_Victory::
    setflag 0x29C
    goto LegendsAshes_End

LegendsPastSilph_F11_NPC3_Victory::
    setflag 0x29D
    goto LegendsAshes_End

LegendsPastSilph_F11_NPC5_Victory::
    setflag 0x29E
    goto LegendsAshes_End
