Johto_Mercury_1_99_Cliff_Edge_Gate_MapScripts::
	.byte 0

Johto_Mercury_1_99_Cliff_Edge_Gate_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_1_99_Cliff_Edge_Gate_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_1_99_Cliff_Edge_Gate_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_1_99_Cliff_Edge_Gate_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_1_100_SILENT_HILL, 10, 4
	waitstate
	release
	end
Johto_Mercury_1_99_Cliff_Edge_Gate_Inspect_Text:
	.string "Mercury Johto 1.99. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
