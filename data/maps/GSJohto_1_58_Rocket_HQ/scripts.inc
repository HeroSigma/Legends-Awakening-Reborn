GSJohto_1_58_Rocket_HQ_MapScripts::
	.byte 0

GSJohto_1_58_Rocket_HQ_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_58_Rocket_HQ_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_58_Rocket_HQ_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_58_Rocket_HQ_Next::
	closemessage
	warp MAP_GSJOHTO_1_59_BURNED_TOWER, 20, 11
	waitstate
	release
	end
GSJohto_1_58_Rocket_HQ_Text:
	.string "Johto 1.58: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
