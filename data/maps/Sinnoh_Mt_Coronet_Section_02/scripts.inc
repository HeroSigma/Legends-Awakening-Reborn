Sinnoh_Mt_Coronet_Section_02_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_36_82_Mt_Coronet_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_36_82_Mt_Coronet_EventScript_Construction_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_36_82_Mt_Coronet_EventScript_Construction_Cancel
	warp MAP_HYPERSINNOH_36_35_ROUTE_216, 1
	waitstate
	release
	end
HyperSinnoh_36_82_Mt_Coronet_EventScript_Construction_Cancel:
	release
	end
HyperSinnoh_36_82_Mt_Coronet_EventScript_Construction_Text:
	.string "This passage is under construction.\pWould you like to inspect beyond it?$"
