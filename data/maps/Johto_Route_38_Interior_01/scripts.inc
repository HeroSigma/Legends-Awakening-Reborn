Johto_Route_38_Interior_01_MapScripts::
	.byte 0

GSJohto_35_4_Route_38_Inspect::
	lock
	faceplayer
	msgbox GSJohto_35_4_Route_38_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_35_4_Route_38_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_35_4_Route_38_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_29_ROUTE_39, 26, 9
	waitstate
	release
	end
GSJohto_35_4_Route_38_Inspect_Text:
	.string "Mercury Johto 3.92. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
