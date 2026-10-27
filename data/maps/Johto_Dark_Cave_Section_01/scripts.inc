Johto_Dark_Cave_Section_01_MapScripts::
	.byte 0

Johto_Dark_Cave_Section_01_Inspect::
	lock
	faceplayer
	msgbox Johto_Dark_Cave_Section_01_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Dark_Cave_Section_01_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Dark_Cave_Section_01_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_1_DARK_CAVE, 58, 4
	waitstate
	release
	end
Johto_Dark_Cave_Section_01_Inspect_Text:
	.string "Mercury Johto 1.125. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
