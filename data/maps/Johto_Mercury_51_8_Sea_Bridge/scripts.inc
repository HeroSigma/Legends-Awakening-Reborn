Johto_Mercury_51_8_Sea_Bridge_MapScripts::
	.byte 0

Johto_Mercury_51_8_Sea_Bridge_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_51_8_Sea_Bridge_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_51_8_Sea_Bridge_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_51_8_Sea_Bridge_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_51_9_JOHTO_MINE, 65, 3
	waitstate
	release
	end
Johto_Mercury_51_8_Sea_Bridge_Inspect_Text:
	.string "Mercury Johto 51.8. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
