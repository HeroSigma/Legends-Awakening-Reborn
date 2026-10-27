Johto_Route_48_MapScripts::
	.byte 0

GSJohto_3_38_Route_48_Inspect::
	lock
	faceplayer
	msgbox GSJohto_3_38_Route_48_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_3_38_Route_48_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_3_38_Route_48_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_56_27_CLIFFSIDE_TOWN, 43, 34
	waitstate
	release
	end
GSJohto_3_38_Route_48_Inspect_Text:
	.string "Mercury Johto 56.26. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
