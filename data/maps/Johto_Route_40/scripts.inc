Johto_Route_40_MapScripts::
	.byte 0

GSJohto_3_30_Route_40_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_30_Route_40_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_30_Route_40_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_30_Route_40_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_31_ROUTE_41, 14, 43
	waitstate
	release
	end
GSJohto_3_30_Route_40_Inspect_Text:
	.string "Mercury Johto 3.95. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
