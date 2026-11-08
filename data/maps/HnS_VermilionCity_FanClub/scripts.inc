HnS_VermilionCity_FanClub_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VermilionCity_FanClub_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VermilionCity_FanClub_Next
 release
 end
HnS_VermilionCity_FanClub_Next::
 warp MAP_HNS_REGION_VERMILIONCITY_HOUSE1, 6, 3
 waitstate
 release
 end
