Johto_Mercury_56_18_Nameless_Ruins_MapScripts::
	.byte 0

Johto_Mercury_56_18_Nameless_Ruins_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_56_18_Nameless_Ruins_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_56_18_Nameless_Ruins_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_56_18_Nameless_Ruins_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_56_21_NAMELESS_RUINS, 3, 15
	waitstate
	release
	end
Johto_Mercury_56_18_Nameless_Ruins_Inspect_Text:
	.string "Mercury Johto 56.18. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
