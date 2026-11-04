# Palette Back transition and row spacing

The intro textbox clear routine multiplied tile dimensions by font metrics, leaving part of the window uncleared. Returning from the color picker to the shorter gender prompt therefore left the end of the old instructions visible. Clearing the entire pixel buffer fixes this for all intro prompt replacements.

The picker now uses 32-pixel row spacing with a 14-pixel offset between labels and values. Its taller 11-by-12-tile window keeps all three rows readable, and a compile-time bound keeps its graphics below the intro border tiles. Field and intro graphics base offsets remain separate.

Native tests compare the complete gender-prompt pixel buffer before entering the picker and after Back for both protagonists, in addition to visual captures, color preview/cancellation, save/load, full intro/naming and both box modes. All 566 palette checks and 26 intro checks pass on the recorded ROM hash. Tests use disposable saves.
