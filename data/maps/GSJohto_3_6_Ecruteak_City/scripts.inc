GSJohto_3_6_Ecruteak_City_MapScripts::
	.byte 0

GSJohto_3_6_Ecruteak_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_6_Ecruteak_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_6_Ecruteak_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_6_Ecruteak_City_Next::
	closemessage
	warp MAP_GSJOHTO_3_7_OLIVINE_CITY, 15, 18
	waitstate
	release
	end
GSJohto_3_6_Ecruteak_City_Text:
	.string "Johto 3.6: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
