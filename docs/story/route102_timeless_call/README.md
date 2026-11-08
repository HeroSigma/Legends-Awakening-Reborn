# Route 102: the call from Timeless Woods

The first visit to X12–14, Y8 starts a project-owned scene. It does not require defeating Allen. If Allen starts his native battle first, his post-battle continuation checks the same strip and runs the scene after his dialogue. A battle outside the strip does not trigger the scene remotely.

The player pauses, looks toward the northwest opening, hears an eerie psychic chime and an unidentified call of their own name. The camera pans to the existing Timeless Woods entrance at (6,3), the call repeats, and the camera returns to the player. No player walking is forced. Trainer teams, rewards, other NPCs and existing Woods warps remain unchanged.

Dialogue:

- Unidentified call: “{PLAYER}…”
- Player: “What is calling me? That opening in the trees… The voice is coming from there.”
- Unidentified call: “{PLAYER}…”
- Player: “I heard it again. It knows my name… That trainer is blocking the path on the left. There must be another way to get in there.”

The name is expanded from the current save and displayed as dialogue, accompanied by `SE_M_PSYBEAM2`; this is not synthesized speech.

Persistent state uses formerly unused native storage: `FLAG_LA_TIMELESS_WOODS_CALL_HEARD` (0x39) and `VAR_LA_TIMELESS_WOODS_CALL_STATE` (0x408B): 0 unseen, 1 active, 2 completed. The map transition synchronizes the state with the completion flag. No save structure changes.

Validation exercises both genders and all three cells, an unbeaten-Allen bypass, an actual Allen battle followed by the scene, camera position and return, repeat visits, and native save/continue using an isolated test save. See `runtime_validation.json` and `tools/la_world/importers/amap/hns_runtime/test_timeless_call.py`.
