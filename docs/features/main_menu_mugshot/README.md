# Continue menu with mugshot

Adapts Archie and Mudskip's main-menu UI to Legends Awakening Reborn. Source: https://github.com/TeamAquasHideout/pokeemerald/tree/main_menu at 3691421b97ff8402afcd84b149b1f9c0bc2b21ec. Original guide: https://github.com/pret/pokeemerald/wiki/New-Main-Menu-UI-With-Mugshot-by-Archie-and-Mudskip. Credits: Archie (code), Mudskip (graphics), ghoulslash (UI shell), Grunt Lucas (technical guidance).

Saved games show a teal Continue panel with the selected protagonist, party icons, saved location, time, badge count and Pokédex count when unlocked. Up/down selects Continue versus the lower row; left/right selects New Game or Options. B returns to the title. With no save, the original New Game/Options choices remain available. Save warnings still run before entering the replacement screen.

New Game enters our existing Legends character creator. Options returns to the selected Options panel. Normal 14-box and compact 60-box storage continue using their existing save formats. No save structure or player identity changes are required.

The port uses current decompression/icon interfaces, releases all sprite/window/background resources before changing screens, and avoids the donor's resource cleanup use-after-free. Long custom location names fit the header; empty parties, fainted Pokémon and zero egg-cycle denominators are handled safely.

Validation uses isolated emulator batteries and never opens the release save. `validation.json` records the tested ROM hash and native title-menu checks, including both genders, empty/one/full parties, repeated Options returns, Continue, B-to-title, custom New Game and no-save Options. The production PC suite also verifies all 1,800 compact slots, save recovery and Continue. The field Start-menu suite checks its existing 446 navigation/return cases.
