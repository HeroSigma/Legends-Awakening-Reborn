#ifndef GUARD_WORLD_MAP_H
#define GUARD_WORLD_MAP_H
void WorldMap_Open(void (*callback)(void));
const u8 *WorldMap_LocationAt(u16 x, u16 y);
u8 WorldMap_RegionAt(u16 x, u16 y);
#endif
