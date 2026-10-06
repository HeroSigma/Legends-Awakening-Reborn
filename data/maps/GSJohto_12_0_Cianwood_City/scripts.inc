GSJohto_12_0_Cianwood_City_MapScripts::
	.byte 0

GSJohto_12_0_Cianwood_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_12_0_Cianwood_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_12_0_Cianwood_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_12_0_Cianwood_City_Next::
	closemessage
	warp MAP_GSJOHTO_12_1_ROUTE_42, 14, 12
	waitstate
	release
	end
GSJohto_12_0_Cianwood_City_Text:
	.string "Johto 12.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
