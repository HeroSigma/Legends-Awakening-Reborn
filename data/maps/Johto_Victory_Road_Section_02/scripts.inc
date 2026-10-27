Johto_Victory_Road_Section_02_MapScripts::
	.byte 0

GSJohto_1_41_Victory_Road_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_41_Victory_Road_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_41_Victory_Road_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_41_Victory_Road_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_54_0_BLACKTHORN_CITY, 12, 37
	waitstate
	release
	end
GSJohto_1_41_Victory_Road_Inspect_Text:
	.string "Mercury Johto 53.10. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
