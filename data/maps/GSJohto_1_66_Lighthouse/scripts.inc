GSJohto_1_66_Lighthouse_MapScripts::
	.byte 0

GSJohto_1_66_Lighthouse_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_66_Lighthouse_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_66_Lighthouse_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_66_Lighthouse_Next::
	closemessage
	warp MAP_GSJOHTO_1_71_NATIONAL_PARK, 6, 5
	waitstate
	release
	end
GSJohto_1_66_Lighthouse_Text:
	.string "Johto 1.66: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
