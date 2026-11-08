Johto_Mercury_3_47_Route_34_MapScripts::
	.byte 0

Johto_Mercury_3_47_Route_34_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_3_47_Route_34_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_3_47_Route_34_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_3_47_Route_34_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_3_49_ROUTE_41, 14, 15
	waitstate
	release
	end
Johto_Mercury_3_47_Route_34_Inspect_Text:
	.string "Mercury Johto 3.47. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
