GSJohto_3_37_Route_47_MapScripts::
	.byte 0

GSJohto_3_37_Route_47_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_37_Route_47_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_37_Route_47_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_37_Route_47_Next::
	closemessage
	warp MAP_GSJOHTO_3_38_ROUTE_48, 11, 13
	waitstate
	release
	end
GSJohto_3_37_Route_47_Text:
	.string "Johto 3.37: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
