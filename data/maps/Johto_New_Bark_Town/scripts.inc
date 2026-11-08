Johto_New_Bark_Town_MapScripts::
	.byte 0

GSJohto_1_11_New_Bark_Town_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_11_New_Bark_Town_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_11_New_Bark_Town_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_11_New_Bark_Town_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_14_4_BLACKTHORN_CITY, 7, 6
	waitstate
	release
	end
GSJohto_1_11_New_Bark_Town_Inspect_Text:
	.string "Mercury Johto 32.1. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
