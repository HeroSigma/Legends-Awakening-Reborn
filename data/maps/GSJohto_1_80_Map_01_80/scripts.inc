GSJohto_1_80_Map_01_80_MapScripts::
	.byte 0

GSJohto_1_80_Map_01_80_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_80_Map_01_80_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_80_Map_01_80_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_80_Map_01_80_Next::
	closemessage
	warp MAP_GSJOHTO_1_81_UNION_CAVE, 4, 3
	waitstate
	release
	end
GSJohto_1_80_Map_01_80_Text:
	.string "Johto 1.80: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
