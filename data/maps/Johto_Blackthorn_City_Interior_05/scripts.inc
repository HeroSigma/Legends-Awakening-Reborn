Johto_Blackthorn_City_Interior_05_MapScripts::
	.byte 0

GSJohto_14_6_Blackthorn_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_14_6_Blackthorn_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_14_6_Blackthorn_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_14_6_Blackthorn_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_11_NEW_BARK_TOWN, 5, 5
	waitstate
	release
	end
GSJohto_14_6_Blackthorn_City_Inspect_Text:
	.string "Mercury Johto 32.0. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
