Johto_Route_42_Section_01_MapScripts::
	.byte 0

GSJohto_12_1_Route_42_Inspect::
	lock
	faceplayer
	msgbox GSJohto_12_1_Route_42_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_12_1_Route_42_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_12_1_Route_42_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_0_NEW_BARK_TOWN, 22, 11
	waitstate
	release
	end
GSJohto_12_1_Route_42_Inspect_Text:
	.string "Area held. No Mercury counterpart.\p"
	.string "YES: next. NO: Littleroot.$"
