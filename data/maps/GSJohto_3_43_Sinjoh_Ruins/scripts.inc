GSJohto_3_43_Sinjoh_Ruins_MapScripts::
	.byte 0

GSJohto_3_43_Sinjoh_Ruins_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_43_Sinjoh_Ruins_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_43_Sinjoh_Ruins_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_43_Sinjoh_Ruins_Next::
	closemessage
	warp MAP_GSJOHTO_3_44_MT_SILVER, 51, 10
	waitstate
	release
	end
GSJohto_3_43_Sinjoh_Ruins_Text:
	.string "Johto 3.43: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
