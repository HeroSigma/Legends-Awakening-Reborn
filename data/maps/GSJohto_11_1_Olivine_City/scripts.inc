GSJohto_11_1_Olivine_City_MapScripts::
	.byte 0

GSJohto_11_1_Olivine_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_11_1_Olivine_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_11_1_Olivine_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_11_1_Olivine_City_Next::
	closemessage
	warp MAP_GSJOHTO_11_2_OLIVINE_CITY, 6, 5
	waitstate
	release
	end
GSJohto_11_1_Olivine_City_Text:
	.string "Johto 11.1: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
