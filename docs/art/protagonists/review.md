# Aren and Aria player artwork canary

Aren and Aria replace the native playable Brendan and May standing/walking artwork. Both sheets use the native 144x32 indexed format (nine 16x32 frames), original frame ordering, timing and east-facing mirroring. The 18-frame normal graphics also include a duplicated nine-frame sheet for running at native running cadence; dedicated running poses remain future artwork. Ruby Brendan and May rival graphics remain separate.

The user character reference was polished with the built-in imagegen tool. Prompt: preserve Aren black spiky hair/silver forelock and Aria long brown hair/light streak/green clip; clean matching black-white-green outfits; transparent atlas with standing and alternating walking poses facing down/up/left/right; crisp GBA pixel-art appearance. Native preparation cropped and scaled those frames, reduced each sheet to at most fifteen opaque colors, encoded transparency as palette index zero and reordered frames to the original playable sprite contract. East uses native mirroring rather than separate generated frames.

Only normal overworld player artwork is ported in this canary. Bikes, Surf, fishing, field moves, battle back sprites, trainer cards and other movement/menu artwork retain their existing assets. Running temporarily reuses walking poses. New normal-player palettes are isolated from the original movement palettes. No save fields, map layouts, story flags or story movements were changed.

Sources: graphics/object_events/pics/people/aren and aria; palettes/aren.pal and aria.pal. polished_reference.png retains the generated source. aren_walking_8x.png and aria_walking_8x.png show actual indexed frames. aren_bedroom.png and aria_bedroom.png show isolated native mGBA captures. Earlier *_native_preview.png drafts are superseded by the walking sheets.

## Pixel-authored revision

The normal player sheets and palettes now use pixel_authored_trial instead of the reduced imagegen atlas. Native Brendan/May body and pose templates are retained; hair and clothing are authored as indexed native pixels. Side-standing uses native frame 2 and east-facing mirroring. Running still reuses walking poses; other movement states and battle artwork are unchanged. See pixel_authored_trial/README.md for the current revision.
