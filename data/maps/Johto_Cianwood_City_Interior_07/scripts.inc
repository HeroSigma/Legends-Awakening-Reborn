Johto_Cianwood_City_Interior_07_MapScripts::
	.byte 0

GSJohto_12_5_Cianwood_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_12_5_Cianwood_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_12_5_Cianwood_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_12_5_Cianwood_City_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_51_6_GOLDENROD_CITY, 9, 8
	waitstate
	release
	end
GSJohto_12_5_Cianwood_City_Inspect_Text:
	.string "Mercury Johto 51.2. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
