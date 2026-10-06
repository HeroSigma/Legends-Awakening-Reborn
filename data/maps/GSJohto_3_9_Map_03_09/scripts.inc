GSJohto_3_9_Map_03_09_MapScripts::
	.byte 0

GSJohto_3_9_Map_03_09_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_9_Map_03_09_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_9_Map_03_09_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_9_Map_03_09_Next::
	closemessage
	warp MAP_GSJOHTO_3_10_BLACKTHORN_CITY, 12, 34
	waitstate
	release
	end
GSJohto_3_9_Map_03_09_Text:
	.string "Johto 3.9: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
