GSJohto_14_8_Blackthorn_City_MapScripts::
	.byte 0

GSJohto_14_8_Blackthorn_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_14_8_Blackthorn_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_14_8_Blackthorn_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_14_8_Blackthorn_City_Next::
	closemessage
	warp MAP_GSJOHTO_14_9_BLACKTHORN_CITY, 5, 8
	waitstate
	release
	end
GSJohto_14_8_Blackthorn_City_Text:
	.string "Johto 14.8: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
