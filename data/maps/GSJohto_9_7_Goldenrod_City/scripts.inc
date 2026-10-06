GSJohto_9_7_Goldenrod_City_MapScripts::
	.byte 0

GSJohto_9_7_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_9_7_Goldenrod_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_9_7_Goldenrod_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_9_7_Goldenrod_City_Next::
	closemessage
	warp MAP_GSJOHTO_10_0_GOLDENROD_CITY, 10, 25
	waitstate
	release
	end
GSJohto_9_7_Goldenrod_City_Text:
	.string "Johto 9.7: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
