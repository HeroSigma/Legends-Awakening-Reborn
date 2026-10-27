Johto_Mahogany_Town_MapScripts::
	.byte 0

GSJohto_3_4_Mahogany_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_4_Mahogany_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_4_Mahogany_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_4_Mahogany_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_5_GOLDENROD_CITY, 8, 26
	waitstate
	release
	end
GSJohto_3_4_Mahogany_Town_Inspect_Text:
	.string "Mercury Johto 3.74. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
