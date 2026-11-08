Johto_Mercury_3_106_Route_26_MapScripts::
	.byte 0

Johto_Mercury_3_106_Route_26_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_3_106_Route_26_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_3_106_Route_26_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_3_106_Route_26_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_82_UNION_CAVE, 18, 5
	waitstate
	release
	end
Johto_Mercury_3_106_Route_26_Inspect_Text:
	.string "Mercury Johto 3.106. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
