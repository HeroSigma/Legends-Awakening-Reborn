SlateportCity_OceanicMuseum_2F_MapScripts::
	map_script MAP_SCRIPT_ON_LOAD, SlateportMuseum_HideBarry
	.byte 0

SlateportMuseum_HideBarry:
	setflag FLAG_TEMP_1
	end

SlateportCity_OceanicMuseum_2F_EventScript_CaptStern::
	lock
	faceplayer
	setspeaker SP_NAME_PLAYER
	msgbox SlateportMuseum_Text_Delivery, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	msgbox SlateportCity_OceanicMuseum_2F_Text_ThankYouForTheParts, MSGBOX_DEFAULT
	closemessage
	playbgm MUS_ENCOUNTER_AQUA, TRUE
	addobject LOCALID_OCEANIC_MUSEUM_2F_GRUNT_1
	applymovement LOCALID_OCEANIC_MUSEUM_2F_GRUNT_1, SlateportCity_OceanicMuseum_2F_Movement_FirstGruntEnter
	waitmovement 0
	addobject LOCALID_OCEANIC_MUSEUM_2F_GRUNT_2
	applymovement LOCALID_OCEANIC_MUSEUM_2F_GRUNT_2, SlateportCity_OceanicMuseum_2F_Movement_SecondGruntEnter
	waitmovement 0
	applymovement LOCALID_OCEANIC_MUSEUM_2F_GRUNT_1, SlateportCity_OceanicMuseum_2F_Movement_FirstGruntApproach
	applymovement LOCALID_OCEANIC_MUSEUM_2F_GRUNT_2, SlateportCity_OceanicMuseum_2F_Movement_SecondGruntApproach
	waitmovement 0
	call_if_eq VAR_FACING, DIR_SOUTH, SlateportCity_OceanicMuseum_2F_EventScript_PlayerFaceGrunts
	call_if_eq VAR_FACING, DIR_EAST, SlateportCity_OceanicMuseum_2F_EventScript_PlayerFaceGrunts
	setspeaker SP_NAME_AQUA_GRUNT
	msgbox SlateportCity_OceanicMuseum_2F_Text_WellTakeThoseParts, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	call_if_ne VAR_FACING, DIR_EAST, SlateportCity_OceanicMuseum_2F_EventScript_SternFaceGrunts
	msgbox SlateportCity_OceanicMuseum_2F_Text_SternWhoAreYou, MSGBOX_DEFAULT
	setspeaker SP_NAME_AQUA_GRUNT
	msgbox SlateportCity_OceanicMuseum_2F_Text_WereTeamAqua, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	closemessage
	call SlateportMuseum_BarryArrives
	applymovement LOCALID_OCEANIC_MUSEUM_2F_GRUNT_2, SlateportCity_OceanicMuseum_2F_Movement_GruntApproachToBattle
	waitmovement 0
	call_if_eq VAR_FACING, DIR_SOUTH, SlateportCity_OceanicMuseum_2F_EventScript_PlayerApproachGruntSouth
	call_if_eq VAR_FACING, DIR_WEST, SlateportCity_OceanicMuseum_2F_EventScript_PlayerApproachGruntWest
	trainerbattle_no_intro TRAINER_GRUNT_MUSEUM_1, SlateportCity_OceanicMuseum_2F_Text_Grunt1Defeat
	lockall
	setspeaker SP_NAME_AQUA_GRUNT
	msgbox SlateportCity_OceanicMuseum_2F_Text_BossGoingToBeFurious, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	closemessage
	applymovement LOCALID_OCEANIC_MUSEUM_2F_GRUNT_2, SlateportCity_OceanicMuseum_2F_Movement_GruntDefeated
	waitmovement 0
	playse SE_PIN
	applymovement LOCALID_OCEANIC_MUSEUM_2F_GRUNT_1, Common_Movement_ExclamationMark
	waitmovement 0
	setspeaker SP_NAME_BARRY
	msgbox SlateportMuseum_Text_BarryWins, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	closemessage
	applymovement LOCALID_OCEANIC_MUSEUM_2F_GRUNT_1, Common_Movement_WalkInPlaceFasterDown
	applymovement LOCALID_OCEANIC_MUSEUM_2F_GRUNT_2, Common_Movement_WalkInPlaceFasterUp
	waitmovement 0
	setspeaker SP_NAME_AQUA_GRUNT
	msgbox SlateportCity_OceanicMuseum_2F_Text_MeddlingKid, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	closemessage
	delay 35
	addobject LOCALID_OCEANIC_MUSEUM_2F_ARCHIE
	applymovement LOCALID_OCEANIC_MUSEUM_2F_ARCHIE, SlateportCity_OceanicMuseum_2F_Movement_ArchieEnter
	applymovement LOCALID_OCEANIC_MUSEUM_2F_GRUNT_2, SlateportCity_OceanicMuseum_2F_Movement_GruntMoveForArchie
	waitmovement 0
	applymovement LOCALID_OCEANIC_MUSEUM_2F_ARCHIE, SlateportMuseum_Movement_ArchieFaceBarry
	waitmovement 0
	turnobject LOCALID_OCEANIC_MUSEUM_2F_BARRY, DIR_SOUTH
	turnobject LOCALID_PLAYER, DIR_WEST
	setspeaker SP_NAME_ARCHIE
	msgbox SlateportCity_OceanicMuseum_2F_Text_CameToSeeWhatsTakingSoLong, MSGBOX_DEFAULT
	setspeaker SP_NAME_BARRY
	msgbox SlateportMuseum_Text_BarryChallengesArchie, MSGBOX_DEFAULT
	setspeaker SP_NAME_ARCHIE
	msgbox SlateportMuseum_Text_ArchieAnswersBarry, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_OCEANIC_MUSEUM_2F_ARCHIE, SlateportMuseum_Movement_ArchieFacePlayer
	waitmovement 0
	turnobject LOCALID_OCEANIC_MUSEUM_2F_BARRY, DIR_EAST
	setspeaker SP_NAME_PLAYER
	msgbox SlateportMuseum_Text_PlayerQuestionsArchie, MSGBOX_DEFAULT
	setspeaker SP_NAME_ARCHIE
	msgbox SlateportCity_OceanicMuseum_2F_Text_ArchieWarning, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	closemessage
	savebgm MUS_DUMMY
	fadedefaultbgm
	fadescreen FADE_TO_BLACK
	removeobject LOCALID_OCEANIC_MUSEUM_2F_ARCHIE
	removeobject LOCALID_OCEANIC_MUSEUM_2F_GRUNT_1
	removeobject LOCALID_OCEANIC_MUSEUM_2F_GRUNT_2
	fadescreen FADE_FROM_BLACK
	delay 30
	setflag FLAG_HIDE_SLATEPORT_CITY_OCEANIC_MUSEUM_AQUA_GRUNTS
	call SlateportMuseum_BarryConversation
	applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterRight
	waitmovement 0
	msgbox SlateportCity_OceanicMuseum_2F_Text_SternThankYouForSavingUs, MSGBOX_DEFAULT
	setvar VAR_0x8004, ITEM_DEVON_PARTS
	call Common_EventScript_PlayerHandedOverTheItem
	msgbox SlateportCity_OceanicMuseum_2F_Text_SternIveGotToGo, MSGBOX_DEFAULT
	closemessage
	fadescreen FADE_TO_BLACK
	playfanfare MUS_HEAL
	waitfanfare
	special HealPlayerParty
	callnative UpdateFollowingPokemon
	removeobject LOCALID_OCEANIC_MUSEUM_2F_CAPT_STERN
	setflag FLAG_HIDE_ROUTE_110_TEAM_AQUA
	call_if_eq VAR_REGISTER_BIRCH_STATE, 0, SlateportCity_OceanicMuseum_2F_EventScript_ReadyRegisterBirch
	setflag FLAG_DELIVERED_DEVON_GOODS
	clearflag FLAG_HIDE_ROUTE_116_DEVON_EMPLOYEE
	setflag FLAG_HIDE_RUSTBORO_CITY_DEVON_CORP_3F_EMPLOYEE
	setvar VAR_SLATEPORT_OUTSIDE_MUSEUM_STATE, 1
	fadescreen FADE_FROM_BLACK
	release
	end

SlateportMuseum_BarryArrives:
	playse SE_PIN
	clearflag FLAG_TEMP_1
	addobject LOCALID_OCEANIC_MUSEUM_2F_BARRY
	applymovement LOCALID_OCEANIC_MUSEUM_2F_BARRY, SlateportMuseum_Movement_BarryRunsIn
	waitmovement 0
	copyobjectxytoperm LOCALID_OCEANIC_MUSEUM_2F_BARRY
	turnobject LOCALID_OCEANIC_MUSEUM_2F_GRUNT_1, DIR_WEST
	setspeaker SP_NAME_BARRY
	msgbox SlateportMuseum_Text_BarryIntervenes, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox SlateportMuseum_Text_PlayerProtectStern, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	closemessage
	return

SlateportMuseum_BarryConversation:
	turnobject LOCALID_PLAYER, DIR_WEST
	turnobject LOCALID_OCEANIC_MUSEUM_2F_BARRY, DIR_EAST
	setspeaker SP_NAME_BARRY
	msgbox SlateportMuseum_Text_BarryPhone, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox SlateportMuseum_Text_PlayerHoenn, MSGBOX_DEFAULT
	setspeaker SP_NAME_BARRY
	msgbox SlateportMuseum_Text_BarrySinnoh, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox SlateportMuseum_Text_PlayerOfferHelp, MSGBOX_DEFAULT
	setspeaker SP_NAME_BARRY
	msgbox SlateportMuseum_Text_BarryRushesOff, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_OCEANIC_MUSEUM_2F_BARRY, SlateportMuseum_Movement_BarryRunsOut
	waitmovement 0
	removeobject LOCALID_OCEANIC_MUSEUM_2F_BARRY
	setflag FLAG_TEMP_1
	setspeaker SP_NAME_PLAYER
	msgbox SlateportMuseum_Text_PlayerAfterBarry, MSGBOX_DEFAULT
	closemessage
	setspeaker SP_NAME_NONE
	return

SlateportMuseum_Movement_BarryRunsIn:
	walk_fast_down
	walk_fast_down
	walk_fast_down
	walk_fast_down
	walk_fast_right
	walk_fast_right
	walk_fast_right
	face_right
	step_end

SlateportMuseum_Movement_BarryRunsOut:
	walk_fast_left
	walk_fast_left
	walk_fast_left
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_fast_up
	step_end

SlateportMuseum_Text_Delivery:
	.string "Captain Stern? Devon sent me.\nI've got the parts you ordered.$"

SlateportMuseum_Text_BarryIntervenes:
	.string "Hey! Leave them alone!\pI'll battle this one!\nYou take the other!$"

SlateportMuseum_Text_BarryWins:
	.string "And that's the match!\pWhat, you thought I'd go easy\non you just because I'm lost?$"

SlateportMuseum_Text_PlayerProtectStern:
	.string "I've got it. Captain Stern,\nstay behind me!$"

SlateportMuseum_Text_BarryPhone:
	.string "Phew! All I wanted was a phone!\pI saw a line outside and figured\nsomeone here could help.\pI got tired of waiting. How was I\nsupposed to know who they were?$"

SlateportMuseum_Text_PlayerHoenn:
	.string "You're in Slateport City.\nThis is Hoenn. Where are you from?$"

SlateportMuseum_Text_BarrySinnoh:
	.string "Hoenn?! I'm Barry, from Sinnoh!\pI was on my way home when this\nbright crack opened in the road.\pThen I was here. Dad's going to\nwonder where I've gone!$"

SlateportMuseum_Text_PlayerOfferHelp:
	.string "A rift brought you here. I know\nsomeone who might be able to help…$"

SlateportMuseum_Text_BarryRushesOff:
	.string "Wait! If this is a port, somebody\ndown at the docks must have a phone!\pThanks! I'll see you around!$"

SlateportMuseum_Text_PlayerAfterBarry:
	.string "He's already gone. I bet rushing in\nis how he got caught up in all this.$"

SlateportCity_OceanicMuseum_2F_EventScript_ReadyRegisterBirch::
	setvar VAR_REGISTER_BIRCH_STATE, 1
	return

SlateportCity_OceanicMuseum_2F_EventScript_PlayerFaceGrunts::
	applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterLeft
	waitmovement 0
	return

SlateportCity_OceanicMuseum_2F_EventScript_SternFaceGrunts::
	applymovement LOCALID_OCEANIC_MUSEUM_2F_CAPT_STERN, Common_Movement_WalkInPlaceFasterLeft
	waitmovement 0
	return

SlateportCity_OceanicMuseum_2F_EventScript_PlayerApproachGruntSouth::
	applymovement LOCALID_PLAYER, SlateportCity_OceanicMuseum_2F_Movement_PlayerApproachGruntSouth
	waitmovement 0
	return

SlateportCity_OceanicMuseum_2F_EventScript_PlayerApproachGruntWest::
	applymovement LOCALID_PLAYER, SlateportCity_OceanicMuseum_2F_Movement_PlayerApproachGruntWest
	waitmovement 0
	return

SlateportCity_OceanicMuseum_2F_Movement_PlayerApproachGruntSouth:
	walk_left
	walk_down
	walk_in_place_faster_left
	step_end

SlateportCity_OceanicMuseum_2F_Movement_PlayerApproachGruntWest:
	walk_up
	walk_left
	walk_left
	walk_down
	walk_in_place_faster_left
	step_end

SlateportCity_OceanicMuseum_2F_Movement_Unused:
	walk_up
	walk_left
	walk_left
	walk_left
	walk_left
	walk_left
	walk_up
	walk_up
	walk_left
	walk_left
	walk_up
	walk_up
	delay_8
	step_end

SlateportMuseum_Movement_ArchieFaceBarry:
	walk_left
	face_up
	step_end

SlateportMuseum_Movement_ArchieFacePlayer:
	walk_right
	walk_right
	face_right
	step_end

SlateportCity_OceanicMuseum_2F_Movement_ArchieEnter:
	walk_down
	walk_down
	walk_down
	walk_down
	walk_down
	walk_right
	walk_right
	walk_right
	walk_right
	step_end

SlateportCity_OceanicMuseum_2F_Movement_GruntApproachToBattle:
	walk_right
	step_end

SlateportCity_OceanicMuseum_2F_Movement_FirstGruntEnter:
	walk_down
	walk_right
	walk_in_place_faster_down
	step_end

SlateportCity_OceanicMuseum_2F_Movement_FirstGruntApproach:
	walk_down
	walk_down
	walk_down
	walk_right
	walk_right
	walk_right
	step_end

SlateportCity_OceanicMuseum_2F_Movement_GruntDefeated:
	lock_facing_direction
	walk_left
	unlock_facing_direction
	step_end

SlateportCity_OceanicMuseum_2F_Movement_SecondGruntEnter:
	walk_down
	step_end

SlateportCity_OceanicMuseum_2F_Movement_SecondGruntApproach:
	walk_down
	walk_down
	walk_down
	walk_down
	walk_right
	walk_right
	walk_right
	walk_right
	step_end

SlateportCity_OceanicMuseum_2F_Movement_GruntMoveForArchie:
	delay_16
	delay_16
	delay_16
	delay_16
	delay_16
	delay_16
	delay_16
	delay_16
	delay_8
	walk_fast_down
	walk_in_place_faster_up
	step_end

SlateportCity_OceanicMuseum_2F_EventScript_WaterQualitySample1::
	msgbox SlateportCity_OceanicMuseum_2F_Text_WaterQualitySample1, MSGBOX_SIGN
	end

SlateportCity_OceanicMuseum_2F_EventScript_WaterQualitySample2::
	msgbox SlateportCity_OceanicMuseum_2F_Text_WaterQualitySample2, MSGBOX_SIGN
	end

SlateportCity_OceanicMuseum_2F_EventScript_PressureExperiment::
	msgbox SlateportCity_OceanicMuseum_2F_Text_PressureExperiment, MSGBOX_SIGN
	end

SlateportCity_OceanicMuseum_2F_EventScript_HoennModel::
	msgbox SlateportCity_OceanicMuseum_2F_Text_HoennModel, MSGBOX_SIGN
	end

SlateportCity_OceanicMuseum_2F_EventScript_DeepSeawaterDisplay::
	msgbox SlateportCity_OceanicMuseum_2F_Text_DeepSeawaterDisplay, MSGBOX_SIGN
	end

SlateportCity_OceanicMuseum_2F_EventScript_SurfaceSeawaterDisplay::
	msgbox SlateportCity_OceanicMuseum_2F_Text_SurfaceSeawaterDisplay, MSGBOX_SIGN
	end

SlateportCity_OceanicMuseum_2F_EventScript_SSTidalReplica::
	msgbox SlateportCity_OceanicMuseum_2F_Text_SSTidalReplica, MSGBOX_SIGN
	end

SlateportCity_OceanicMuseum_2F_EventScript_SubmarineReplica::
	msgbox SlateportCity_OceanicMuseum_2F_Text_SubmarineReplica, MSGBOX_SIGN
	end

SlateportCity_OceanicMuseum_2F_EventScript_SubmersibleReplica::
	msgbox SlateportCity_OceanicMuseum_2F_Text_SumbersibleReplica, MSGBOX_SIGN
	end

SlateportCity_OceanicMuseum_2F_EventScript_SSAnneReplica::
	msgbox SlateportCity_OceanicMuseum_2F_Text_SSAnneReplica, MSGBOX_SIGN
	end

SlateportCity_OceanicMuseum_2F_EventScript_MuseumPatron1::
	msgbox SlateportCity_OceanicMuseum_2F_Text_RemindsMeOfAbandonedShip, MSGBOX_NPC
	end

SlateportCity_OceanicMuseum_2F_EventScript_MuseumPatron2::
	msgbox SlateportCity_OceanicMuseum_2F_Text_DontRunInMuseum, MSGBOX_NPC
	end

SlateportCity_OceanicMuseum_2F_EventScript_MuseumPatron3::
	lock
	faceplayer
	msgbox SlateportCity_OceanicMuseum_2F_Text_WantToRideSubmarine, MSGBOX_DEFAULT
	closemessage
	applymovement VAR_LAST_TALKED, Common_Movement_FaceOriginalDirection
	waitmovement 0
	release
	end

SlateportCity_OceanicMuseum_2F_Text_ThankYouForTheParts:
	.string "Yes? If you're looking for STERN,\n"
	.string "that would be me.\p"
	.string "Ah! Those must be the parts I ordered\n"
	.string "from MR. STONE of DEVON.\p"
	.string "Thank you! That's great!\n"
	.string "We can prepare for our expedition now.$"

SlateportCity_OceanicMuseum_2F_Text_WellTakeThoseParts:
	.string "Hehehe, hold it!\n"
	.string "We'll take those parts!$"

SlateportCity_OceanicMuseum_2F_Text_SternWhoAreYou:
	.string "CAPT. STERN: Wh-what?\n"
	.string "Who are you people?$"

SlateportCity_OceanicMuseum_2F_Text_WereTeamAqua:
	.string "We're TEAM AQUA!\p"
	.string "Our BOSS wants those parts!\n"
	.string "Shut your yap and fork them over!$"

SlateportCity_OceanicMuseum_2F_Text_Grunt1Defeat:
	.string "Awaaaah!\n"
	.string "A kid beat me!$"

SlateportCity_OceanicMuseum_2F_Text_BossGoingToBeFurious:
	.string "Oh, man, what a disaster…\n"
	.string "The BOSS is going to be furious…$"

SlateportCity_OceanicMuseum_2F_Text_LetMeTakeCareOfThis:
	.string "Humph, sniveling wimp!\n"
	.string "Let me take care of this!$"

SlateportCity_OceanicMuseum_2F_Text_Grunt2Defeat:
	.string "What?!\n"
	.string "I lost, too!$"

SlateportCity_OceanicMuseum_2F_Text_MeddlingKid:
	.string "Now what? If we don't get the parts,\n"
	.string "we're in for it!\p"
	.string "Arrgh, I didn't count on being meddled\n"
	.string "with by some meddling kid!$"

SlateportCity_OceanicMuseum_2F_Text_CameToSeeWhatsTakingSoLong:
	.string "I sent two of my crew to collect\na crate. What's the holdup?\pYou there. Why are you standing\nbetween my crew and the stairs?$"

SlateportMuseum_Text_BarryChallengesArchie:
	.string "Your crew? They tried to rob him!\pIf you're their boss, tell them to\nleave Captain Stern alone!$"

SlateportMuseum_Text_ArchieAnswersBarry:
	.string "Name's Archie. I lead Team Aqua.\pYou've got nerve, kid. Now step\nback. I need a word with your friend.$"

SlateportMuseum_Text_PlayerQuestionsArchie:
	.string "The parts are for Captain Stern.\nWhat does Team Aqua want with them?$"

SlateportCity_OceanicMuseum_2F_Text_ArchieWarning:
	.string "My crew saw the sea split open\noff Slateport. Then it closed.\pStern's equipment could tell us\nwhat happened under the surface.\pThe sea keeps this world alive.\nI won't wait for Devon's permission\lto find out what's happening to it.\pCrew, back to the docks. We'll\nfind another way to get a reading.\pAnd you two. Stay out of my way\nif we meet again.$"

SlateportCity_OceanicMuseum_2F_Text_SternThankYouForSavingUs:
	.string "CAPT. STERN: Thank you, {PLAYER}.\pYou and that boy kept them away\nfrom the parts. May I see them?$"

SlateportCity_OceanicMuseum_2F_Text_SternIveGotToGo:
	.string "CAPT. STERN: These will seal the\npressure housing on our scanner.\pI hadn't heard about the sea\nsplitting open. I'll have the crew\lcheck our readings before we sail.\pI'll get word to Devon. You've\ndone plenty for us today.$"

SlateportCity_OceanicMuseum_2F_Text_RemindsMeOfAbandonedShip:
	.string "I saw a model of a ship here.\p"
	.string "It reminded me of the ABANDONED SHIP\n"
	.string "near DEWFORD TOWN…$"

SlateportCity_OceanicMuseum_2F_Text_DontRunInMuseum:
	.string "Don't you dare run around inside\n"
	.string "the MUSEUM!$"

SlateportCity_OceanicMuseum_2F_Text_WantToRideSubmarine:
	.string "Wow, the submarine's awesome!\n"
	.string "I want to go for a ride!$"

SlateportCity_OceanicMuseum_2F_Text_WaterQualitySample1:
	.string "“WATER QUALITY SAMPLE 1,” the\n"
	.string "label says.\p"
	.string "The sea is all connected, but the\n"
	.string "water seems to differ by region.$"

SlateportCity_OceanicMuseum_2F_Text_WaterQualitySample2:
	.string "“WATER QUALITY SAMPLE 2,” the\n"
	.string "label says.\p"
	.string "Does the saltiness of seawater differ\n"
	.string "by region, too?$"

SlateportCity_OceanicMuseum_2F_Text_PressureExperiment:
	.string "A rubber ball is expanding and\n"
	.string "shrinking.\p"
	.string "“In the sea, the weight of water itself\n"
	.string "exerts pressure.\p"
	.string "“In shallow water, the pressure is not\n"
	.string "very heavy.\p"
	.string "“However, in extremely deep water,\n"
	.string "the pressure can reach even tens of\l"
	.string "thousands of tons on a small area.”$"

SlateportCity_OceanicMuseum_2F_Text_HoennModel:
	.string "“MODEL OF HOENN REGION”\p"
	.string "It's a miniature diorama of the\n"
	.string "HOENN region.\p"
	.string "Where is LITTLEROOT TOWN on this?$"

SlateportCity_OceanicMuseum_2F_Text_DeepSeawaterDisplay:
	.string "It's a display on the flow of seawater.\p"
	.string "“Near the bottom of the sea, water\n"
	.string "flows due to differences in such\l"
	.string "factors as temperature and salinity.”$"

SlateportCity_OceanicMuseum_2F_Text_SurfaceSeawaterDisplay:
	.string "It's a display on the flow of seawater.\p"
	.string "“Toward the surface, seawater flows\n"
	.string "as currents driven by the winds.”$"

SlateportCity_OceanicMuseum_2F_Text_SSTidalReplica:
	.string "“THE FERRY S.S. TIDAL\p"
	.string "“A scale replica of the ship under\n"
	.string "construction at STERN'S SHIPYARD.”$"

SlateportCity_OceanicMuseum_2F_Text_SubmarineReplica:
	.string "“SUBMARINE EXPLORER 1\p"
	.string "“A replica of the high-performance\n"
	.string "ocean floor exploration submarine.”$"

SlateportCity_OceanicMuseum_2F_Text_SumbersibleReplica:
	.string "“SUBMERSIBLE POD\p"
	.string "“A replica of a compact, unmanned\n"
	.string "pod for seafloor exploration.”$"

SlateportCity_OceanicMuseum_2F_Text_SSAnneReplica:
	.string "“S.S. ANNE\p"
	.string "“A replica of the luxury liner that\n"
	.string "circles the globe.”$"
