# Fixed Legend Update transfer — 2026-11-08

Target: HeroSigma/Legends-Awakening-Reborn, branch Fixed-Legend-Update.
Git rejects spaces in branch names; requested display name was Fixed Legend Update.
Base: feature/compact-pc-60-boxes at 00f717efe440272b6fdbc123a9742c288a5a56ce.
Active source: /home/allan/projects/Legends-Awakening-Reborn, test/qol-first-three,
15b474aef700c8d6cde3b69b7d9e79646f31a6f1 (November 7).
Remote names in that checkout: herosigma = correct Reborn; origin = RHH engine.

## Evidence and preservation

The active source is 125 commits ahead of the base's common ancestor, with four
base-only commits. Those four are an extracted compact-PC line; active history
contains the complete project snapshot and subsequent expanded-bag/storage fixes.
The merge keeps both parents. All runtime files in its result are byte-identical
to the active source commit. The only merge-result differences from that commit
are the base README and docs/compact-pc/README.md, which preserve base documentation.
Eighteen conflicts were resolved to the active implementation after comparison:
the base storage versions would discard expanded-bag save support, later activity
gates, full-sheet streaming cleanup, and later UI changes.

All 225 changed/new active files (16,571,887 bytes) were restored from a pre-change
archive and SHA-256 verified. active-files.json lists each file and hash.
This includes story/quests, Ashes/Silph, villain alliance, Dynamax, overworld
resource pressure, regional encounters, stairs, map/tileset work, graphics,
research, validation evidence and project instructions.
commits-from-local.txt lists all 125 retained commits relative to the target base.
Only two source commits were absent from all existing Reborn remote branches:
c5a0b902f1 and 15b474aef7. Most newer features were already on Reborn feature branches.

## Other repositories and trials

All six old LegendsAwaken remote branches were fetched into local legacy-audit
refs; legacy-remote-branches.txt records their tips. The newest tip is March 21,
2026, not the newest project work. Its master diverges substantially (1,012
old-only / 1,712 active-only commits), so blindly merging it would import an older,
different engine/world implementation. It was not used as the modern source.

Windows Documents/GitHub/LegendsAwaken is at 50e7ee1203 (January 2) and has three
uncommitted trainer PNGs. They and their binary patch are retained in legacy-local.
Windows Desktop/Legends Awakening/Legends-Awakening is clean at e8bd1cd7b0,
the upstream 1.17.0 release, and has no project edits to transfer.

/home/allan/la-scratch/la is an older September trial at 5559be953 with ten
uncommitted files: map-section/save-format widening and region-map changes.
Its patch is retained as legacy-local/scratch.patch; it is not applied to modern
runtime because it changes Pokemon/save layout and contains unfinished changes.
The field-move worktree's one modified generated 4bpp is retained in field.patch.
That branch's committed feature already exists in the modern history.
No original working tree, save, release ROM, or default branch was modified.

## Safety and verification

Pre-transfer archives and patches are retained locally in
/home/allan/legend-transfer-20261108. Active file hashes were verified after restore.
The new-history blob review found no files over 10 MiB, no ROM/save/ELF/archive
paths, and no matches for common GitHub/AWS/OpenAI tokens or private-key headers.
This is a pattern-based review, not proof that arbitrary secrets are absent.
Project encounter JSON/CSV inventories and small game binary assets are intentional.
CSV CRLF records trigger Git trailing-whitespace notices; original bytes are preserved.
No parent-engine update or default-branch merge is performed by this transfer.

## Transfer validation details

All 37 changed JSON files parsed; all 15 changed Python files compiled.
The regional source test passed for 30,768 encounter slots and 955 species/forms.
A clean build exposed two missing palette source files that existed only as ignored
binary palettes in the active checkout. Recovered la_roster_18.pal (16 colors)
and battle_interface/bw/textbox.pal (32 colors); reconversion was byte-for-byte
equal to the active binary assets. These portable sources are included.
Git applies the existing repository line-ending attributes when storing files;
the original-byte hashes describe the captured local files before normalization.
Whitespace review found only preserved patch syntax and one existing final blank
line in audit_project_stairs.py, in addition to normal CSV CRLF handling.
Native integration tests use hardcoded original-checkout paths and were not rerun
against the isolated copy. Existing validation JSON/screenshots are transferred
evidence from earlier work, not claimed as newly executed tests.
