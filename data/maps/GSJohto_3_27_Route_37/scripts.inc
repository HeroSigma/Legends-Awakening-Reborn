GSJohto_3_27_Route_37_MapScripts::
	.byte 0

GSJohto_3_27_Route_37_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_27_Route_37_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_27_Route_37_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_27_Route_37_Next::
	closemessage
	warp MAP_GSJOHTO_3_28_ROUTE_38, 26, 15
	waitstate
	release
	end
GSJohto_3_27_Route_37_Text:
	.string "Johto 3.27: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
