Hoenn_Meteor_Temple_Interior_01_MapScripts::
	.byte 0

@ Project-owned reservation; registered asset map, no donor gameplay.
HyperHoenn_34_17_Meteor_Temple_EventScript_HyperConstruction_Registered1::
	lock
	faceplayer
	msgbox HyperHoenn_34_17_Meteor_Temple_Text_HyperConstruction_Registered1, MSGBOX_DEFAULT
	release
	end

HyperHoenn_34_17_Meteor_Temple_Text_HyperConstruction_Registered1:
	.string "This area is under construction.\p"
	.string "Please check back later!$"
