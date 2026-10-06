GSJohto_3_22_Route_32_MapScripts::
	.byte 0

GSJohto_3_22_Route_32_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_22_Route_32_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_22_Route_32_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_22_Route_32_Next::
	closemessage
	warp MAP_GSJOHTO_3_23_ROUTE_33, 25, 4
	waitstate
	release
	end
GSJohto_3_22_Route_32_Text:
	.string "Johto 3.22: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
