BWA_3_23_MapScripts::
	.byte 0

BWA_3_23_Inspect::
	lock
	faceplayer
	msgbox BWA_3_23_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_3_23_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_3_23_Next::
	closemessage
	warp MAP_BWA_3_24, 30, 15
	waitstate
	release
	end
BWA_3_23_Text:
	.string "BWA inspection 5 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
