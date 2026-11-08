Johto_Mahogany_Town_Interior_03_MapScripts::
	.byte 0

GSJohto_8_2_Mahogany_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_8_2_Mahogany_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_8_2_Mahogany_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_8_2_Mahogany_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_5_1_MAHOGANY_TOWN, 6, 15
	waitstate
	release
	end
GSJohto_8_2_Mahogany_Town_Inspect_Text:
	.string "Mercury Johto 53.2. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
