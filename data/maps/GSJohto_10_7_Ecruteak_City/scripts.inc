GSJohto_10_7_Ecruteak_City_MapScripts::
	.byte 0

GSJohto_10_7_Ecruteak_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_7_Ecruteak_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_7_Ecruteak_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_7_Ecruteak_City_Next::
	closemessage
	warp MAP_GSJOHTO_10_8_ECRUTEAK_CITY, 3, 3
	waitstate
	release
	end
GSJohto_10_7_Ecruteak_City_Text:
	.string "Johto 10.7: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
