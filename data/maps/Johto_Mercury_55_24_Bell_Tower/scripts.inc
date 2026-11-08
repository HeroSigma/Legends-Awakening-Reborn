Johto_Mercury_55_24_Bell_Tower_MapScripts::
	.byte 0

Johto_Mercury_55_24_Bell_Tower_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_55_24_Bell_Tower_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_55_24_Bell_Tower_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_55_24_Bell_Tower_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_93_BELL_TOWER, 15, 5
	waitstate
	release
	end
Johto_Mercury_55_24_Bell_Tower_Inspect_Text:
	.string "Mercury Johto 55.24. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
