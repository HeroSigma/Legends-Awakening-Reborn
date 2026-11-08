Sinnoh_Route_210_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_35_16_Route_210_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_35_16_Route_210_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_35_16_Route_210_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
