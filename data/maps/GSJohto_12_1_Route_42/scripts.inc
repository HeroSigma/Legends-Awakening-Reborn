GSJohto_12_1_Route_42_MapScripts::
	.byte 0

GSJohto_12_1_Route_42_Inspect::
	lock
	faceplayer
	msgbox GSJohto_12_1_Route_42_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_12_1_Route_42_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_12_1_Route_42_Next::
	closemessage
	warp MAP_GSJOHTO_12_2_CIANWOOD_CITY, 5, 3
	waitstate
	release
	end
GSJohto_12_1_Route_42_Text:
	.string "Johto 12.1: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
