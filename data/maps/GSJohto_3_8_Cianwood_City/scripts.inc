GSJohto_3_8_Cianwood_City_MapScripts::
	.byte 0

GSJohto_3_8_Cianwood_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_8_Cianwood_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_8_Cianwood_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_8_Cianwood_City_Next::
	closemessage
	warp MAP_GSJOHTO_3_9_MAP_03_09, 19, 9
	waitstate
	release
	end
GSJohto_3_8_Cianwood_City_Text:
	.string "Johto 3.8: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
