Johto_New_Bark_Town_Interior_08_MapScripts::
	.byte 0

GSJohto_26_1_New_Bark_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_26_1_New_Bark_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_26_1_New_Bark_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_26_1_New_Bark_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_4_0_NEW_BARK_TOWN, 3, 4
	waitstate
	release
	end
GSJohto_26_1_New_Bark_Town_Inspect_Text:
	.string "Mercury Johto 43.2. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
