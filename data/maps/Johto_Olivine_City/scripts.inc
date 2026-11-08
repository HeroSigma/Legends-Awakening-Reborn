Johto_Olivine_City_MapScripts::
	.byte 0

Johto_Olivine_City_Inspect::
	lock
	faceplayer
	msgbox Johto_Olivine_City_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Olivine_City_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Olivine_City_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_11_7_OLIVINE_CITY, 3, 9
	waitstate
	release
	end
Johto_Olivine_City_Inspect_Text:
	.string "Mercury Johto 49.10. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
