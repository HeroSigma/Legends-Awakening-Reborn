Sinnoh_Sinnoh_Region_Interior_01_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_37_95_Sinnoh_Region_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_37_95_Sinnoh_Region_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_37_95_Sinnoh_Region_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
