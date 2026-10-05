@ Fixed source routes; existing map files remain unchanged.

HyperSinnoh_RockClimb_SE::
    lockall
    call HyperSinnoh_RockClimbPrompt
    goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
    applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_RockClimbMovement_SE
    waitmovement OBJ_EVENT_ID_PLAYER
    goto HyperSinnoh_RockClimbEnd
HyperSinnoh_RockClimbMovement_SE:
    walk_right
    walk_slow_diag_southeast
    walk_slow_diag_southeast
    walk_slow_diag_southeast
    walk_slow_diag_southeast
    walk_right
    step_end

HyperSinnoh_RockClimb_NW::
    lockall
    call HyperSinnoh_RockClimbPrompt
    goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
    applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_RockClimbMovement_NW
    waitmovement OBJ_EVENT_ID_PLAYER
    goto HyperSinnoh_RockClimbEnd
HyperSinnoh_RockClimbMovement_NW:
    walk_left
    walk_slow_diag_northwest
    walk_slow_diag_northwest
    walk_slow_diag_northwest
    walk_slow_diag_northwest
    walk_left
    step_end

HyperSinnoh_RockClimb_NE::
    lockall
    call HyperSinnoh_RockClimbPrompt
    goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
    applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_RockClimbMovement_NE
    waitmovement OBJ_EVENT_ID_PLAYER
    goto HyperSinnoh_RockClimbEnd
HyperSinnoh_RockClimbMovement_NE:
    walk_right
    walk_slow_diag_northeast
    walk_slow_diag_northeast
    walk_right
    step_end

HyperSinnoh_RockClimb_SW::
    lockall
    call HyperSinnoh_RockClimbPrompt
    goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
    applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_RockClimbMovement_SW
    waitmovement OBJ_EVENT_ID_PLAYER
    goto HyperSinnoh_RockClimbEnd
HyperSinnoh_RockClimbMovement_SW:
    walk_left
    walk_slow_diag_southwest
    walk_slow_diag_southwest
    walk_left
    step_end

HyperSinnoh_RockClimbPrompt:
    callnative HyperSinnoh_RockClimbSelectMon
    msgbox Text_WantToRockClimb, MSGBOX_YESNO
    goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbReturn
    goto_if_eq VAR_0x8004, PARTY_SIZE, HyperSinnoh_RockClimbHelper
    bufferpartymonnick STR_VAR_1, VAR_0x8004
    setfieldeffectargument 0, VAR_0x8004
    msgbox Text_MonUsedRockClimb, MSGBOX_DEFAULT
    closemessage
    dofieldeffect FLDEFF_FIELD_MOVE_SHOW_MON_INIT
    waitfieldeffect FLDEFF_FIELD_MOVE_SHOW_MON
    setvar VAR_RESULT, YES
    return
HyperSinnoh_RockClimbHelper:
    closemessage
    showmonpic SPECIES_BIBAREL, 10, 3
    playmoncry SPECIES_BIBAREL, CRY_MODE_NORMAL
    msgbox HyperSinnoh_RockClimbHelperText, MSGBOX_DEFAULT
    waitmoncry
    hidemonpic
    closemessage
    setvar VAR_RESULT, YES
HyperSinnoh_RockClimbReturn:
    return
HyperSinnoh_RockClimbEnd:
    releaseall
    end
HyperSinnoh_RockClimbHelperText:
    .string "You used the ride gear to call a\n"
    .string "wild Bibarel to help you climb!$"
