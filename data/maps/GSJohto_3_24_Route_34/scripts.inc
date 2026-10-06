GSJohto_3_24_Route_34_MapScripts::
	.byte 0

GSJohto_3_24_Route_34_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_24_Route_34_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_24_Route_34_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_24_Route_34_Next::
	closemessage
	warp MAP_GSJOHTO_3_25_ROUTE_35, 12, 8
	waitstate
	release
	end
GSJohto_3_24_Route_34_Text:
	.string "Johto 3.24: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
