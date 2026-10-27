Johto_Mercury_45_6_Route_31_MapScripts::
	.byte 0

Johto_Mercury_45_6_Route_31_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_45_6_Route_31_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_45_6_Route_31_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_45_6_Route_31_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_6_5_VIOLET_CITY, 16, 12
	waitstate
	release
	end
Johto_Mercury_45_6_Route_31_Inspect_Text:
	.string "Mercury Johto 45.6. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
