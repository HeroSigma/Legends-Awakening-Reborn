GSJohto_3_21_Route_31_MapScripts::
	.byte 0

GSJohto_3_21_Route_31_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_21_Route_31_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_21_Route_31_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_21_Route_31_Next::
	closemessage
	warp MAP_GSJOHTO_3_22_ROUTE_32, 11, 106
	waitstate
	release
	end
GSJohto_3_21_Route_31_Text:
	.string "Johto 3.21: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
