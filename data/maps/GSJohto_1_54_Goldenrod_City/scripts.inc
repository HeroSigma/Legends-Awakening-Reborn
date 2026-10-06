GSJohto_1_54_Goldenrod_City_MapScripts::
	.byte 0

GSJohto_1_54_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_54_Goldenrod_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_54_Goldenrod_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_54_Goldenrod_City_Next::
	closemessage
	warp MAP_GSJOHTO_1_55_GOLDENROD_TOWER, 9, 12
	waitstate
	release
	end
GSJohto_1_54_Goldenrod_City_Text:
	.string "Johto 1.54: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
