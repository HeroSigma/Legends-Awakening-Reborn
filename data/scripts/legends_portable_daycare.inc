@ No map actors or warps: reuse the native daycare's shared pair and egg.
LegendsDaycare_Remote::
	lockall
	goto_if_unset FLAG_RETURNED_DEVON_GOODS, LegendsDaycare_Locked
	goto_if_unset FLAG_RECEIVED_POKENAV, LegendsDaycare_Locked
	goto_if_unset FLAG_LANDMARK_POKEMON_DAYCARE, LegendsDaycare_NotRegistered
	msgbox LegendsDaycare_Text_Manage, MSGBOX_YESNO
	goto_if_ne VAR_RESULT, YES, LegendsDaycare_AskEgg
	setvar VAR_0x8008, 1
	goto LegendsDaycare_ParentService
LegendsDaycare_AskEgg:
	msgbox LegendsDaycare_Text_Collect, MSGBOX_YESNO
	goto_if_ne VAR_RESULT, YES, LegendsDaycare_Exit
	goto LegendsDaycare_EggService
LegendsDaycare_Locked:
	msgbox LegendsDaycare_Text_Locked, MSGBOX_DEFAULT
	goto LegendsDaycare_Exit
LegendsDaycare_NotRegistered:
	msgbox LegendsDaycare_Text_Register, MSGBOX_DEFAULT
LegendsDaycare_Exit:
	releaseall
	end
LegendsDaycare_Text_Manage:
	.string "DAY-CARE remote connection.\p"
	.string "Manage the POKéMON we are raising?\n"
	.string "Select NO to check for an EGG.$"
LegendsDaycare_Text_Collect:
	.string "Check the DAY-CARE for an EGG?$"
LegendsDaycare_Text_Locked:
	.string "Devon's remote nursery service\n"
	.string "is not available yet.$"
LegendsDaycare_Text_Register:
	.string "Visit the Route 117 DAY-CARE first\n"
	.string "to register for remote care.$"
