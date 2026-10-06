# GS Chronicles Johto asset/travel port

ROM SHA-256: 83de12ab57692aa39d5eff5314d404aed06b466b038ace637a8b84c9c25f1569. Extracted 398 readable slots from 426 table slots; 28 unreadable headers are held. 266 Johto-labelled maps registered in existing available map banks, with one Johto map section. The invalid EEEEE section is excluded. Existing map IDs retain their positions.

Hyper regions and BWA/SWSH remain untouched. Donor NPC, map scripts, progression flags, encounters and save logic are not imported. Maps use translated behavior attributes, donor geometry, static tiles/palettes/metatiles and explicitly mapped project static warps/connections. Animations remain static pending donor callback port; do not call these fully asset-complete. Unresolved custom behavior IDs require review.

Kanto: 121 named slots, 119 exactly match FireRed blockdata in their original slots. Two changed slots: Vermilion 3.12 is substantial edited geometry; Pallet 3.15 is a small fragment in an empty field. Names alone do not establish Kanto coverage. No Kanto maps activated.

## Runtime test

Littleroot teleport scientist: JOHTO begins at New Bark Town. Walk the static regional links. Inspection scientists offer YES for the next inspectable donor map, NO to Littleroot. Rooms retain art but have no donor NPC/gameplay services. Blank/low-detail maps: 12; no safe arrival cluster: 43. Maps without an arrival remain registered for Porymap inspection and can only be reached if valid natural static links exist. Do not fabricate walkable pads.

Test city/route/cave graphics, doors and reciprocal returns, map edges, water/Surf/collision, elevation/ledges, both genders, save/reload and return to Littleroot. Visit prior BWA, Galar, Hoenn and Sinnoh regression destinations. Scientist placement and bank declarations need runtime review. All maps are under construction; encounters, gyms, shops, healing/Fly, puzzles and story ownership remain future project work.

Review raw metadata in manifest.json; held maps in manual_review.json; Kanto comparison in kanto_audit.json. Unova work remains paused.

Validation: 266 linked Johto maps and the prior BWA batch passed. Existing Hyper checks passed for 780 maps, 213 banks, 30160 native cells and 6252 animation DMA transfers. Historical whole-file hash gate is superseded for the authorized declaration/script/registry additions; tracked preexisting map JSON/scripts and registry positions were independently verified unchanged. Porymap declarations are present directly in its configured header/graphics/metatile files; GUI opening remains a user check.
