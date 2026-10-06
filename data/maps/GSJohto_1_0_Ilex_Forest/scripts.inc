GSJohto_1_0_Ilex_Forest_MapScripts::
	.byte 0

GSJohto_1_0_Ilex_Forest_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_0_Ilex_Forest_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_0_Ilex_Forest_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_0_Ilex_Forest_Next::
	closemessage
	warp MAP_GSJOHTO_1_3_CIANWOOD_CITY, 30, 18
	waitstate
	release
	end
GSJohto_1_0_Ilex_Forest_Text:
	.string "Johto 1.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
