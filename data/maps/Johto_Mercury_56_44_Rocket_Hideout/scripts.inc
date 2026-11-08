Johto_Mercury_56_44_Rocket_Hideout_MapScripts::
	.byte 0

Johto_Mercury_56_44_Rocket_Hideout_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_56_44_Rocket_Hideout_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_56_44_Rocket_Hideout_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_56_44_Rocket_Hideout_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_56_45_ROCKET_HIDEOUT, 46, 9
	waitstate
	release
	end
Johto_Mercury_56_44_Rocket_Hideout_Inspect_Text:
	.string "Mercury Johto 56.44. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
