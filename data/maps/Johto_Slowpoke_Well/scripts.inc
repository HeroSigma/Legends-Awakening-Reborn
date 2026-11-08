Johto_Slowpoke_Well_MapScripts::
	.byte 0

Johto_Slowpoke_Well_Inspect::
	lock
	faceplayer
	msgbox Johto_Slowpoke_Well_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Slowpoke_Well_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Slowpoke_Well_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_1_96_SILENT_HILL, 8, 11
	waitstate
	release
	end
Johto_Slowpoke_Well_Inspect_Text:
	.string "Mercury Johto 1.95. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
