GSJohto_11_9_Olivine_City_MapScripts::
	.byte 0

GSJohto_11_9_Olivine_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_11_9_Olivine_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_11_9_Olivine_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_11_9_Olivine_City_Next::
	closemessage
	warp MAP_GSJOHTO_12_0_CIANWOOD_CITY, 11, 12
	waitstate
	release
	end
GSJohto_11_9_Olivine_City_Text:
	.string "Johto 11.9: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
