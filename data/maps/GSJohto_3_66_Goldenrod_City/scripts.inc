GSJohto_3_66_Goldenrod_City_MapScripts::
	.byte 0

GSJohto_3_66_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_66_Goldenrod_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_66_Goldenrod_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_66_Goldenrod_City_Next::
	closemessage
	warp MAP_GSJOHTO_4_0_NEW_BARK_TOWN, 4, 4
	waitstate
	release
	end
GSJohto_3_66_Goldenrod_City_Text:
	.string "Johto 3.66: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
