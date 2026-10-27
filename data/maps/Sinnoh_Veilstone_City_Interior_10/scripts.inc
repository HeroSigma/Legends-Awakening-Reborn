Sinnoh_Veilstone_City_Interior_10_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_37_70_Veilstone_City_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_37_70_Veilstone_City_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_37_70_Veilstone_City_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
