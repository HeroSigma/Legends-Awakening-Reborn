GSJohto_9_4_Cianwood_City_MapScripts::
	.byte 0

GSJohto_9_4_Cianwood_City_Inspect::
	lock
	faceplayer
	msgbox GSJohto_9_4_Cianwood_City_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_9_4_Cianwood_City_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_9_4_Cianwood_City_Next::
	closemessage
	warp MAP_GSJOHTO_9_5_ECRUTEAK_CITY, 9, 4
	waitstate
	release
	end
GSJohto_9_4_Cianwood_City_Text:
	.string "Johto 9.4: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
