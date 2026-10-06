GSJohto_35_0_Route_34_MapScripts::
	.byte 0

GSJohto_35_0_Route_34_Inspect::
	lock
	faceplayer
	msgbox GSJohto_35_0_Route_34_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_35_0_Route_34_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_35_0_Route_34_Next::
	closemessage
	warp MAP_GSJOHTO_35_3_LAKE_OF_RAGE, 4, 3
	waitstate
	release
	end
GSJohto_35_0_Route_34_Text:
	.string "Johto 35.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
