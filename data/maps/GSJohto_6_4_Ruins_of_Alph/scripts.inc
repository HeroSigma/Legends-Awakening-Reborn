GSJohto_6_4_Ruins_of_Alph_MapScripts::
	.byte 0

GSJohto_6_4_Ruins_of_Alph_Inspect::
	lock
	faceplayer
	msgbox GSJohto_6_4_Ruins_of_Alph_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_6_4_Ruins_of_Alph_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_6_4_Ruins_of_Alph_Next::
	closemessage
	warp MAP_GSJOHTO_6_5_VIOLET_CITY, 12, 20
	waitstate
	release
	end
GSJohto_6_4_Ruins_of_Alph_Text:
	.string "Johto 6.4: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
