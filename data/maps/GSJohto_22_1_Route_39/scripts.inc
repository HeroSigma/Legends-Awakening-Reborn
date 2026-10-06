GSJohto_22_1_Route_39_MapScripts::
	.byte 0

GSJohto_22_1_Route_39_Inspect::
	lock
	faceplayer
	msgbox GSJohto_22_1_Route_39_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_22_1_Route_39_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_22_1_Route_39_Next::
	closemessage
	warp MAP_GSJOHTO_23_1_ROUTE_40, 6, 5
	waitstate
	release
	end
GSJohto_22_1_Route_39_Text:
	.string "Johto 22.1: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
