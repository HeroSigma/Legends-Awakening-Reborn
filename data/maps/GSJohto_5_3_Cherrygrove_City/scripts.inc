GSJohto_5_3_Cherrygrove_City_MapScripts::
	.byte 0

GSJohto_5_3_Cherrygrove_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_5_3_Cherrygrove_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_5_3_Cherrygrove_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_5_3_Cherrygrove_City_Next::
	closemessage
	warp MAP_GSJOHTO_5_4_CHERRYGROVE_CITY, 12, 20
	waitstate
	release
	end
GSJohto_5_3_Cherrygrove_City_Text:
	.string "Johto 5.3: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
