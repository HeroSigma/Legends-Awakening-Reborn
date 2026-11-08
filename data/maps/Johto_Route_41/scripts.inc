Johto_Route_41_MapScripts::
	.byte 0

Johto_Route_41_Inspect::
	lock
	faceplayer
	msgbox Johto_Route_41_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Route_41_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Route_41_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_32_ROUTE_42, 76, 13
	waitstate
	release
	end
Johto_Route_41_Inspect_Text:
	.string "Mercury Johto 3.96. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
