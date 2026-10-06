GSJohto_1_18_S_S_Anne_MapScripts::
	.byte 0

GSJohto_1_18_S_S_Anne_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_18_S_S_Anne_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_18_S_S_Anne_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_18_S_S_Anne_Next::
	closemessage
	warp MAP_GSJOHTO_1_19_S_S_ANNE, 3, 4
	waitstate
	release
	end
GSJohto_1_18_S_S_Anne_Text:
	.string "Johto 1.18: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
