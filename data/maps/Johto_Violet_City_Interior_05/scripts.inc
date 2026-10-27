Johto_Violet_City_Interior_05_MapScripts::
	.byte 0

GSJohto_6_5_Violet_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_6_5_Violet_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_6_5_Violet_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_6_5_Violet_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_6_7_VIOLET_CITY, 2, 6
	waitstate
	release
	end
GSJohto_6_5_Violet_City_Inspect_Text:
	.string "Mercury Johto 46.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
