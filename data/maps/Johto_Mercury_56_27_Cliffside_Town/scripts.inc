Johto_Mercury_56_27_Cliffside_Town_MapScripts::
	.byte 0

Johto_Mercury_56_27_Cliffside_Town_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_56_27_Cliffside_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_56_27_Cliffside_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_56_27_Cliffside_Town_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_56_28_CLIFF_EDGE_GATE, 8, 12
	waitstate
	release
	end
Johto_Mercury_56_27_Cliffside_Town_Inspect_Text:
	.string "Mercury Johto 56.27. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
