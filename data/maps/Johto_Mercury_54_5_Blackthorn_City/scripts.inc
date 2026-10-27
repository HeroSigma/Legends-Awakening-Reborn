Johto_Mercury_54_5_Blackthorn_City_MapScripts::
	.byte 0

Johto_Mercury_54_5_Blackthorn_City_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_54_5_Blackthorn_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_54_5_Blackthorn_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_54_5_Blackthorn_City_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_54_8_DRAGON_S_DEN, 8, 5
	waitstate
	release
	end
Johto_Mercury_54_5_Blackthorn_City_Inspect_Text:
	.string "Mercury Johto 54.5. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
