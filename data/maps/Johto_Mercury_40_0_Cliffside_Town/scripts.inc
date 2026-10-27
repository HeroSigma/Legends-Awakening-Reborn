Johto_Mercury_40_0_Cliffside_Town_MapScripts::
	.byte 0

Johto_Mercury_40_0_Cliffside_Town_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_40_0_Cliffside_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_40_0_Cliffside_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_40_0_Cliffside_Town_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_41_0_ROUTE_27, 3, 5
	waitstate
	release
	end
Johto_Mercury_40_0_Cliffside_Town_Inspect_Text:
	.string "Mercury Johto 40.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
