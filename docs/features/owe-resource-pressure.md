# Overworld sprite resource pressure

Route 104 could show a fatal assertion while spawning species 972, Alolan Exeggutor. Its 64x64 compressed overworld sheet competes with other NPC, follower and wild sprite tiles. The availability check was correctly rejecting the spawn but incorrectly treating ordinary resource exhaustion as a fatal error.

CheckCanLoadOWE now returns false normally when palette or contiguous tile capacity is insufficient. The existing caller sets its retry timer and leaves current actors intact. Existing adaptive object limits and regional species distribution remain unchanged. This applies to all species rather than removing Alolan Exeggutor.

Native disposable-save tests cover full tile allocation, full palettes, both together, restoration, direct Alolan Exeggutor sprite spawning and continued Route 104 execution. See owe-resource-validation.json.
