Johto_Mercury_55_0_Tohjo_Falls_MapScripts::
	.byte 0

Johto_Mercury_55_0_Tohjo_Falls_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_55_0_Tohjo_Falls_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_55_0_Tohjo_Falls_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_55_0_Tohjo_Falls_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_55_1_ROUTE_26, 11, 2
	waitstate
	release
	end
Johto_Mercury_55_0_Tohjo_Falls_Inspect_Text:
	.string "Mercury Johto 55.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
