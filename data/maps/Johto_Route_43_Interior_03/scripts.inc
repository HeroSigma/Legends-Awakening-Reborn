Johto_Route_43_Interior_03_MapScripts::
	.byte 0

GSJohto_24_1_Route_43_Inspect::
	lock
	faceplayer
	msgbox GSJohto_24_1_Route_43_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_24_1_Route_43_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_24_1_Route_43_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_44_14_GOLDENROD_CITY, 6, 6
	waitstate
	release
	end
GSJohto_24_1_Route_43_Inspect_Text:
	.string "Mercury Johto 44.13. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
