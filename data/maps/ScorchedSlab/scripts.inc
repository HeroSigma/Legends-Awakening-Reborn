ScorchedSlab_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, ScorchedSlab_OnTransition
	.byte 0

ScorchedSlab_OnTransition:
	setflag FLAG_LANDMARK_SCORCHED_SLAB
	end


@ Project construction notice; no donor gameplay.
ScorchedSlab_EventScript_HyperConstruction_Canary7_1::
	lock
	faceplayer
	msgbox ScorchedSlab_EventScript_HyperConstruction_Canary7_1_Text, MSGBOX_DEFAULT
	release
	end
ScorchedSlab_EventScript_HyperConstruction_Canary7_1_Text:
	.string "This area is under construction.\p"
	.string "Please check back later!$"
