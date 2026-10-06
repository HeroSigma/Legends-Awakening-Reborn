GSJohto_10_19_Ecruteak_City_MapScripts::
	.byte 0

GSJohto_10_19_Ecruteak_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_19_Ecruteak_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_19_Ecruteak_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_19_Ecruteak_City_Next::
	closemessage
	warp MAP_GSJOHTO_11_0_OLIVINE_CITY, 4, 4
	waitstate
	release
	end
GSJohto_10_19_Ecruteak_City_Text:
	.string "Johto 10.19: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
