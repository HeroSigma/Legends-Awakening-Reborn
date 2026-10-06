GSJohto_23_1_Route_40_MapScripts::
	.byte 0

GSJohto_23_1_Route_40_Inspect::
	lock
	faceplayer
	msgbox GSJohto_23_1_Route_40_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_23_1_Route_40_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_23_1_Route_40_Next::
	closemessage
	warp MAP_GSJOHTO_23_2_NEW_BARK_TOWN, 6, 6
	waitstate
	release
	end
GSJohto_23_1_Route_40_Text:
	.string "Johto 23.1: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
