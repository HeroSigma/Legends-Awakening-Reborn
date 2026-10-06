GSJohto_5_0_Cherrygrove_City_MapScripts::
	.byte 0

GSJohto_5_0_Cherrygrove_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_5_0_Cherrygrove_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_5_0_Cherrygrove_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_5_0_Cherrygrove_City_Next::
	closemessage
	warp MAP_GSJOHTO_5_1_MAHOGANY_TOWN, 8, 50
	waitstate
	release
	end
GSJohto_5_0_Cherrygrove_City_Text:
	.string "Johto 5.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
