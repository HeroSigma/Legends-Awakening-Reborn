Johto_Mercury_1_112_Phantom_Forest_MapScripts::
	.byte 0

Johto_Mercury_1_112_Phantom_Forest_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_1_112_Phantom_Forest_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_1_112_Phantom_Forest_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_1_112_Phantom_Forest_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_1_113_SEABREAK_CAVE, 4, 14
	waitstate
	release
	end
Johto_Mercury_1_112_Phantom_Forest_Inspect_Text:
	.string "Mercury Johto 1.112. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
