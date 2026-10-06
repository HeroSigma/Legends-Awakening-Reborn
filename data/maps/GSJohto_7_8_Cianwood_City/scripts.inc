GSJohto_7_8_Cianwood_City_MapScripts::
	.byte 0

GSJohto_7_8_Cianwood_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_7_8_Cianwood_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_7_8_Cianwood_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_7_8_Cianwood_City_Next::
	closemessage
	warp MAP_GSJOHTO_7_9_AZALEA_TOWN, 5, 4
	waitstate
	release
	end
GSJohto_7_8_Cianwood_City_Text:
	.string "Johto 7.8: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
