Johto_Mercury_44_16_Route_41_MapScripts::
	.byte 0

Johto_Mercury_44_16_Route_41_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_44_16_Route_41_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_44_16_Route_41_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_44_16_Route_41_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_5_4_CHERRYGROVE_CITY, 10, 16
	waitstate
	release
	end
Johto_Mercury_44_16_Route_41_Inspect_Text:
	.string "Mercury Johto 44.16. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
