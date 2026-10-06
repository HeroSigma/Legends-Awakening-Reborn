GSJohto_3_41_Tohjo_Falls_MapScripts::
	.byte 0

GSJohto_3_41_Tohjo_Falls_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_41_Tohjo_Falls_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_41_Tohjo_Falls_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_41_Tohjo_Falls_Next::
	closemessage
	warp MAP_GSJOHTO_3_42_ROUTE_28, 5, 31
	waitstate
	release
	end
GSJohto_3_41_Tohjo_Falls_Text:
	.string "Johto 3.41: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
