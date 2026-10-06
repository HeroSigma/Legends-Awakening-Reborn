BWA_5_4_MapScripts::
	.byte 0

BWA_5_4_Inspect::
	lock
	faceplayer
	msgbox BWA_5_4_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_5_4_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_5_4_Next::
	closemessage
	warp MAP_BWA_6_2, 10, 15
	waitstate
	release
	end
BWA_5_4_Text:
	.string "BWA inspection 13 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
