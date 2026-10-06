GSJohto_9_6_Goldenrod_City_MapScripts::
	.byte 0

GSJohto_9_6_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_9_6_Goldenrod_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_9_6_Goldenrod_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_9_6_Goldenrod_City_Next::
	closemessage
	warp MAP_GSJOHTO_9_7_GOLDENROD_CITY, 4, 3
	waitstate
	release
	end
GSJohto_9_6_Goldenrod_City_Text:
	.string "Johto 9.6: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
