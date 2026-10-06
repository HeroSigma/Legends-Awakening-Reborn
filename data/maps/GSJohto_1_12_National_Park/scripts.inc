GSJohto_1_12_National_Park_MapScripts::
	.byte 0

GSJohto_1_12_National_Park_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_12_National_Park_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_12_National_Park_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_12_National_Park_Next::
	closemessage
	warp MAP_GSJOHTO_1_18_S_S_ANNE, 3, 4
	waitstate
	release
	end
GSJohto_1_12_National_Park_Text:
	.string "Johto 1.12: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
