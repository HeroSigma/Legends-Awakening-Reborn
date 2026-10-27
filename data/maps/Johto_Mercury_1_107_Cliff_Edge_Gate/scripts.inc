Johto_Mercury_1_107_Cliff_Edge_Gate_MapScripts::
	.byte 0

Johto_Mercury_1_107_Cliff_Edge_Gate_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_1_107_Cliff_Edge_Gate_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_1_107_Cliff_Edge_Gate_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_1_107_Cliff_Edge_Gate_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_1_108_SEABREAK_CAVE, 6, 9
	waitstate
	release
	end
Johto_Mercury_1_107_Cliff_Edge_Gate_Inspect_Text:
	.string "Mercury Johto 1.107. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
