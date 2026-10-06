GSJohto_12_4_Cianwood_City_MapScripts::
	.byte 0

GSJohto_12_4_Cianwood_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_12_4_Cianwood_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_12_4_Cianwood_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_12_4_Cianwood_City_Next::
	closemessage
	warp MAP_GSJOHTO_12_5_CIANWOOD_CITY, 12, 20
	waitstate
	release
	end
GSJohto_12_4_Cianwood_City_Text:
	.string "Johto 12.4: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
