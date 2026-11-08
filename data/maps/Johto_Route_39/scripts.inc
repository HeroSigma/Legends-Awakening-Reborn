Johto_Route_39_MapScripts::
	.byte 0

GSJohto_3_29_Route_39_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_29_Route_39_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_29_Route_39_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_29_Route_39_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_31_UNION_CAVE, 27, 34
	waitstate
	release
	end
GSJohto_3_29_Route_39_Inspect_Text:
	.string "Mercury Johto 3.93. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
