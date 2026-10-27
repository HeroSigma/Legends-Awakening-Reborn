Johto_National_Park_MapScripts::
	.byte 0

GSJohto_1_12_National_Park_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_12_National_Park_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_12_National_Park_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_12_National_Park_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_2_DARK_CAVE, 15, 7
	waitstate
	release
	end
GSJohto_1_12_National_Park_Inspect_Text:
	.string "Mercury Johto 1.124. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
