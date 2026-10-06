GSJohto_11_0_Olivine_City_MapScripts::
	.byte 0

GSJohto_11_0_Olivine_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_11_0_Olivine_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_11_0_Olivine_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_11_0_Olivine_City_Next::
	closemessage
	warp MAP_GSJOHTO_11_1_OLIVINE_CITY, 9, 4
	waitstate
	release
	end
GSJohto_11_0_Olivine_City_Text:
	.string "Johto 11.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
