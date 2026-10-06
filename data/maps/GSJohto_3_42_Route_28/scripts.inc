GSJohto_3_42_Route_28_MapScripts::
	.byte 0

GSJohto_3_42_Route_28_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_42_Route_28_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_42_Route_28_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_42_Route_28_Next::
	closemessage
	warp MAP_GSJOHTO_3_43_SINJOH_RUINS, 11, 20
	waitstate
	release
	end
GSJohto_3_42_Route_28_Text:
	.string "Johto 3.42: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
