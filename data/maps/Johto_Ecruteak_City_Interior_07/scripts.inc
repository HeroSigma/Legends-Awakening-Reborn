Johto_Ecruteak_City_Interior_07_MapScripts::
	.byte 0

GSJohto_10_11_Ecruteak_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_11_Ecruteak_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_11_Ecruteak_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_11_Ecruteak_City_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_48_2_BELLCHIME_TRAIL, 17, 23
	waitstate
	release
	end
GSJohto_10_11_Ecruteak_City_Inspect_Text:
	.string "Mercury Johto 48.1. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
