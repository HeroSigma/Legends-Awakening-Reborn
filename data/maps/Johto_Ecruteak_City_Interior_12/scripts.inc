Johto_Ecruteak_City_Interior_12_MapScripts::
	.byte 0

GSJohto_10_17_Ecruteak_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_17_Ecruteak_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_17_Ecruteak_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_17_Ecruteak_City_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_52_12_BELLCHIME_TRAIL, 10, 19
	waitstate
	release
	end
GSJohto_10_17_Ecruteak_City_Inspect_Text:
	.string "Mercury Johto 52.11. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
