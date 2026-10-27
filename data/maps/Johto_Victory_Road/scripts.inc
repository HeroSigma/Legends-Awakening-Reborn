Johto_Victory_Road_MapScripts::
	.byte 0

Johto_Victory_Road_Inspect::
	lock
	faceplayer
	msgbox Johto_Victory_Road_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Victory_Road_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Victory_Road_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_40_VICTORY_ROAD, 24, 6
	waitstate
	release
	end
Johto_Victory_Road_Inspect_Text:
	.string "Mercury Johto 53.8. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
