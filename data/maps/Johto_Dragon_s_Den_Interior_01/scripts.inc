Johto_Dragon_s_Den_Interior_01_MapScripts::
	.byte 0

GSJohto_14_2_Dragon_s_Den_Inspect::
	lock
	faceplayer
	msgbox GSJohto_14_2_Dragon_s_Den_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_14_2_Dragon_s_Den_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_14_2_Dragon_s_Den_Inspect_Next::
	closemessage
	warp MAP_GSJOHTO_1_97_DRAGON_S_DEN, 2, 7
	waitstate
	release
	end
GSJohto_14_2_Dragon_s_Den_Inspect_Text:
	.string "Mercury Johto 54.1. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
