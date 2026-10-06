GSJohto_1_11_New_Bark_Town_MapScripts::
	.byte 0

GSJohto_1_11_New_Bark_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_11_New_Bark_Town_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_11_New_Bark_Town_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_11_New_Bark_Town_Next::
	closemessage
	warp MAP_GSJOHTO_1_12_NATIONAL_PARK, 18, 35
	waitstate
	release
	end
GSJohto_1_11_New_Bark_Town_Text:
	.string "Johto 1.11: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
