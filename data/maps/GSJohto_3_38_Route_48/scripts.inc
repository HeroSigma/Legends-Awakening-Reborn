GSJohto_3_38_Route_48_MapScripts::
	.byte 0

GSJohto_3_38_Route_48_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_38_Route_48_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_38_Route_48_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_38_Route_48_Next::
	closemessage
	warp MAP_GSJOHTO_3_39_ROUTE_27, 15, 25
	waitstate
	release
	end
GSJohto_3_38_Route_48_Text:
	.string "Johto 3.38: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
