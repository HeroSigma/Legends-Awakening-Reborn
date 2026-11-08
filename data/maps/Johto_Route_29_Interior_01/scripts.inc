Johto_Route_29_Interior_01_MapScripts::
	.byte 0

Johto_Route_29_Interior_01_Inspect::
	lock
	faceplayer
	msgbox Johto_Route_29_Interior_01_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Route_29_Interior_01_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Route_29_Interior_01_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_44_1_ROUTE_31, 3, 7
	waitstate
	release
	end
Johto_Route_29_Interior_01_Inspect_Text:
	.string "Mercury Johto 44.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
