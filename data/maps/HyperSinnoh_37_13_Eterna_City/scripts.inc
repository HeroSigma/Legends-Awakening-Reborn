HyperSinnoh_37_13_Eterna_City_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_37_13_Eterna_City_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_37_13_Eterna_City_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_37_13_Eterna_City_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"

@ Project asset/travel notice.
HyperSinnoh_37_13_Eterna_City_EventScript_HeldEntrance_1::
	lock
	faceplayer
	msgbox HyperSinnoh_37_13_Eterna_City_EventScript_HeldEntrance_1_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_37_13_Eterna_City_EventScript_HeldEntrance_1_Text:
	.string "This entrance is under construction.\pPlease check back later!$"
