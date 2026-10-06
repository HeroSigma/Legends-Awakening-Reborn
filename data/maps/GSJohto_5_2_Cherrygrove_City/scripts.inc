GSJohto_5_2_Cherrygrove_City_MapScripts::
	.byte 0

GSJohto_5_2_Cherrygrove_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_5_2_Cherrygrove_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_5_2_Cherrygrove_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_5_2_Cherrygrove_City_Next::
	closemessage
	warp MAP_GSJOHTO_5_3_CHERRYGROVE_CITY, 9, 4
	waitstate
	release
	end
GSJohto_5_2_Cherrygrove_City_Text:
	.string "Johto 5.2: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
