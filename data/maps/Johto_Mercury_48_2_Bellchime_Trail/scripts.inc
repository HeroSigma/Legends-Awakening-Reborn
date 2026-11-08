Johto_Mercury_48_2_Bellchime_Trail_MapScripts::
	.byte 0

Johto_Mercury_48_2_Bellchime_Trail_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_48_2_Bellchime_Trail_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_48_2_Bellchime_Trail_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_48_2_Bellchime_Trail_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_59_BURNED_TOWER, 12, 19
	waitstate
	release
	end
Johto_Mercury_48_2_Bellchime_Trail_Inspect_Text:
	.string "Mercury Johto 48.2. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
