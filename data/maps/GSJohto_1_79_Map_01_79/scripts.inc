GSJohto_1_79_Map_01_79_MapScripts::
	.byte 0

GSJohto_1_79_Map_01_79_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_79_Map_01_79_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_79_Map_01_79_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_79_Map_01_79_Next::
	closemessage
	warp MAP_GSJOHTO_1_80_MAP_01_80, 5, 8
	waitstate
	release
	end
GSJohto_1_79_Map_01_79_Text:
	.string "Johto 1.79: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
