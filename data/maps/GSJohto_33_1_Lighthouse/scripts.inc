GSJohto_33_1_Lighthouse_MapScripts::
	.byte 0

GSJohto_33_1_Lighthouse_Inspect::
	lock
	faceplayer
	msgbox GSJohto_33_1_Lighthouse_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_33_1_Lighthouse_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_33_1_Lighthouse_Next::
	closemessage
	warp MAP_GSJOHTO_33_4_LIGHTHOUSE, 8, 3
	waitstate
	release
	end
GSJohto_33_1_Lighthouse_Text:
	.string "Johto 33.1: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
