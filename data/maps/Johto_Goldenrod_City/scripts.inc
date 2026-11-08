Johto_Goldenrod_City_MapScripts::
	.byte 0

GSJohto_1_52_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_52_Goldenrod_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_52_Goldenrod_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_52_Goldenrod_City_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_56_74_CLIFFSIDE_TOWN, 10, 16
	waitstate
	release
	end
GSJohto_1_52_Goldenrod_City_Inspect_Text:
	.string "Mercury Johto 56.69. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
