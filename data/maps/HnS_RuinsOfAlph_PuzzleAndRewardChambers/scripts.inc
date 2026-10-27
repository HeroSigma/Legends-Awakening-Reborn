HnS_RuinsOfAlph_PuzzleAndRewardChambers_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_RuinsOfAlph_PuzzleAndRewardChambers_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_RuinsOfAlph_PuzzleAndRewardChambers_Next
 release
 end
HnS_RuinsOfAlph_PuzzleAndRewardChambers_Next::
 warp MAP_HNS_REGION_UNIONCAVE_1F, 24, 31
 waitstate
 release
 end
