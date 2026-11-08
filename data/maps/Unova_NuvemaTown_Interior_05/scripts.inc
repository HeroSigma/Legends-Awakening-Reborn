Unova_NuvemaTown_Interior_05_MapScripts::
	.byte 0

BWA_42_0_Inspect::
	lock
	faceplayer
	msgbox BWA_42_0_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, BWA_42_0_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
BWA_42_0_Next::
	closemessage
	warp MAP_BWA_1_30, 45, 19
	waitstate
	release
	end
BWA_42_0_Text:
	.string "BWA inspection 19 of 19.\n"
	.string "Visit the next map?\p"
	.string "YES: next. NO: Littleroot.$"
