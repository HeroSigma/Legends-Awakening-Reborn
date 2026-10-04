Underwater_SootopolisCity_MapScripts::
	map_script MAP_SCRIPT_ON_RESUME, Underwater_SootopolisCity_OnResume
	.byte 0

Underwater_SootopolisCity_OnResume:
	setdivewarp MAP_SOOTOPOLIS_CITY, 29, 53
	end


@ Project construction notice; no donor gameplay.
Underwater_SootopolisCity_EventScript_HyperConstruction_Canary9_1::
	lock
	faceplayer
	msgbox Underwater_SootopolisCity_EventScript_HyperConstruction_Canary9_1_Text, MSGBOX_DEFAULT
	release
	end
Underwater_SootopolisCity_EventScript_HyperConstruction_Canary9_1_Text:
	.string "This area is under construction.\p"
	.string "Please check back later!$"
