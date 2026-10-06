GSJohto_12_7_Route_48_MapScripts::
	.byte 0

GSJohto_12_7_Route_48_Inspect::
	lock
	faceplayer
	msgbox GSJohto_12_7_Route_48_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_12_7_Route_48_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_12_7_Route_48_Next::
	closemessage
	warp MAP_GSJOHTO_13_0_MAP_13_00, 9, 4
	waitstate
	release
	end
GSJohto_12_7_Route_48_Text:
	.string "Johto 12.7: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
