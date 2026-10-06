GSJohto_3_33_Route_43_MapScripts::
	.byte 0

GSJohto_3_33_Route_43_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_33_Route_43_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_33_Route_43_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_33_Route_43_Next::
	closemessage
	warp MAP_GSJOHTO_3_34_ROUTE_44, 86, 9
	waitstate
	release
	end
GSJohto_3_33_Route_43_Text:
	.string "Johto 3.33: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
