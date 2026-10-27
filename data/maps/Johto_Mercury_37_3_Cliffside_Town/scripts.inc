Johto_Mercury_37_3_Cliffside_Town_MapScripts::
	.byte 0

Johto_Mercury_37_3_Cliffside_Town_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_37_3_Cliffside_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_37_3_Cliffside_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_37_3_Cliffside_Town_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_37_4_JOHTO_MINE, 2, 6
	waitstate
	release
	end
Johto_Mercury_37_3_Cliffside_Town_Inspect_Text:
	.string "Mercury Johto 37.3. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
