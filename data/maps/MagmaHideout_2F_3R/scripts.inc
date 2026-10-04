MagmaHideout_2F_3R_MapScripts::
	.byte 0


@ Project-owned reservation; registered asset map, no donor gameplay.
MagmaHideout_2F_3R_EventScript_HyperConstruction_Registered1::
	lock
	faceplayer
	msgbox MagmaHideout_2F_3R_Text_HyperConstruction_Registered1, MSGBOX_DEFAULT
	release
	end

MagmaHideout_2F_3R_Text_HyperConstruction_Registered1:
	.string "This area is under construction.\p"
	.string "Please check back later!$"
