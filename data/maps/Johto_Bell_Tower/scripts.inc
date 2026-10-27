Johto_Bell_Tower_MapScripts::
	.byte 0

GSJohto_1_93_Bell_Tower_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_93_Bell_Tower_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_93_Bell_Tower_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_93_Bell_Tower_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_55_26_BELL_TOWER, 8, 14
	waitstate
	release
	end
GSJohto_1_93_Bell_Tower_Inspect_Text:
	.string "Mercury Johto 55.25. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
