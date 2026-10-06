GSJohto_3_39_Route_27_MapScripts::
	.byte 0

GSJohto_3_39_Route_27_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_39_Route_27_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_39_Route_27_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_39_Route_27_Next::
	closemessage
	warp MAP_GSJOHTO_3_40_ROUTE_27, 10, 24
	waitstate
	release
	end
GSJohto_3_39_Route_27_Text:
	.string "Johto 3.39: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
