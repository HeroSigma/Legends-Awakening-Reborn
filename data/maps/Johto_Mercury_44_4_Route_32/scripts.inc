Johto_Mercury_44_4_Route_32_MapScripts::
	.byte 0

Johto_Mercury_44_4_Route_32_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_44_4_Route_32_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_44_4_Route_32_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_44_4_Route_32_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_44_5_AZALEA_TOWN, 7, 8
	waitstate
	release
	end
Johto_Mercury_44_4_Route_32_Inspect_Text:
	.string "Mercury Johto 44.4. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
