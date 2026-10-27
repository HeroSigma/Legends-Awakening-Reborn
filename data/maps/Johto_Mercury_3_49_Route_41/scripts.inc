Johto_Mercury_3_49_Route_41_MapScripts::
	.byte 0

Johto_Mercury_3_49_Route_41_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_3_49_Route_41_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_3_49_Route_41_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_3_49_Route_41_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_1_CHERRYGROVE_CITY, 26, 7
	waitstate
	release
	end
Johto_Mercury_3_49_Route_41_Inspect_Text:
	.string "Mercury Johto 3.49. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
