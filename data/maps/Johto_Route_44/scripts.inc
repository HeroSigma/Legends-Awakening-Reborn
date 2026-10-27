Johto_Route_44_MapScripts::
	.byte 0

GSJohto_3_34_Route_44_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_34_Route_44_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_34_Route_44_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_34_Route_44_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_33_ROUTE_43, 35, 45
	waitstate
	release
	end
GSJohto_3_34_Route_44_Inspect_Text:
	.string "Mercury Johto 3.98. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
