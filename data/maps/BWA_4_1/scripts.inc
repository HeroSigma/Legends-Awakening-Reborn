BWA_4_1_MapScripts::
	.byte 0

BWA_4_1_Inspect::
	lock
	faceplayer
	msgbox BWA_4_1_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_4_1_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_4_1_Next::
	closemessage
	warp MAP_BWA_4_2, 6, 5
	waitstate
	release
	end
BWA_4_1_Text:
	.string "BWA inspection 10 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
