Johto_Ice_Path_Section_03_MapScripts::
	.byte 0

Johto_Ice_Path_Section_03_Inspect::
	lock
	faceplayer
	msgbox Johto_Ice_Path_Section_03_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Ice_Path_Section_03_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Ice_Path_Section_03_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_39_VICTORY_ROAD, 12, 9
	waitstate
	release
	end
Johto_Ice_Path_Section_03_Inspect_Text:
	.string "Mercury Johto 53.7. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
