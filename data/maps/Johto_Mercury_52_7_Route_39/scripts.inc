Johto_Mercury_52_7_Route_39_MapScripts::
	.byte 0

Johto_Mercury_52_7_Route_39_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_52_7_Route_39_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_52_7_Route_39_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_52_7_Route_39_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_10_17_ECRUTEAK_CITY, 3, 1
	waitstate
	release
	end
Johto_Mercury_52_7_Route_39_Inspect_Text:
	.string "Mercury Johto 52.7. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
