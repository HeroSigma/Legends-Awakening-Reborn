HnS_VermilionCity_House3_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VermilionCity_House3_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VermilionCity_House3_Next
 release
 end
HnS_VermilionCity_House3_Next::
 warp MAP_HNS_REGION_LAVENDERTOWN_POKEMONCENTER, 7, 5
 waitstate
 release
 end
