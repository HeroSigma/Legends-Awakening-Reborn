Johto_Goldenrod_City_Interior_06_MapScripts::
	.byte 0

GSJohto_9_3_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_9_3_Goldenrod_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_9_3_Goldenrod_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_9_3_Goldenrod_City_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_50_14_GOLDENROD_CITY, 18, 5
	waitstate
	release
	end
GSJohto_9_3_Goldenrod_City_Inspect_Text:
	.string "Mercury Johto 50.13. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
