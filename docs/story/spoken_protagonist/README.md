# Speaking protagonist: Woods through Dewford departure

Aren/Aria ask questions and make decisions aloud under SP_NAME_PLAYER. The chosen player name is used; no fixed gender or protagonist name is inserted. Existing speaker IDs remain stable. Stone, Briney and the Aqua grunt receive appended speaker IDs.

- Petalburg Woods: asks about rift research, challenges the Triad, demands answers as they take the recordings, checks the researchers are safe, shares the witnessed Timeless Woods clue when its existing flag is set, and agrees to meet them in Rustboro. Unknown-clue saves ask about the device without inventing knowledge.
- Rustboro: volunteers to recover the second stolen shipment, reports the hostage/rescue and questions why the hardware matters before accepting the office invitation.
- Stone/Birch: asks whether the device and thefts mean someone controls the rifts; Stone and Birch distinguish evidence from speculation. The player asks for Steven's location and a contact method, accepts the delivery and agrees to report disturbances safely.
- Route 116/Rusturf: promises to help Peeko, challenges and questions the grunt, introduces themselves to Briney, and speaks during the reunion. No implied silent self-introduction.
- Briney's cottage: asks for passage and explains the deliveries instead of Briney reading an unspoken request. Acceptance and refusal have spoken responses; original Yes/No and boat progression remain intact.

No new flags, variables, save layout or map data. Existing conditional information, battles, item rewards, once-only gates, movement paths, recovery state, letter/PokeNav grants and sailing choices are retained. Internal legacy text labels such as Thought remain where referenced, but the lines now address the researchers aloud.

Native tests cover both protagonists and storage modes, grunt battle continuation (injected native win, not combat difficulty), the rescue and return state, Briney's consent/decline/departure, namebox rendering and all new dialogue widths. Existing Woods/Rustboro regression tests cover rewards, no replay, loss/retry and Tera onboarding. Old in-game saves remain compatible; completed cutscenes are not reset or replayed automatically.

## Dialogue colors

Field messages now use the active speaker to supply established body-text colors: player light blue, Brendan green, May/Red red, Wally light green, Briney and Aqua grunt blue. Researchers and narration retain normal readable gray. Existing explicit script color controls take priority. The renderer prefixes only the bounded expanded field-message buffer, after determining the namebox speaker; no save state or namebox palette changes. Item messages with SP_NAME_NONE retain default colors.
