HnS_LilycoveCity_ContestLobby_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_LilycoveCity_ContestLobby_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_LilycoveCity_ContestLobby_Next
 release
 end
HnS_LilycoveCity_ContestLobby_Next::
 warp MAP_HNS_REGION_TRADECENTER, 6, 4
 waitstate
 release
 end
