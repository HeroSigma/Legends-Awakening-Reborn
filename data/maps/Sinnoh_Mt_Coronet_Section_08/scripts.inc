Sinnoh_Mt_Coronet_Section_08_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_36_88_Mt_Coronet_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_36_88_Mt_Coronet_EventScript_Construction_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_36_88_Mt_Coronet_EventScript_Construction_Cancel
	warp MAP_HYPERSINNOH_36_91_MT_CORONET, 5
	waitstate
	release
	end
HyperSinnoh_36_88_Mt_Coronet_EventScript_Construction_Cancel:
	release
	end
HyperSinnoh_36_88_Mt_Coronet_EventScript_Construction_Text:
	.string "This passage is under construction.\pWould you like to inspect beyond it?$"
