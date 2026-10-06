GSJohto_1_86_Whirl_Islands_MapScripts::
	.byte 0

GSJohto_1_86_Whirl_Islands_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_86_Whirl_Islands_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_86_Whirl_Islands_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_86_Whirl_Islands_Next::
	closemessage
	warp MAP_GSJOHTO_1_88_RUINS_OF_ALPH, 18, 7
	waitstate
	release
	end
GSJohto_1_86_Whirl_Islands_Text:
	.string "Johto 1.86: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
