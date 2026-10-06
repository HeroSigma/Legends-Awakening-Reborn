GSJohto_4_1_New_Bark_Town_MapScripts::
	.byte 0

GSJohto_4_1_New_Bark_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_4_1_New_Bark_Town_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_4_1_New_Bark_Town_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_4_1_New_Bark_Town_Next::
	closemessage
	warp MAP_GSJOHTO_4_2_NEW_BARK_TOWN, 3, 3
	waitstate
	release
	end
GSJohto_4_1_New_Bark_Town_Text:
	.string "Johto 4.1: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
