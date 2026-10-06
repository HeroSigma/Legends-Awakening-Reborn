BWA_6_5_MapScripts::
	.byte 0

BWA_6_5_Inspect::
	lock
	faceplayer
	msgbox BWA_6_5_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_6_5_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_6_5_Next::
	closemessage
	warp MAP_BWA_8_0, 8, 6
	waitstate
	release
	end
BWA_6_5_Text:
	.string "BWA inspection 16 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
