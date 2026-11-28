Common_EventScript_FindItem::
	callnative GetItemBallIdAndAmountFromTemplate
	goto_if_ne VAR_RESULT, ITEM_MASTER_BALL, Common_EventScript_FindItemReady
	goto_if_unset FLAG_SYS_GAME_CLEAR, Common_EventScript_MasterBallSealed
Common_EventScript_FindItemReady:
	finditem VAR_RESULT VAR_0x8009
	end

Common_EventScript_MasterBallSealed:
    lockall
    msgbox Common_Text_MasterBallSealed, MSGBOX_DEFAULT
    releaseall
    end
Common_Text_MasterBallSealed:
    .string "A League seal secures this case.\nIt opens only for a Champion.$"
