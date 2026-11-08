Johto_Lighthouse_Interior_06_MapScripts::
	.byte 0

GSJohto_33_0_Lighthouse_Inspect::
	lock
	faceplayer
	msgbox GSJohto_33_0_Lighthouse_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_33_0_Lighthouse_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_33_0_Lighthouse_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_35_0_ROUTE_34, 2, 7
	waitstate
	release
	end
GSJohto_33_0_Lighthouse_Inspect_Text:
	.string "Mercury Johto 49.19. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
