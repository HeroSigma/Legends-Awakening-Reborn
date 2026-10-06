GSJohto_9_2_Goldenrod_City_MapScripts::
	.byte 0

GSJohto_9_2_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_9_2_Goldenrod_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_9_2_Goldenrod_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_9_2_Goldenrod_City_Next::
	closemessage
	warp MAP_GSJOHTO_9_3_GOLDENROD_CITY, 7, 4
	waitstate
	release
	end
GSJohto_9_2_Goldenrod_City_Text:
	.string "Johto 9.2: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
