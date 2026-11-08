Sinnoh_Spear_Pillar_Section_01_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_36_95_Spear_Pillar_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_36_95_Spear_Pillar_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_36_95_Spear_Pillar_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"

@ Project asset/travel notice.
HyperSinnoh_36_95_Spear_Pillar_EventScript_Inspect_36_92::
	lock
	faceplayer
	msgbox HyperSinnoh_36_95_Spear_Pillar_EventScript_Inspect_36_92_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_36_95_Spear_Pillar_EventScript_Inspect_36_92_Cancel
	warp MAP_HYPERSINNOH_36_92_MT_CORONET, 0
	waitstate
	release
	end
HyperSinnoh_36_95_Spear_Pillar_EventScript_Inspect_36_92_Cancel:
	release
	end
HyperSinnoh_36_95_Spear_Pillar_EventScript_Inspect_36_92_Text:
	.string "This annex is under construction.\pWould you like to inspect it?$"

@ Project asset/travel notice.
HyperSinnoh_36_95_Spear_Pillar_EventScript_Inspect_36_96::
	lock
	faceplayer
	msgbox HyperSinnoh_36_95_Spear_Pillar_EventScript_Inspect_36_96_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_36_95_Spear_Pillar_EventScript_Inspect_36_96_Cancel
	warp MAP_HYPERSINNOH_36_96_SPEAR_PILLAR, 0
	waitstate
	release
	end
HyperSinnoh_36_95_Spear_Pillar_EventScript_Inspect_36_96_Cancel:
	release
	end
HyperSinnoh_36_95_Spear_Pillar_EventScript_Inspect_36_96_Text:
	.string "This annex is under construction.\pWould you like to inspect it?$"
