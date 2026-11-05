# Rustboro: May and Silver

After May's optional Rustboro battle, she heals the player. Silver calls from the north, walks into the conversation, and introduces himself as a displaced Johto traveler. The speaking protagonist and May explain Hoenn and the rifts. Silver challenges the player, admits what he saw after losing, and heads north to investigate alone. May then points the player toward Briney's cottage.

May appears for either protagonist. Both established siblings become available through the existing PokéNav registration. The new scene also works for saves that already defeated May.

## Battle

Silver uses Zubat, Gastly, Magnemite, Abra, Sneasel and shiny Totodile: early-stage adaptations of his Johto team families. The competitive trainer system provides legal moves, perfect IVs, role-based EVs, smart AI, two healing items and a single eligible gimmick. Route/badge scaling keeps him below the upcoming Gym cap. This story battle is singles and does not ask for a format.

The team is healed before Silver and after victory. Losing keeps May's victory, records Silver's introduction, and leaves Silver waiting for a short retry. Existing save storage layouts and trainer-flag capacity are unchanged.

## Staging and state

- Silver enters at (18,48), walks south to (18,54), then exits north.
- Under the healing fade the player stands at (18,55) and May at (17,54).
- May returns to (16,52) after the scene.
- `FLAG_LA_HIDE_RUSTBORO_SILVER` (0x49): visibility.
- `FLAG_LA_MET_SILVER` (0x4A): introduction/retry checkpoint.
- `FLAG_LA_DEFEATED_SILVER_RUSTBORO` (0x4B): completion.

## Art attribution

Overworld: existing Hyper Emerald `gfx_077` roster asset.
Battle portrait and palette: Pokémon HnS, local `pokehns-canary-source` revision `167aa6d5`, files `graphics/trainers/front_pics/silver_hns.png` and `graphics/trainers/palettes/silver_hns.pal`. Credits: HnS / Lil Dill and the HnS team, with their Modern Emerald / resetes12, RHH and pret upstream chain. The HnS back sprite was located but is not used for this opponent battle.

## Validation

`test_rustboro_silver.py` uses isolated emulator saves and checks both protagonists, normal and 60-box storage, opposite route trigger edges, starter families, badge caps, six legal team members, shiny ace, portrait selection, healing, dialogue, positions, completion/save reload, whiteout/retry and existing-May-victory compatibility. Battle outcomes are injected only after native turn readiness; these checks do not establish AI difficulty.

`test_rustboro_silver_text.py` measures the rendered text with a seven-character wide player name. Reports record the ROM hash. No user save is loaded.
