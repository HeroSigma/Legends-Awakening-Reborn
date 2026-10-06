GSJohto_3_23_Route_33_MapScripts::
	.byte 0

GSJohto_3_23_Route_33_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_23_Route_33_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_23_Route_33_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_23_Route_33_Next::
	closemessage
	warp MAP_GSJOHTO_3_24_ROUTE_34, 13, 6
	waitstate
	release
	end
GSJohto_3_23_Route_33_Text:
	.string "Johto 3.23: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
