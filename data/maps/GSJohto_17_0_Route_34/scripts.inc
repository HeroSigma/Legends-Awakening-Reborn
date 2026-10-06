GSJohto_17_0_Route_34_MapScripts::
	.byte 0

GSJohto_17_0_Route_34_Inspect::
	lock
	faceplayer
	msgbox GSJohto_17_0_Route_34_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_17_0_Route_34_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_17_0_Route_34_Next::
	closemessage
	warp MAP_GSJOHTO_18_0_ROUTE_32, 12, 20
	waitstate
	release
	end
GSJohto_17_0_Route_34_Text:
	.string "Johto 17.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
