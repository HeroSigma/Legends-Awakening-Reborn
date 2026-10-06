GSJohto_1_51_Goldenrod_Tower_MapScripts::
	.byte 0

GSJohto_1_51_Goldenrod_Tower_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_51_Goldenrod_Tower_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_51_Goldenrod_Tower_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_51_Goldenrod_Tower_Next::
	closemessage
	warp MAP_GSJOHTO_1_52_GOLDENROD_CITY, 26, 14
	waitstate
	release
	end
GSJohto_1_51_Goldenrod_Tower_Text:
	.string "Johto 1.51: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
