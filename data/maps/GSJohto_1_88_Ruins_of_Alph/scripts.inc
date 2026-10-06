GSJohto_1_88_Ruins_of_Alph_MapScripts::
	.byte 0

GSJohto_1_88_Ruins_of_Alph_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_88_Ruins_of_Alph_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_88_Ruins_of_Alph_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_88_Ruins_of_Alph_Next::
	closemessage
	warp MAP_GSJOHTO_1_89_RUINS_OF_ALPH, 3, 15
	waitstate
	release
	end
GSJohto_1_88_Ruins_of_Alph_Text:
	.string "Johto 1.88: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
