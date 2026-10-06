GSJohto_6_1_Violet_City_MapScripts::
	.byte 0

GSJohto_6_1_Violet_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_6_1_Violet_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_6_1_Violet_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_6_1_Violet_City_Next::
	closemessage
	warp MAP_GSJOHTO_6_2_VIOLET_CITY, 6, 7
	waitstate
	release
	end
GSJohto_6_1_Violet_City_Text:
	.string "Johto 6.1: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
