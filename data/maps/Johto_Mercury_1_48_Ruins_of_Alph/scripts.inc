Johto_Mercury_1_48_Ruins_of_Alph_MapScripts::
	.byte 0

Johto_Mercury_1_48_Ruins_of_Alph_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_1_48_Ruins_of_Alph_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_1_48_Ruins_of_Alph_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_1_48_Ruins_of_Alph_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_1_49_RUINS_OF_ALPH, 27, 3
	waitstate
	release
	end
Johto_Mercury_1_48_Ruins_of_Alph_Inspect_Text:
	.string "Mercury Johto 1.48. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
