Johto_Lake_of_Rage_Interior_02_MapScripts::
	.byte 0

GSJohto_34_0_Lake_of_Rage_Inspect::
	lock
	faceplayer
	msgbox GSJohto_34_0_Lake_of_Rage_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_34_0_Lake_of_Rage_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_34_0_Lake_of_Rage_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_10_9_ECRUTEAK_CITY, 5, 6
	waitstate
	release
	end
GSJohto_34_0_Lake_of_Rage_Inspect_Text:
	.string "Mercury Johto 34.7. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
