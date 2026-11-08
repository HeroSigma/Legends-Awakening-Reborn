Johto_Mercury_46_5_Violet_City_MapScripts::
	.byte 0

Johto_Mercury_46_5_Violet_City_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_46_5_Violet_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_46_5_Violet_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_46_5_Violet_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_6_2_VIOLET_CITY, 7, 17
	waitstate
	release
	end
Johto_Mercury_46_5_Violet_City_Inspect_Text:
	.string "Mercury Johto 46.5. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
