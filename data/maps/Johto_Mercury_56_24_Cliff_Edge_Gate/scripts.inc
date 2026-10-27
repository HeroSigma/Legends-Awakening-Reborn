Johto_Mercury_56_24_Cliff_Edge_Gate_MapScripts::
	.byte 0

Johto_Mercury_56_24_Cliff_Edge_Gate_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_56_24_Cliff_Edge_Gate_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_56_24_Cliff_Edge_Gate_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_56_24_Cliff_Edge_Gate_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_37_ROUTE_47, 21, 11
	waitstate
	release
	end
Johto_Mercury_56_24_Cliff_Edge_Gate_Inspect_Text:
	.string "Mercury Johto 56.24. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
