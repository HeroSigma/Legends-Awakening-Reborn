# Passive egg nursery

Implemented: after returning Devon Goods and receiving the PokeNav, eggs stored in Box 1 receive native walking egg-cycle progress. Other boxes remain ordinary storage. Withdraw an egg into the party to hatch through the normal sequence; eggs never silently become Pokemon in storage.

Uses existing egg friendship/cycle data, the native cycle clock and incubator party bonus. No new save fields or extra storage allocations. Accessors support both 14 and 60 boxes. Bad eggs and non-eggs are excluded. Progress stops at zero and persists with normal saving. Moving an egg away from Box 1 pauses nursery progress.

Runtime checklist: locked before Devon; deposit eggs in Box 1, walk, save/reload, withdraw and hatch. Verify inheritance in both storage modes. No real battery save is used by automated tests.
