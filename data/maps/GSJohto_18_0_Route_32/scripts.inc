GSJohto_18_0_Route_32_MapScripts::
	.byte 0

GSJohto_18_0_Route_32_Inspect::
	lock
	faceplayer
	msgbox GSJohto_18_0_Route_32_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_18_0_Route_32_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_18_0_Route_32_Next::
	closemessage
	warp MAP_GSJOHTO_21_0_ROUTE_48, 12, 20
	waitstate
	release
	end
GSJohto_18_0_Route_32_Text:
	.string "Johto 18.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
