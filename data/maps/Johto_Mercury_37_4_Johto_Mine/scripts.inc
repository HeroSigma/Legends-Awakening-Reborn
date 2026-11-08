Johto_Mercury_37_4_Johto_Mine_MapScripts::
	.byte 0

Johto_Mercury_37_4_Johto_Mine_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_37_4_Johto_Mine_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_37_4_Johto_Mine_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_37_4_Johto_Mine_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_39_0_ROUTE_26, 3, 5
	waitstate
	release
	end
Johto_Mercury_37_4_Johto_Mine_Inspect_Text:
	.string "Mercury Johto 37.4. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
