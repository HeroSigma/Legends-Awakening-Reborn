Johto_Route_34_Interior_02_MapScripts::
	.byte 0

GSJohto_17_0_Route_34_Inspect::
	lock
	faceplayer
	msgbox GSJohto_17_0_Route_34_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_17_0_Route_34_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_17_0_Route_34_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_16_0_ROUTE_34, 6, 6
	waitstate
	release
	end
GSJohto_17_0_Route_34_Inspect_Text:
	.string "Mercury Johto 44.6. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
