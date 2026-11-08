Johto_Route_43_MapScripts::
	.byte 0

GSJohto_3_33_Route_43_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_33_Route_43_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_33_Route_43_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_33_Route_43_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_3_11_LAKE_OF_RAGE, 13, 8
	waitstate
	release
	end
GSJohto_3_33_Route_43_Inspect_Text:
	.string "Mercury Johto 3.99. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
