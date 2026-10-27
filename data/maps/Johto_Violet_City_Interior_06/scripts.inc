Johto_Violet_City_Interior_06_MapScripts::
	.byte 0

GSJohto_6_7_Violet_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_6_7_Violet_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_6_7_Violet_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_6_7_Violet_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_7_2_VIOLET_CITY, 4, 6
	waitstate
	release
	end
GSJohto_6_7_Violet_City_Inspect_Text:
	.string "Mercury Johto 46.1. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
