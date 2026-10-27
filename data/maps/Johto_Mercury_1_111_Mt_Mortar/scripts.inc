Johto_Mercury_1_111_Mt_Mortar_MapScripts::
	.byte 0

Johto_Mercury_1_111_Mt_Mortar_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_1_111_Mt_Mortar_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_1_111_Mt_Mortar_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_1_111_Mt_Mortar_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_1_112_PHANTOM_FOREST, 20, 6
	waitstate
	release
	end
Johto_Mercury_1_111_Mt_Mortar_Inspect_Text:
	.string "Mercury Johto 1.111. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
