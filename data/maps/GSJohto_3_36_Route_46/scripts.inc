GSJohto_3_36_Route_46_MapScripts::
	.byte 0

GSJohto_3_36_Route_46_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_36_Route_46_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_36_Route_46_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_36_Route_46_Next::
	closemessage
	warp MAP_GSJOHTO_3_37_ROUTE_47, 85, 34
	waitstate
	release
	end
GSJohto_3_36_Route_46_Text:
	.string "Johto 3.36: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
