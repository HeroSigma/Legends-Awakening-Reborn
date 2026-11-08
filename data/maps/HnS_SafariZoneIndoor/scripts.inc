HnS_SafariZoneIndoor_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SafariZoneIndoor_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SafariZoneIndoor_Next
 release
 end
HnS_SafariZoneIndoor_Next::
 warp MAP_HNS_REGION_SOUTHERNISLAND_EXTERIOR, 16, 17
 waitstate
 release
 end
