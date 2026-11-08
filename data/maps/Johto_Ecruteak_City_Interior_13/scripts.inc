Johto_Ecruteak_City_Interior_13_MapScripts::
	.byte 0

GSJohto_10_18_Ecruteak_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_18_Ecruteak_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_18_Ecruteak_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_18_Ecruteak_City_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_34_4_CLIFFSIDE_TOWN, 3, 5
	waitstate
	release
	end
GSJohto_10_18_Ecruteak_City_Inspect_Text:
	.string "Mercury Johto 34.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
