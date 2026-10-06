BWA_8_0_MapScripts::
	.byte 0

BWA_8_0_Inspect::
	lock
	faceplayer
	msgbox BWA_8_0_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_8_0_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_8_0_Next::
	closemessage
	warp MAP_BWA_39_0, 20, 34
	waitstate
	release
	end
BWA_8_0_Text:
	.string "BWA inspection 17 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
