GSJohto_11_4_Olivine_City_MapScripts::
	.byte 0

GSJohto_11_4_Olivine_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_11_4_Olivine_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_11_4_Olivine_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_11_4_Olivine_City_Next::
	closemessage
	warp MAP_GSJOHTO_11_5_OLIVINE_CITY, 12, 20
	waitstate
	release
	end
GSJohto_11_4_Olivine_City_Text:
	.string "Johto 11.4: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
