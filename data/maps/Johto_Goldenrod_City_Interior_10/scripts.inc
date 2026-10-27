Johto_Goldenrod_City_Interior_10_MapScripts::
	.byte 0

GSJohto_10_3_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_3_Goldenrod_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_3_Goldenrod_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_3_Goldenrod_City_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_50_22_GOLDENROD_CITY, 7, 9
	waitstate
	release
	end
GSJohto_10_3_Goldenrod_City_Inspect_Text:
	.string "Mercury Johto 50.21. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
