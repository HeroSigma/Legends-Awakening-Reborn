GSJohto_10_15_Ecruteak_City_MapScripts::
	.byte 0

GSJohto_10_15_Ecruteak_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_15_Ecruteak_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_15_Ecruteak_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_15_Ecruteak_City_Next::
	closemessage
	warp MAP_GSJOHTO_10_16_ECRUTEAK_CITY, 5, 7
	waitstate
	release
	end
GSJohto_10_15_Ecruteak_City_Text:
	.string "Johto 10.15: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
