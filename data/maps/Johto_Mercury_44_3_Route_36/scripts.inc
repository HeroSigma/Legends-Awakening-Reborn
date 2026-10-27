Johto_Mercury_44_3_Route_36_MapScripts::
	.byte 0

Johto_Mercury_44_3_Route_36_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_44_3_Route_36_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_44_3_Route_36_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_44_3_Route_36_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_44_4_ROUTE_32, 3, 9
	waitstate
	release
	end
Johto_Mercury_44_3_Route_36_Inspect_Text:
	.string "Mercury Johto 44.3. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
