Johto_Mercury_55_3_Slowpoke_Well_MapScripts::
	.byte 0

Johto_Mercury_55_3_Slowpoke_Well_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_55_3_Slowpoke_Well_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_55_3_Slowpoke_Well_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_55_3_Slowpoke_Well_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_55_4_SLOWPOKE_WELL, 6, 5
	waitstate
	release
	end
Johto_Mercury_55_3_Slowpoke_Well_Inspect_Text:
	.string "Mercury Johto 55.3. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
