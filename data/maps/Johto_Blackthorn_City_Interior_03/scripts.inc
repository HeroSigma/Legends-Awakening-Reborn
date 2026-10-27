Johto_Blackthorn_City_Interior_03_MapScripts::
	.byte 0

GSJohto_14_4_Blackthorn_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_14_4_Blackthorn_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_14_4_Blackthorn_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_14_4_Blackthorn_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_14_8_BLACKTHORN_CITY, 1, 5
	waitstate
	release
	end
GSJohto_14_4_Blackthorn_City_Inspect_Text:
	.string "Mercury Johto 32.2. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
