Johto_New_Bark_Town_Interior_07_MapScripts::
	.byte 0

GSJohto_23_2_New_Bark_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_23_2_New_Bark_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_23_2_New_Bark_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_23_2_New_Bark_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_4_1_NEW_BARK_TOWN, 5, 5
	waitstate
	release
	end
GSJohto_23_2_New_Bark_Town_Inspect_Text:
	.string "Mercury Johto 43.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
