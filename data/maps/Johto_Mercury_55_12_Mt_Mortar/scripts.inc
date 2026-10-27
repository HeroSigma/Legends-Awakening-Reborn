Johto_Mercury_55_12_Mt_Mortar_MapScripts::
	.byte 0

Johto_Mercury_55_12_Mt_Mortar_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_55_12_Mt_Mortar_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_55_12_Mt_Mortar_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_55_12_Mt_Mortar_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_55_13_MT_MORTAR, 23, 10
	waitstate
	release
	end
Johto_Mercury_55_12_Mt_Mortar_Inspect_Text:
	.string "Mercury Johto 55.12. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
