Johto_Route_40_Interior_01_MapScripts::
	.byte 0

GSJohto_23_1_Route_40_Inspect::
	lock
	faceplayer
	msgbox GSJohto_23_1_Route_40_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_23_1_Route_40_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_23_1_Route_40_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_56_24_CLIFF_EDGE_GATE, 7, 36
	waitstate
	release
	end
GSJohto_23_1_Route_40_Inspect_Text:
	.string "Mercury Johto 56.23. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
