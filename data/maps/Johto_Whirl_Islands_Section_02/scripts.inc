Johto_Whirl_Islands_Section_02_MapScripts::
	.byte 0

Johto_Whirl_Islands_Section_02_Inspect::
	lock
	faceplayer
	msgbox Johto_Whirl_Islands_Section_02_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Whirl_Islands_Section_02_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Whirl_Islands_Section_02_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_55_17_BELL_TOWER, 3, 6
	waitstate
	release
	end
Johto_Whirl_Islands_Section_02_Inspect_Text:
	.string "Mercury Johto 55.16. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
