Johto_Route_32_Interior_01_MapScripts::
	.byte 0

GSJohto_18_0_Route_32_Inspect::
	lock
	faceplayer
	msgbox GSJohto_18_0_Route_32_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_18_0_Route_32_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_18_0_Route_32_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_6_3_VIOLET_CITY, 3, 5
	waitstate
	release
	end
GSJohto_18_0_Route_32_Inspect_Text:
	.string "Mercury Johto 46.8. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
