Johto_Mercury_34_5_Cliffside_Town_MapScripts::
	.byte 0

Johto_Mercury_34_5_Cliffside_Town_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_34_5_Cliffside_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_34_5_Cliffside_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_34_5_Cliffside_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_34_0_LAKE_OF_RAGE, 3, 5
	waitstate
	release
	end
Johto_Mercury_34_5_Cliffside_Town_Inspect_Text:
	.string "Mercury Johto 34.5. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
