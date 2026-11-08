Johto_Ecruteak_City_Interior_08_MapScripts::
	.byte 0

GSJohto_10_12_Ecruteak_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_12_Ecruteak_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_12_Ecruteak_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_12_Ecruteak_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_22_1_ROUTE_39, 8, 4
	waitstate
	release
	end
GSJohto_10_12_Ecruteak_City_Inspect_Text:
	.string "Mercury Johto 52.5. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
