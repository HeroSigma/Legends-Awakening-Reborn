GSJohto_3_7_Olivine_City_MapScripts::
	.byte 0

GSJohto_3_7_Olivine_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_7_Olivine_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_7_Olivine_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_7_Olivine_City_Next::
	closemessage
	warp MAP_GSJOHTO_3_8_CIANWOOD_CITY, 20, 17
	waitstate
	release
	end
GSJohto_3_7_Olivine_City_Text:
	.string "Johto 3.7: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
