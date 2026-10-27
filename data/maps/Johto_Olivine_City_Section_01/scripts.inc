Johto_Olivine_City_Section_01_MapScripts::
	.byte 0

GSJohto_3_7_Olivine_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_7_Olivine_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_7_Olivine_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_7_Olivine_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_8_CIANWOOD_CITY, 18, 13
	waitstate
	release
	end
GSJohto_3_7_Olivine_City_Inspect_Text:
	.string "Mercury Johto 3.72. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
