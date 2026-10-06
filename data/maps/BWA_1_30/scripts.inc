BWA_1_30_MapScripts::
	.byte 0

BWA_1_30_Inspect::
	lock
	faceplayer
	msgbox BWA_1_30_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_1_30_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_1_30_Next::
	closemessage
	warp MAP_BWA_3_4, 30, 17
	waitstate
	release
	end
BWA_1_30_Text:
	.string "BWA inspection 1 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
