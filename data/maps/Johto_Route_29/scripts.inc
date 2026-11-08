Johto_Route_29_MapScripts::
	.byte 0

GSJohto_1_98_Route_29_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_98_Route_29_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_98_Route_29_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_98_Route_29_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_36_ROUTE_46, 21, 11
	waitstate
	release
	end
GSJohto_1_98_Route_29_Inspect_Text:
	.string "Mercury Johto 3.79. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
