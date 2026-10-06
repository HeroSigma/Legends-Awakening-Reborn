GSJohto_3_26_Route_36_MapScripts::
	.byte 0

GSJohto_3_26_Route_36_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_26_Route_36_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_26_Route_36_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_26_Route_36_Next::
	closemessage
	warp MAP_GSJOHTO_3_27_ROUTE_37, 13, 15
	waitstate
	release
	end
GSJohto_3_26_Route_36_Text:
	.string "Johto 3.26: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
