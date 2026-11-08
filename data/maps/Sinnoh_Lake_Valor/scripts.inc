Sinnoh_Lake_Valor_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_36_44_Lake_Valor_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_36_44_Lake_Valor_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_36_44_Lake_Valor_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
