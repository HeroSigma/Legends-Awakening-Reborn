GSJohto_33_4_Lighthouse_MapScripts::
	.byte 0

GSJohto_33_4_Lighthouse_Inspect::
	lock
	faceplayer
	msgbox GSJohto_33_4_Lighthouse_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_33_4_Lighthouse_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_33_4_Lighthouse_Next::
	closemessage
	warp MAP_GSJOHTO_34_0_LAKE_OF_RAGE, 4, 3
	waitstate
	release
	end
GSJohto_33_4_Lighthouse_Text:
	.string "Johto 33.4: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
