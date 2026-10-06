GSJohto_3_19_Route_29_MapScripts::
	.byte 0

GSJohto_3_19_Route_29_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_19_Route_29_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_19_Route_29_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_19_Route_29_Next::
	closemessage
	warp MAP_GSJOHTO_3_20_ROUTE_30, 28, 7
	waitstate
	release
	end
GSJohto_3_19_Route_29_Text:
	.string "Johto 3.19: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
