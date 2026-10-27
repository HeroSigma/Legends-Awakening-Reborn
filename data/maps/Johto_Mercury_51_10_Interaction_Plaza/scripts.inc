Johto_Mercury_51_10_Interaction_Plaza_MapScripts::
	.byte 0

Johto_Mercury_51_10_Interaction_Plaza_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_51_10_Interaction_Plaza_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_51_10_Interaction_Plaza_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_51_10_Interaction_Plaza_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_52_2_SPROUT_TOWER, 10, 12
	waitstate
	release
	end
Johto_Mercury_51_10_Interaction_Plaza_Inspect_Text:
	.string "Mercury Johto 51.10. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
