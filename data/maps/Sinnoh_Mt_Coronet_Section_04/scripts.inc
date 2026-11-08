Sinnoh_Mt_Coronet_Section_04_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_36_84_Mt_Coronet_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_36_84_Mt_Coronet_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_36_84_Mt_Coronet_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
