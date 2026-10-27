Johto_Sprout_Tower_MapScripts::
	.byte 0

GSJohto_1_37_Sprout_Tower_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_37_Sprout_Tower_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_37_Sprout_Tower_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_37_Sprout_Tower_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_1_89_SPROUT_TOWER, 20, 7
	waitstate
	release
	end
GSJohto_1_37_Sprout_Tower_Inspect_Text:
	.string "Mercury Johto 1.88. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
