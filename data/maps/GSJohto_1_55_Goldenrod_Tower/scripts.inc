GSJohto_1_55_Goldenrod_Tower_MapScripts::
	.byte 0

GSJohto_1_55_Goldenrod_Tower_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_55_Goldenrod_Tower_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_55_Goldenrod_Tower_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_55_Goldenrod_Tower_Next::
	closemessage
	warp MAP_GSJOHTO_1_56_ROCKET_HQ, 8, 27
	waitstate
	release
	end
GSJohto_1_55_Goldenrod_Tower_Text:
	.string "Johto 1.55: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
