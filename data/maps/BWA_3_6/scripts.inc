BWA_3_6_MapScripts::
	.byte 0

BWA_3_6_Inspect::
	lock
	faceplayer
	msgbox BWA_3_6_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_3_6_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_3_6_Next::
	closemessage
	warp MAP_BWA_3_20, 20, 30
	waitstate
	release
	end
BWA_3_6_Text:
	.string "BWA inspection 3 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
