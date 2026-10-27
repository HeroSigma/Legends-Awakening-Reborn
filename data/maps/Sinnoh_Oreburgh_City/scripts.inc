Sinnoh_Oreburgh_City_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperSinnoh_36_3_Oreburgh_City_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperSinnoh_36_3_Oreburgh_City_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperSinnoh_36_3_Oreburgh_City_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"

@ Project asset/travel notice.
HyperSinnoh_36_3_Oreburgh_City_EventScript_ReturnHoenn::
	lock
	faceplayer
	msgbox HyperSinnoh_36_3_Oreburgh_City_EventScript_ReturnHoenn_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_36_3_Oreburgh_City_EventScript_ReturnHoenn_Cancel
	warp MAP_SOOTOPOLIS_CITY_MYSTERY_EVENTS_HOUSE_1F, 10, 6
	waitstate
	release
	end
HyperSinnoh_36_3_Oreburgh_City_EventScript_ReturnHoenn_Cancel:
	release
	end
HyperSinnoh_36_3_Oreburgh_City_EventScript_ReturnHoenn_Text:
	.string "Would you like to return to Hoenn?$"
