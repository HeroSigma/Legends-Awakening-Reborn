HyperSinnoh_26_67_Canalave_City_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_26_67_Canalave_City_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_26_67_Canalave_City_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_26_67_Canalave_City_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
