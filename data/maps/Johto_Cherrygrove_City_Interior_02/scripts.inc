Johto_Cherrygrove_City_Interior_02_MapScripts::
	.byte 0

GSJohto_5_2_Cherrygrove_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_5_2_Cherrygrove_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_5_2_Cherrygrove_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_5_2_Cherrygrove_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_5_3_CHERRYGROVE_CITY, 8, 6
	waitstate
	release
	end
GSJohto_5_2_Cherrygrove_City_Inspect_Text:
	.string "Mercury Johto 45.3. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
