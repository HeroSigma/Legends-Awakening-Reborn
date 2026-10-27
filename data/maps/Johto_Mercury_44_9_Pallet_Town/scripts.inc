Johto_Mercury_44_9_Pallet_Town_MapScripts::
	.byte 0

Johto_Mercury_44_9_Pallet_Town_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_44_9_Pallet_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_44_9_Pallet_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_44_9_Pallet_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_18_1_ROUTE_35, 3, 3
	waitstate
	release
	end
Johto_Mercury_44_9_Pallet_Town_Inspect_Text:
	.string "Mercury Johto 44.9. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
