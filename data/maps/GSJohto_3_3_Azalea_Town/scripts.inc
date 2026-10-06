GSJohto_3_3_Azalea_Town_MapScripts::
	.byte 0

GSJohto_3_3_Azalea_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_3_Azalea_Town_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_3_Azalea_Town_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_3_Azalea_Town_Next::
	closemessage
	warp MAP_GSJOHTO_3_4_MAHOGANY_TOWN, 13, 6
	waitstate
	release
	end
GSJohto_3_3_Azalea_Town_Text:
	.string "Johto 3.3: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
