GSJohto_21_0_Route_48_MapScripts::
	.byte 0

GSJohto_21_0_Route_48_Inspect::
	lock
	faceplayer
	msgbox GSJohto_21_0_Route_48_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_21_0_Route_48_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_21_0_Route_48_Next::
	closemessage
	warp MAP_GSJOHTO_22_1_ROUTE_39, 6, 5
	waitstate
	release
	end
GSJohto_21_0_Route_48_Text:
	.string "Johto 21.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
