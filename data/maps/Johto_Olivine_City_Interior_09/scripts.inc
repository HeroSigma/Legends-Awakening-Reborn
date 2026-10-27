Johto_Olivine_City_Interior_09_MapScripts::
	.byte 0

GSJohto_11_8_Olivine_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_11_8_Olivine_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_11_8_Olivine_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_11_8_Olivine_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_96_OLIVINE_CITY, 6, 17
	waitstate
	release
	end
GSJohto_11_8_Olivine_City_Inspect_Text:
	.string "Mercury Johto 49.9. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
