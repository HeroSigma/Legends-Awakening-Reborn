@ First downstairs report. Uses canonical Hoenn progression and project dialogue only.
LegendsDownstairs_SetupMale::
    setvar VAR_0x8004, MALE
    goto LegendsDownstairs_Check
LegendsDownstairs_SetupFemale::
    setvar VAR_0x8004, FEMALE
LegendsDownstairs_Check:
    goto_if_unset FLAG_LA_INTRO_ACTIVE, LegendsDownstairs_Return
    goto_if_unset FLAG_LA_ELARA_PACKAGE_SCENE_COMPLETE, LegendsDownstairs_Return
    goto_if_set FLAG_LA_WATCHED_RIFT_REPORT, LegendsDownstairs_Return
    goto_if_set FLAG_RESCUED_BIRCH, LegendsDownstairs_Return
    goto_if_ne VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_COMPLETE, LegendsDownstairs_Return
    checkplayergender
    goto_if_ne VAR_RESULT, VAR_0x8004, LegendsDownstairs_Return
    setvar VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_RIFT_REPORT
    goto_if_eq VAR_0x8004, FEMALE, LegendsDownstairs_PlaceElaraFemale
    setobjectxyperm LOCALID_PLAYERS_HOUSE_1F_MOM, 4, 5
    setobjectmovementtype LOCALID_PLAYERS_HOUSE_1F_MOM, MOVEMENT_TYPE_FACE_UP
    return
LegendsDownstairs_PlaceElaraFemale:
    setobjectxyperm LOCALID_PLAYERS_HOUSE_1F_MOM, 6, 5
    setobjectmovementtype LOCALID_PLAYERS_HOUSE_1F_MOM, MOVEMENT_TYPE_FACE_UP
LegendsDownstairs_Return:
    return

@ Old previews can be continued at the stair landing without relocating a save.
@ Elsewhere downstairs, defer the new report until the next normal entry.
LegendsDownstairs_ResumeMale:
    setvar VAR_TEMP_2, 1
    getplayerxy VAR_0x8005, VAR_0x8006
    goto_if_ne VAR_0x8005, 8, LegendsDownstairs_End
    goto_if_ne VAR_0x8006, 3, LegendsDownstairs_End
    call LegendsDownstairs_SetupMale
    goto_if_ne VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_RIFT_REPORT, LegendsDownstairs_End
    setobjectxy LOCALID_PLAYERS_HOUSE_1F_MOM, 4, 5
    goto LegendsDownstairs_Report
LegendsDownstairs_ResumeFemale:
    setvar VAR_TEMP_2, 1
    getplayerxy VAR_0x8005, VAR_0x8006
    goto_if_ne VAR_0x8005, 2, LegendsDownstairs_End
    goto_if_ne VAR_0x8006, 3, LegendsDownstairs_End
    call LegendsDownstairs_SetupFemale
    goto_if_ne VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_RIFT_REPORT, LegendsDownstairs_End
    setobjectxy LOCALID_PLAYERS_HOUSE_1F_MOM, 6, 5
    goto LegendsDownstairs_Report
LegendsDownstairs_End:
    end

LegendsDownstairs_Report::
    lockall
    setvar VAR_TEMP_2, 1
    setvar VAR_0x8005, LOCALID_PLAYERS_HOUSE_1F_MOM
    playse SE_PIN
    applymovement LOCALID_PLAYERS_HOUSE_1F_MOM, Common_Movement_ExclamationMark
    waitmovement 0
    setspeaker SP_NAME_MOM
    msgbox LegendsDownstairs_Text_ComeLook, MSGBOX_DEFAULT
    closemessage
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsDownstairs_ApproachFemale
    applymovement LOCALID_PLAYER, PlayersHouse_1F_Movement_PlayerApproachTVForGymMale
    waitmovement 0
    applymovement LOCALID_PLAYERS_HOUSE_1F_MOM, PlayersHouse_1F_Movement_MomMakeRoomToSeeTVMale
    waitmovement 0
    applymovement LOCALID_PLAYER, PlayersHouse_1F_Movement_PlayerMoveToTVMale
    waitmovement 0
    goto LegendsDownstairs_Watch
LegendsDownstairs_ApproachFemale:
    applymovement LOCALID_PLAYER, PlayersHouse_1F_Movement_PlayerApproachTVForGymFemale
    waitmovement 0
    applymovement LOCALID_PLAYERS_HOUSE_1F_MOM, PlayersHouse_1F_Movement_MomMakeRoomToSeeTVFemale
    waitmovement 0
    applymovement LOCALID_PLAYER, PlayersHouse_1F_Movement_PlayerMoveToTVFemale
    waitmovement 0
LegendsDownstairs_Watch:
    applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterUp
    waitmovement 0
    playbgm MUS_ENCOUNTER_INTERVIEWER, FALSE
    special TurnOnTVScreen
    setspeaker LegendsDownstairs_Name_News
    msgbox LegendsDownstairs_Text_Report0, MSGBOX_DEFAULT
    setspeaker LegendsDownstairs_Name_News
    msgbox LegendsDownstairs_Text_Report1, MSGBOX_DEFAULT
    setspeaker LegendsDownstairs_Name_News
    msgbox LegendsDownstairs_Text_Report2, MSGBOX_DEFAULT
    setspeaker LegendsDownstairs_Name_News
    msgbox LegendsDownstairs_Text_Report3, MSGBOX_DEFAULT
    setspeaker LegendsDownstairs_Name_News
    msgbox LegendsDownstairs_Text_Report4, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsDownstairs_Text_Report5, MSGBOX_DEFAULT
    setspeaker LegendsDownstairs_Name_News
    msgbox LegendsDownstairs_Text_Report6, MSGBOX_DEFAULT
    setspeaker LegendsDownstairs_Name_News
    msgbox LegendsDownstairs_Text_Report7, MSGBOX_DEFAULT
    setspeaker LegendsDownstairs_Name_News
    msgbox LegendsDownstairs_Text_Report8, MSGBOX_DEFAULT
    setspeaker LegendsDownstairs_Name_News
    msgbox LegendsDownstairs_Text_Report9, MSGBOX_DEFAULT
    closemessage
    delay 25
    setspeaker SP_NAME_MOM
    msgbox LegendsDownstairs_Text_Report10, MSGBOX_DEFAULT
    closemessage
    delay 25
    setspeaker SP_NAME_PLAYER
    msgbox LegendsDownstairs_Text_Report11, MSGBOX_DEFAULT
    closemessage
    delay 25
    setspeaker SP_NAME_MOM
    msgbox LegendsDownstairs_Text_Report12, MSGBOX_DEFAULT
    closemessage
    delay 25
    setspeaker LegendsDownstairs_Name_News
    msgbox LegendsDownstairs_Text_Report13, MSGBOX_DEFAULT
    setspeaker LegendsDownstairs_Name_News
    msgbox LegendsDownstairs_Text_Report14, MSGBOX_DEFAULT
    closemessage
    special TurnOffTVScreen
    fadedefaultbgm
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsDownstairs_FaceElaraFemale
    applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterLeft
    goto LegendsDownstairs_AfterReport
LegendsDownstairs_FaceElaraFemale:
    applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterRight
LegendsDownstairs_AfterReport:
    waitmovement 0
    applymovement LOCALID_PLAYERS_HOUSE_1F_MOM, Common_Movement_FacePlayer
    waitmovement 0
    setspeaker SP_NAME_PLAYER
    msgbox LegendsDownstairs_Text_After0, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsDownstairs_Text_After1, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsDownstairs_Text_After2, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsDownstairs_Text_After3, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsDownstairs_Text_After4, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsDownstairs_Text_After5, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsDownstairs_Text_After6, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsDownstairs_Text_After7, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsDownstairs_Text_After8, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsDownstairs_Text_After9, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsDownstairs_Text_After10, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsDownstairs_Text_After11, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsDownstairs_Text_After12, MSGBOX_DEFAULT
    setspeaker SP_NAME_MOM
    msgbox LegendsDownstairs_Text_After13, MSGBOX_DEFAULT
    closemessage
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsDownstairs_SeatFemale
    applymovement LOCALID_PLAYERS_HOUSE_1F_MOM, PlayersHouse_1F_Movement_MomReturnToSeatMale
    waitmovement 0
    goto LegendsDownstairs_Finish
LegendsDownstairs_SeatFemale:
    applymovement LOCALID_PLAYERS_HOUSE_1F_MOM, PlayersHouse_1F_Movement_MomReturnToSeatFemale
    waitmovement 0
LegendsDownstairs_Finish:
    setflag FLAG_LA_WATCHED_RIFT_REPORT
    setflag FLAG_SYS_TV_HOME
    setvar VAR_LITTLEROOT_INTRO_STATE, LA_INTRO_COMPLETE
    setvar VAR_TEMP_1, 1
    setspeaker SP_NAME_NONE
    releaseall
    end

LegendsDownstairs_ElaraReminder::
    setspeaker SP_NAME_MOM
    msgbox LegendsDownstairs_Text_Reminder, MSGBOX_DEFAULT
    setspeaker SP_NAME_NONE
    release
    end

LegendsDownstairs_Name_News:
    .string "NEWS ANCHOR$"

LegendsDownstairs_Text_ComeLook:
    .string "{PLAYER}, come here a moment.\nYou should see this.$"

LegendsDownstairs_Text_Reminder:
    .string "Try the house next door for Professor\nBirch. And stay away from those rifts.$"

LegendsDownstairs_Text_Report0:
    .string "We interrupt our scheduled Petalburg\nGym report with a developing story.$"

LegendsDownstairs_Text_Report1:
    .string "Unstable openings have appeared\nacross Hoenn.\pScientists are calling them rifts.$"

LegendsDownstairs_Text_Report2:
    .string "Witnesses describe distant cities\nand unfamiliar mountains.\pThese places do not match the\nsurrounding landscape.$"

LegendsDownstairs_Text_Report3:
    .string "The views vanish as the rifts close.\pWhere they lead remains unknown.$"

LegendsDownstairs_Text_Report4:
    .string "None of the rifts have stayed stable.\pDo not approach or enter them.$"

LegendsDownstairs_Text_Report5:
    .string "{COLOR LIGHT_BLUE}Places on the other side...?$"

LegendsDownstairs_Text_Report6:
    .string "Unusual POKéMON outbreaks have been\nreported near the affected areas.$"

LegendsDownstairs_Text_Report7:
    .string "Some of these POKéMON are native\nto regions far beyond Hoenn.\pHow they arrived remains unknown.$"

LegendsDownstairs_Text_Report8:
    .string "Scientists are investigating a link\nbetween the rifts and outbreaks.$"

LegendsDownstairs_Text_Report9:
    .string "Lead scientist Colress is overseeing\nthe investigation.\pLocal researchers are assisting him.$"

LegendsDownstairs_Text_Report10:
    .string "(quietly) Colress...?\nWhat is he doing here...?$"

LegendsDownstairs_Text_Report11:
    .string "{COLOR LIGHT_BLUE}You know him?$"

LegendsDownstairs_Text_Report12:
    .string "I recognize the name.\nThat's all.$"

LegendsDownstairs_Text_Report13:
    .string "Report any unusual sightings to the\nresearch team.\pKeep a safe distance from all rifts.$"

LegendsDownstairs_Text_Report14:
    .string "We will bring you further updates as\ninformation is confirmed.$"

LegendsDownstairs_Text_After0:
    .string "{COLOR LIGHT_BLUE}Rifts, strange POKéMON...\nIs that what you wanted to tell me?$"

LegendsDownstairs_Text_After1:
    .string "I wanted you to hear it before you\nwent outside.$"

LegendsDownstairs_Text_After2:
    .string "Whatever those things are, they aren't\nsomewhere to go exploring.$"

LegendsDownstairs_Text_After3:
    .string "{COLOR LIGHT_BLUE}You don't have to look at me like that.$"

LegendsDownstairs_Text_After4:
    .string "Then don't give me a reason to.$"

LegendsDownstairs_Text_After5:
    .string "{COLOR LIGHT_BLUE}What about the POKéMON?\nAre they all right?$"

LegendsDownstairs_Text_After6:
    .string "I hope so. Professor Birch has been\nlooking into the sightings too.$"

LegendsDownstairs_Text_After7:
    .string "{COLOR LIGHT_BLUE}Maybe he'll know what's going on.$"

LegendsDownstairs_Text_After8:
    .string "Try the house next door first. His\nfamily should know where he's working.$"

LegendsDownstairs_Text_After9:
    .string "{COLOR LIGHT_BLUE}And Colress?$"

LegendsDownstairs_Text_After10:
    .string "Leave the scientists to their work.\pIf you see a rift, keep your distance.$"

LegendsDownstairs_Text_After11:
    .string "{COLOR LIGHT_BLUE}I'll be careful.$"

LegendsDownstairs_Text_After12:
    .string "That's not quite what I asked.$"

LegendsDownstairs_Text_After13:
    .string "Go on. And keep that package with you.\nWe still don't know who sent it.$"

