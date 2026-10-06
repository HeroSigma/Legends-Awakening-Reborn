GSJohto_3_44_Mt_Silver_MapScripts::
	.byte 0

GSJohto_3_44_Mt_Silver_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_44_Mt_Silver_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_44_Mt_Silver_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_44_Mt_Silver_Next::
	closemessage
	warp MAP_GSJOHTO_3_66_GOLDENROD_CITY, 13, 15
	waitstate
	release
	end
GSJohto_3_44_Mt_Silver_Text:
	.string "Johto 3.44: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
