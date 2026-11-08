Johto_Azalea_Town_Interior_03_MapScripts::
	.byte 0

GSJohto_7_3_Azalea_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_7_3_Azalea_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_7_3_Azalea_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_7_3_Azalea_Town_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_47_1_AZALEA_TOWN, 5, 5
	waitstate
	release
	end
GSJohto_7_3_Azalea_Town_Inspect_Text:
	.string "Mercury Johto 47.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
