MeteorFalls_B1F_2R_MapScripts::
	.byte 0


@ Project-owned reservation; registered asset map, no donor gameplay.
MeteorFalls_B1F_2R_EventScript_HyperConstruction_Registered1::
	lock
	faceplayer
	msgbox MeteorFalls_B1F_2R_Text_HyperConstruction_Registered1, MSGBOX_DEFAULT
	release
	end

MeteorFalls_B1F_2R_Text_HyperConstruction_Registered1:
	.string "This area is under construction.\p"
	.string "Please check back later!$"
