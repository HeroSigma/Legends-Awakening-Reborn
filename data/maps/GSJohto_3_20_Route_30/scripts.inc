GSJohto_3_20_Route_30_MapScripts::
	.byte 0

GSJohto_3_20_Route_30_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_20_Route_30_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_20_Route_30_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_20_Route_30_Next::
	closemessage
	warp MAP_GSJOHTO_3_21_ROUTE_31, 41, 7
	waitstate
	release
	end
GSJohto_3_20_Route_30_Text:
	.string "Johto 3.20: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
