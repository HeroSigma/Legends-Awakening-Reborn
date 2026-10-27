Johto_Route_39_Interior_01_MapScripts::
	.byte 0

GSJohto_22_1_Route_39_Inspect::
	lock
	faceplayer
	msgbox GSJohto_22_1_Route_39_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_22_1_Route_39_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_22_1_Route_39_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_52_7_ROUTE_39, 6, 7
	waitstate
	release
	end
GSJohto_22_1_Route_39_Inspect_Text:
	.string "Mercury Johto 52.6. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
