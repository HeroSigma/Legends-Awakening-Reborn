Johto_Lighthouse_Interior_02_MapScripts::
	.byte 0

GSJohto_1_63_Lighthouse_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_63_Lighthouse_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_63_Lighthouse_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_63_Lighthouse_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_49_13_GLITTER_LIGHTHOUSE, 34, 11
	waitstate
	release
	end
GSJohto_1_63_Lighthouse_Inspect_Text:
	.string "Mercury Johto 49.12. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
