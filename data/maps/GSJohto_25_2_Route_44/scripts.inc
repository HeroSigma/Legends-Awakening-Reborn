GSJohto_25_2_Route_44_MapScripts::
	.byte 0

GSJohto_25_2_Route_44_Inspect::
	lock
	faceplayer
	msgbox GSJohto_25_2_Route_44_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_25_2_Route_44_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_25_2_Route_44_Next::
	closemessage
	warp MAP_GSJOHTO_26_1_NEW_BARK_TOWN, 4, 3
	waitstate
	release
	end
GSJohto_25_2_Route_44_Text:
	.string "Johto 25.2: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
