BWA_3_24_MapScripts::
	.byte 0

BWA_3_24_Inspect::
	lock
	faceplayer
	msgbox BWA_3_24_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_3_24_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_3_24_Next::
	closemessage
	warp MAP_BWA_3_45, 25, 15
	waitstate
	release
	end
BWA_3_24_Text:
	.string "BWA inspection 6 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
