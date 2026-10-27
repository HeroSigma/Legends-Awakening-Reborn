Johto_Cherrygrove_City_Interior_04_MapScripts::
	.byte 0

GSJohto_5_4_Cherrygrove_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_5_4_Cherrygrove_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_5_4_Cherrygrove_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_5_4_Cherrygrove_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_15_0_CHERRYGROVE_CITY, 3, 9
	waitstate
	release
	end
GSJohto_5_4_Cherrygrove_City_Inspect_Text:
	.string "Mercury Johto 45.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
