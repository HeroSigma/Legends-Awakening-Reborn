AbandonedShip_Underwater1_MapScripts::
	map_script MAP_SCRIPT_ON_RESUME, AbandonedShip_Underwater1_OnResume
	.byte 0

AbandonedShip_Underwater1_OnResume:
	setdivewarp MAP_ABANDONED_SHIP_HIDDEN_FLOOR_CORRIDORS, 0, 10
	end


@ Project construction notice; no donor gameplay.
AbandonedShip_Underwater1_EventScript_HyperConstruction_Canary6_1::
	lock
	faceplayer
	msgbox AbandonedShip_Underwater1_EventScript_HyperConstruction_Canary6_1_Text, MSGBOX_DEFAULT
	release
	end
AbandonedShip_Underwater1_EventScript_HyperConstruction_Canary6_1_Text:
	.string "This area is under construction.\p"
	.string "Please check back later!$"

@ Project construction notice; no donor gameplay.
AbandonedShip_Underwater1_EventScript_HyperConstruction_Canary6_2::
	lock
	faceplayer
	msgbox AbandonedShip_Underwater1_EventScript_HyperConstruction_Canary6_2_Text, MSGBOX_DEFAULT
	release
	end
AbandonedShip_Underwater1_EventScript_HyperConstruction_Canary6_2_Text:
	.string "This area is under construction.\p"
	.string "Please check back later!$"

@ Project construction notice; no donor gameplay.
AbandonedShip_Underwater1_EventScript_HyperConstruction_Canary6_3::
	lock
	faceplayer
	msgbox AbandonedShip_Underwater1_EventScript_HyperConstruction_Canary6_3_Text, MSGBOX_DEFAULT
	release
	end
AbandonedShip_Underwater1_EventScript_HyperConstruction_Canary6_3_Text:
	.string "This area is under construction.\p"
	.string "Please check back later!$"
