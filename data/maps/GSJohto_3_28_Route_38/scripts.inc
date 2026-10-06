GSJohto_3_28_Route_38_MapScripts::
	.byte 0

GSJohto_3_28_Route_38_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_28_Route_38_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_28_Route_38_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_28_Route_38_Next::
	closemessage
	warp MAP_GSJOHTO_3_29_ROUTE_39, 7, 6
	waitstate
	release
	end
GSJohto_3_28_Route_38_Text:
	.string "Johto 3.28: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
