GSJohto_1_53_Goldenrod_City_MapScripts::
	.byte 0

GSJohto_1_53_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_53_Goldenrod_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_53_Goldenrod_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_53_Goldenrod_City_Next::
	closemessage
	warp MAP_GSJOHTO_1_54_GOLDENROD_CITY, 17, 6
	waitstate
	release
	end
GSJohto_1_53_Goldenrod_City_Text:
	.string "Johto 1.53: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
