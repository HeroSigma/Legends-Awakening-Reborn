GSJohto_1_3_Cianwood_City_MapScripts::
	.byte 0

GSJohto_1_3_Cianwood_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_3_Cianwood_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_3_Cianwood_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_3_Cianwood_City_Next::
	closemessage
	warp MAP_GSJOHTO_1_4_S_S_ANNE, 32, 7
	waitstate
	release
	end
GSJohto_1_3_Cianwood_City_Text:
	.string "Johto 1.3: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
