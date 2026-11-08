HnS_RuinsOfAlph_WordsRoom3_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_RuinsOfAlph_WordsRoom3_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_RuinsOfAlph_WordsRoom3_Next
 release
 end
HnS_RuinsOfAlph_WordsRoom3_Next::
 warp MAP_HNS_REGION_RUINSOFALPH_WORDSROOM4, 10, 6
 waitstate
 release
 end
