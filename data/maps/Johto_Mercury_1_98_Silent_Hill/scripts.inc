Johto_Mercury_1_98_Silent_Hill_MapScripts::
	.byte 0

Johto_Mercury_1_98_Silent_Hill_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_1_98_Silent_Hill_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_1_98_Silent_Hill_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_1_98_Silent_Hill_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_1_99_CLIFF_EDGE_GATE, 8, 37
	waitstate
	release
	end
Johto_Mercury_1_98_Silent_Hill_Inspect_Text:
	.string "Mercury Johto 1.98. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
