# Trainer teams by location

The authoring generator now reads trainer-battle references in map scripts, including Lavaridge's buried-trainer macro (its first argument is a local object ID, not a trainer ID).

Gym students use their Gym's theme ahead of generic trainer class/native ace. All eight Hoenn Gyms are covered. Their six-member rosters rotate deterministically by trainer identity; runtime resolves level-legal evolution stages and legal moves/abilities at the existing badge cap. Dewford students use Heracross rather than the Breloom family so they do not field pure-Grass Shroomish at the Fighting Gym's cap.

Ordinary trainers in mapped forests, caves, mountain areas, volcanic areas and coastal routes receive environmental cores. Relevant forest Bug/Ninja/Bird specialists and coastal aquatic specialists retain class-specific roles. Trainers shared across conflicting areas keep their class identity rather than guessing a location. Remaining ordinary route trainers retain native/class cores. Imported maps without registered trainer battles do not gain new battles from this change.

Leaders, League, rivals, villain teams, scripted story battles and excluded tutorial/partner profiles retain their authored identities. Singles/doubles permissions, shiny-ace policy, smart AI, battle items and existing evolution/move legality remain unchanged. No save schema or map edits.

Location metadata in competitive-trainer-profiles.json records each assigned environment and source map.

## Coverage

- cave: 1 trainers
- coast: 92 trainers
- forest: 2 trainers
- gym:electric: 5 trainers
- gym:fighting: 6 trainers
- gym:fire: 8 trainers
- gym:flying: 6 trainers
- gym:normal: 7 trainers
- gym:psychic: 12 trainers
- gym:rock: 3 trainers
- gym:water: 10 trainers
- mountain: 24 trainers
- volcanic: 12 trainers
