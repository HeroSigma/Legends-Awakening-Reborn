Johto_Lighthouse_Interior_07_MapScripts::
	.byte 0

GSJohto_33_1_Lighthouse_Inspect::
	lock
	faceplayer
	msgbox GSJohto_33_1_Lighthouse_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_33_1_Lighthouse_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_33_1_Lighthouse_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_33_0_LIGHTHOUSE, 3, 4
	waitstate
	release
	end
GSJohto_33_1_Lighthouse_Inspect_Text:
	.string "Mercury Johto 49.18. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
