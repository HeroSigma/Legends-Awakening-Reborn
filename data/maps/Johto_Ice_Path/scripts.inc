Johto_Ice_Path_MapScripts::
	.byte 0

Johto_Ice_Path_Inspect::
	lock
	faceplayer
	msgbox Johto_Ice_Path_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Ice_Path_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Ice_Path_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_34_ICE_PATH, 18, 7
	waitstate
	release
	end
Johto_Ice_Path_Inspect_Text:
	.string "Mercury Johto 53.4. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
