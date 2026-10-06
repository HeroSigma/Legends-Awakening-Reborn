GSJohto_1_78_Map_01_78_MapScripts::
	.byte 0

GSJohto_1_78_Map_01_78_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_78_Map_01_78_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_78_Map_01_78_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_78_Map_01_78_Next::
	closemessage
	warp MAP_GSJOHTO_1_79_MAP_01_79, 9, 4
	waitstate
	release
	end
GSJohto_1_78_Map_01_78_Text:
	.string "Johto 1.78: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
