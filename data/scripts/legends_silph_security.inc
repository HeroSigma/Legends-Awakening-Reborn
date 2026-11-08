@ Project-owned state on the Kanto_SilphCo maps.
LegendsSilph_Load_1::
    end
LegendsSilph_Load_2::
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 0, LegendsSilph_Load_2_Open_0
    call LegendsSilphNative_Close2FDoor1
    goto LegendsSilph_Load_2_Next_0
LegendsSilph_Load_2_Open_0:
    call LegendsSilphNative_Open2FDoor1
LegendsSilph_Load_2_Next_0:
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 1, LegendsSilph_Load_2_Open_1
    call LegendsSilphNative_Close2FDoor2
    goto LegendsSilph_Load_2_Next_1
LegendsSilph_Load_2_Open_1:
    call LegendsSilphNative_Open2FDoor2
LegendsSilph_Load_2_Next_1:
    end
LegendsSilph_Load_3::
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 2, LegendsSilph_Load_3_Open_2
    call LegendsSilphNative_Close3FDoor1
    goto LegendsSilph_Load_3_Next_2
LegendsSilph_Load_3_Open_2:
    call LegendsSilphNative_Open3FDoor1
LegendsSilph_Load_3_Next_2:
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 3, LegendsSilph_Load_3_Open_3
    call LegendsSilphNative_Close3FDoor2
    goto LegendsSilph_Load_3_Next_3
LegendsSilph_Load_3_Open_3:
    call LegendsSilphNative_Open3FDoor2
LegendsSilph_Load_3_Next_3:
    end
LegendsSilph_Load_4::
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 4, LegendsSilph_Load_4_Open_4
    call LegendsSilphNative_Close4FDoor1
    goto LegendsSilph_Load_4_Next_4
LegendsSilph_Load_4_Open_4:
    call LegendsSilphNative_Open4FDoor1
LegendsSilph_Load_4_Next_4:
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 5, LegendsSilph_Load_4_Open_5
    call LegendsSilphNative_Close4FDoor2
    goto LegendsSilph_Load_4_Next_5
LegendsSilph_Load_4_Open_5:
    call LegendsSilphNative_Open4FDoor2
LegendsSilph_Load_4_Next_5:
    end
LegendsSilph_Load_5::
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 6, LegendsSilph_Load_5_Open_6
    call LegendsSilphNative_Close5FDoor1
    goto LegendsSilph_Load_5_Next_6
LegendsSilph_Load_5_Open_6:
    call LegendsSilphNative_Open5FDoor1
LegendsSilph_Load_5_Next_6:
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 7, LegendsSilph_Load_5_Open_7
    call LegendsSilphNative_Close5FDoor2
    goto LegendsSilph_Load_5_Next_7
LegendsSilph_Load_5_Open_7:
    call LegendsSilphNative_Open5FDoor2
LegendsSilph_Load_5_Next_7:
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 8, LegendsSilph_Load_5_Open_8
    call LegendsSilphNative_Close5FDoor3
    goto LegendsSilph_Load_5_Next_8
LegendsSilph_Load_5_Open_8:
    call LegendsSilphNative_Open5FDoor3
LegendsSilph_Load_5_Next_8:
    end
LegendsSilph_Load_6::
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 9, LegendsSilph_Load_6_Open_9
    call LegendsSilphNative_Close6FDoor
    goto LegendsSilph_Load_6_Next_9
LegendsSilph_Load_6_Open_9:
    call LegendsSilphNative_Open6FDoor
LegendsSilph_Load_6_Next_9:
    end
LegendsSilph_Load_7::
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 10, LegendsSilph_Load_7_Open_10
    call LegendsSilphNative_Close7FDoor1
    goto LegendsSilph_Load_7_Next_10
LegendsSilph_Load_7_Open_10:
    call LegendsSilphNative_Open7FDoor1
LegendsSilph_Load_7_Next_10:
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 11, LegendsSilph_Load_7_Open_11
    call LegendsSilphNative_Close7FDoor2
    goto LegendsSilph_Load_7_Next_11
LegendsSilph_Load_7_Open_11:
    call LegendsSilphNative_Open7FDoor2
LegendsSilph_Load_7_Next_11:
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 12, LegendsSilph_Load_7_Open_12
    call LegendsSilphNative_Close7FDoor3
    goto LegendsSilph_Load_7_Next_12
LegendsSilph_Load_7_Open_12:
    call LegendsSilphNative_Open7FDoor3
LegendsSilph_Load_7_Next_12:
    end
LegendsSilph_Load_8::
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 13, LegendsSilph_Load_8_Open_13
    call LegendsSilphNative_Close8FDoor
    goto LegendsSilph_Load_8_Next_13
LegendsSilph_Load_8_Open_13:
    call LegendsSilphNative_Open8FDoor
LegendsSilph_Load_8_Next_13:
    end
LegendsSilph_Load_9::
    call LegendsSilphNative_Open9FDoor1
    call LegendsSilphNative_Open9FDoor2
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 16, LegendsSilph_Load_9_Open_16
    call LegendsSilphNative_Close9FDoor3
    goto LegendsSilph_Load_9_Next_16
LegendsSilph_Load_9_Open_16:
    call LegendsSilphNative_Open9FDoor3
LegendsSilph_Load_9_Next_16:
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 17, LegendsSilph_Load_9_Open_17
    call LegendsSilphNative_Close9FDoor4
    goto LegendsSilph_Load_9_Next_17
LegendsSilph_Load_9_Open_17:
    call LegendsSilphNative_Open9FDoor4
LegendsSilph_Load_9_Next_17:
    end
LegendsSilph_Load_10::
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 18, LegendsSilph_Load_10_Open_18
    call LegendsSilphNative_Close10FDoor
    goto LegendsSilph_Load_10_Next_18
LegendsSilph_Load_10_Open_18:
    call LegendsSilphNative_Open10FDoor
LegendsSilph_Load_10_Next_18:
    end
LegendsSilph_Load_11::
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 19, LegendsSilph_Load_11_Open_19
    call LegendsSilphNative_Close11FDoor
    goto LegendsSilph_Load_11_Next_19
LegendsSilph_Load_11_Open_19:
    call LegendsSilphNative_Open11FDoor
LegendsSilph_Load_11_Next_19:
    end
LegendsSilph_Door_0::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 0, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open2FDoor1
    setflag FLAG_LA_SILPH_DOOR_BASE + 0
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_1::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 1, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open2FDoor2
    setflag FLAG_LA_SILPH_DOOR_BASE + 1
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_2::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 2, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open3FDoor1
    setflag FLAG_LA_SILPH_DOOR_BASE + 2
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_3::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 3, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open3FDoor2
    setflag FLAG_LA_SILPH_DOOR_BASE + 3
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_4::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 4, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open4FDoor1
    setflag FLAG_LA_SILPH_DOOR_BASE + 4
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_5::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 5, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open4FDoor2
    setflag FLAG_LA_SILPH_DOOR_BASE + 5
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_6::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 6, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open5FDoor1
    setflag FLAG_LA_SILPH_DOOR_BASE + 6
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_7::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 7, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open5FDoor2
    setflag FLAG_LA_SILPH_DOOR_BASE + 7
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_8::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 8, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open5FDoor3
    setflag FLAG_LA_SILPH_DOOR_BASE + 8
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_9::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 9, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open6FDoor
    setflag FLAG_LA_SILPH_DOOR_BASE + 9
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_10::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 10, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open7FDoor1
    setflag FLAG_LA_SILPH_DOOR_BASE + 10
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_11::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 11, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open7FDoor2
    setflag FLAG_LA_SILPH_DOOR_BASE + 11
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_12::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 12, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open7FDoor3
    setflag FLAG_LA_SILPH_DOOR_BASE + 12
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_13::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 13, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open8FDoor
    setflag FLAG_LA_SILPH_DOOR_BASE + 13
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_14::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 14, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open9FDoor1
    setflag FLAG_LA_SILPH_DOOR_BASE + 14
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_15::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 15, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open9FDoor2
    setflag FLAG_LA_SILPH_DOOR_BASE + 15
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_16::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 16, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open9FDoor3
    setflag FLAG_LA_SILPH_DOOR_BASE + 16
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_17::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 17, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open9FDoor4
    setflag FLAG_LA_SILPH_DOOR_BASE + 17
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_18::
    lockall
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 18, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open10FDoor
    setflag FLAG_LA_SILPH_DOOR_BASE + 18
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_Door_19::
    lockall
    goto_if_unset FLAG_LA_SILPH_PETREL_DEFEATED, LegendsAshes_AdminGate
    goto_if_unset FLAG_LA_SILPH_ARIANA_DEFEATED, LegendsAshes_AdminGate
    goto_if_unset FLAG_LA_SILPH_WALLY_FOUND, LegendsAshes_AdminGate
    setspeaker SP_NAME_NONE
    goto_if_set FLAG_LA_SILPH_DOOR_BASE + 19, LegendsSilph_DoorAlreadyOpen
    checkitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsSilph_DoorLocked
    msgbox SilphSecurity_Text_CardUsed, MSGBOX_DEFAULT
    closemessage
    playse SE_UNLOCK
    call LegendsSilphNative_Open11FDoor
    setflag FLAG_LA_SILPH_DOOR_BASE + 19
    special DrawWholeMapView
    goto LegendsAshes_End
LegendsSilph_DoorLocked::
    msgbox SilphSecurity_Text_Locked, MSGBOX_DEFAULT
    goto LegendsAshes_End
LegendsSilph_DoorAlreadyOpen::
    msgbox SilphSecurity_Text_Open, MSGBOX_DEFAULT
    goto LegendsAshes_End
SilphSecurity_Text_Locked:
    .string "A security door.\nIt needs Silph's Card Key.$"
SilphSecurity_Text_CardUsed:
    .string "The Card Key matches the lock.\nThe security door opens!$"
SilphSecurity_Text_Open:
    .string "The security door is unlocked.$"
LegendsSilph_EnterElevator::
    lockall
    setspeaker SP_NAME_PLAYER
    msgbox SilphSecurity_Text_Elevator, MSGBOX_DEFAULT
    closemessage
    warp MAP_KANTOAR_1_58_SILPHCO_ELEVATOR, 2, 4
    waitstate
    end
LegendsSilph_ElevatorPanel::
    msgbox SilphSecurity_Text_Panel, MSGBOX_SIGN
    end
LegendsSilph_CardKey::
    lockall
    goto_if_set FLAG_LA_SILPH_CARD_KEY, LegendsAshes_End
    setspeaker SP_NAME_PLAYER
    msgbox SilphSecurity_Text_KeyFound, MSGBOX_DEFAULT
    setspeaker SP_NAME_NONE
    giveitem ITEM_CARD_KEY
    goto_if_eq VAR_RESULT, FALSE, LegendsAshes_End
    setflag FLAG_LA_SILPH_CARD_KEY
    removeobject LOCALID_LA_SILPH_CARDKEY
    goto LegendsAshes_End
SilphSecurity_Text_Elevator:
    .string "The elevator has stopped on this floor.\nI can check the cabin.$"
SilphSecurity_Text_Panel:
    .string "Emergency stop: 9F.\nThe controls are disabled.$"
SilphSecurity_Text_KeyFound:
    .string "The dropped Card Key!\nThis should open the security doors.$"
LegendsSilph_Loot_0::
    lockall
    setspeaker SP_NAME_NONE
    giveitem ITEM_ALAKAZITE
    goto_if_eq VAR_RESULT, FALSE, LegendsAshes_End
    setflag FLAG_LA_SILPH_LOOT_BASE + 0
    removeobject LOCALID_LA_SILPH_LOOT_F3
    goto LegendsAshes_End
LegendsSilph_Loot_1::
    lockall
    setspeaker SP_NAME_NONE
    giveitem ITEM_MANECTITE
    goto_if_eq VAR_RESULT, FALSE, LegendsAshes_End
    setflag FLAG_LA_SILPH_LOOT_BASE + 1
    removeobject LOCALID_LA_SILPH_LOOT_F4
    goto LegendsAshes_End
LegendsSilph_Loot_2::
    lockall
    setspeaker SP_NAME_NONE
    giveitem ITEM_SCIZORITE
    goto_if_eq VAR_RESULT, FALSE, LegendsAshes_End
    setflag FLAG_LA_SILPH_LOOT_BASE + 2
    removeobject LOCALID_LA_SILPH_LOOT_F6
    goto LegendsAshes_End
LegendsSilph_Loot_3::
    lockall
    setspeaker SP_NAME_NONE
    giveitem ITEM_NORMALIUM_Z
    goto_if_eq VAR_RESULT, FALSE, LegendsAshes_End
    setflag FLAG_LA_SILPH_LOOT_BASE + 3
    removeobject LOCALID_LA_SILPH_LOOT_F5
    goto LegendsAshes_End
LegendsSilph_Loot_4::
    lockall
    setspeaker SP_NAME_NONE
    giveitem ITEM_ELECTRIUM_Z
    goto_if_eq VAR_RESULT, FALSE, LegendsAshes_End
    setflag FLAG_LA_SILPH_LOOT_BASE + 4
    removeobject LOCALID_LA_SILPH_LOOT_F7
    goto LegendsAshes_End
LegendsSilph_Loot_5::
    lockall
    setspeaker SP_NAME_NONE
    giveitem ITEM_PSYCHIUM_Z
    goto_if_eq VAR_RESULT, FALSE, LegendsAshes_End
    setflag FLAG_LA_SILPH_LOOT_BASE + 5
    removeobject LOCALID_LA_SILPH_LOOT_F10
    goto LegendsAshes_End
LegendsSilph_Porygon::
    lockall
    goto_if_set FLAG_LA_SILPH_PORYGON, LegendsAshes_End
    setspeaker SP_NAME_PLAYER
    msgbox SilphSecurity_Text_Porygon, MSGBOX_YESNO
    goto_if_eq VAR_RESULT, NO, LegendsAshes_End
    setspeaker SP_NAME_NONE
    givemon SPECIES_PORYGON, 25, ITEM_NONE
    goto_if_eq VAR_RESULT, 2, LegendsSilph_StorageFull
    setflag FLAG_LA_SILPH_PORYGON
    removeobject LOCALID_LA_SILPH_PORYGON
    msgbox SilphSecurity_Text_PorygonJoined, MSGBOX_DEFAULT
    goto LegendsAshes_End
LegendsSilph_StorageFull:
    msgbox SilphSecurity_Text_StorageFull, MSGBOX_DEFAULT
    goto LegendsAshes_End
SilphSecurity_Text_Porygon:
    .string "A Silph Poké Ball with a Porygon!\nThe transfer label is still attached.\pTake Porygon with you?$"
SilphSecurity_Text_PorygonJoined:
    .string "Porygon joined you!\nCheck your party or Pokémon storage.$"
SilphSecurity_Text_StorageFull:
    .string "Your party and storage are full.\nPorygon will wait here.$"

SilphSecurity_Text_Guard_0:
    .string "This floor is restricted.\nRocket controls the security system.$"

SilphSecurity_Text_Guard_1:
    .string "The labs are sealed.\nNo Card Key, no access.$"

SilphSecurity_Text_Guard_2:
    .string "You're not one of the technicians.\nStep away from those records!$"

SilphSecurity_Text_Guard_3:
    .string "Those supplies belong to our operation.\nKeep your hands off them!$"

SilphSecurity_Text_Guard_4:
    .string "We're securing the research floors.\nYou shouldn't have made it this far.$"

SilphSecurity_Text_Guard_5:
    .string "The executives want the building quiet.\nI'll make sure you stay that way.$"

SilphSecurity_Text_Guard_6:
    .string "Someone let the boy and Kirlia escape.\nYou're not helping them go anywhere!$"

SilphSecurity_Text_Guard_7:
    .string "The ninth floor is under lockdown.\nNobody reaches the upper offices!$"

LegendsSilph_FlanneryToGym::
    closemessage
    applymovement LOCALID_ASHES_LAVA_FLANNERY, SilphSecurity_FlanneryWalk
    waitmovement 0
    opendoor 5, 15
    waitdooranim
    applymovement LOCALID_ASHES_LAVA_FLANNERY, SilphSecurity_FlanneryEnter
    waitmovement 0
    removeobject LOCALID_ASHES_LAVA_FLANNERY
    closedoor 5, 15
    waitdooranim
    setflag FLAG_LA_FLANNERY_RETURNED_GYM
    setflag FLAG_TEMP_5
    return
SilphSecurity_FlanneryWalk:
    walk_left
    walk_down
    walk_down
    walk_down
    walk_down
    walk_down
    walk_left
    walk_down
    walk_down
    walk_left
    walk_left
    walk_up
    face_up
    step_end
SilphSecurity_FlanneryEnter:
    walk_up
    step_end

LegendsSilph_EnterOffice::
    goto_if_set FLAG_LA_SILPH_GIOVANNIS_FLED, LegendsBlue_End
    lockall
    getplayerxy VAR_0x8008, VAR_0x8009
    goto_if_eq VAR_0x8008, 5, LegendsSilph_OfficeLeft
    applymovement LOCALID_PLAYER, SilphSecurity_OfficeRight
    waitmovement 0
    goto LegendsAshes_TwoGiovannis
LegendsSilph_OfficeLeft:
    applymovement LOCALID_PLAYER, SilphSecurity_OfficeLeft
    waitmovement 0
    goto LegendsAshes_TwoGiovannis
SilphSecurity_OfficeLeft:
    walk_right
SilphSecurity_OfficeRight:
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_up
    walk_up
    walk_up
    walk_up
    walk_up
    face_left
    step_end

@ Door geometry adapted from the project native silphco_doors scripts.
LegendsSilphNative_Close2FDoor1::
	setmetatile 5, 8, METATILE_SilphCo_HorizontalBarrier_TopLeft, 1
	setmetatile 6, 8, METATILE_SilphCo_HorizontalBarrier_TopRight, 1
	setmetatile 5, 9, METATILE_SilphCo_HorizontalBarrier_BottomLeft, 1
	setmetatile 6, 9, METATILE_SilphCo_HorizontalBarrier_BottomRight, 1
	setmetatile 6, 10, METATILE_SilphCo_Floor_ShadeFull, 0
	return

LegendsSilphNative_Close2FDoor2::
	setmetatile 5, 15, METATILE_SilphCo_HorizontalBarrier_TopLeft, 1
	setmetatile 6, 15, METATILE_SilphCo_HorizontalBarrier_TopRight, 1
	setmetatile 5, 16, METATILE_SilphCo_HorizontalBarrier_BottomLeft, 1
	setmetatile 6, 16, METATILE_SilphCo_HorizontalBarrier_BottomRight, 1
	setmetatile 6, 17, METATILE_SilphCo_Floor_ShadeFull, 0
	return

LegendsSilphNative_Close3FDoor1::
	setmetatile 9, 11, METATILE_SilphCo_VerticalBarrier_TopLeft, 1
	setmetatile 10, 11, METATILE_SilphCo_VerticalBarrier_TopRight, 1
	setmetatile 9, 12, METATILE_SilphCo_VerticalBarrier_MidLeft, 1
	setmetatile 10, 12, METATILE_SilphCo_VerticalBarrier_MidRight, 1
	setmetatile 9, 13, METATILE_SilphCo_VerticalBarrier_BottomLeft, 1
	setmetatile 10, 13, METATILE_SilphCo_VerticalBarrier_BottomRight, 1
	return

LegendsSilphNative_Close3FDoor2::
	setmetatile 20, 11, METATILE_SilphCo_VerticalBarrier_TopLeft, 1
	setmetatile 21, 11, METATILE_SilphCo_VerticalBarrier_TopRight, 1
	setmetatile 20, 12, METATILE_SilphCo_VerticalBarrier_MidLeft, 1
	setmetatile 21, 12, METATILE_SilphCo_VerticalBarrier_MidRight, 1
	setmetatile 20, 13, METATILE_SilphCo_VerticalBarrier_BottomLeft, 1
	setmetatile 21, 13, METATILE_SilphCo_VerticalBarrier_BottomRight, 1
	return

LegendsSilphNative_Close4FDoor1::
	setmetatile 3, 16, METATILE_SilphCo_HorizontalBarrier_TopLeft, 1
	setmetatile 4, 16, METATILE_SilphCo_HorizontalBarrier_TopRight, 1
	setmetatile 3, 17, METATILE_SilphCo_HorizontalBarrier_BottomLeft, 1
	setmetatile 4, 17, METATILE_SilphCo_HorizontalBarrier_BottomRight, 1
	setmetatile 4, 18, METATILE_SilphCo_Floor_ShadeFull, 0
	return

LegendsSilphNative_Close4FDoor2::
	setmetatile 14, 11, METATILE_SilphCo_HorizontalBarrier_TopLeft, 1
	setmetatile 15, 11, METATILE_SilphCo_HorizontalBarrier_TopRight, 1
	setmetatile 14, 12, METATILE_SilphCo_HorizontalBarrier_BottomLeft, 1
	setmetatile 15, 12, METATILE_SilphCo_HorizontalBarrier_BottomRight, 1
	setmetatile 15, 13, METATILE_SilphCo_Floor_ShadeFull, 0
	return

LegendsSilphNative_Close5FDoor1::
	setmetatile 7, 8, METATILE_SilphCo_VerticalBarrier_TopLeft, 1
	setmetatile 8, 8, METATILE_SilphCo_VerticalBarrier_TopRight, 1
	setmetatile 7, 9, METATILE_SilphCo_VerticalBarrier_MidLeft, 1
	setmetatile 8, 9, METATILE_SilphCo_VerticalBarrier_MidRight, 1
	setmetatile 7, 10, METATILE_SilphCo_VerticalBarrier_BottomLeft, 1
	setmetatile 8, 10, METATILE_SilphCo_VerticalBarrier_BottomRight, 1
	return

LegendsSilphNative_Close5FDoor2::
	setmetatile 7, 17, METATILE_SilphCo_VerticalBarrier_TopLeft, 1
	setmetatile 8, 17, METATILE_SilphCo_VerticalBarrier_TopRight, 1
	setmetatile 7, 18, METATILE_SilphCo_VerticalBarrier_MidLeft, 1
	setmetatile 8, 18, METATILE_SilphCo_VerticalBarrier_MidRight, 1
	setmetatile 7, 19, METATILE_SilphCo_VerticalBarrier_BottomLeft, 1
	setmetatile 8, 19, METATILE_SilphCo_VerticalBarrier_BottomRight, 1
	return

LegendsSilphNative_Close5FDoor3::
	setmetatile 18, 12, METATILE_SilphCo_VerticalBarrier_TopLeft, 1
	setmetatile 19, 12, METATILE_SilphCo_VerticalBarrier_TopRight, 1
	setmetatile 18, 13, METATILE_SilphCo_VerticalBarrier_MidLeft, 1
	setmetatile 19, 13, METATILE_SilphCo_VerticalBarrier_MidRight, 1
	setmetatile 18, 14, METATILE_SilphCo_VerticalBarrier_BottomLeft, 1
	setmetatile 19, 14, METATILE_SilphCo_VerticalBarrier_BottomRight, 1
	return

LegendsSilphNative_Close6FDoor::
	setmetatile 5, 14, METATILE_SilphCo_VerticalBarrier_TopLeft, 1
	setmetatile 6, 14, METATILE_SilphCo_VerticalBarrier_TopRight, 1
	setmetatile 5, 15, METATILE_SilphCo_VerticalBarrier_MidLeft, 1
	setmetatile 6, 15, METATILE_SilphCo_VerticalBarrier_MidRight, 1
	setmetatile 5, 16, METATILE_SilphCo_VerticalBarrier_BottomLeft, 1
	setmetatile 6, 16, METATILE_SilphCo_VerticalBarrier_BottomRight, 1
	return

LegendsSilphNative_Close7FDoor1::
	setmetatile 11, 8, METATILE_SilphCo_HorizontalBarrier_TopLeft, 1
	setmetatile 12, 8, METATILE_SilphCo_HorizontalBarrier_TopRight, 1
	setmetatile 11, 9, METATILE_SilphCo_HorizontalBarrier_BottomLeft, 1
	setmetatile 12, 9, METATILE_SilphCo_HorizontalBarrier_BottomRight, 1
	setmetatile 12, 10, METATILE_SilphCo_Floor_ShadeFull, 0
	return

LegendsSilphNative_Close7FDoor2::
	setmetatile 24, 7, METATILE_SilphCo_HorizontalBarrier_TopLeft, 1
	setmetatile 25, 7, METATILE_SilphCo_HorizontalBarrier_TopRight, 1
	setmetatile 24, 8, METATILE_SilphCo_HorizontalBarrier_BottomLeft, 1
	setmetatile 25, 8, METATILE_SilphCo_HorizontalBarrier_BottomRight, 1
	setmetatile 25, 9, METATILE_SilphCo_Floor_ShadeFull, 0
	return

LegendsSilphNative_Close7FDoor3::
	setmetatile 25, 13, METATILE_SilphCo_HorizontalBarrier_TopLeft, 1
	setmetatile 26, 13, METATILE_SilphCo_HorizontalBarrier_TopRight, 1
	setmetatile 25, 14, METATILE_SilphCo_HorizontalBarrier_BottomLeft, 1
	setmetatile 26, 14, METATILE_SilphCo_HorizontalBarrier_BottomRight, 1
	setmetatile 26, 15, METATILE_SilphCo_Floor_ShadeFull, 0
	return

LegendsSilphNative_Close8FDoor::
	setmetatile 5, 9, METATILE_SilphCo_VerticalBarrier_TopLeft, 1
	setmetatile 6, 9, METATILE_SilphCo_VerticalBarrier_TopRight, 1
	setmetatile 5, 10, METATILE_SilphCo_VerticalBarrier_MidLeft, 1
	setmetatile 6, 10, METATILE_SilphCo_VerticalBarrier_MidRight, 1
	setmetatile 5, 11, METATILE_SilphCo_VerticalBarrier_BottomLeft, 1
	setmetatile 6, 11, METATILE_SilphCo_VerticalBarrier_BottomRight, 1
	return

LegendsSilphNative_Close9FDoor1::
	setmetatile 2, 9, METATILE_SilphCo_VerticalBarrier_TopLeft, 1
	setmetatile 3, 9, METATILE_SilphCo_VerticalBarrier_TopRight, 1
	setmetatile 2, 10, METATILE_SilphCo_VerticalBarrier_MidLeft, 1
	setmetatile 3, 10, METATILE_SilphCo_VerticalBarrier_MidRight, 1
	setmetatile 2, 11, METATILE_SilphCo_VerticalBarrier_BottomLeft, 1
	setmetatile 3, 11, METATILE_SilphCo_VerticalBarrier_BottomRight, 1
	return

LegendsSilphNative_Close9FDoor2::
	setmetatile 12, 15, METATILE_SilphCo_VerticalBarrier_TopLeft, 1
	setmetatile 13, 15, METATILE_SilphCo_VerticalBarrier_TopRight, 1
	setmetatile 12, 16, METATILE_SilphCo_VerticalBarrier_MidLeft, 1
	setmetatile 13, 16, METATILE_SilphCo_VerticalBarrier_MidRight, 1
	setmetatile 12, 17, METATILE_SilphCo_VerticalBarrier_BottomLeft, 1
	setmetatile 13, 17, METATILE_SilphCo_VerticalBarrier_BottomRight, 1
	return

LegendsSilphNative_Close9FDoor3::
	setmetatile 21, 6, METATILE_SilphCo_HorizontalBarrier_TopLeft, 1
	setmetatile 22, 6, METATILE_SilphCo_HorizontalBarrier_TopRight, 1
	setmetatile 21, 7, METATILE_SilphCo_HorizontalBarrier_BottomLeft, 1
	setmetatile 22, 7, METATILE_SilphCo_HorizontalBarrier_BottomRight, 1
	setmetatile 22, 8, METATILE_SilphCo_Floor_ShadeFull, 0
	return

LegendsSilphNative_Close9FDoor4::
	setmetatile 21, 12, METATILE_SilphCo_HorizontalBarrier_TopLeft, 1
	setmetatile 22, 12, METATILE_SilphCo_HorizontalBarrier_TopRight, 1
	setmetatile 21, 13, METATILE_SilphCo_HorizontalBarrier_BottomLeft, 1
	setmetatile 22, 13, METATILE_SilphCo_HorizontalBarrier_BottomRight, 1
	setmetatile 22, 14, METATILE_SilphCo_Floor_ShadeFull, 0
	return

LegendsSilphNative_Close10FDoor::
	setmetatile 12, 11, METATILE_SilphCo_HorizontalBarrier_TopLeft, 1
	setmetatile 13, 11, METATILE_SilphCo_HorizontalBarrier_TopRight, 1
	setmetatile 12, 12, METATILE_SilphCo_HorizontalBarrier_BottomLeft, 1
	setmetatile 13, 12, METATILE_SilphCo_HorizontalBarrier_BottomRight, 1
	setmetatile 13, 13, METATILE_SilphCo_Floor_ShadeFull, 0
	return

LegendsSilphNative_Close11FDoor::
	setmetatile 5, 16, METATILE_SilphCo_HorizontalBarrier_TopLeft, 1
	setmetatile 6, 16, METATILE_SilphCo_HorizontalBarrier_TopRight, 1
	setmetatile 5, 17, METATILE_SilphCo_HorizontalBarrier_BottomLeft, 1
	setmetatile 6, 17, METATILE_SilphCo_HorizontalBarrier_BottomRight, 1
	setmetatile 6, 18, METATILE_SilphCo_Floor_ShadeFull, 0
	return

LegendsSilphNative_Open2FDoor1::
	setmetatile 5, 8, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 6, 8, METATILE_SilphCo_Floor, 0
	setmetatile 5, 9, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 6, 9, METATILE_SilphCo_Floor, 0
	setmetatile 6, 10, METATILE_SilphCo_Floor, 0
	return

LegendsSilphNative_Open2FDoor2::
	setmetatile 5, 15, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 6, 15, METATILE_SilphCo_Floor, 0
	setmetatile 5, 16, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 6, 16, METATILE_SilphCo_Floor, 0
	setmetatile 6, 17, METATILE_SilphCo_Floor, 0
	return

LegendsSilphNative_Open3FDoor1::
	setmetatile 9, 11, METATILE_SilphCo_Wall_LeftEdge, 1
	setmetatile 10, 11, METATILE_SilphCo_Wall_RightEdge, 1
	setmetatile 9, 12, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 10, 12, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 9, 13, METATILE_SilphCo_Floor_WallLeftCorner, 0
	setmetatile 10, 13, METATILE_SilphCo_Floor_WallRightCorner, 0
	return

LegendsSilphNative_Open3FDoor2::
	setmetatile 20, 11, METATILE_SilphCo_Wall_LeftEdge, 1
	setmetatile 21, 11, METATILE_SilphCo_Wall_RightEdge, 1
	setmetatile 20, 12, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 21, 12, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 20, 13, METATILE_SilphCo_Floor_WallLeftCorner, 0
	setmetatile 21, 13, METATILE_SilphCo_Floor_WallRightCorner, 0
	return

LegendsSilphNative_Open4FDoor1::
	setmetatile 3, 16, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 4, 16, METATILE_SilphCo_Floor, 0
	setmetatile 3, 17, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 4, 17, METATILE_SilphCo_Floor, 0
	setmetatile 4, 18, METATILE_SilphCo_Floor, 0
	return

LegendsSilphNative_Open4FDoor2::
	setmetatile 14, 11, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 15, 11, METATILE_SilphCo_Floor, 0
	setmetatile 14, 12, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 15, 12, METATILE_SilphCo_Floor, 0
	setmetatile 15, 13, METATILE_SilphCo_Floor, 0
	return

LegendsSilphNative_Open5FDoor1::
	setmetatile 7, 8, METATILE_SilphCo_Wall_LeftEdge, 1
	setmetatile 8, 8, METATILE_SilphCo_Wall_RightEdge, 1
	setmetatile 7, 9, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 8, 9, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 7, 10, METATILE_SilphCo_Floor_WallLeftCorner, 0
	setmetatile 8, 10, METATILE_SilphCo_Floor_WallRightCorner, 0
	return

LegendsSilphNative_Open5FDoor2::
	setmetatile 7, 17, METATILE_SilphCo_Wall_LeftEdge, 1
	setmetatile 8, 17, METATILE_SilphCo_Wall_RightEdge, 1
	setmetatile 7, 18, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 8, 18, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 7, 19, METATILE_SilphCo_Floor_WallLeftCorner, 0
	setmetatile 8, 19, METATILE_SilphCo_Floor_WallRightCorner, 0
	return

LegendsSilphNative_Open5FDoor3::
	setmetatile 18, 12, METATILE_SilphCo_Wall_LeftEdge, 1
	setmetatile 19, 12, METATILE_SilphCo_Wall_RightEdge, 1
	setmetatile 18, 13, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 19, 13, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 18, 14, METATILE_SilphCo_Floor_WallLeftCorner, 0
	setmetatile 19, 14, METATILE_SilphCo_Floor_WallRightCorner, 0
	return

LegendsSilphNative_Open6FDoor::
	setmetatile 5, 14, METATILE_SilphCo_Wall_LeftEdge, 1
	setmetatile 6, 14, METATILE_SilphCo_Wall_RightEdge, 1
	setmetatile 5, 15, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 6, 15, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 5, 16, METATILE_SilphCo_Floor_WallLeftCorner, 0
	setmetatile 6, 16, METATILE_SilphCo_Floor_WallRightCorner, 0
	return

LegendsSilphNative_Open7FDoor1::
	setmetatile 11, 8, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 12, 8, METATILE_SilphCo_Floor, 0
	setmetatile 11, 9, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 12, 9, METATILE_SilphCo_Floor, 0
	setmetatile 12, 10, METATILE_SilphCo_Floor, 0
	return

LegendsSilphNative_Open7FDoor2::
	setmetatile 24, 7, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 25, 7, METATILE_SilphCo_Floor, 0
	setmetatile 24, 8, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 25, 8, METATILE_SilphCo_Floor, 0
	setmetatile 25, 9, METATILE_SilphCo_Floor, 0
	return

LegendsSilphNative_Open7FDoor3::
	setmetatile 25, 13, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 26, 13, METATILE_SilphCo_Floor, 0
	setmetatile 25, 14, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 26, 14, METATILE_SilphCo_Floor, 0
	setmetatile 26, 15, METATILE_SilphCo_Floor, 0
	return

LegendsSilphNative_Open8FDoor::
	setmetatile 5, 9, METATILE_SilphCo_Wall_LeftEdge, 1
	setmetatile 6, 9, METATILE_SilphCo_Wall_RightEdge, 1
	setmetatile 5, 10, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 6, 10, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 5, 11, METATILE_SilphCo_Floor_WallLeftCorner, 0
	setmetatile 6, 11, METATILE_SilphCo_Floor_WallRightCorner, 0
	return

LegendsSilphNative_Open9FDoor1::
	setmetatile 2, 9, METATILE_SilphCo_Wall_LeftEdge, 1
	setmetatile 3, 9, METATILE_SilphCo_Wall_RightEdge, 1
	setmetatile 2, 10, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 3, 10, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 2, 11, METATILE_SilphCo_Floor_WallLeftCorner, 0
	setmetatile 3, 11, METATILE_SilphCo_Floor_WallRightCorner, 0
	return

LegendsSilphNative_Open9FDoor2::
	setmetatile 12, 15, METATILE_SilphCo_Wall_LeftEdge, 1
	setmetatile 13, 15, METATILE_SilphCo_Wall_RightEdge, 1
	setmetatile 12, 16, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 13, 16, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 12, 17, METATILE_SilphCo_Floor_WallLeftCorner, 0
	setmetatile 13, 17, METATILE_SilphCo_Floor_WallRightCorner, 0
	return

LegendsSilphNative_Open9FDoor3::
	setmetatile 21, 6, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 22, 6, METATILE_SilphCo_Floor, 0
	setmetatile 21, 7, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 22, 7, METATILE_SilphCo_Floor, 0
	setmetatile 22, 8, METATILE_SilphCo_Floor, 0
	return

LegendsSilphNative_Open9FDoor4::
	setmetatile 21, 12, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 22, 12, METATILE_SilphCo_Floor, 0
	setmetatile 21, 13, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 22, 13, METATILE_SilphCo_Floor, 0
	setmetatile 22, 14, METATILE_SilphCo_Floor, 0
	return

LegendsSilphNative_Open10FDoor::
	setmetatile 12, 11, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 13, 11, METATILE_SilphCo_Floor, 0
	setmetatile 12, 12, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 13, 12, METATILE_SilphCo_Floor, 0
	setmetatile 13, 13, METATILE_SilphCo_Floor, 0
	return

LegendsSilphNative_Open11FDoor::
	setmetatile 5, 16, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 6, 16, METATILE_SilphCo_Floor, 0
	setmetatile 5, 17, METATILE_SilphCo_Floor_ShadeFull, 0
	setmetatile 6, 17, METATILE_SilphCo_Floor, 0
	setmetatile 6, 18, METATILE_SilphCo_Floor, 0
	return

