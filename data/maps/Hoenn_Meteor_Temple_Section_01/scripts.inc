Hoenn_Meteor_Temple_Section_01_MapScripts::
	.byte 0

@ Project-owned reservation; registered asset map, no donor gameplay.
HyperHoenn_35_54_Meteor_Temple_EventScript_HyperConstruction_Registered1::
	lock
	faceplayer
	msgbox HyperHoenn_35_54_Meteor_Temple_Text_HyperConstruction_Registered1, MSGBOX_DEFAULT
	release
	end

HyperHoenn_35_54_Meteor_Temple_Text_HyperConstruction_Registered1:
	.string "This area is under construction.\p"
	.string "Please check back later!$"
