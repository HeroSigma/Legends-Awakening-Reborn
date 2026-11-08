Johto_Union_Cave_Section_03_MapScripts::
	.byte 0

GSJohto_1_82_Union_Cave_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_82_Union_Cave_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_82_Union_Cave_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_82_Union_Cave_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_7_8_CIANWOOD_CITY, 4, 6
	waitstate
	release
	end
GSJohto_1_82_Union_Cave_Inspect_Text:
	.string "Mercury Johto 3.107. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
