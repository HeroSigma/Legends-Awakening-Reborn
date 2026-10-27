HnsRegion_OnTransition::
 setflag FLAG_HIDE_HNS_PLACEHOLDER_VARIANTS
 end
HnsRegion_NoOp::
 end
HnsRegion_Placeholder::
 lock
 faceplayer
 msgbox HnsRegion_PlaceholderText, MSGBOX_DEFAULT
 release
 end
HnsRegion_Sign::
 msgbox HnsRegion_PlaceholderText, MSGBOX_SIGN
 end
HnsRegion_PlaceholderText:
 .string "This area is under construction.\p"
 .string "Story and services are coming later.$"
HnsRegion_InspectText:
 .string "Regional map inspection.\p"
 .string "Visit the next preserved map?$"
