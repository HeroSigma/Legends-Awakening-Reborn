GSJohto_3_0_New_Bark_Town_MapScripts::
	.byte 0

GSJohto_3_0_New_Bark_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_0_New_Bark_Town_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_0_New_Bark_Town_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_0_New_Bark_Town_Next::
	closemessage
	warp MAP_GSJOHTO_3_1_CHERRYGROVE_CITY, 37, 6
	waitstate
	release
	end
GSJohto_3_0_New_Bark_Town_Text:
	.string "Johto 3.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
