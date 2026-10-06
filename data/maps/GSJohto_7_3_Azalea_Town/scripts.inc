GSJohto_7_3_Azalea_Town_MapScripts::
	.byte 0

GSJohto_7_3_Azalea_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_7_3_Azalea_Town_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_7_3_Azalea_Town_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_7_3_Azalea_Town_Next::
	closemessage
	warp MAP_GSJOHTO_7_5_AZALEA_TOWN, 11, 19
	waitstate
	release
	end
GSJohto_7_3_Azalea_Town_Text:
	.string "Johto 7.3: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
