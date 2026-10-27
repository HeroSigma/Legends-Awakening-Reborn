Johto_Ice_Path_Section_01_MapScripts::
	.byte 0

Johto_Ice_Path_Section_01_Inspect::
	lock
	faceplayer
	msgbox Johto_Ice_Path_Section_01_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Ice_Path_Section_01_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Ice_Path_Section_01_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_35_ICE_PATH, 45, 4
	waitstate
	release
	end
Johto_Ice_Path_Section_01_Inspect_Text:
	.string "Mercury Johto 53.5. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
