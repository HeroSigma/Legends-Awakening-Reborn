LaCollection_Blocked::
    lockall
    msgbox LaCollection_Blocked_Text, MSGBOX_DEFAULT
    releaseall
    end

LaCollection_Blocked_Text:
    .string "This activity is unavailable while\n"
    .string "60-box collection mode is enabled.$"
