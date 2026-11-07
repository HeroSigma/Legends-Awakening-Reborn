GraniteCave_StevensRoom_MapScripts::
	.byte 0

GraniteCave_StevensRoom_EventScript_Steven::
	lock
	faceplayer
	setspeaker SP_NAME_STEVEN
	msgbox GraniteCave_StevensRoom_Text_ImStevenLetterForMe, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox GraniteCave_StevensRoom_Text_PlayerLetter, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	setvar VAR_0x8004, ITEM_LETTER
	call Common_EventScript_PlayerHandedOverTheItem
	setflag FLAG_DELIVERED_STEVEN_LETTER
	checkitem ITEM_DYNAMAX_BAND
	call_if_eq VAR_RESULT, TRUE, GraniteCave_StevensRoom_EventScript_InspectBand
	setspeaker SP_NAME_STEVEN
	msgbox GraniteCave_StevensRoom_Text_ThankYouTakeThis, MSGBOX_DEFAULT
	setspeaker SP_NAME_NONE
	giveitem ITEM_TM_STEEL_WING
	call_if_eq VAR_RESULT, FALSE, GraniteCave_StevensRoom_EventScript_BagFull
	setspeaker SP_NAME_STEVEN
	msgbox GraniteCave_StevensRoom_Text_CouldBecomeChampionLetsRegister, MSGBOX_DEFAULT
	closemessage
	setspeaker SP_NAME_NONE
	delay 30
	playfanfare MUS_REGISTER_MATCH_CALL
	msgbox GraniteCave_StevensRoom_Text_RegisteredSteven, MSGBOX_DEFAULT
	waitfanfare
	closemessage
	delay 30
	setflag FLAG_REGISTERED_STEVEN_POKENAV
	setspeaker SP_NAME_STEVEN
	msgbox GraniteCave_StevensRoom_Text_IveGotToHurryAlong, MSGBOX_DEFAULT
	closemessage
	setspeaker SP_NAME_NONE
	call_if_eq VAR_FACING, DIR_NORTH, GraniteCave_StevensRoom_EventScript_StevenExitNorth
	call_if_eq VAR_FACING, DIR_SOUTH, GraniteCave_StevensRoom_EventScript_StevenExitSouth
	call_if_eq VAR_FACING, DIR_WEST, GraniteCave_StevensRoom_EventScript_StevenExitWestEast
	call_if_eq VAR_FACING, DIR_EAST, GraniteCave_StevensRoom_EventScript_StevenExitWestEast
	playse SE_EXIT
	removeobject LOCALID_GRANITE_CAVE_STEVEN
	release
	end

GraniteCave_StevensRoom_EventScript_InspectBand:
	setspeaker SP_NAME_PLAYER
	msgbox GraniteCave_StevensRoom_Text_ShowBand, MSGBOX_DEFAULT
	setspeaker SP_NAME_STEVEN
	msgbox GraniteCave_StevensRoom_Text_RecognizeBand, MSGBOX_DEFAULT
	setspeaker SP_NAME_PLAYER
	msgbox GraniteCave_StevensRoom_Text_RingClosed, MSGBOX_DEFAULT
	setspeaker SP_NAME_STEVEN
	msgbox GraniteCave_StevensRoom_Text_RiftTraces, MSGBOX_DEFAULT
	return

GraniteCave_StevensRoom_EventScript_StevenExitNorth::
	applymovement LOCALID_GRANITE_CAVE_STEVEN, GraniteCave_StevensRoom_Movement_StevenExit
	waitmovement 0
	return

GraniteCave_StevensRoom_EventScript_StevenExitWestEast::
	applymovement LOCALID_PLAYER, GraniteCave_StevensRoom_Movement_PlayerTurnTowardExit
	applymovement LOCALID_GRANITE_CAVE_STEVEN, GraniteCave_StevensRoom_Movement_StevenExit
	waitmovement 0
	return

GraniteCave_StevensRoom_EventScript_StevenExitSouth::
	applymovement LOCALID_PLAYER, GraniteCave_StevensRoom_Movement_PlayerTurnTowardExit
	applymovement LOCALID_GRANITE_CAVE_STEVEN, GraniteCave_StevensRoom_Movement_StevenExitSouth
	waitmovement 0
	return

GraniteCave_StevensRoom_EventScript_BagFull::
	msgbox GraniteCave_StevensRoom_Text_OhBagIsFull, MSGBOX_DEFAULT
	return

GraniteCave_StevensRoom_Movement_StevenExit:
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	delay_8
	step_end

GraniteCave_StevensRoom_Movement_PlayerTurnTowardExit:
	delay_16
	delay_16
	delay_16
	walk_in_place_faster_up
	step_end

GraniteCave_StevensRoom_Movement_StevenExitSouth:
	walk_left
	walk_up
	walk_up
	walk_up
	walk_right
	walk_up
	walk_up
	delay_8
	step_end

GraniteCave_StevensRoom_Text_ImStevenLetterForMe:
	.string "My name is STEVEN.\p"
	.string "I'm interested in rare stones,\n"
	.string "so I travel here and there.\p"
	.string "Oh?\n"
	.string "A LETTER for me?$"

GraniteCave_StevensRoom_Text_PlayerLetter:
	.string "Mr. Stone asked me to give this to\nyou. I came over with Mr. Briney.$"

GraniteCave_StevensRoom_Text_ShowBand:
	.string "Before you go, could you look at\nthis band?\pA Pokémon came out of a ring on\nthe beach and left it behind.$"

GraniteCave_StevensRoom_Text_RecognizeBand:
	.string "That's a Dynamax Band. They make\nthese in Galar.\pWhen that ring closed, did it leave\nanything behind besides the band?$"

GraniteCave_StevensRoom_Text_RingClosed:
	.string "No. It just folded shut. The sand\nwhere it opened looked untouched.$"

GraniteCave_StevensRoom_Text_RiftTraces:
	.string "The rifts I've studied leave marks\non the rock around them.\pA ring that closes that cleanly?\nI'd like to see it for myself.\pKeep the band. If you see that\nPokémon again, let me know.$"

GraniteCave_StevensRoom_Text_ThankYouTakeThis:
	.string "Thank you for bringing the letter.\p"
	.string "You went through all this trouble to\n"
	.string "deliver that. I need to thank you.\p"
	.string "Let me see…\n"
	.string "I'll give you this TM.\p"
	.string "It contains my favorite move,\n"
	.string "STEEL WING.$"

GraniteCave_StevensRoom_Text_CouldBecomeChampionLetsRegister:
	.string "Your POKéMON appear quite\n"
	.string "capable.\p"
	.string "If you keep training, you could even\n"
	.string "become the CHAMPION of the POKéMON\l"
	.string "LEAGUE one day. That's what I think.\p"
	.string "I know, since we've gotten to know each\n"
	.string "other, let's register one another in\l"
	.string "our POKéNAVS.\p"
	.string "… … … … … …$"

GraniteCave_StevensRoom_Text_RegisteredSteven:
	.string "Registered STEVEN\n"
	.string "in the POKéNAV.$"

GraniteCave_StevensRoom_Text_IveGotToHurryAlong:
	.string "I should get going. If you're taking\nDevon's parts to Slateport,\lMr. Briney can sail you there.$"

GraniteCave_StevensRoom_Text_OhBagIsFull:
	.string "Oh, your BAG is full…\n"
	.string "That's too bad, then.$"


@ Project-owned reservation; no donor gameplay, flags or warp destination.
GraniteCave_StevensRoom_EventScript_HyperConstruction_1::
	lock
	faceplayer
	msgbox GraniteCave_StevensRoom_Text_HyperConstruction_1, MSGBOX_DEFAULT
	release
	end

GraniteCave_StevensRoom_Text_HyperConstruction_1:
	.string "Allearth Lake is\n"
	.string "under construction.\p"
	.string "Please check back later!$"
