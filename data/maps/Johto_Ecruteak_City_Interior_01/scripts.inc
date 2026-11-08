Johto_Ecruteak_City_Interior_01_MapScripts::
	.byte 0

GSJohto_9_5_Ecruteak_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_9_5_Ecruteak_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_9_5_Ecruteak_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_9_5_Ecruteak_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_9_4_CIANWOOD_CITY, 4, 6
	waitstate
	release
	end
GSJohto_9_5_Ecruteak_City_Inspect_Text:
	.string "Mercury Johto 48.7. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
