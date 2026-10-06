GSJohto_13_1_Map_13_01_MapScripts::
	.byte 0

GSJohto_13_1_Map_13_01_Inspect::
	lock
	faceplayer
	msgbox GSJohto_13_1_Map_13_01_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_13_1_Map_13_01_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_13_1_Map_13_01_Next::
	closemessage
	warp MAP_GSJOHTO_14_0_CIANWOOD_CITY, 4, 3
	waitstate
	release
	end
GSJohto_13_1_Map_13_01_Text:
	.string "Johto 13.1: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
