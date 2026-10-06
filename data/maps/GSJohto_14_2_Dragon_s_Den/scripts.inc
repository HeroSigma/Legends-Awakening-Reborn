GSJohto_14_2_Dragon_s_Den_MapScripts::
	.byte 0

GSJohto_14_2_Dragon_s_Den_Inspect::
	lock
	faceplayer
	msgbox GSJohto_14_2_Dragon_s_Den_Text, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, GSJohto_14_2_Dragon_s_Den_Next
	closemessage
	warp MAP_LITTLEROOT_TOWN, 10, 17
	waitstate
	release
	end
GSJohto_14_2_Dragon_s_Den_Next::
	closemessage
	warp MAP_GSJOHTO_14_3_BLACKTHORN_CITY, 18, 33
	waitstate
	release
	end
GSJohto_14_2_Dragon_s_Den_Text:
	.string "Johto 14.2: under construction.\n"
	.string "YES: next map. NO: Littleroot.$"
