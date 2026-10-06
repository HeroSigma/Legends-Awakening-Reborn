GSJohto_3_35_Route_45_MapScripts::
	.byte 0

GSJohto_3_35_Route_45_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_35_Route_45_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_35_Route_45_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_35_Route_45_Next::
	closemessage
	warp MAP_GSJOHTO_3_36_ROUTE_46, 24, 7
	waitstate
	release
	end
GSJohto_3_35_Route_45_Text:
	.string "Johto 3.35: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
