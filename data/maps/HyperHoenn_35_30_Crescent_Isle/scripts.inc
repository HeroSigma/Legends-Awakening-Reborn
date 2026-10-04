HyperHoenn_35_30_Crescent_Isle_MapScripts::
	.byte 0

@ Project-owned reservation; registered asset map, no donor gameplay.
HyperHoenn_35_30_Crescent_Isle_EventScript_HyperConstruction_Registered1::
	lock
	faceplayer
	msgbox HyperHoenn_35_30_Crescent_Isle_Text_HyperConstruction_Registered1, MSGBOX_DEFAULT
	release
	end

HyperHoenn_35_30_Crescent_Isle_Text_HyperConstruction_Registered1:
	.string "This area is under construction.\p"
	.string "Please check back later!$"
