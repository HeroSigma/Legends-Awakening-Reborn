GSJohto_1_81_Union_Cave_MapScripts::
	.byte 0

GSJohto_1_81_Union_Cave_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_81_Union_Cave_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_81_Union_Cave_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_81_Union_Cave_Next::
	closemessage
	warp MAP_GSJOHTO_1_82_UNION_CAVE, 2, 4
	waitstate
	release
	end
GSJohto_1_81_Union_Cave_Text:
	.string "Johto 1.81: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
