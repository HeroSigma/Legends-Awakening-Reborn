# Water mounts

Eligible supported Surf Pokemon automatically become visible mounts after the native Surf field-effect sequence. While already surfing, Party -> Follower -> Ride selects a compatible healthy swimmer. Surf's existing badge unlock and field-move compatibility are required. Normal water entry, shoreline hops, currents, waterfalls, collisions, encounters and native Surf state remain in charge.

L+R and Recall cannot dismount offshore. A fainted or absent mount safely returns to the native Surf sprite and blob. Menus and battles retain Surf and the proper protagonist gender. Native Surf remains safe when reloading without temporary mount state. Indoors/cave water can use water mounts while ground riding remains outdoor-only.

Two appended graphics aliases distinguish seated water avatars from seated ground avatars during native state reconstruction. No save structures change; Surf remains bit 3 and Dive remains bit 4. The native Surf blob remains allocated for its lifecycle but hides while a mount is drawn. Its bob callback does not overwrite rider positioning, and only ride-owned visibility changes are restored.

Validation: 74 native water checks across both protagonists and both storage modes, native A-button Surf entry, missing badge rejection, offshore dismount refusal, movement, party return, invalid species rejection, fainted-mount fallback, battle escape/return, battery save/reload and shore exit. Test batteries are isolated from the user save. Swimming/flying mounts additionally require Fly permission and retain Surf when landing over water. The report pins the tested ROM.
