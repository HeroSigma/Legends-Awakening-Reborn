Johto_Burned_Tower_MapScripts::
	.byte 0

GSJohto_1_59_Burned_Tower_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_59_Burned_Tower_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_59_Burned_Tower_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_59_Burned_Tower_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_60_BURNED_TOWER, 14, 19
	waitstate
	release
	end
GSJohto_1_59_Burned_Tower_Inspect_Text:
	.string "Mercury Johto 48.3. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
