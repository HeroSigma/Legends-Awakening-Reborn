# Regional map organization

Imported maps are grouped by region and category (towns/cities, routes, caves, forests, centers, shops, gyms, interiors and special areas). Editor-visible donor prefixes are removed. Native game map-group membership and indices are preserved because map routines depend on those group boundaries. Their group labels now include the region.

The original group table and renamed map files are backed up in .la_work/regional_groups_backup. address_migration.json records every old and new address; renames.json records editor map names. Map constants and layout IDs remain unchanged. Existing saves located in imported maps may refer to their old numeric addresses; use a fresh test save or a save in native Littleroot. Historical donor import tools use old names and must consult these rename ledgers before being rerun.

Checks: every map remains registered once; all connection/warp targets resolve; native map addresses unchanged; imported group sizes <=127 (signed map index); map constants and layouts unchanged. Emulator traversal remains pending.
