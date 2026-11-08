HnS_RuinsOfAlph_WordsRoom4_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_RuinsOfAlph_WordsRoom4_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_RuinsOfAlph_WordsRoom4_Next
 release
 end
HnS_RuinsOfAlph_WordsRoom4_Next::
 warp MAP_HNS_REGION_ROUTE19_CAVE, 8, 10
 waitstate
 release
 end
