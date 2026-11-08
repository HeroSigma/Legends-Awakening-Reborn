Johto_Azalea_Town_MapScripts::
	.byte 0

GSJohto_3_3_Azalea_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_3_Azalea_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_3_Azalea_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_3_Azalea_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_6_ECRUTEAK_CITY, 44, 24
	waitstate
	release
	end
GSJohto_3_3_Azalea_Town_Inspect_Text:
	.string "Mercury Johto 3.69. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
