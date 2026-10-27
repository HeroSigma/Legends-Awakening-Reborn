Johto_Ruins_of_Alph_Interior_02_MapScripts::
	.byte 0

GSJohto_6_4_Ruins_of_Alph_Inspect::
	lock
	faceplayer
	msgbox GSJohto_6_4_Ruins_of_Alph_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_6_4_Ruins_of_Alph_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_6_4_Ruins_of_Alph_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_56_10_GOLDENROD_CITY, 11, 8
	waitstate
	release
	end
GSJohto_6_4_Ruins_of_Alph_Inspect_Text:
	.string "Mercury Johto 56.9. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
