@ Hazel and both rivals, using the canonical next-door house for either player.
LegendsNextDoor_SetupMale::
    setvar VAR_0x8004, MALE
    goto LegendsNextDoor_Setup
LegendsNextDoor_SetupFemale::
    setvar VAR_0x8004, FEMALE
LegendsNextDoor_Setup:
    setvar VAR_TEMP_3, 0
    setflag FLAG_HIDE_LA_NEXTDOOR_RIVALS
    goto_if_unset FLAG_LA_INTRO_ACTIVE, LegendsNextDoor_Return
    goto_if_unset FLAG_LA_WATCHED_RIFT_REPORT, LegendsNextDoor_Return
    goto_if_set FLAG_RESCUED_BIRCH, LegendsNextDoor_Return
    checkplayergender
    goto_if_ne VAR_RESULT, VAR_0x8004, LegendsNextDoor_Return
    goto_if_set FLAG_LA_MET_BRENDAN_AND_MAY, LegendsNextDoor_SetResident
    clearflag FLAG_HIDE_LA_NEXTDOOR_RIVALS
    setvar VAR_TEMP_3, 1
LegendsNextDoor_Return:
    return

@ Called by the native first greeting after Hazel's existing approach movement.
LegendsNextDoor_TryGreeting::
    goto_if_unset FLAG_LA_INTRO_ACTIVE, LegendsNextDoor_Return
    goto_if_unset FLAG_LA_WATCHED_RIFT_REPORT, LegendsNextDoor_Return
    goto_if_set FLAG_LA_MET_BRENDAN_AND_MAY, LegendsNextDoor_Return
    goto_if_set FLAG_RESCUED_BIRCH, LegendsNextDoor_Return
    setvar VAR_TEMP_4, 1
    goto LegendsNextDoor_Scene

@ Upgrade pre-Birch preview saves that already consumed the native family greeting.
@ No player relocation or actor approach is performed for these arbitrary positions.
LegendsNextDoor_Resume:
    lockall
    setvar VAR_TEMP_4, 0
LegendsNextDoor_Scene:
    setvar VAR_TEMP_3, 0
    lockall
    call LegendsNextDoor_HazelFacePlayer
    setspeaker SP_NAME_HAZEL
    msgbox LegendsNextDoor_Text_0, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsNextDoor_Text_1, MSGBOX_DEFAULT
    setspeaker SP_NAME_HAZEL
    msgbox LegendsNextDoor_Text_2, MSGBOX_DEFAULT
    setspeaker SP_NAME_HAZEL
    msgbox LegendsNextDoor_Text_3, MSGBOX_DEFAULT
    setspeaker SP_NAME_HAZEL
    msgbox LegendsNextDoor_Text_4, MSGBOX_DEFAULT
    closemessage
    call_if_eq VAR_TEMP_4, 1, LegendsNextDoor_Approach
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsNextDoor_Text_5, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsNextDoor_Text_6, MSGBOX_DEFAULT
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsNextDoor_Text_7, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsNextDoor_Text_8, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsNextDoor_Text_9, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsNextDoor_Text_10, MSGBOX_DEFAULT
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsNextDoor_Text_11, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsNextDoor_Text_12, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsNextDoor_Text_13, MSGBOX_DEFAULT
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsNextDoor_Text_14, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsNextDoor_Text_15, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsNextDoor_Text_16, MSGBOX_DEFAULT
    setspeaker SP_NAME_HAZEL
    msgbox LegendsNextDoor_Text_17, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsNextDoor_Text_18, MSGBOX_DEFAULT
    setspeaker SP_NAME_HAZEL
    msgbox LegendsNextDoor_Text_19, MSGBOX_DEFAULT
    setspeaker SP_NAME_HAZEL
    msgbox LegendsNextDoor_Text_20, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsNextDoor_Text_21, MSGBOX_DEFAULT
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsNextDoor_Text_22, MSGBOX_DEFAULT
    setspeaker SP_NAME_HAZEL
    msgbox LegendsNextDoor_Text_23, MSGBOX_DEFAULT
    setspeaker SP_NAME_PLAYER
    msgbox LegendsNextDoor_Text_24, MSGBOX_DEFAULT
    closemessage
    setflag FLAG_LA_MET_BRENDAN_AND_MAY
    setflag FLAG_MET_RIVAL_MOM
    setvar VAR_LITTLEROOT_RIVAL_STATE, 3
    setvar VAR_LITTLEROOT_TOWN_STATE, 1
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsNextDoor_CompleteFemale
    setvar VAR_LITTLEROOT_HOUSES_STATE_BRENDAN, 2
    goto LegendsNextDoor_Complete
LegendsNextDoor_CompleteFemale:
    setvar VAR_LITTLEROOT_HOUSES_STATE_MAY, 2
LegendsNextDoor_Complete:
    setflag FLAG_HIDE_LITTLEROOT_TOWN_BRENDANS_HOUSE_BRENDAN
    setflag FLAG_HIDE_LITTLEROOT_TOWN_MAYS_HOUSE_MAY
    setflag FLAG_HIDE_LITTLEROOT_TOWN_BRENDANS_HOUSE_RIVAL_BEDROOM
    setflag FLAG_HIDE_LITTLEROOT_TOWN_MAYS_HOUSE_RIVAL_BEDROOM
    setflag FLAG_HIDE_LITTLEROOT_TOWN_BRENDANS_HOUSE_2F_POKE_BALL
    setflag FLAG_HIDE_LITTLEROOT_TOWN_MAYS_HOUSE_2F_POKE_BALL
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsNextDoor_DepartLinesFemale
    setspeaker SP_NAME_MAY
    msgbox LegendsNextDoor_Text_MayStays, MSGBOX_DEFAULT
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsNextDoor_Text_BrendanLeaves, MSGBOX_DEFAULT
    goto LegendsNextDoor_StartDepart
LegendsNextDoor_DepartLinesFemale:
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsNextDoor_Text_BrendanStays, MSGBOX_DEFAULT
    setspeaker SP_NAME_MAY
    msgbox LegendsNextDoor_Text_MayLeaves, MSGBOX_DEFAULT
LegendsNextDoor_StartDepart:
    closemessage
    call LegendsNextDoor_Depart
    setflag FLAG_HIDE_LA_NEXTDOOR_RIVALS
    call LegendsNextDoor_SetResident
    call LegendsNextDoor_HazelFacePlayer
    releaseall
    end

@ Move Hazel out of the line between the player and the two rivals.
LegendsNextDoor_Approach:
    applymovement LOCALID_RIVALS_HOUSE_1F_MOM, LegendsNextDoor_HazelStepAside
    waitmovement 0
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsNextDoor_ApproachFemale
    applymovement LOCALID_LA_NEXTDOOR_BRENDAN, LegendsNextDoor_BrendanApproachMale
    waitmovement 0
    applymovement LOCALID_LA_NEXTDOOR_MAY, LegendsNextDoor_MayApproachMale
    waitmovement 0
    goto LegendsNextDoor_FacePlayer
LegendsNextDoor_ApproachFemale:
    applymovement LOCALID_LA_NEXTDOOR_BRENDAN, LegendsNextDoor_BrendanApproachFemale
    waitmovement 0
    applymovement LOCALID_LA_NEXTDOOR_MAY, LegendsNextDoor_MayApproachFemale
    waitmovement 0
LegendsNextDoor_FacePlayer:
    call LegendsNextDoor_HazelFacePlayer
    applymovement LOCALID_LA_NEXTDOOR_BRENDAN, Common_Movement_FacePlayer
    applymovement LOCALID_LA_NEXTDOOR_MAY, Common_Movement_FacePlayer
    waitmovement 0
    return

LegendsNextDoor_Depart:
    @ Arbitrary-position preview resumes never path actors through the player.
    goto_if_eq VAR_TEMP_4, 0, LegendsNextDoor_RemoveResumeActors
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsNextDoor_DepartFemale
    applymovement LOCALID_LA_NEXTDOOR_MAY, LegendsNextDoor_MayToStairs
    waitmovement 0
    playse SE_EXIT
    removeobject LOCALID_LA_NEXTDOOR_MAY
    applymovement LOCALID_LA_NEXTDOOR_BRENDAN, LegendsNextDoor_BrendanToDoor
    waitmovement 0
    playse SE_EXIT
    removeobject LOCALID_LA_NEXTDOOR_BRENDAN
    return
LegendsNextDoor_DepartFemale:
    applymovement LOCALID_LA_NEXTDOOR_MAY, LegendsNextDoor_MayToDoor
    waitmovement 0
    playse SE_EXIT
    removeobject LOCALID_LA_NEXTDOOR_MAY
    applymovement LOCALID_RIVALS_HOUSE_1F_MOM, Common_Movement_WalkLeft
    waitmovement 0
    applymovement LOCALID_LA_NEXTDOOR_BRENDAN, LegendsNextDoor_BrendanToStairs
    waitmovement 0
    playse SE_EXIT
    removeobject LOCALID_LA_NEXTDOOR_BRENDAN
    return
LegendsNextDoor_RemoveResumeActors:
    removeobject LOCALID_LA_NEXTDOOR_MAY
    removeobject LOCALID_LA_NEXTDOOR_BRENDAN
    return

@ Reconcile already-completed preview saves as well as the new departure.
LegendsNextDoor_SetResident:
    setflag FLAG_HIDE_LA_NEXTDOOR_RIVALS
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsNextDoor_SetResidentFemale
    clearflag FLAG_HIDE_LITTLEROOT_TOWN_MAYS_HOUSE_RIVAL_BEDROOM
    return
LegendsNextDoor_SetResidentFemale:
    clearflag FLAG_HIDE_LITTLEROOT_TOWN_BRENDANS_HOUSE_RIVAL_BEDROOM
    return

LegendsNextDoor_SetupRoomMale::
    setvar VAR_0x8004, MALE
    goto LegendsNextDoor_SetupRoom
LegendsNextDoor_SetupRoomFemale::
    setvar VAR_0x8004, FEMALE
LegendsNextDoor_SetupRoom:
    goto_if_unset FLAG_LA_MET_BRENDAN_AND_MAY, LegendsNextDoor_Return
    goto_if_set FLAG_RESCUED_BIRCH, LegendsNextDoor_Return
    checkplayergender
    goto_if_ne VAR_RESULT, VAR_0x8004, LegendsNextDoor_Return
    call LegendsNextDoor_SetResident
    @ The native rival state positions subsequent visits at the PC.
    goto_if_set FLAG_LA_RIVAL_SETTLED_AT_PC, LegendsNextDoor_Return
    setvar VAR_TEMP_3, 2
    goto_if_eq VAR_RESULT, FEMALE, LegendsNextDoor_PlaceRoomFemale
    setobjectxyperm LOCALID_RIVALS_HOUSE_2F_RIVAL, 2, 3
    setobjectmovementtype LOCALID_RIVALS_HOUSE_2F_RIVAL, MOVEMENT_TYPE_FACE_RIGHT
    return
LegendsNextDoor_PlaceRoomFemale:
    setobjectxyperm LOCALID_RIVALS_HOUSE_2F_RIVAL, 6, 3
    setobjectmovementtype LOCALID_RIVALS_HOUSE_2F_RIVAL, MOVEMENT_TYPE_FACE_LEFT
    return
LegendsNextDoor_RoomToPC:
    lockall
    setvar VAR_TEMP_3, 0
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsNextDoor_RoomToPCFemale
    applymovement LOCALID_RIVALS_HOUSE_2F_RIVAL, LegendsNextDoor_MayRoomPC
    waitmovement 0
    goto LegendsNextDoor_PCReady
LegendsNextDoor_RoomToPCFemale:
    applymovement LOCALID_RIVALS_HOUSE_2F_RIVAL, LegendsNextDoor_BrendanRoomPC
    waitmovement 0
LegendsNextDoor_PCReady:
    playse SE_PC_ON
    setflag FLAG_LA_RIVAL_SETTLED_AT_PC
    releaseall
    end
LegendsNextDoor_TryRoomTalk:
    goto_if_unset FLAG_LA_MET_BRENDAN_AND_MAY, LegendsNextDoor_Return
    goto_if_set FLAG_RESCUED_BIRCH, LegendsNextDoor_Return
    checkplayergender
    goto_if_eq VAR_RESULT, FEMALE, LegendsNextDoor_TalkBrendan
    goto LegendsNextDoor_TalkMay

LegendsNextDoor_TalkHazel::
    lock
    faceplayer
    setspeaker SP_NAME_HAZEL
    goto_if_set FLAG_RESCUED_BIRCH, LegendsNextDoor_HazelLater
    msgbox LegendsNextDoor_Text_HazelReminder, MSGBOX_DEFAULT
    release
    end
LegendsNextDoor_HazelLater:
    msgbox LegendsNextDoor_Text_HazelLater, MSGBOX_DEFAULT
    release
    end
LegendsNextDoor_TalkBrendan::
    lock
    faceplayer
    setspeaker SP_NAME_BRENDAN
    msgbox LegendsNextDoor_Text_BrendanReminder, MSGBOX_DEFAULT
    release
    end
LegendsNextDoor_TalkMay::
    lock
    faceplayer
    setspeaker SP_NAME_MAY
    msgbox LegendsNextDoor_Text_MayReminder, MSGBOX_DEFAULT
    release
    end

LegendsNextDoor_Text_0:
    .string "You must be {PLAYER}.\nElara said you might stop by.$"

LegendsNextDoor_Text_1:
    .string "{COLOR LIGHT_BLUE}I'm looking for Professor Birch.$"

LegendsNextDoor_Text_2:
    .string "I'm Hazel. Birch meant to stay\nat the lab.\pThen he heard about more sightings.$"

LegendsNextDoor_Text_3:
    .string "I was sorting his field notes.\pHe's finding POKéMON missing from\nall his older records.$"

LegendsNextDoor_Text_4:
    .string "These are our children, Brendan\nand May. They help with his surveys.$"

LegendsNextDoor_Text_5:
    .string "{COLOR GREEN}If you're looking for Dad, try\nwherever he was told not to wander.$"

LegendsNextDoor_Text_6:
    .string "{COLOR RED}He's checking sightings, Brendan.\nThat isn't the same as getting lost.$"

LegendsNextDoor_Text_7:
    .string "{COLOR GREEN}Those aren't mutually exclusive.$"

LegendsNextDoor_Text_8:
    .string "{COLOR RED}You saw the report, right?\pI wonder if those POKéMON\nare frightened.$"

LegendsNextDoor_Text_9:
    .string "{COLOR RED}Strange places. Strange people.\pThey don't know what's happened\nto them either.$"

LegendsNextDoor_Text_10:
    .string "{COLOR LIGHT_BLUE}Yeah. I asked Elara about that too.$"

LegendsNextDoor_Text_11:
    .string "{COLOR GREEN}I'd like to know how they got here.\pWithout sticking my head in a rift,\nbefore anyone asks.$"

LegendsNextDoor_Text_12:
    .string "{COLOR LIGHT_BLUE}Elara gave me much the same warning.$"

LegendsNextDoor_Text_13:
    .string "{COLOR RED}Good. Then that's one less person\nI have to talk out of something.$"

LegendsNextDoor_Text_14:
    .string "{COLOR GREEN}Speaking of which, when you get a\nPOKéMON, we should have a battle.$"

LegendsNextDoor_Text_15:
    .string "{COLOR RED}You'll have to battle me too.\pDon't let Brendan claim the only\nchallenge around here.$"

LegendsNextDoor_Text_16:
    .string "{COLOR LIGHT_BLUE}I came looking for a professor\nand got two challenges instead.$"

LegendsNextDoor_Text_17:
    .string "A very efficient introduction.$"

LegendsNextDoor_Text_18:
    .string "{COLOR LIGHT_BLUE}Is Colress working with Birch?$"

LegendsNextDoor_Text_19:
    .string "Birch shares his observations\nwith the research team.\pColress is coordinating their\ninvestigation.$"

LegendsNextDoor_Text_20:
    .string "Birch puts the POKéMON first.\pSomeone has to find out how\nthey're coping.$"

LegendsNextDoor_Text_21:
    .string "{COLOR RED}Dad said he was checking Route 101.\pLet's finish up and get going.$"

LegendsNextDoor_Text_22:
    .string "{COLOR GREEN}Try the lab on your way.\pIf he's gone, take the path north\nto Route 101.$"

LegendsNextDoor_Text_23:
    .string "Stay on the path until you have\na POKéMON of your own.\pIf something looks wrong, get help.$"

LegendsNextDoor_Text_24:
    .string "{COLOR LIGHT_BLUE}Find Birch. Stay on the path.\nNo exploring rifts.\pThat should be simple enough.$"

LegendsNextDoor_Text_HazelReminder:
    .string "Try Birch's lab, then the path north\nto Route 101.\pOne of them is checking the PC.\nThe other has already headed out.$"

LegendsNextDoor_Text_HazelLater:
    .string "Thank you for helping my husband.\pPlease look after yourself out there.\nElara will want to hear how you are.$"

LegendsNextDoor_Text_BrendanReminder:
    .string "{COLOR GREEN}I'm checking Dad's survey notes.\pFind him first. Our battle can wait\nuntil you've got a partner.$"

LegendsNextDoor_Text_MayReminder:
    .string "{COLOR RED}If you see an unfamiliar POKéMON,\nwatch it from a safe distance.\pBeing lost doesn't make it dangerous.$"

LegendsNextDoor_HazelStepAside:
    walk_up
    step_end

LegendsNextDoor_BrendanApproachMale:
    walk_down
    walk_down
    walk_down
    walk_left
    step_end

LegendsNextDoor_BrendanApproachFemale:
    walk_down
    walk_down
    walk_down
    walk_right
    step_end

LegendsNextDoor_MayApproachMale:
    walk_left
    walk_left
    walk_left
    walk_down
    walk_down
    step_end

LegendsNextDoor_MayApproachFemale:
    walk_right
    walk_right
    walk_right
    walk_down
    walk_down
    step_end

LegendsNextDoor_MayToStairs:
    walk_up
    walk_up
    walk_up
    walk_up
    walk_up
    step_end

LegendsNextDoor_BrendanToDoor:
    walk_right
    walk_up
    walk_up
    walk_left
    walk_left
    walk_left
    walk_down
    walk_down
    walk_in_place_faster_down
    step_end

LegendsNextDoor_MayToDoor:
    walk_right
    walk_down
    walk_in_place_faster_down
    step_end

LegendsNextDoor_BrendanToStairs:
    walk_up
    walk_right
    walk_up
    walk_up
    walk_up
    walk_up
    walk_up
    step_end

LegendsNextDoor_MayRoomPC:
    walk_up
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_right
    walk_in_place_faster_up
    step_end

LegendsNextDoor_BrendanRoomPC:
    walk_up
    walk_left
    walk_left
    walk_left
    walk_left
    walk_left
    walk_left
    walk_in_place_faster_up
    step_end

LegendsNextDoor_Text_MayStays:
    .string "{COLOR RED}I'll check Dad's notes on my PC.\nThen I'll catch up.$"
LegendsNextDoor_Text_BrendanLeaves:
    .string "{COLOR GREEN}I'll head out. See you around,\n{PLAYER}!$"
LegendsNextDoor_Text_BrendanStays:
    .string "{COLOR GREEN}I'll get Dad's notes from my PC.\nDon't start without me!$"
LegendsNextDoor_Text_MayLeaves:
    .string "{COLOR RED}I'll take the kit outside.\nSee you soon, {PLAYER}!$"

@ Face the player without relying on the last-talked object in a cutscene.
LegendsNextDoor_HazelFacePlayer:
    applymovement LOCALID_RIVALS_HOUSE_1F_MOM, Common_Movement_FacePlayer
    waitmovement 0
    return
