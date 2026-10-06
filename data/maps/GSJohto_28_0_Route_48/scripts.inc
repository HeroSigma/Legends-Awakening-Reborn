GSJohto_28_0_Route_48_MapScripts::
	.byte 0

GSJohto_28_0_Route_48_Inspect::
	lock
	faceplayer
	msgbox GSJohto_28_0_Route_48_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_28_0_Route_48_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_28_0_Route_48_Next::
	closemessage
	warp MAP_GSJOHTO_29_0_ROUTE_28, 5, 3
	waitstate
	release
	end
GSJohto_28_0_Route_48_Text:
	.string "Johto 28.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
