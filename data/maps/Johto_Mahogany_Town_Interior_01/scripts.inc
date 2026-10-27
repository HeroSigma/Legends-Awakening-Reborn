Johto_Mahogany_Town_Interior_01_MapScripts::
	.byte 0

GSJohto_5_1_Mahogany_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_5_1_Mahogany_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_5_1_Mahogany_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_5_1_Mahogany_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_33_ICE_PATH, 53, 19
	waitstate
	release
	end
GSJohto_5_1_Mahogany_Town_Inspect_Text:
	.string "Mercury Johto 53.3. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
