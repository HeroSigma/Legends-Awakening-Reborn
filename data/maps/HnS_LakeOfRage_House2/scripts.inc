HnS_LakeOfRage_House2_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_LakeOfRage_House2_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_LakeOfRage_House2_Next
 release
 end
HnS_LakeOfRage_House2_Next::
 warp MAP_HNS_REGION_BLACKTHORNCITY_POKEMONCENTER, 8, 5
 waitstate
 release
 end
