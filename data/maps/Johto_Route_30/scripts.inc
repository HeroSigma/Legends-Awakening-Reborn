Johto_Route_30_MapScripts::
	.byte 0

GSJohto_3_20_Route_30_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_20_Route_30_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_20_Route_30_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_20_Route_30_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_21_ROUTE_31, 36, 8
	waitstate
	release
	end
GSJohto_3_20_Route_30_Inspect_Text:
	.string "Mercury Johto 3.82. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
