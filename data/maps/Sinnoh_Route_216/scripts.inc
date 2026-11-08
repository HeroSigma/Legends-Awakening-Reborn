Sinnoh_Route_216_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_36_35_Route_216_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_36_35_Route_216_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_36_35_Route_216_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
