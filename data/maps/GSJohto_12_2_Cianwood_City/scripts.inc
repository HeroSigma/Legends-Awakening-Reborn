GSJohto_12_2_Cianwood_City_MapScripts::
	.byte 0

GSJohto_12_2_Cianwood_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_12_2_Cianwood_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_12_2_Cianwood_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_12_2_Cianwood_City_Next::
	closemessage
	warp MAP_GSJOHTO_12_3_CIANWOOD_CITY, 6, 3
	waitstate
	release
	end
GSJohto_12_2_Cianwood_City_Text:
	.string "Johto 12.2: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
