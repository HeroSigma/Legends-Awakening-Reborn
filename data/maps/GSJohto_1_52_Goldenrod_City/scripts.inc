GSJohto_1_52_Goldenrod_City_MapScripts::
	.byte 0

GSJohto_1_52_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_52_Goldenrod_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_52_Goldenrod_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_52_Goldenrod_City_Next::
	closemessage
	warp MAP_GSJOHTO_1_53_GOLDENROD_CITY, 27, 5
	waitstate
	release
	end
GSJohto_1_52_Goldenrod_City_Text:
	.string "Johto 1.52: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
