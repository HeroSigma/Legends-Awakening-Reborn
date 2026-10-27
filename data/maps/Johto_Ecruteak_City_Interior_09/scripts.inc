Johto_Ecruteak_City_Interior_09_MapScripts::
	.byte 0

GSJohto_10_13_Ecruteak_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_13_Ecruteak_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_13_Ecruteak_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_13_Ecruteak_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_10_11_ECRUTEAK_CITY, 3, 3
	waitstate
	release
	end
GSJohto_10_13_Ecruteak_City_Inspect_Text:
	.string "Mercury Johto 48.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
