Johto_Olivine_City_Interior_05_MapScripts::
	.byte 0

GSJohto_11_4_Olivine_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_11_4_Olivine_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_11_4_Olivine_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_11_4_Olivine_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_11_9_OLIVINE_CITY, 3, 6
	waitstate
	release
	end
GSJohto_11_4_Olivine_City_Inspect_Text:
	.string "Mercury Johto 49.7. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
