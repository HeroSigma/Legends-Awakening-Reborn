GSJohto_1_82_Union_Cave_MapScripts::
	.byte 0

GSJohto_1_82_Union_Cave_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_82_Union_Cave_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_82_Union_Cave_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_82_Union_Cave_Next::
	closemessage
	warp MAP_GSJOHTO_1_86_WHIRL_ISLANDS, 31, 5
	waitstate
	release
	end
GSJohto_1_82_Union_Cave_Text:
	.string "Johto 1.82: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
