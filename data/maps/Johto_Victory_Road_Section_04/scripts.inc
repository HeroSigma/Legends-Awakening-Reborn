Johto_Victory_Road_Section_04_MapScripts::
	.byte 0

Johto_Victory_Road_Section_04_Inspect::
	lock
	faceplayer
	msgbox Johto_Victory_Road_Section_04_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Victory_Road_Section_04_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Victory_Road_Section_04_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_44_VICTORY_ROAD, 12, 8
	waitstate
	release
	end
Johto_Victory_Road_Section_04_Inspect_Text:
	.string "Mercury Johto 1.40. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
