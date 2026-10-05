@ Project vertical traversal on inspected Hyper rock strips.
HyperSinnoh_VerticalClimb_0_NORTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_0_NORTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_0_NORTH_Movement:
	walk_up
	walk_up
	walk_up
	walk_up
	step_end
HyperSinnoh_VerticalClimb_0_SOUTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_0_SOUTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_0_SOUTH_Movement:
	walk_down
	walk_down
	walk_down
	walk_down
	step_end
HyperSinnoh_VerticalClimb_1_NORTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_1_NORTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_1_NORTH_Movement:
	walk_up
	walk_up
	walk_up
	walk_up
	step_end
HyperSinnoh_VerticalClimb_1_SOUTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_1_SOUTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_1_SOUTH_Movement:
	walk_down
	walk_down
	walk_down
	walk_down
	step_end
HyperSinnoh_VerticalClimb_2_NORTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_2_NORTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_2_NORTH_Movement:
	walk_up
	walk_up
	step_end
HyperSinnoh_VerticalClimb_2_SOUTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_2_SOUTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_2_SOUTH_Movement:
	walk_down
	walk_down
	step_end
HyperSinnoh_VerticalClimb_3_NORTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_3_NORTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_3_NORTH_Movement:
	walk_up
	walk_up
	step_end
HyperSinnoh_VerticalClimb_3_SOUTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_3_SOUTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_3_SOUTH_Movement:
	walk_down
	walk_down
	step_end
HyperSinnoh_VerticalClimb_4_NORTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_4_NORTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_4_NORTH_Movement:
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	step_end
HyperSinnoh_VerticalClimb_4_SOUTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_4_SOUTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_4_SOUTH_Movement:
	walk_down
	walk_down
	walk_down
	walk_down
	walk_down
	walk_down
	step_end
HyperSinnoh_VerticalClimb_5_NORTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_5_NORTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_5_NORTH_Movement:
	walk_up
	walk_up
	walk_up
	step_end
HyperSinnoh_VerticalClimb_5_SOUTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_5_SOUTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_5_SOUTH_Movement:
	walk_down
	walk_down
	walk_down
	step_end
HyperSinnoh_VerticalClimb_6_NORTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_6_NORTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_6_NORTH_Movement:
	walk_up
	walk_up
	walk_up
	step_end
HyperSinnoh_VerticalClimb_6_SOUTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_6_SOUTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_6_SOUTH_Movement:
	walk_down
	walk_down
	walk_down
	step_end
HyperSinnoh_VerticalClimb_7_NORTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_7_NORTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_7_NORTH_Movement:
	walk_up
	walk_up
	step_end
HyperSinnoh_VerticalClimb_7_SOUTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_7_SOUTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_7_SOUTH_Movement:
	walk_down
	walk_down
	step_end
HyperSinnoh_VerticalClimb_8_NORTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_8_NORTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_8_NORTH_Movement:
	walk_up
	walk_up
	walk_up
	step_end
HyperSinnoh_VerticalClimb_8_SOUTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_8_SOUTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_8_SOUTH_Movement:
	walk_down
	walk_down
	walk_down
	step_end
HyperSinnoh_VerticalClimb_9_NORTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_9_NORTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_9_NORTH_Movement:
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	step_end
HyperSinnoh_VerticalClimb_9_SOUTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_9_SOUTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_9_SOUTH_Movement:
	walk_down
	walk_down
	walk_down
	walk_down
	walk_down
	step_end
HyperSinnoh_VerticalClimb_10_NORTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_10_NORTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_10_NORTH_Movement:
	walk_up
	walk_up
	walk_up
	walk_up
	step_end
HyperSinnoh_VerticalClimb_10_SOUTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_10_SOUTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_10_SOUTH_Movement:
	walk_down
	walk_down
	walk_down
	walk_down
	step_end
HyperSinnoh_VerticalClimb_11_NORTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_11_NORTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_11_NORTH_Movement:
	walk_up
	walk_up
	walk_up
	step_end
HyperSinnoh_VerticalClimb_11_SOUTH::
	lockall
	call HyperSinnoh_RockClimbPrompt
	goto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd
	applymovement OBJ_EVENT_ID_PLAYER, HyperSinnoh_VerticalClimb_11_SOUTH_Movement
	waitmovement OBJ_EVENT_ID_PLAYER
	goto HyperSinnoh_RockClimbEnd
HyperSinnoh_VerticalClimb_11_SOUTH_Movement:
	walk_down
	walk_down
	walk_down
	step_end
