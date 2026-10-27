Johto_Ice_Path_Section_02_MapScripts::
	.byte 0

Johto_Ice_Path_Section_02_Inspect::
	lock
	faceplayer
	msgbox Johto_Ice_Path_Section_02_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Ice_Path_Section_02_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Ice_Path_Section_02_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_67_ICE_PATH, 19, 4
	waitstate
	release
	end
Johto_Ice_Path_Section_02_Inspect_Text:
	.string "Mercury Johto 53.6. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
