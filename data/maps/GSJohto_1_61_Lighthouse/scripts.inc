GSJohto_1_61_Lighthouse_MapScripts::
	.byte 0

GSJohto_1_61_Lighthouse_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_61_Lighthouse_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_61_Lighthouse_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_61_Lighthouse_Next::
	closemessage
	warp MAP_GSJOHTO_1_62_LIGHTHOUSE, 13, 4
	waitstate
	release
	end
GSJohto_1_61_Lighthouse_Text:
	.string "Johto 1.61: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
