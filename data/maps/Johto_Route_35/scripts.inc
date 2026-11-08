Johto_Route_35_MapScripts::
	.byte 0

GSJohto_3_25_Route_35_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_25_Route_35_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_25_Route_35_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_25_Route_35_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_28_ROUTE_38, 57, 6
	waitstate
	release
	end
GSJohto_3_25_Route_35_Inspect_Text:
	.string "Mercury Johto 3.90. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
