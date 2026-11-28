RustboroCity_DevonCorp_3F_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, RustboroCity_DevonCorp_3F_OnTransition
	map_script MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE, RustboroCity_DevonCorp_3F_OnWarp
	map_script MAP_SCRIPT_ON_FRAME_TABLE, RustboroCity_DevonCorp_3F_OnFrame
	.byte 0

RustboroCity_DevonCorp_3F_OnTransition:
	call_if_eq VAR_DEVON_CORP_3F_STATE, 0, RustboroCity_DevonCorp_3F_EventScript_SetEmployeePos
	end

RustboroCity_DevonCorp_3F_EventScript_SetEmployeePos::
	setobjectxyperm LOCALID_DEVON_CORP_3F_EMPLOYEE, 3, 2
	setobjectmovementtype LOCALID_DEVON_CORP_3F_EMPLOYEE, MOVEMENT_TYPE_FACE_LEFT
	return

RustboroCity_DevonCorp_3F_OnWarp:
	map_script_2 VAR_DEVON_CORP_3F_STATE, 0, RustboroCity_DevonCorp_3F_EventScript_PlayerFaceEast
	.2byte 0

RustboroCity_DevonCorp_3F_EventScript_PlayerFaceEast::
	turnobject LOCALID_PLAYER, DIR_EAST
	end

RustboroCity_DevonCorp_3F_OnFrame:
	map_script_2 VAR_DEVON_CORP_3F_STATE, 0, RustboroCity_DevonCorp_3F_EventScript_MeetPresident
	.2byte 0

RustboroCity_DevonCorp_3F_EventScript_MeetPresident::
	lockall
	setspeaker SP_NAME_DEVON_RESEARCHER
	msgbox RustboroCity_DevonCorp_3F_Text_ThisIs3rdFloorWaitHere, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_DEVON_CORP_3F_EMPLOYEE, RustboroCity_DevonCorp_3F_Movement_EmployeeWalkOffscreen
	waitmovement 0
	delay 80
	applymovement LOCALID_DEVON_CORP_3F_EMPLOYEE, RustboroCity_DevonCorp_3F_Movement_EmployeeReturnToPlayer
	waitmovement 0
	msgbox RustboroCity_DevonCorp_3F_Text_WordWithPresidentComeWithMe, MSGBOX_DEFAULT
	closemessage
	playbgm MUS_FOLLOW_ME, FALSE
	applymovement LOCALID_DEVON_CORP_3F_EMPLOYEE, RustboroCity_DevonCorp_3F_Movement_LeadPlayerToPresident
	applymovement LOCALID_PLAYER, RustboroCity_DevonCorp_3F_Movement_PlayerFollowToPresident
	waitmovement 0
	msgbox RustboroCity_DevonCorp_3F_Text_PleaseGoAhead, MSGBOX_DEFAULT
	closemessage
	fadedefaultbgm
	applymovement LOCALID_DEVON_CORP_3F_EMPLOYEE, RustboroCity_DevonCorp_3F_Movement_EmployeeFaceDesk
	applymovement LOCALID_PLAYER, RustboroCity_DevonCorp_3F_Movement_PlayerApproachDesk
	waitmovement 0
	setspeaker SP_NAME_STONE
	msgbox RustboroCity_DevonCorp_3F_Text_MrStoneIHaveFavor, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox LegendsVoice_StoneQuestion, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	setspeaker SP_NAME_STONE
	msgbox LegendsVoice_StoneEvidence, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	setspeaker SP_NAME_PLAYER
	msgbox LegendsVoice_StoneOffer, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	setspeaker SP_NAME_STONE
	msgbox LegendsVoice_StoneLetter, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	giveitem ITEM_LETTER
	setspeaker SP_NAME_PLAYER
	msgbox LegendsVoice_ContactQuestion, MSGBOX_DEFAULT
	setspeaker SP_NAME_STONE
	msgbox RustboroCity_DevonCorp_3F_Text_MrStoneWantYouToHaveThis, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	playfanfare MUS_OBTAIN_ITEM
	message RustboroCity_DevonCorp_3F_Text_ReceivedPokenav
	waitfanfare
	setflag FLAG_SYS_POKENAV_GET
	setflag FLAG_RECEIVED_POKENAV
	setflag FLAG_HIDE_RUSTBORO_CITY_POKEMON_SCHOOL_SCOTT
	setspeaker SP_NAME_STONE
	msgbox RustboroCity_DevonCorp_3F_Text_MrStoneExplainPokenavRestUp, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	closemessage
	call Common_EventScript_OutOfCenterPartyHeal
	playse SE_PC_LOGIN
	msgbox LegendsRustboro_Text_BirchConnected, MSGBOX_DEFAULT
	setspeaker SP_NAME_BIRCH
	msgbox LegendsRustboro_Text_BirchReport, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox LegendsVoice_BirchQuestion, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	setspeaker SP_NAME_BIRCH
	msgbox LegendsVoice_BirchAnswer, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	setspeaker SP_NAME_PLAYER
	msgbox LegendsVoice_BirchPromise, MSGBOX_DEFAULT
	setspeaker SP_NAME_STONE
	setspeaker SP_NAME_STONE
	msgbox RustboroCity_DevonCorp_3F_Text_MrStoneGoWithCautionAndCare, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox LegendsVoice_StoneDeparture, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	setflag FLAG_HIDE_ROUTE_116_WANDAS_BOYFRIEND
	clearflag FLAG_HIDE_RUSTURF_TUNNEL_WANDAS_BOYFRIEND
	clearflag FLAG_HIDE_RUSTURF_TUNNEL_WANDA
	clearflag FLAG_HIDE_BRINEYS_HOUSE_MR_BRINEY
	clearflag FLAG_HIDE_BRINEYS_HOUSE_PEEKO
	setvar VAR_BRINEY_LOCATION, 1
	clearflag FLAG_HIDE_RUSTBORO_CITY_RIVAL
	setvar VAR_DEVON_CORP_3F_STATE, 1
	setvar VAR_RUSTBORO_CITY_STATE, 6
	releaseall
	end

RustboroCity_DevonCorp_3F_Movement_Unused:
	walk_up
	walk_up
	walk_up
	walk_in_place_faster_left
	step_end

RustboroCity_DevonCorp_3F_Movement_LeadPlayerToPresident:
	walk_right
	walk_right
	walk_right
	walk_down
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_in_place_faster_left
	step_end

RustboroCity_DevonCorp_3F_Movement_EmployeeFaceDesk:
	delay_16
	walk_in_place_faster_down
	step_end

RustboroCity_DevonCorp_3F_Movement_EmployeeWalkOffscreen:
	walk_right
	walk_right
	walk_right
	walk_down
	walk_right
	walk_right
	walk_right
	walk_right
	step_end

RustboroCity_DevonCorp_3F_Movement_EmployeeReturnToPlayer:
	walk_left
	walk_left
	walk_left
	walk_left
	walk_up
	walk_left
	walk_left
	walk_left
	step_end

RustboroCity_DevonCorp_3F_Movement_PlayerFollowToPresident:
	walk_right
	walk_right
	walk_right
	walk_right
	walk_down
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	step_end

RustboroCity_DevonCorp_3F_Movement_PlayerApproachDesk:
	delay_16
	delay_16
	walk_down
	walk_down
	walk_in_place_faster_right
	step_end

RustboroCity_DevonCorp_3F_EventScript_MrStone::
    lock
    faceplayer
    setspeaker SP_NAME_STONE
    goto_if_set FLAG_LA_STONE_SHINY_CHARM, RustboroCity_DevonCorp_3F_EventScript_MrStoneAfterFavor
    goto_if_set FLAG_DELIVERED_STEVEN_LETTER, RustboroCity_DevonCorp_3F_EventScript_GiveShinyCharm
    msgbox RustboroCity_DevonCorp_3F_Text_CountingOnYou, MSGBOX_DEFAULT
    goto RustboroCity_DevonCorp_3F_EventScript_StoneEnd

RustboroCity_DevonCorp_3F_EventScript_GiveShinyCharm::
    msgbox RustboroCity_DevonCorp_3F_Text_ThankYouForDeliveringLetter, MSGBOX_DEFAULT
    checkitem ITEM_SHINY_CHARM
    goto_if_eq VAR_RESULT, TRUE, RustboroCity_DevonCorp_3F_EventScript_AlreadyHasCharm
    setspeaker SP_NAME_NONE
    giveitem ITEM_SHINY_CHARM
    goto_if_eq VAR_RESULT, FALSE, Common_EventScript_ShowBagIsFull
    setflag FLAG_LA_STONE_SHINY_CHARM
    setspeaker SP_NAME_PLAYER
    msgbox RustboroCity_DevonCorp_3F_Text_PlayerCharmQuestion, MSGBOX_DEFAULT
    setspeaker SP_NAME_STONE
    msgbox RustboroCity_DevonCorp_3F_Text_ExplainShinyCharm, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox RustboroCity_DevonCorp_3F_Text_PlayerCharmPromise, MSGBOX_DEFAULT
    setspeaker SP_NAME_STONE
    msgbox RustboroCity_DevonCorp_3F_Text_StoneCharmReply, MSGBOX_DEFAULT
    goto RustboroCity_DevonCorp_3F_EventScript_StoneEnd

RustboroCity_DevonCorp_3F_EventScript_AlreadyHasCharm:
    setflag FLAG_LA_STONE_SHINY_CHARM
    setspeaker SP_NAME_PLAYER
    msgbox RustboroCity_DevonCorp_3F_Text_PlayerHasCharm, MSGBOX_DEFAULT
    setspeaker SP_NAME_STONE
    msgbox RustboroCity_DevonCorp_3F_Text_ExplainShinyCharm, MSGBOX_DEFAULT
    goto RustboroCity_DevonCorp_3F_EventScript_StoneEnd

RustboroCity_DevonCorp_3F_EventScript_MrStoneAfterFavor::
    msgbox RustboroCity_DevonCorp_3F_Text_StoneAfterCharm, MSGBOX_DEFAULT
RustboroCity_DevonCorp_3F_EventScript_StoneEnd:
    closemessage
    applymovement VAR_LAST_TALKED, Common_Movement_FaceOriginalDirection
    waitmovement 0
    setspeaker SP_NAME_NONE
    release
    end

RustboroCity_DevonCorp_3F_EventScript_Employee::
	lock
	faceplayer
	goto_if_set FLAG_RECEIVED_REPEAT_BALL, RustboroCity_DevonCorp_3F_EventScript_EmployeeBalls
	msgbox RustboroCity_DevonCorp_3F_Text_VisitCaptSternShipyard, MSGBOX_DEFAULT
	release
	end

RustboroCity_DevonCorp_3F_EventScript_EmployeeBalls::
	msgbox RustboroCity_DevonCorp_3F_Text_RepeatAndTimerHugelyPopular, MSGBOX_DEFAULT
	release
	end

RustboroCity_DevonCorp_3F_EventScript_RareRocksDisplay::
	msgbox RustboroCity_DevonCorp_3F_Text_RareRocksDisplay, MSGBOX_SIGN
	end

RustboroCity_DevonCorp_3F_Text_MrStoneIHaveFavor:
	.string "I'm Mr. Stone, Devon's president.\nOur researchers told me what you did.\pYou protected them in the woods\nand recovered our shipment.\pThank you, {PLAYER}.\pThose stolen Silph recordings\ncaptured distortions near the rifts.$"

RustboroCity_DevonCorp_3F_Text_MrStoneWantYouToHaveThis:
	.string "You'll need a reliable way to keep\nin touch while you're traveling.\pPlease take this, with our thanks.$"

RustboroCity_DevonCorp_3F_Text_ReceivedPokenav:
	.string "{PLAYER} received a PokéNav.$"

RustboroCity_DevonCorp_3F_Text_MrStoneExplainPokenavRestUp:
	.string "That's a PokéNav. It includes a map\nof Hoenn and a contact system.\pYou'll be able to find Dewford\nand Slateport on its map.\pBefore we discuss your journey,\nlet's let your partners rest.$"

RustboroCity_DevonCorp_3F_Text_MrStoneGoWithCautionAndCare:
	.string "I'll contact research teams outside\nHoenn and compare their findings.\pFor now, take the letter to Steven,\nthen the Devon Parts to Captain Stern.\pYou don't have to solve this alone,\n{PLAYER}. Travel carefully.$"

RustboroCity_DevonCorp_3F_Text_CountingOnYou:
	.string "I'm counting on you. Travel safely!$"

RustboroCity_DevonCorp_3F_Text_ThankYouForDeliveringLetter:
    .string "Steven received my letter? Splendid!\nThank you, {PLAYER}.\pOur researchers found this while\nstudying a special stone.\pI'd like you to have it.$"
RustboroCity_DevonCorp_3F_Text_PlayerCharmQuestion:
    .string "A charm? Was it part of the stone?$"
RustboroCity_DevonCorp_3F_Text_ExplainShinyCharm:
    .string "It was lying beside it. We still\ndon't understand the connection.\pThe researchers carrying it kept\nspotting unusually colored Pok?mon.\pPerhaps you'll have better luck\nstudying it out in the field!$"
RustboroCity_DevonCorp_3F_Text_PlayerCharmPromise:
    .string "I'll keep it with me. If it leads\nto anything, I'll let you know.$"
RustboroCity_DevonCorp_3F_Text_StoneCharmReply:
    .string "That's the spirit! A discovery\nis only the beginning.$"
RustboroCity_DevonCorp_3F_Text_PlayerHasCharm:
    .string "I already have one like that.\nDo you know what it does?$"
RustboroCity_DevonCorp_3F_Text_StoneAfterCharm:
    .string "How is that charm treating you?\nKeep your eyes open, {PLAYER}.\pIf you notice anything unusual,\nDevon would love to hear about it.$"

RustboroCity_DevonCorp_3F_Text_ThisIs3rdFloorWaitHere:
	.string "This is our president's office.\nPlease wait here a moment.\pOur Silph colleague is checking the\nreadings we managed to keep.\pThe stolen parcel is meant for\nCaptain Stern in Slateport.\pWe still need it delivered safely.\nI'll ask the president what to do.$"

RustboroCity_DevonCorp_3F_Text_WordWithPresidentComeWithMe:
	.string "Our president would like to have\na word with you.\pPlease come with me.$"

RustboroCity_DevonCorp_3F_Text_PleaseGoAhead:
	.string "Please, go ahead.$"

RustboroCity_DevonCorp_3F_Text_VisitCaptSternShipyard:
	.string "If you visit the SHIPYARD in SLATEPORT,\n"
	.string "you should go see CAPT. STERN.$"

RustboroCity_DevonCorp_3F_Text_RepeatAndTimerHugelyPopular:
	.string "DEVON's new products, the REPEAT BALL\n"
	.string "and TIMER BALL, have become hugely\l"
	.string "popular among TRAINERS.$"

RustboroCity_DevonCorp_3F_Text_RareRocksDisplay:
	.string "It's a collection of rare rocks and\n"
	.string "stones assembled by the PRESIDENT.$"


LegendsRustboro_Text_BirchConnected:
    .string "One moment. Professor Birch is\njoining us over the office line.$"
LegendsRustboro_Text_BirchReport:
	.string "I'm glad you're safe, {PLAYER}.\nNorman passed on your report.\pTwo men, a missing object,\nand now stolen research…$"
