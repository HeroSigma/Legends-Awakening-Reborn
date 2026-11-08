Johto_Union_Cave_Section_04_MapScripts::
	.byte 0

Johto_Union_Cave_Section_04_Inspect::
	lock
	faceplayer
	msgbox Johto_Union_Cave_Section_04_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Union_Cave_Section_04_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Union_Cave_Section_04_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_23_ROUTE_33, 9, 11
	waitstate
	release
	end
Johto_Union_Cave_Section_04_Inspect_Text:
	.string "Mercury Johto 3.86. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
