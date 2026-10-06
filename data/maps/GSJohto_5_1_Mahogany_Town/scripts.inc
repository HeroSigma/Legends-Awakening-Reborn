GSJohto_5_1_Mahogany_Town_MapScripts::
	.byte 0

GSJohto_5_1_Mahogany_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_5_1_Mahogany_Town_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_5_1_Mahogany_Town_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_5_1_Mahogany_Town_Next::
	closemessage
	warp MAP_GSJOHTO_5_2_CHERRYGROVE_CITY, 4, 3
	waitstate
	release
	end
GSJohto_5_1_Mahogany_Town_Text:
	.string "Johto 5.1: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
