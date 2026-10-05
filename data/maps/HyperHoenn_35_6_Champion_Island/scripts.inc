HyperHoenn_35_6_Champion_Island_MapScripts::
	.byte 0

@ Project-owned reservation; registered asset map, no donor gameplay.
HyperHoenn_35_6_Champion_Island_EventScript_HyperConstruction_Registered1::
	lock
	faceplayer
	msgbox HyperHoenn_35_6_Champion_Island_Text_HyperConstruction_Registered1, MSGBOX_DEFAULT
	release
	end

HyperHoenn_35_6_Champion_Island_Text_HyperConstruction_Registered1:
	.string "This area is under construction.\p"
	.string "Please check back later!$"

@ Project asset/travel notice.
HyperHoenn_35_6_Champion_Island_EventScript_Inspect_26_59::
	lock
	faceplayer
	msgbox HyperHoenn_35_6_Champion_Island_EventScript_Inspect_26_59_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, HyperHoenn_35_6_Champion_Island_EventScript_Inspect_26_59_Cancel
	warp MAP_HYPERHOENN_26_59_CHAMPION_ISLAND, 0
	waitstate
	release
	end
HyperHoenn_35_6_Champion_Island_EventScript_Inspect_26_59_Cancel:
	release
	end
HyperHoenn_35_6_Champion_Island_EventScript_Inspect_26_59_Text:
	.string "This annex is under construction.\pWould you like to inspect it?$"
