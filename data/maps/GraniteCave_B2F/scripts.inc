GraniteCave_B2F_MapScripts::
	.byte 0


@ Project-owned reservation; no donor gameplay, flags or warp destination.
GraniteCave_B2F_EventScript_HyperConstruction_1::
	lock
	faceplayer
	msgbox GraniteCave_B2F_Text_HyperConstruction_1, MSGBOX_DEFAULT
	release
	end

GraniteCave_B2F_Text_HyperConstruction_1:
	.string "Ultra Space is\n"
	.string "under construction.\p"
	.string "Please check back later!$"
