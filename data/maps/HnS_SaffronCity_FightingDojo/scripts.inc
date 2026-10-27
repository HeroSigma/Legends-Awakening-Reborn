HnS_SaffronCity_FightingDojo_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SaffronCity_FightingDojo_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SaffronCity_FightingDojo_Next
 release
 end
HnS_SaffronCity_FightingDojo_Next::
 warp MAP_HNS_REGION_SAFFRONCITY_FIGHTINGDOJOVIP, 21, 21
 waitstate
 release
 end
