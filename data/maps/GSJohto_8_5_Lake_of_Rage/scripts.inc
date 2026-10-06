GSJohto_8_5_Lake_of_Rage_MapScripts::
	.byte 0

GSJohto_8_5_Lake_of_Rage_Inspect::
	lock
	faceplayer
	msgbox GSJohto_8_5_Lake_of_Rage_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_8_5_Lake_of_Rage_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_8_5_Lake_of_Rage_Next::
	closemessage
	warp MAP_GSJOHTO_9_0_GOLDENROD_CITY, 4, 3
	waitstate
	release
	end
GSJohto_8_5_Lake_of_Rage_Text:
	.string "Johto 8.5: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
