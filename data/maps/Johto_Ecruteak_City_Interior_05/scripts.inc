Johto_Ecruteak_City_Interior_05_MapScripts::
	.byte 0

GSJohto_10_9_Ecruteak_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_9_Ecruteak_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_9_Ecruteak_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_9_Ecruteak_City_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_35_1_GOLDENROD_CITY, 10, 16
	waitstate
	release
	end
GSJohto_10_9_Ecruteak_City_Inspect_Text:
	.string "Mercury Johto 35.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
