GSJohto_13_0_Map_13_00_MapScripts::
	.byte 0

GSJohto_13_0_Map_13_00_Inspect::
	lock
	faceplayer
	msgbox GSJohto_13_0_Map_13_00_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_13_0_Map_13_00_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_13_0_Map_13_00_Next::
	closemessage
	warp MAP_GSJOHTO_13_1_MAP_13_01, 6, 4
	waitstate
	release
	end
GSJohto_13_0_Map_13_00_Text:
	.string "Johto 13.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
