Johto_Cianwood_City_Interior_01_MapScripts::
	.byte 0

GSJohto_7_8_Cianwood_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_7_8_Cianwood_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_7_8_Cianwood_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_7_8_Cianwood_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_14_9_BLACKTHORN_CITY, 4, 7
	waitstate
	release
	end
GSJohto_7_8_Cianwood_City_Inspect_Text:
	.string "Mercury Johto 31.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
