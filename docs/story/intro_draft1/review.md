# Legends Rewake opening — playable dialogue draft 1

Implemented: black-screen Creator introduction in light red; fade into Birch's green introduction; Aren/Aria selection labels and default names; editable naming; confirmation/rejection; Birch's recognition and timed pauses; Littleroot/Hoenn farewell and native new-game handoff.

Dialogue follows the current Legends Rewake draft. Only line/page breaks and Pokemon typography are adapted to the engine. No early Caelum/family/Rift revelation is added.

Editing:
- Creator text, Pokemon reveal text and selection labels: src/data/text/legends_intro.h.
- Birch dialogue: data/text/birch_speech.inc.
- Scene timing and transitions: Task_LegendsCreator_* and native Birch tasks in src/main_menu.c.
- Human-readable draft: dialogue.json (reference; the C/assembly text is authoritative).

Character portraits remain the project's existing male/female intro art. The naming screen supports custom names; recognition uses the actual selected name.

The subsequent A Strange Delivery bedroom prologue now owns the normal new-game handoff. See ../bedroom_prologue/review.md. Previously exported intro-only/exploration ROMs remain separate historical previews.

Validation:
- Native ROM build succeeds.
- Full intro completes for both character choices.
- Rejecting the name returns to selection and naming.
- Seven-character custom name expands correctly in recognition dialogue.
- Native font-width check: widest draft line is 182 pixels, below both window limits.
- Creator and Birch scenes inspected in native mGBA screenshots.
- No regional maps/layouts, save structures, story flags or field-move systems changed.

Pre-change files are backed up under .la_work/story/intro_draft1_backup. The previous exploration ROM remains in its separate Downloads folder.

## Complete-thought pagination revision

Creator dialogue now uses ten complete-thought pages in a taller text area (up to three lines). Wording is unchanged. All ten pages were captured in mGBA; complete three-line passages remain visible together. The rebuilt ROM passes the existing male/female, name-rejection and custom-name intro checks. Existing exploration-start handoff remains unchanged.
