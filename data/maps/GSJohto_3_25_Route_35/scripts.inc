GSJohto_3_25_Route_35_MapScripts::
	.byte 0

GSJohto_3_25_Route_35_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_25_Route_35_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_25_Route_35_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_25_Route_35_Next::
	closemessage
	warp MAP_GSJOHTO_3_26_ROUTE_36, 6, 12
	waitstate
	release
	end
GSJohto_3_25_Route_35_Text:
	.string "Johto 3.25: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
