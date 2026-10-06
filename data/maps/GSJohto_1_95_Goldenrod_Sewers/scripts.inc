GSJohto_1_95_Goldenrod_Sewers_MapScripts::
	.byte 0

GSJohto_1_95_Goldenrod_Sewers_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_95_Goldenrod_Sewers_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_95_Goldenrod_Sewers_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_95_Goldenrod_Sewers_Next::
	closemessage
	warp MAP_GSJOHTO_1_97_DRAGON_S_DEN, 29, 33
	waitstate
	release
	end
GSJohto_1_95_Goldenrod_Sewers_Text:
	.string "Johto 1.95: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
