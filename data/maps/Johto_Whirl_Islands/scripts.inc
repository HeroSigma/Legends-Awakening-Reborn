Johto_Whirl_Islands_MapScripts::
	.byte 0

Johto_Whirl_Islands_Inspect::
	lock
	faceplayer
	msgbox Johto_Whirl_Islands_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Whirl_Islands_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Whirl_Islands_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_84_WHIRL_ISLANDS, 39, 34
	waitstate
	release
	end
Johto_Whirl_Islands_Inspect_Text:
	.string "Mercury Johto 55.14. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
