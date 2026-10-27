Johto_Route_32_MapScripts::
	.byte 0

GSJohto_3_22_Route_32_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_22_Route_32_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_22_Route_32_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_22_Route_32_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_26_ROUTE_36, 5, 14
	waitstate
	release
	end
GSJohto_3_22_Route_32_Inspect_Text:
	.string "Mercury Johto 3.84. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
