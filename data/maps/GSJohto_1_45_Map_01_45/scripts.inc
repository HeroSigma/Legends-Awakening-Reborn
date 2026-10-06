GSJohto_1_45_Map_01_45_MapScripts::
	.byte 0

GSJohto_1_45_Map_01_45_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_45_Map_01_45_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_45_Map_01_45_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_45_Map_01_45_Next::
	closemessage
	warp MAP_GSJOHTO_1_47_GOLDENROD_TOWER, 20, 3
	waitstate
	release
	end
GSJohto_1_45_Map_01_45_Text:
	.string "Johto 1.45: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
