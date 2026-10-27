Unova_NuvemaTown_Interior_01_MapScripts::
	.byte 0

BWA_4_0_Inspect::
	lock
	faceplayer
	msgbox BWA_4_0_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_4_0_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_4_0_Next::
	closemessage
	warp MAP_BWA_4_1, 6, 4
	waitstate
	release
	end
BWA_4_0_Text:
	.string "BWA inspection 9 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
