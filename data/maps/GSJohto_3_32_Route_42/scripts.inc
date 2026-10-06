GSJohto_3_32_Route_42_MapScripts::
	.byte 0

GSJohto_3_32_Route_42_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_32_Route_42_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_32_Route_42_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_32_Route_42_Next::
	closemessage
	warp MAP_GSJOHTO_3_33_ROUTE_43, 24, 48
	waitstate
	release
	end
GSJohto_3_32_Route_42_Text:
	.string "Johto 3.32: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
