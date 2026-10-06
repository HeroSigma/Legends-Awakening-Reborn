GSJohto_1_62_Lighthouse_MapScripts::
	.byte 0

GSJohto_1_62_Lighthouse_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_62_Lighthouse_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_62_Lighthouse_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_62_Lighthouse_Next::
	closemessage
	warp MAP_GSJOHTO_1_63_LIGHTHOUSE, 4, 6
	waitstate
	release
	end
GSJohto_1_62_Lighthouse_Text:
	.string "Johto 1.62: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
