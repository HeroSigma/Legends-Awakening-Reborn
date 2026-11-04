# BW battle UI

Adapted from Mudskip's BW battle UI, https://github.com/mudskipper13/pokeemerald/tree/feature/bwBattleUI at b7989298. Feature changes were isolated against its upstream parent 68a5890c, rather than replacing the project's battle engine. Original UI code and art remain credited to Mudskip and the contributors credited by that branch. The selection cursor has Legends Awakening teal accents.

Includes action and move panels, outlined health-box text, HP/EXP bars, party-ball summaries, ability popups and gimmick controls. Shared battle text graphics used by trade and egg hatch are routed through the same UI loader. Wider subsprite coordinates support the new panel layout; no save structure changes are made.

Compatibility adaptations retain the project's DamageContext calculations, dynamic move descriptions, type previews, modern PP field names, SwSh bag and party callbacks, outdoor time-of-day lighting and scripted battle restrictions. Existing fonts keep their IDs; BW outlined fonts are appended and included in the space-saving build. Move names reserve space beside PP. New palettes are confined to the battle UI.

Native emulator reports use disposable saves only. Coverage includes four-move navigation, description opening/closing, return to actions, Mega/Z/Tera availability and selection/cancellation, UI-only previews of locked Dynamax/Ultra Burst triggers, bag healing/capture, party cancellation/switching, day/night background isolation, dynamic power/accuracy calculations, and the full Littleroot chapter including Red's forced-loss battle and the Route 103 four-trainer battle in both storage modes. Preview fixtures do not grant locked gimmicks to actual saves.
