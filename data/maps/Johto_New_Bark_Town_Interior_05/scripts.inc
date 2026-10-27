Johto_New_Bark_Town_Interior_05_MapScripts::
	.byte 0

GSJohto_15_2_New_Bark_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_15_2_New_Bark_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_15_2_New_Bark_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_15_2_New_Bark_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_4_3_NEW_BARK_TOWN, 5, 6
	waitstate
	release
	end
GSJohto_15_2_New_Bark_Town_Inspect_Text:
	.string "Mercury Johto 43.5. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
