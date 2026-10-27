Johto_New_Bark_Town_Section_01_MapScripts::
	.byte 0

GSJohto_3_0_New_Bark_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_0_New_Bark_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_0_New_Bark_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_0_New_Bark_Town_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_0_0_CELADON_DEPT, 6, 7
	waitstate
	release
	end
GSJohto_3_0_New_Bark_Town_Inspect_Text:
	.string "Mercury Johto 3.66. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
