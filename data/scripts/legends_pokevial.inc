@ Three-dose field healing. Persistent state uses one existing unused var/flag.
LegendsPokevial_Use::
    lockall
    setspeaker SP_NAME_NONE
    special LegendsPokevialPrepare
    goto_if_eq VAR_RESULT, 1, LegendsPokevial_Empty
    goto_if_eq VAR_RESULT, 2, LegendsPokevial_Healthy
    goto_if_eq VAR_RESULT, 3, LegendsPokevial_End
    msgbox LegendsPokevial_Text_Confirm, MSGBOX_YESNO
    goto_if_ne VAR_RESULT, YES, LegendsPokevial_End
    special LegendsPokevialHeal
    goto_if_ne VAR_RESULT, 0, LegendsPokevial_End
    playfanfare MUS_HEAL
    msgbox LegendsPokevial_Text_Healed, MSGBOX_DEFAULT
    waitfanfare
    goto LegendsPokevial_End
LegendsPokevial_Empty:
    msgbox LegendsPokevial_Text_Empty, MSGBOX_DEFAULT
    goto LegendsPokevial_End
LegendsPokevial_Healthy:
    msgbox LegendsPokevial_Text_Healthy, MSGBOX_DEFAULT
LegendsPokevial_End:
    releaseall
    end

@ Called after the Woods rescue and at Devon reception for already-completed saves.
LegendsPokevial_Reward::
    goto_if_set FLAG_LA_POKEVIAL_RECEIVED, LegendsPokevial_Return
    goto_if_eq VAR_PETALBURG_WOODS_STATE, 0, LegendsPokevial_Return
LegendsPokevial_GiveReward:
    setspeaker SP_NAME_DEVON_RESEARCHER
    msgbox LegendsPokevial_Text_Reward, MSGBOX_DEFAULT
    setspeaker SP_NAME_NONE
    giveitem ITEM_POKEVIAL
    goto_if_eq VAR_RESULT, FALSE, LegendsPokevial_NoRoom
    special LegendsPokevialGrant
    setspeaker SP_NAME_DEVON_RESEARCHER
    msgbox LegendsPokevial_Text_Explain, MSGBOX_DEFAULT
    setspeaker SP_NAME_NONE
LegendsPokevial_Return:
    return
LegendsPokevial_NoRoom:
    msgbox LegendsPokevial_Text_NoRoom, MSGBOX_DEFAULT
    return

LegendsPokevial_Text_Confirm:
    .string "Pokévial charges: {STR_VAR_1}/3.\nUse one to fully heal your party?$"
LegendsPokevial_Text_Healed:
    .string "Your party is fully restored!\nPokévial charges remaining: {STR_VAR_1}/3.$"
LegendsPokevial_Text_Empty:
    .string "The Pokévial is empty.\pHeal at a POKéMON CENTER or rest stop\nto refill its three charges.$"
LegendsPokevial_Text_Healthy:
    .string "Your party is already fully rested.\nNo charge was used.$"
LegendsPokevial_Text_Reward:
    .string "For protecting us in PETALBURG WOODS,\nplease take this Pokévial.\pIt's a joint DEVON and SILPH prototype\nfor TRAINERS working far from town.$"
LegendsPokevial_Text_Explain:
    .string "One charge restores your whole party,\nincluding fainted partners and PP.\pIt holds three charges. A POKéMON\nCENTER or rest stop will refill it.\pUse it from your KEY ITEMS pocket,\nor register it for quick access.\pSave those charges for when you need\nthem. It cannot be used in battle.$"
LegendsPokevial_Text_NoRoom:
    .string "Make room for a KEY ITEM, then speak\nto reception at DEVON to collect it.$"
