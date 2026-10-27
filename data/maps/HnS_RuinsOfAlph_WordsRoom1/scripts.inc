HnS_RuinsOfAlph_WordsRoom1_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_RuinsOfAlph_WordsRoom1_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_RuinsOfAlph_WordsRoom1_Next
 release
 end
HnS_RuinsOfAlph_WordsRoom1_Next::
 warp MAP_HNS_REGION_RUINSOFALPH_WORDSROOM2, 10, 6
 waitstate
 release
 end
