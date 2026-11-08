Johto_Route_37_MapScripts::
	.byte 0

GSJohto_3_27_Route_37_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_27_Route_37_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_27_Route_37_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_27_Route_37_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_25_ROUTE_35, 12, 7
	waitstate
	release
	end
GSJohto_3_27_Route_37_Inspect_Text:
	.string "Mercury Johto 3.89. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
