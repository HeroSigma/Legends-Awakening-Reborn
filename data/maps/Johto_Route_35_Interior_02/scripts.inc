Johto_Route_35_Interior_02_MapScripts::
	.byte 0

Johto_Route_35_Interior_02_Inspect::
	lock
	faceplayer
	msgbox Johto_Route_35_Interior_02_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Route_35_Interior_02_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Route_35_Interior_02_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_44_9_PALLET_TOWN, 3, 9
	waitstate
	release
	end
Johto_Route_35_Interior_02_Inspect_Text:
	.string "Mercury Johto 44.8. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
