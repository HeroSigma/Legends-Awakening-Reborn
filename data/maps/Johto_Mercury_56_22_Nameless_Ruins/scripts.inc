Johto_Mercury_56_22_Nameless_Ruins_MapScripts::
	.byte 0

Johto_Mercury_56_22_Nameless_Ruins_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_56_22_Nameless_Ruins_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_56_22_Nameless_Ruins_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_56_22_Nameless_Ruins_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_23_1_ROUTE_40, 6, 6
	waitstate
	release
	end
Johto_Mercury_56_22_Nameless_Ruins_Inspect_Text:
	.string "Mercury Johto 56.22. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
