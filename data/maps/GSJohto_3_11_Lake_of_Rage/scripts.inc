GSJohto_3_11_Lake_of_Rage_MapScripts::
	.byte 0

GSJohto_3_11_Lake_of_Rage_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_11_Lake_of_Rage_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_11_Lake_of_Rage_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_11_Lake_of_Rage_Next::
	closemessage
	warp MAP_GSJOHTO_3_19_ROUTE_29, 32, 5
	waitstate
	release
	end
GSJohto_3_11_Lake_of_Rage_Text:
	.string "Johto 3.11: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
