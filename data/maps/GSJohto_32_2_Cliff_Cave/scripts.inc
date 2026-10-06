GSJohto_32_2_Cliff_Cave_MapScripts::
	.byte 0

GSJohto_32_2_Cliff_Cave_Inspect::
	lock
	faceplayer
	msgbox GSJohto_32_2_Cliff_Cave_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_32_2_Cliff_Cave_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_32_2_Cliff_Cave_Next::
	closemessage
	warp MAP_GSJOHTO_32_3_CLIFF_CAVE, 4, 3
	waitstate
	release
	end
GSJohto_32_2_Cliff_Cave_Text:
	.string "Johto 32.2: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
