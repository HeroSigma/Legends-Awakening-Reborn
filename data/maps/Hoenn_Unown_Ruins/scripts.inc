Hoenn_Unown_Ruins_MapScripts::
	.byte 0

@ Project-owned reservation; registered asset map, no donor gameplay.
HyperHoenn_34_46_Unown_Ruins_EventScript_HyperConstruction_Registered1::
	lock
	faceplayer
	msgbox HyperHoenn_34_46_Unown_Ruins_Text_HyperConstruction_Registered1, MSGBOX_DEFAULT
	release
	end

HyperHoenn_34_46_Unown_Ruins_Text_HyperConstruction_Registered1:
	.string "This area is under construction.\p"
	.string "Please check back later!$"
