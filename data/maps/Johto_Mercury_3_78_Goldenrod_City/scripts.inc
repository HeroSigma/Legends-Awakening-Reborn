Johto_Mercury_3_78_Goldenrod_City_MapScripts::
	.byte 0

Johto_Mercury_3_78_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_3_78_Goldenrod_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_3_78_Goldenrod_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_3_78_Goldenrod_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_98_ROUTE_29, 28, 5
	waitstate
	release
	end
Johto_Mercury_3_78_Goldenrod_City_Inspect_Text:
	.string "Mercury Johto 3.78. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
