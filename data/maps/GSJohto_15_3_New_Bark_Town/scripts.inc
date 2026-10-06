GSJohto_15_3_New_Bark_Town_MapScripts::
	.byte 0

GSJohto_15_3_New_Bark_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_15_3_New_Bark_Town_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_15_3_New_Bark_Town_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_15_3_New_Bark_Town_Next::
	closemessage
	warp MAP_GSJOHTO_17_0_ROUTE_34, 4, 5
	waitstate
	release
	end
GSJohto_15_3_New_Bark_Town_Text:
	.string "Johto 15.3: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
