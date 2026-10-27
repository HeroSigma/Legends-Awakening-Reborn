# Standing 32x32 likeness trial

Review only: one down-facing idle per character; no active graphics, ROM or save changed.

Generated with the built-in imagegen tool using installed trainer fronts and original character concept. Prompt: same character identity, black spiky/silver-forelock Aren and long brown/pale-streak/green-clip Aria, matching white/black/green jackets, trousers/shorts, green shoes, satchel; compact slightly top-down overworld neutral standing, 32x32 logical canvas,15 opaque colors plus transparency, no extra detail/soft shading/background. Aria also used Aren draft as style reference.

The generator did not produce literal32x32 files. Native conversion thresholds alpha, crops to sprite, fits a deliberately broader22x30 silhouette, anchors feet to bottom of32x32, and encodes <=15 opaque colors plus transparent index zero. Each sprite is still a draft; this is not pixel-exact reproduction of the trainer art. *_standing_32.png are actual indexed assets; *_standing_8x.png are nearest-neighbor previews. In *_old_left_trial_right_8x.png the existing playable art is LEFT and new trial RIGHT at identical enlargement.

These sprites are taller/wider than the original player art. Actual integration would require32x32 normal sprite/OAM/frame layout, consistent walking/running/other states, checking doors and indoor overlaps, and preserving the existing one-cell collision anchor. None of those runtime changes are made by this trial.
