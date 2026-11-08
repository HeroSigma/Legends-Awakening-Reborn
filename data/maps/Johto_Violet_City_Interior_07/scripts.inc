Johto_Violet_City_Interior_07_MapScripts::
	.byte 0

GSJohto_7_2_Violet_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_7_2_Violet_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_7_2_Violet_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_7_2_Violet_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_6_1_VIOLET_CITY, 3, 9
	waitstate
	release
	end
GSJohto_7_2_Violet_City_Inspect_Text:
	.string "Mercury Johto 46.2. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
