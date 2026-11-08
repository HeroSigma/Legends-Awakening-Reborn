Johto_Mercury_52_12_Bellchime_Trail_MapScripts::
	.byte 0

Johto_Mercury_52_12_Bellchime_Trail_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_52_12_Bellchime_Trail_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_52_12_Bellchime_Trail_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_52_12_Bellchime_Trail_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_52_35_PALLET_TOWN, 4, 12
	waitstate
	release
	end
Johto_Mercury_52_12_Bellchime_Trail_Inspect_Text:
	.string "Mercury Johto 52.12. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
