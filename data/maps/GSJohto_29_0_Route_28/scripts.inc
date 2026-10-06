GSJohto_29_0_Route_28_MapScripts::
	.byte 0

GSJohto_29_0_Route_28_Inspect::
	lock
	faceplayer
	msgbox GSJohto_29_0_Route_28_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_29_0_Route_28_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_29_0_Route_28_Next::
	closemessage
	warp MAP_GSJOHTO_30_0_MT_SILVER, 7, 5
	waitstate
	release
	end
GSJohto_29_0_Route_28_Text:
	.string "Johto 29.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
