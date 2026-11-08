Unova_CasteliaCity_MapScripts::
	.byte 0

BWA_3_4_Inspect::
	lock
	faceplayer
	msgbox BWA_3_4_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_3_4_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_3_4_Next::
	closemessage
	warp MAP_BWA_3_6, 57, 20
	waitstate
	release
	end
BWA_3_4_Text:
	.string "BWA inspection 2 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
