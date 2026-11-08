HnS_CherrygroveCity_House2_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CherrygroveCity_House2_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CherrygroveCity_House2_Next
 release
 end
HnS_CherrygroveCity_House2_Next::
 warp MAP_HNS_REGION_CHERRYGROVECITY_HOUSE3, 4, 5
 waitstate
 release
 end
