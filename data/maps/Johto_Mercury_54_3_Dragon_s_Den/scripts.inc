Johto_Mercury_54_3_Dragon_s_Den_MapScripts::
	.byte 0

Johto_Mercury_54_3_Dragon_s_Den_Inspect::
	lock
	faceplayer
	msgbox Johto_Mercury_54_3_Dragon_s_Den_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Johto_Mercury_54_3_Dragon_s_Den_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
Johto_Mercury_54_3_Dragon_s_Den_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_14_5_BLACKTHORN_CITY, 5, 6
	waitstate
	release
	end
Johto_Mercury_54_3_Dragon_s_Den_Inspect_Text:
	.string "Mercury Johto 54.3. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
