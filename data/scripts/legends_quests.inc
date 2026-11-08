@ Quest claims are transactional: no ledger bit is set until delivery succeeds.
LegendsQuest_EnsureTracker::
    checkitem ITEM_RIFT_TRACKER
    goto_if_eq VAR_RESULT, TRUE, LegendsQuest_Return
    additem ITEM_RIFT_TRACKER
LegendsQuest_Return::
    return

LegendsQuest_ClaimFromMenu::
    lockall
    special LegendsQuest_Claim
    goto_if_ne VAR_RESULT, 1, LegendsQuest_NotReady
    playfanfare MUS_OBTAIN_ITEM
    msgbox LegendsQuest_Text_Claimed, MSGBOX_DEFAULT
    waitfanfare
    releaseall
    end
LegendsQuest_NotReady:
    msgbox LegendsQuest_Text_NotReady, MSGBOX_DEFAULT
    releaseall
    end
LegendsQuest_Text_Claimed:
    .string "Research reward collected!$"
LegendsQuest_Text_NotReady:
    .string "Check the quest's objectives and\nvisit its giver to claim the reward.\pGym rewards follow badge order.\nMake sure your Bag has space.$"

LegendsQuest_FieldResearcher::
    lock
    faceplayer
    setvar VAR_0x8004, 18
    special LegendsQuest_Accept
    goto_if_eq VAR_RESULT, 3, LegendsQuest_SideDone
    msgbox LegendsQuest_Text_Medicine, MSGBOX_YESNO
    goto_if_ne VAR_RESULT, YES, LegendsQuest_SideEnd
    setvar VAR_0x8004, 18
    special LegendsQuest_Claim
    goto_if_ne VAR_RESULT, 1, LegendsQuest_SideMissing
    playfanfare MUS_OBTAIN_ITEM
    msgbox LegendsQuest_Text_Sash, MSGBOX_DEFAULT
    waitfanfare
    goto LegendsQuest_SideEnd
LegendsQuest_RaltsEnthusiast::
    lock
    faceplayer
    setvar VAR_0x8004, 19
    special LegendsQuest_Accept
    goto_if_eq VAR_RESULT, 3, LegendsQuest_SideDone
    msgbox LegendsQuest_Text_Ralts, MSGBOX_YESNO
    goto_if_ne VAR_RESULT, YES, LegendsQuest_SideEnd
    closemessage
    special ChoosePartyMon
    goto_if_ge VAR_0x8004, PARTY_SIZE, LegendsQuest_SideEnd
    copyvar VAR_0x8009, VAR_0x8004
    msgbox LegendsQuest_Text_TradeConfirm, MSGBOX_YESNO
    goto_if_ne VAR_RESULT, YES, LegendsQuest_SideEnd
    copyvar VAR_0x8004, VAR_0x8009
    special LegendsQuest_TradeRalts
    goto_if_ne VAR_RESULT, 1, LegendsQuest_SideMissing
    playfanfare MUS_OBTAIN_ITEM
    msgbox LegendsQuest_Text_Shiny, MSGBOX_DEFAULT
    waitfanfare
    goto LegendsQuest_SideEnd
LegendsQuest_SideDone:
    msgbox LegendsQuest_Text_Done, MSGBOX_DEFAULT
    goto LegendsQuest_SideEnd
LegendsQuest_SideMissing:
    msgbox LegendsQuest_Text_Missing, MSGBOX_DEFAULT
LegendsQuest_SideEnd:
    release
    end
LegendsQuest_Text_Medicine:
    .string "I'm stocking our field medical kit.\nCould you spare three Super Potions?\pI'll exchange a Focus Sash for them.\nWould you like to make the exchange?$"
LegendsQuest_Text_Sash:
    .string "Three Super Potions exchanged\nfor a Focus Sash!\pThank you! This will keep our\nresearch team out in the field.$"
LegendsQuest_Text_Ralts:
    .string "I've been studying Ralts colors.\nI'd like to exchange my shiny Ralts\lfor a non-shiny Ralts.\pYour partner's level, moves, traits\nand held item will be preserved.\pInterested? You can choose a Ralts\nand confirm before we exchange.$"
LegendsQuest_Text_TradeConfirm:
    .string "Exchange the selected Ralts?\nThis exchange cannot be undone.$"
LegendsQuest_Text_Shiny:
    .string "The exchange is complete!\nTake good care of your shiny Ralts.$"
LegendsQuest_Text_Done:
    .string "Thanks again for helping with\nmy research!$"
LegendsQuest_Text_Missing:
    .string "We can't complete the exchange yet.\nCheck the requested items or Pokémon,\land leave space for your reward.$"

LegendsQuest_StoryReward::
    special LegendsQuest_StoryPrepare
    checkitemspace VAR_0x8000, 1
    goto_if_eq VAR_RESULT, FALSE, LegendsQuest_Return
    copyvar VAR_0x800A, VAR_0x8004
    copyvar VAR_0x800B, VAR_0x8000
    closemessage
    giveitem VAR_0x800B
    copyvar VAR_0x8004, VAR_0x800A
    special LegendsQuest_StoryFinish
    return

LegendsQuest_GymReward::
    special LegendsQuest_Claim
    goto_if_ne VAR_RESULT, 1, LegendsQuest_Return
    lockall
    closemessage
    playfanfare MUS_OBTAIN_ITEM
    msgbox LegendsQuest_Text_GymReward, MSGBOX_DEFAULT
    waitfanfare
    return
LegendsQuest_Text_GymReward:
    .string "Your Gym trial is complete!\n{PLAYER} received {STR_VAR_1}!$"
