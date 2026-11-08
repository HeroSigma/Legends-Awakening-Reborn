Johto_Blackthorn_City_Interior_04_MapScripts::
	.byte 0

GSJohto_14_5_Blackthorn_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_14_5_Blackthorn_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_14_5_Blackthorn_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_14_5_Blackthorn_City_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_54_5_BLACKTHORN_CITY, 4, 15
	waitstate
	release
	end
GSJohto_14_5_Blackthorn_City_Inspect_Text:
	.string "Mercury Johto 54.4. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
