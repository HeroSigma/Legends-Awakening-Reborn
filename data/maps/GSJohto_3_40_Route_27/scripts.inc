GSJohto_3_40_Route_27_MapScripts::
	.byte 0

GSJohto_3_40_Route_27_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_40_Route_27_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_40_Route_27_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_40_Route_27_Next::
	closemessage
	warp MAP_GSJOHTO_3_41_TOHJO_FALLS, 16, 10
	waitstate
	release
	end
GSJohto_3_40_Route_27_Text:
	.string "Johto 3.40: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
