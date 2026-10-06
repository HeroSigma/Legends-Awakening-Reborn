GSJohto_1_76_Map_01_76_MapScripts::
	.byte 0

GSJohto_1_76_Map_01_76_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_76_Map_01_76_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_76_Map_01_76_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_76_Map_01_76_Next::
	closemessage
	warp MAP_GSJOHTO_1_77_MAP_01_77, 6, 30
	waitstate
	release
	end
GSJohto_1_76_Map_01_76_Text:
	.string "Johto 1.76: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
