Johto_Mercury_49_13_Glitter_Lighthouse_MapScripts::
	.byte 0

Johto_Mercury_49_13_Glitter_Lighthouse_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_49_13_Glitter_Lighthouse_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_49_13_Glitter_Lighthouse_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_49_13_Glitter_Lighthouse_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_49_14_GLITTER_LIGHTHOUSE, 20, 16
	waitstate
	release
	end
Johto_Mercury_49_13_Glitter_Lighthouse_Inspect_Text:
	.string "Mercury Johto 49.13. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
