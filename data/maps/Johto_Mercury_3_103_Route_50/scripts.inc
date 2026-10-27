Johto_Mercury_3_103_Route_50_MapScripts::
	.byte 0

Johto_Mercury_3_103_Route_50_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_3_103_Route_50_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_3_103_Route_50_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_3_103_Route_50_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_3_104_ROUTE_51, 18, 1
	waitstate
	release
	end
Johto_Mercury_3_103_Route_50_Inspect_Text:
	.string "Mercury Johto 3.103. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
