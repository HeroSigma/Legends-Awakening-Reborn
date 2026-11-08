Johto_Route_36_Section_01_MapScripts::
	.byte 0

GSJohto_3_26_Route_36_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_26_Route_36_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_26_Route_36_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_26_Route_36_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_92_UNION_CAVE, 10, 48
	waitstate
	release
	end
GSJohto_3_26_Route_36_Inspect_Text:
	.string "Mercury Johto 3.85. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
