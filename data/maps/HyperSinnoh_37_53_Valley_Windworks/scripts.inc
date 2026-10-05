HyperSinnoh_37_53_Valley_Windworks_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_37_53_Valley_Windworks_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_37_53_Valley_Windworks_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_37_53_Valley_Windworks_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
