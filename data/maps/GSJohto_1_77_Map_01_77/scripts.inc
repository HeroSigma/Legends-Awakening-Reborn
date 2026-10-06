GSJohto_1_77_Map_01_77_MapScripts::
	.byte 0

GSJohto_1_77_Map_01_77_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_77_Map_01_77_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_77_Map_01_77_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_77_Map_01_77_Next::
	closemessage
	warp MAP_GSJOHTO_1_78_MAP_01_78, 6, 30
	waitstate
	release
	end
GSJohto_1_77_Map_01_77_Text:
	.string "Johto 1.77: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
