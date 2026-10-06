GSJohto_24_1_Route_43_MapScripts::
	.byte 0

GSJohto_24_1_Route_43_Inspect::
	lock
	faceplayer
	msgbox GSJohto_24_1_Route_43_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_24_1_Route_43_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_24_1_Route_43_Next::
	closemessage
	warp MAP_GSJOHTO_25_2_ROUTE_44, 6, 5
	waitstate
	release
	end
GSJohto_24_1_Route_43_Text:
	.string "Johto 24.1: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
