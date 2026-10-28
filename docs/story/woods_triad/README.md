# Petalburg Woods: Devon / Silph / Shadow Triad

Replaces the original Woods Aqua interruption only. Later Aqua incidents remain distinct story beats.

A Devon energy researcher and a visiting Silph researcher compare simultaneous rift readings. A modified Silph Scope recorded buildings, people and a different sky through a brief opening. One Shadow Triad member demands the recording; the player protects the researchers in a normal story singles battle. After defeat, the other two members appear on the open northern path. They take the Scope backup drive and mention a recovered device needing a stable reference. The team withdraws north, leaving the researchers and the numerical readings safe. The player is asked to report at Devon in Rustboro. The internal connection to the Timeless Woods object is only stated if the player actually witnessed that meeting.

## Assets and battle

- Overworld: archived BWA `gfx_049`, registered as `OBJ_EVENT_GFX_LA_ROSTER_SHADOWTRIAD` with all nine native standard frames and its source palette.
- Battle portrait: BWA trainer portrait 99, separate new `TRAINER_PIC_SHADOW_TRIAD`; no Aqua art is rebound globally. Extraction records the exact donor hash and offsets.
- Original trainer ID retained for flag compatibility; name is TRIAD, class is generic Pokemon Trainer.
- Six-member post-Dex profile: Pawniard, Zubat, Koffing, Sneasel, Zorua, shiny Absol ace. Level target 16, capped by existing progression, with the existing smart AI, legal move/ability/evolution checks, two healing items, and one deterministic Tera/Z gimmick. No gym-format prompt is added to this story encounter.

## State and compatibility

- Existing `VAR_PETALBURG_WOODS_STATE`: 0 pending; 1 completed. Existing Devon and grunt hide flags remain authoritative.
- `FLAG_HIDE_LA_WOODS_TRIAD_BACKUP` uses formerly unused 0x041; backup actors are hidden on map load and added only during the scene.
- `FLAG_LA_WOODS_TRIAD_COMPLETE` (0x042) records the new completed scene.
- `FLAG_LA_WOODS_RIFT_RECORD_STOLEN` (0x043) records the stolen Scope drive for later story writing.
- Previously completed saves hide all new scene actors without inventing the new theft/completion flags.
- Loss retains pending state and supports a full retry. The Great Ball reward remains; a full stack takes a nonblocking alternate branch. Completion/reload cannot repeat the reward or scene.
- Existing Woods trainers, items, exits and construction reservations are retained. No save-structure changes.

## Validation

`tools/la_world/storage/test_woods_triad_story.py` uses isolated native mGBA saves for both trigger columns, both protagonists and storage modes, all three visible actors on walkable ground, team legality and shiny ace, save/reload, no replay, loss/retry, full reward stack, and completed legacy saves. Battle outcomes are injected through native win/loss end handlers: this validates scene continuation and trainer setup, not combat difficulty. Screenshots record the research dialogue, donor trainer portrait, and three-member appearance.
