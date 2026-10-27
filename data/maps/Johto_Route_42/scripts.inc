Johto_Route_42_MapScripts::
	.byte 0

GSJohto_3_32_Route_42_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_32_Route_42_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_32_Route_42_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_32_Route_42_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_34_ROUTE_44, 84, 13
	waitstate
	release
	end
GSJohto_3_32_Route_42_Inspect_Text:
	.string "Mercury Johto 3.97. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
