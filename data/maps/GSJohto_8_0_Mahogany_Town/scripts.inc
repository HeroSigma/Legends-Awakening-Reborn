GSJohto_8_0_Mahogany_Town_MapScripts::
	.byte 0

GSJohto_8_0_Mahogany_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_8_0_Mahogany_Town_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_8_0_Mahogany_Town_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_8_0_Mahogany_Town_Next::
	closemessage
	warp MAP_GSJOHTO_8_2_MAHOGANY_TOWN, 5, 3
	waitstate
	release
	end
GSJohto_8_0_Mahogany_Town_Text:
	.string "Johto 8.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
