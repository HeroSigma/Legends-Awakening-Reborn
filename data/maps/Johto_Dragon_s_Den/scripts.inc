Johto_Dragon_s_Den_MapScripts::
	.byte 0

GSJohto_1_97_Dragon_s_Den_Inspect::
	lock
	faceplayer
	msgbox GSJohto_1_97_Dragon_s_Den_Inspect_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_1_97_Dragon_s_Den_Inspect_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_1_97_Dragon_s_Den_Inspect_Next::
	closemessage
	warp MAP_JOHTO_MERCURY_54_3_DRAGON_S_DEN, 5, 14
	waitstate
	release
	end
GSJohto_1_97_Dragon_s_Den_Inspect_Text:
	.string "Mercury Johto 54.2. Under construction.\p"
	.string "YES: next. NO: Littleroot.$"
