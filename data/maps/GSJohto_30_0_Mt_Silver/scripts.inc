GSJohto_30_0_Mt_Silver_MapScripts::
	.byte 0

GSJohto_30_0_Mt_Silver_Inspect::
	lock
	faceplayer
	msgbox GSJohto_30_0_Mt_Silver_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_30_0_Mt_Silver_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_30_0_Mt_Silver_Next::
	closemessage
	warp MAP_GSJOHTO_32_0_CLIFF_CAVE, 1, 7
	waitstate
	release
	end
GSJohto_30_0_Mt_Silver_Text:
	.string "Johto 30.0: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
