Hoenn_Route_106_MapScripts::
    map_script MAP_SCRIPT_ON_LOAD, DewfordHoopa_OnLoad
    .byte 0

DewfordHoopa_OnLoad:
    setflag FLAG_TEMP_1
    goto_if_set FLAG_LA_DEWFORD_HOOPA_SEEN, DewfordHoopa_DisableTrigger
    setflag FLAG_LA_HIDE_DEWFORD_DYNAMAX_BAND
    end

DewfordHoopa_DisableTrigger:
    setvar VAR_TEMP_1, 1
    end

DewfordHoopa_EventScript_Sighting::
    goto_if_set FLAG_LA_DEWFORD_HOOPA_SEEN, DewfordHoopa_DisableTrigger
    lockall
    setvar VAR_TEMP_1, 1
    turnobject LOCALID_PLAYER, DIR_WEST
    special SpawnCameraObject
    applymovement LOCALID_CAMERA, DewfordHoopa_CameraLeft
    waitmovement 0
    delay 12
    playse SE_WARP_IN
    clearflag FLAG_TEMP_1
    addobject LOCALID_DEWFORD_HOOPA
    setvar VAR_0x8004, LOCALID_DEWFORD_HOOPA
    setvar VAR_0x8005, FALSE
    callnative PlayDewfordHoopaAnimation
    delay 40
    playmoncry SPECIES_HOOPA, CRY_MODE_NORMAL
    waitmoncry
    delay 26
    playse SE_WARP_OUT
    setvar VAR_0x8004, LOCALID_DEWFORD_HOOPA
    setvar VAR_0x8005, TRUE
    callnative PlayDewfordHoopaAnimation
    delay 32
    removeobject LOCALID_DEWFORD_HOOPA
    setflag FLAG_TEMP_1
    clearflag FLAG_LA_HIDE_DEWFORD_DYNAMAX_BAND
    addobject LOCALID_DEWFORD_DYNAMAX_BAND
    setflag FLAG_LA_DEWFORD_HOOPA_SEEN
    playse SE_SELECT
    delay 28
    applymovement LOCALID_CAMERA, DewfordHoopa_CameraRight
    waitmovement 0
    special RemoveCameraObject
    setspeaker SP_NAME_PLAYER
    msgbox DewfordHoopa_Text_Reaction, MSGBOX_DEFAULT
    closemessage
    setspeaker SP_NAME_NONE
    releaseall
    end

DewfordHoopa_EventScript_DynamaxBand::
    finditem ITEM_DYNAMAX_BAND
    goto_if_unset FLAG_LA_HIDE_DEWFORD_DYNAMAX_BAND, DewfordHoopa_PickupEnd
    lockall
    closemessage
    setspeaker SP_NAME_PLAYER
    msgbox DewfordHoopa_Text_BandReaction, MSGBOX_DEFAULT
    closemessage
    setspeaker SP_NAME_NONE
    releaseall
DewfordHoopa_PickupEnd:
    end

DewfordHoopa_Text_BandReaction:
    .string "A Dynamax Band?\pHow did that Pokémon get one?\pI'll hang on to it. Someone might\nknow where it came from.$"

DewfordHoopa_CameraLeft:
    walk_left
    walk_left
    walk_left
    walk_left
    step_end

DewfordHoopa_CameraRight:
    walk_right
    walk_right
    walk_right
    walk_right
    step_end

DewfordHoopa_Text_Reaction:
    .string "Was that one of the rifts?\pWait… It left something behind.$"

@ Project-owned reservation; registered asset map, no donor gameplay.
HyperHoenn_34_68_Route_106_EventScript_HyperConstruction_Registered1::
	lock
	faceplayer
	msgbox HyperHoenn_34_68_Route_106_Text_HyperConstruction_Registered1, MSGBOX_DEFAULT
	release
	end

HyperHoenn_34_68_Route_106_Text_HyperConstruction_Registered1:
	.string "This area is under construction.\p"
	.string "Please check back later!$"
