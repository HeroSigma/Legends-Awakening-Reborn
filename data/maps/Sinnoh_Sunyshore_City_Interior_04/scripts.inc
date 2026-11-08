Sinnoh_Sunyshore_City_Interior_04_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_37_92_Sunyshore_City_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_37_92_Sunyshore_City_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_37_92_Sunyshore_City_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
