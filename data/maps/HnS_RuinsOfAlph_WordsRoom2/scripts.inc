HnS_RuinsOfAlph_WordsRoom2_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_RuinsOfAlph_WordsRoom2_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_RuinsOfAlph_WordsRoom2_Next
 release
 end
HnS_RuinsOfAlph_WordsRoom2_Next::
 warp MAP_HNS_REGION_RUINSOFALPH_WORDSROOM3, 9, 6
 waitstate
 release
 end
