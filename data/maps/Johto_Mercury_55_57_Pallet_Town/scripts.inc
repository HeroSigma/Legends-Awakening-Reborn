Johto_Mercury_55_57_Pallet_Town_MapScripts::
	.byte 0

Johto_Mercury_55_57_Pallet_Town_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_55_57_Pallet_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_55_57_Pallet_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_55_57_Pallet_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_6_4_RUINS_OF_ALPH, 7, 4
	waitstate
	release
	end
Johto_Mercury_55_57_Pallet_Town_Inspect_Text:
	.string "Mercury Johto 55.57. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
