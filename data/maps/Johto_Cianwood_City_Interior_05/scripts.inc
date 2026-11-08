Johto_Cianwood_City_Interior_05_MapScripts::
	.byte 0

GSJohto_12_3_Cianwood_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_12_3_Cianwood_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_12_3_Cianwood_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_12_3_Cianwood_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_12_0_CIANWOOD_CITY, 9, 16
	waitstate
	release
	end
GSJohto_12_3_Cianwood_City_Inspect_Text:
	.string "Mercury Johto 49.4. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
