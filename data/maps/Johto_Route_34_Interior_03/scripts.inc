Johto_Route_34_Interior_03_MapScripts::
	.byte 0

GSJohto_35_0_Route_34_Inspect::
	lock
	faceplayer
	msgbox GSJohto_35_0_Route_34_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_35_0_Route_34_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_35_0_Route_34_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_9_0_GOLDENROD_CITY, 4, 5
	waitstate
	release
	end
GSJohto_35_0_Route_34_Inspect_Text:
	.string "Mercury Johto 50.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
