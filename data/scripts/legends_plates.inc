@ Blank Plate research; guardian actors/battles are wired in the SOS feature.
LegendsPlates_BirchOffer::
    lockall
    faceplayer
    setspeaker SP_NAME_BIRCH
    msgbox LegendsPlates_Text_Offer, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsPlates_Text_Stirring, MSGBOX_DEFAULT
    setspeaker SP_NAME_BIRCH
    msgbox LegendsPlates_Text_Listen, MSGBOX_YESNO
    goto_if_eq VAR_RESULT, NO, LegendsPlates_Decline
    special LegendsPlates_BeginResearch
    goto_if_ne VAR_RESULT, 1, LegendsPlates_Full
    setspeaker SP_NAME_NONE
    playfanfare MUS_OBTAIN_ITEM
    msgbox LegendsPlates_Text_Received, MSGBOX_DEFAULT
    waitfanfare
    setspeaker SP_NAME_PLAYER
    msgbox LegendsPlates_Text_Promise, MSGBOX_DEFAULT
    setspeaker SP_NAME_BIRCH
    msgbox LegendsPlates_Text_Research, MSGBOX_DEFAULT
    goto LegendsPlates_End
LegendsPlates_Decline:
    msgbox LegendsPlates_Text_Later, MSGBOX_DEFAULT
    goto LegendsPlates_End
LegendsPlates_Full:
    setspeaker SP_NAME_BIRCH
    msgbox LegendsPlates_Text_Full, MSGBOX_DEFAULT
    goto LegendsPlates_End
LegendsPlates_BirchAwakening::
    lockall
    faceplayer
    setspeaker SP_NAME_PLAYER
    msgbox LegendsPlates_Text_Return, MSGBOX_DEFAULT
    setspeaker SP_NAME_BIRCH
    msgbox LegendsPlates_Text_Whole, MSGBOX_DEFAULT
    special LegendsPlates_Awaken
    goto_if_ne VAR_RESULT, 1, LegendsPlates_Full
    setspeaker SP_NAME_NONE
    playfanfare MUS_OBTAIN_ITEM
    msgbox LegendsPlates_Text_Awakened, MSGBOX_DEFAULT
    waitfanfare
    setspeaker SP_NAME_PLAYER
    msgbox LegendsPlates_Text_Answer, MSGBOX_DEFAULT
    setspeaker SP_NAME_BIRCH
    msgbox LegendsPlates_Text_Bond, MSGBOX_DEFAULT
LegendsPlates_End:
    setspeaker SP_NAME_NONE
    releaseall
    end
LegendsPlates_Text_Offer:
    .string "There is another find I'd like you\nto examine. We call it a Blank Plate.\pIt was recovered near a rift, but\nit gives our instruments no reading.$"
LegendsPlates_Text_Stirring:
    .string "Wait... There was a pulse just now.\nDid you feel that?\pIt feels familiar. I can't explain\nwhy, but it doesn't feel empty.$"
LegendsPlates_Text_Listen:
    .string "I felt nothing. Perhaps it responds\nto you in a way we can't measure.\pWould you carry it? We can record\nany new leads in your quest log.$"
LegendsPlates_Text_Received:
    .string "{PLAYER} received the Blank Plate!\pThe Silent Plate was added\nto the quest log.$"
LegendsPlates_Text_Promise:
    .string "I'll keep it with me. If I feel\nthat pulse again, I'll follow it.$"
LegendsPlates_Text_Research:
    .string "Carefully, {PLAYER}. Record what you\nfind before drawing conclusions.\pUse the Plate from your Bag to\ncheck its awakened resonances.$"
LegendsPlates_Text_Later:
    .string "Of course. I'll keep it safe here.\nAsk me when you feel ready.$"
LegendsPlates_Text_Full:
    .string "Bring the Plate and make room in\nyour Bag, then speak to me again.$"
LegendsPlates_Text_Return:
    .string "Professor, all seventeen patterns\nare awake. Listen...\pThat pulse is coming from every\nPlate. They're answering this one.$"
LegendsPlates_Text_Whole:
    .string "And the blank surface is changing.\nHold it steady, {PLAYER}.$"
LegendsPlates_Text_Awakened:
    .string "The Blank Plate became\nthe Legend Plate!$"
LegendsPlates_Text_Answer:
    .string "They're all here. I can feel them.\nBut this isn't where it ends.\pSomething is still waiting\nfor me to understand.$"
LegendsPlates_Text_Bond:
    .string "Then we'll keep looking together.\nThis is more than an artifact.\pWhatever connects you to it,\nyou don't have to face it alone.$"
