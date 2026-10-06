GSJohto_15_0_Cherrygrove_City_MapScripts::
	.byte 0

GSJohto_15_0_Cherrygrove_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_15_0_Cherrygrove_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_15_0_Cherrygrove_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_15_0_Cherrygrove_City_Next::
	closemessage
	warp MAP_GSJOHTO_15_1_ROUTE_30, 5, 3
	waitstate
	release
	end
GSJohto_15_0_Cherrygrove_City_Text:
	.string "Johto 15.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
