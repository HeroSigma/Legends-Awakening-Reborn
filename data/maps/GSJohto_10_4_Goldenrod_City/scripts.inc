GSJohto_10_4_Goldenrod_City_MapScripts::
	.byte 0

GSJohto_10_4_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_4_Goldenrod_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_4_Goldenrod_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_4_Goldenrod_City_Next::
	closemessage
	warp MAP_GSJOHTO_10_5_GOLDENROD_CITY, 16, 28
	waitstate
	release
	end
GSJohto_10_4_Goldenrod_City_Text:
	.string "Johto 10.4: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
