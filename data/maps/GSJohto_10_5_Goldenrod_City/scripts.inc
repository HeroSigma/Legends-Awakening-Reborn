GSJohto_10_5_Goldenrod_City_MapScripts::
	.byte 0

GSJohto_10_5_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_5_Goldenrod_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_5_Goldenrod_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_5_Goldenrod_City_Next::
	closemessage
	warp MAP_GSJOHTO_10_6_ECRUTEAK_CITY, 2, 4
	waitstate
	release
	end
GSJohto_10_5_Goldenrod_City_Text:
	.string "Johto 10.5: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
