# Nurse Joy collection-mode fix

The normal healing script queries PlayerNotAtTrainerHillEntrance and BufferUnionRoomPlayerName after healing. The broad retired-feature filter incorrectly blocked those harmless checks in 60-box mode, interrupting the nurse with the unavailable-activity message. Both checks are now allowed alongside the existing ordinary map initializers.

Collection gates now reference linker-defined SPECIAL_name symbols rather than hardcoded table indices. The generator preserves this binding so future special-table insertions cannot accidentally block unrelated services. Real retired activities remain blocked.

Native tests complete Nurse Joy interactions in Oldale, Petalburg and Lilycove in both 14-box and 60-box modes, check healing and stored-Pokemon markers, and validate every named blocked special. Map initializer, free-training UI/evolution and full PC/save tests also pass. No storage format, save fields, money, party or boxed Pokemon migration is required. Player battery saves are never used by tests.
