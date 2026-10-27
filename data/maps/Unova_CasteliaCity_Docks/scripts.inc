Unova_CasteliaCity_Docks_MapScripts::
	.byte 0

BWA_3_45_Inspect::
	lock
	faceplayer
	msgbox BWA_3_45_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_3_45_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_3_45_Next::
	closemessage
	warp MAP_BWA_3_46, 30, 16
	waitstate
	release
	end
BWA_3_45_Text:
	.string "BWA inspection 7 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
