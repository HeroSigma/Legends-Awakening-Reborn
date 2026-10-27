Johto_Ecruteak_City_Interior_04_MapScripts::
	.byte 0

GSJohto_10_8_Ecruteak_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_8_Ecruteak_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_8_Ecruteak_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_8_Ecruteak_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_9_5_ECRUTEAK_CITY, 3, 9
	waitstate
	release
	end
GSJohto_10_8_Ecruteak_City_Inspect_Text:
	.string "Mercury Johto 48.6. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
