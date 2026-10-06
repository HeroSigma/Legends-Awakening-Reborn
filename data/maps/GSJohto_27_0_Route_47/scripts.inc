GSJohto_27_0_Route_47_MapScripts::
	.byte 0

GSJohto_27_0_Route_47_Inspect::
	lock
	faceplayer
	msgbox GSJohto_27_0_Route_47_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_27_0_Route_47_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_27_0_Route_47_Next::
	closemessage
	warp MAP_GSJOHTO_28_0_ROUTE_48, 20, 8
	waitstate
	release
	end
GSJohto_27_0_Route_47_Text:
	.string "Johto 27.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
