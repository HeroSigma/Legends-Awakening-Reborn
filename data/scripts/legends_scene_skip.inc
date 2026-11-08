@ Repeat-only prompts run at authored boundaries, with no live movement task.
@ Each caller owns a persistent viewed flag and a safe destination before battle.
LegendsScene_OfferSkip::
    setspeaker SP_NAME_NONE
    msgbox LegendsScene_Text_SkipConversation, MSGBOX_YESNO
    closemessage
    return

LegendsScene_Text_SkipConversation:
    .string "You've seen this conversation.\nSkip to the battle?$"
