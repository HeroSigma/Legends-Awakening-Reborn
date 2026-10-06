GSJohto_5_4_Cherrygrove_City_MapScripts::
	.byte 0

GSJohto_5_4_Cherrygrove_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_5_4_Cherrygrove_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_5_4_Cherrygrove_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_5_4_Cherrygrove_City_Next::
	closemessage
	warp MAP_GSJOHTO_6_0_VIOLET_CITY, 12, 4
	waitstate
	release
	end
GSJohto_5_4_Cherrygrove_City_Text:
	.string "Johto 5.4: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
