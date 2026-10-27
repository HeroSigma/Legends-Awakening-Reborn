Hoenn_Outer_Space_Section_02_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperHoenn_34_72_Outer_Space_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperHoenn_34_72_Outer_Space_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperHoenn_34_72_Outer_Space_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
