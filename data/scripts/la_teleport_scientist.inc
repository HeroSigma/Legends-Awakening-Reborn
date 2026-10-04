@ Dev hub NPC: the Teleport Scientist.
@ Reusable across maps so any imported map can be tested from a
@ permanent hub (Littleroot for now).
@
@ Presents a list of destinations (menu defined in src/data/script_menu.h,
@ slot MULTI_UNUSED_19) and warps the player to the chosen one.
@
@ Destinations:
@   Nuvema Town -> (16,22)
@   Postwick    -> (15,24)

LA_TeleportScientist::
	lock
	faceplayer
	msgbox LA_Text_TeleportScientistIntro, MSGBOX_DEFAULT
	multichoice 2, 0, MULTI_UNUSED_19, FALSE
	goto_if_eq VAR_RESULT, 0, LA_TeleportScientist_WarpNuvema
	goto_if_eq VAR_RESULT, 1, LA_TeleportScientist_WarpPostwick
	@ 2 = CANCEL (or B button): just end the conversation.
	goto LA_TeleportScientist_Cancel

LA_TeleportScientist_WarpNuvema::
	closemessage
	warp MAP_AMAP_3_0_NUVEMA_TOWN, 16, 22
	waitstate
	release
	end

LA_TeleportScientist_WarpPostwick::
	closemessage
	warp MAP_AMAP_3_0_POSTWICK, 15, 24
	waitstate
	release
	end

LA_TeleportScientist_Cancel::
	closemessage
	release
	end

LA_Text_TeleportScientistIntro:
	.string "SCIENTIST: Ah! Another volunteer for my\n"
	.string "spatial instability study.\p"
	.string "I can send you to a region my\n"
	.string "equipment imported from another world.\p"
	.string "Where shall I send you?$"
