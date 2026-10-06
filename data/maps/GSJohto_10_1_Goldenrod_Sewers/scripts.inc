GSJohto_10_1_Goldenrod_Sewers_MapScripts::
	.byte 0

GSJohto_10_1_Goldenrod_Sewers_Inspect::
	lock
	faceplayer
	msgbox GSJohto_10_1_Goldenrod_Sewers_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_10_1_Goldenrod_Sewers_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_10_1_Goldenrod_Sewers_Next::
	closemessage
	warp MAP_GSJOHTO_10_2_GOLDENROD_SEWERS, 9, 4
	waitstate
	release
	end
GSJohto_10_1_Goldenrod_Sewers_Text:
	.string "Johto 10.1: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
