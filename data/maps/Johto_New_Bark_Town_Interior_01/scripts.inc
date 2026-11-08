Johto_New_Bark_Town_Interior_01_MapScripts::
	.byte 0

GSJohto_4_0_New_Bark_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_4_0_New_Bark_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_4_0_New_Bark_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_4_0_New_Bark_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_4_2_NEW_BARK_TOWN, 4, 3
	waitstate
	release
	end
GSJohto_4_0_New_Bark_Town_Inspect_Text:
	.string "Mercury Johto 43.3. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
