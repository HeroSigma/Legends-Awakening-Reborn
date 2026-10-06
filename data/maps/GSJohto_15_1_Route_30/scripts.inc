GSJohto_15_1_Route_30_MapScripts::
	.byte 0

GSJohto_15_1_Route_30_Inspect::
	lock
	faceplayer
	msgbox GSJohto_15_1_Route_30_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_15_1_Route_30_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_15_1_Route_30_Next::
	closemessage
	warp MAP_GSJOHTO_15_2_NEW_BARK_TOWN, 3, 6
	waitstate
	release
	end
GSJohto_15_1_Route_30_Text:
	.string "Johto 15.1: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
