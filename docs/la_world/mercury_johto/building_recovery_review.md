# Mercury missing-building investigation

Cherrygrove Mart entrance: donor 3.67, (26,5), target 45.1. The source exported preview already has a blank footprint and exposed door/window art. The supplied alternate Mercury 2.2 ROM has byte-identical Cherrygrove header, layout, blockdata and primary metatile definitions, so swapping those inputs does not recover the building.

The responsible donor visual mechanism has not yet been established. No donor gameplay scripts were imported, and no guessed building stamps were painted. The raw export is not a complete reference for final runtime building appearance. Separate visual asset recovery is required before calling this issue fixed.

`building_footprint_review.json` lists outdoor doorways with mostly grass/blank space above them for manual visual inspection; these are candidates, not confirmed missing buildings.

The stair repair is separate and changes only our previously translated B2/B5 native TOP behaviors to normal walk behavior, retaining all cell collision/elevation and saved map artwork.
