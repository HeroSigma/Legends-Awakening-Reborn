GSJohto_3_29_Route_39_MapScripts::
	.byte 0

GSJohto_3_29_Route_39_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_29_Route_39_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_29_Route_39_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_29_Route_39_Next::
	closemessage
	warp MAP_GSJOHTO_3_30_ROUTE_40, 37, 11
	waitstate
	release
	end
GSJohto_3_29_Route_39_Text:
	.string "Johto 3.29: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
