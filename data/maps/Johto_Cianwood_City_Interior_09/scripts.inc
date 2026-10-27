Johto_Cianwood_City_Interior_09_MapScripts::
	.byte 0

GSJohto_14_0_Cianwood_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_14_0_Cianwood_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_14_0_Cianwood_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_14_0_Cianwood_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_12_2_CIANWOOD_CITY, 4, 6
	waitstate
	release
	end
GSJohto_14_0_Cianwood_City_Inspect_Text:
	.string "Mercury Johto 49.1. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
