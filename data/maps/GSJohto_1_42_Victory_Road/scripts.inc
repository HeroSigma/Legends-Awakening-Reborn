GSJohto_1_42_Victory_Road_MapScripts::
	.byte 0

GSJohto_1_42_Victory_Road_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_42_Victory_Road_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_42_Victory_Road_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_42_Victory_Road_Next::
	closemessage
	warp MAP_GSJOHTO_1_45_MAP_01_45, 6, 15
	waitstate
	release
	end
GSJohto_1_42_Victory_Road_Text:
	.string "Johto 1.42: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
