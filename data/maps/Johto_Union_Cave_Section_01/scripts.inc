Johto_Union_Cave_Section_01_MapScripts::
	.byte 0

Johto_Union_Cave_Section_01_Inspect::
	lock
	faceplayer
	msgbox Johto_Union_Cave_Section_01_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Union_Cave_Section_01_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Union_Cave_Section_01_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_30_ROUTE_40, 19, 10
	waitstate
	release
	end
Johto_Union_Cave_Section_01_Inspect_Text:
	.string "Mercury Johto 3.94. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
