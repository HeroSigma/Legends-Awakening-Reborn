# Batch 6 validation

- 55 room renders visually reviewed; zero invalid used palette references.
- 170 static warp arrivals and 186 active actors audited. Fifteen access warnings require native runtime states; preserved and explained in runtime_state_review.json.
- 12,935 cells compared against archived pre-migration geometry: 49 exact native contracts; six gym floors with documented prior differences retained for runtime review.
- 112 literal scripted setmetatile coordinates are in bounds.
- Full ownership and linked asset verification passed: 780 maps, 213 tilesets, 30160 strict native cell contracts across the broader migration.
- Animation sanitizer checks passed: 21 callbacks, 29 paired combinations, 6,252 frame transfers.
- ROM SHA-256: `b89a948e9facfa1828f8ed8835c3a402379cbea3676553702c965c0c4f89af83`. Same ROM as Batch 5; no new build or map edits necessary.
- In-game puzzles/challenges remain pending testing. Static checks do not establish runtime success.
