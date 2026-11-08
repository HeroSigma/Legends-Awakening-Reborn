Johto_Cherrygrove_City_MapScripts::
	.byte 0

GSJohto_3_1_Cherrygrove_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_1_Cherrygrove_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_1_Cherrygrove_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_1_Cherrygrove_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_2_VIOLET_CITY, 51, 59
	waitstate
	release
	end
GSJohto_3_1_Cherrygrove_City_Inspect_Text:
	.string "Mercury Johto 3.67. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
