Johto_Olivine_City_Interior_02_MapScripts::
	.byte 0

GSJohto_11_1_Olivine_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_11_1_Olivine_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_11_1_Olivine_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_11_1_Olivine_City_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_37_3_CLIFFSIDE_TOWN, 3, 5
	waitstate
	release
	end
GSJohto_11_1_Olivine_City_Inspect_Text:
	.string "Mercury Johto 37.1. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
