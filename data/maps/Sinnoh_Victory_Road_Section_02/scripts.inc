Sinnoh_Victory_Road_Section_02_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_36_73_Victory_Road_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_36_73_Victory_Road_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_36_73_Victory_Road_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
