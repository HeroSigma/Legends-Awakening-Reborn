Johto_Ruins_of_Alph_Section_01_MapScripts::
	.byte 0

GSJohto_1_90_Ruins_of_Alph_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_90_Ruins_of_Alph_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_90_Ruins_of_Alph_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_90_Ruins_of_Alph_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_1_51_RUINS_OF_ALPH, 4, 5
	waitstate
	release
	end
GSJohto_1_90_Ruins_of_Alph_Inspect_Text:
	.string "Mercury Johto 1.50. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
