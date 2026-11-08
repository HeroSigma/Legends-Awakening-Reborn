Johto_Mercury_54_9_Dragon_s_Den_MapScripts::
	.byte 0

Johto_Mercury_54_9_Dragon_s_Den_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_54_9_Dragon_s_Den_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_54_9_Dragon_s_Den_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_54_9_Dragon_s_Den_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_54_11_GOLDENROD_CITY, 7, 4
	waitstate
	release
	end
Johto_Mercury_54_9_Dragon_s_Den_Inspect_Text:
	.string "Mercury Johto 54.9. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
