Johto_Lake_of_Rage_MapScripts::
	.byte 0

GSJohto_3_11_Lake_of_Rage_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_11_Lake_of_Rage_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_11_Lake_of_Rage_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_11_Lake_of_Rage_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_35_ROUTE_45, 12, 5
	waitstate
	release
	end
GSJohto_3_11_Lake_of_Rage_Inspect_Text:
	.string "Mercury Johto 3.100. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
