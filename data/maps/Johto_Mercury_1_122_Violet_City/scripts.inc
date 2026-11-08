Johto_Mercury_1_122_Violet_City_MapScripts::
	.byte 0

Johto_Mercury_1_122_Violet_City_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_1_122_Violet_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_1_122_Violet_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_1_122_Violet_City_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_1_123_SLOWPOKE_WELL, 12, 6
	waitstate
	release
	end
Johto_Mercury_1_122_Violet_City_Inspect_Text:
	.string "Mercury Johto 1.122. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
