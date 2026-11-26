# Mt. Chimney alliance and signature partners

The player and Blue recognize a coordinated Magma, Aqua and Rocket operation.
Blue identifies Rocket and asks for backup; Aren/Aria calls May and Red before
climbing the stairs. Blue and shiny Charizard hold Archie and shiny Mega Sharpedo
while the player fights three consecutive six-Pokémon guards. Maxie has shiny
Mega Camerupt beside him. The three guard rosters are distinct and use the
existing legal, capped smart-team builder, with two healing items each.

Red arrives with shiny Pikachu moving alongside him. May arrives with her shiny
Torchic/Combusken/Blaziken, selected by the current cap. They hold the remaining
guards; May heals the player once after the gauntlet. Red participates in the
summit conversation and follows the Rocket evidence while the player pursues Wally.
The existing Maxie battle, Meteorite and Hoopa/Silph progression remain in place.

## Saved progress

VAR_LA_CHIMNEY_GAUNTLET (0x40E3):

- 0: briefing not seen
- 1: backup called
- 2: Magma defeated
- 3: Aqua defeated
- 4: Rocket defeated; backup arrival pending
- 5: backup arrived

Flags 0x2B9–0x2BB independently track the three guard wins. A loss keeps previous
wins. Completed older Chimney saves bypass the new blockade. Story profile slots
34–36 are map-scoped to Mt. Chimney; Silph and Cozmo retain their existing slots.

## Character roster policy

`data/legends_character_aces.json` records all 55 requested character assignments,
including characters planned for future scenes. It does not claim those future
characters have already been placed in maps. Only Wally, Brendan and May evolve
their overworld partners through the story. All assigned field aces use shiny
colors. Version labels are planning references rather than dialogue names.

Existing authored profiles now consistently use Brendan's Swampert line, May's
Blaziken line, Silver's Feraligatr line, Barry's Infernape line, Red's Pikachu and
Green/Leaf's Blastoise. Early battles retain legal evolution stages. The protected
Route 103 battles likewise use shiny Mudkip/Torchic. Red's fresh Charmander duel
remains a separate introductory team. Wally uses Kirlia in Mauville and Gallade
in Victory Road, switching to Flygon after the Hoenn League. Existing Red partner
appearances and the Silph Mewtwo use shiny field graphics.

## Validation

Native isolated-emulator checks cover both staircase entrances, the backup call,
all three battles, guard defeat persistence through loss/save/load, partner
positions, completed-map reloads and the full Maxie/Hoopa continuation. The ace
audit checks 31 current profiles across nine badge stages for legal parties and
checks generated shiny slots, including Wally's post-League switch. No player
save is loaded by these tests.
