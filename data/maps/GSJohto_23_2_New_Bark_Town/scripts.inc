GSJohto_23_2_New_Bark_Town_MapScripts::
	.byte 0

GSJohto_23_2_New_Bark_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_23_2_New_Bark_Town_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_23_2_New_Bark_Town_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_23_2_New_Bark_Town_Next::
	closemessage
	warp MAP_GSJOHTO_24_1_ROUTE_43, 6, 5
	waitstate
	release
	end
GSJohto_23_2_New_Bark_Town_Text:
	.string "Johto 23.2: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
