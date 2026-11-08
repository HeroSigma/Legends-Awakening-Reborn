Johto_Dark_Cave_MapScripts::
	.byte 0

Johto_Dark_Cave_Inspect::
	lock
	faceplayer
	msgbox Johto_Dark_Cave_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Dark_Cave_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Dark_Cave_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_3_47_ROUTE_34, 18, 15
	waitstate
	release
	end
Johto_Dark_Cave_Inspect_Text:
	.string "Mercury Johto 1.126. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
