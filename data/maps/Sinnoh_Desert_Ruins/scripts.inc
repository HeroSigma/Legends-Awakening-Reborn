Sinnoh_Desert_Ruins_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_35_88_Desert_Ruins_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_35_88_Desert_Ruins_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_35_88_Desert_Ruins_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
