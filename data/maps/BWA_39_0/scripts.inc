BWA_39_0_MapScripts::
	.byte 0

BWA_39_0_Inspect::
	lock
	faceplayer
	msgbox BWA_39_0_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_39_0_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_39_0_Next::
	closemessage
	warp MAP_BWA_42_0, 6, 6
	waitstate
	release
	end
BWA_39_0_Text:
	.string "BWA inspection 18 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
