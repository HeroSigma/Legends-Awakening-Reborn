HyperHoenn_26_59_Champion_Island_MapScripts::
	.byte 0

@ Project asset/travel notice.
HyperHoenn_26_59_Champion_Island_EventScript_Construction::
	lock
	faceplayer
	msgbox HyperHoenn_26_59_Champion_Island_EventScript_Construction_Text, MSGBOX_DEFAULT
	release
	end
HyperHoenn_26_59_Champion_Island_EventScript_Construction_Text:
	.string "This area is under construction.\pPlease check back later!$"
