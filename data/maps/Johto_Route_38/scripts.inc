Johto_Route_38_MapScripts::
	.byte 0

GSJohto_3_28_Route_38_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_28_Route_38_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_28_Route_38_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_28_Route_38_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_35_4_ROUTE_38, 3, 7
	waitstate
	release
	end
GSJohto_3_28_Route_38_Inspect_Text:
	.string "Mercury Johto 3.91. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
