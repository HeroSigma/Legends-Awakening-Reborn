GSJohto_35_3_Lake_of_Rage_MapScripts::
	.byte 0

GSJohto_35_3_Lake_of_Rage_Inspect::
	lock
	faceplayer
	msgbox GSJohto_35_3_Lake_of_Rage_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_35_3_Lake_of_Rage_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_35_3_Lake_of_Rage_Next::
	closemessage
	warp MAP_GSJOHTO_35_4_ROUTE_38, 14, 7
	waitstate
	release
	end
GSJohto_35_3_Lake_of_Rage_Text:
	.string "Johto 35.3: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
