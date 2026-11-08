Johto_Mercury_1_39_Victory_Road_MapScripts::
	.byte 0

Johto_Mercury_1_39_Victory_Road_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_1_39_Victory_Road_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_1_39_Victory_Road_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_1_39_Victory_Road_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_43_VICTORY_ROAD, 12, 18
	waitstate
	release
	end
Johto_Mercury_1_39_Victory_Road_Inspect_Text:
	.string "Mercury Johto 1.39. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
