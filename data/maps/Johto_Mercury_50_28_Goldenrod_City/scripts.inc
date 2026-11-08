Johto_Mercury_50_28_Goldenrod_City_MapScripts::
	.byte 0

Johto_Mercury_50_28_Goldenrod_City_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_50_28_Goldenrod_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_50_28_Goldenrod_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_50_28_Goldenrod_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_9_2_GOLDENROD_CITY, 3, 5
	waitstate
	release
	end
Johto_Mercury_50_28_Goldenrod_City_Inspect_Text:
	.string "Mercury Johto 50.28. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
