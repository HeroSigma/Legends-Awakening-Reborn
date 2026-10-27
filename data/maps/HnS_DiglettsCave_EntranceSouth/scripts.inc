HnS_DiglettsCave_EntranceSouth_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_DiglettsCave_EntranceSouth_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_DiglettsCave_EntranceSouth_Next
 release
 end
HnS_DiglettsCave_EntranceSouth_Next::
 warp MAP_HNS_REGION_DIGLETTSCAVE_TUNNEL, 42, 40
 waitstate
 release
 end
