Johto_Mercury_39_0_Route_26_MapScripts::
	.byte 0

Johto_Mercury_39_0_Route_26_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_39_0_Route_26_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_39_0_Route_26_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_39_0_Route_26_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_40_0_CLIFFSIDE_TOWN, 3, 5
	waitstate
	release
	end
Johto_Mercury_39_0_Route_26_Inspect_Text:
	.string "Mercury Johto 39.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
