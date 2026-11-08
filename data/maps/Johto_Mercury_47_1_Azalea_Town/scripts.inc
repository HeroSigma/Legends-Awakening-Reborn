Johto_Mercury_47_1_Azalea_Town_MapScripts::
	.byte 0

Johto_Mercury_47_1_Azalea_Town_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_47_1_Azalea_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_47_1_Azalea_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_47_1_Azalea_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_7_0_AZALEA_TOWN, 4, 7
	waitstate
	release
	end
Johto_Mercury_47_1_Azalea_Town_Inspect_Text:
	.string "Mercury Johto 47.1. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
