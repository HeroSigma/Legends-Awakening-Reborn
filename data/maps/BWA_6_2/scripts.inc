BWA_6_2_MapScripts::
	.byte 0

BWA_6_2_Inspect::
	lock
	faceplayer
	msgbox BWA_6_2_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_6_2_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_6_2_Next::
	closemessage
	warp MAP_BWA_6_4, 7, 7
	waitstate
	release
	end
BWA_6_2_Text:
	.string "BWA inspection 14 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
