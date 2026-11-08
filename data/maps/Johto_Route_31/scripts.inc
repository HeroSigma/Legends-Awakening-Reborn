Johto_Route_31_MapScripts::
	.byte 0

GSJohto_3_21_Route_31_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_21_Route_31_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_21_Route_31_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_21_Route_31_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_22_ROUTE_32, 28, 116
	waitstate
	release
	end
GSJohto_3_21_Route_31_Inspect_Text:
	.string "Mercury Johto 3.83. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
