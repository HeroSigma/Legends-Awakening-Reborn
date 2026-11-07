#ifndef GUARD_RIFT_TRACKER_H
#define GUARD_RIFT_TRACKER_H
bool32 RiftTracker_IsActive(void);
u32 RiftTracker_Count(void);
void RiftTracker_Draw(u8 win, u8 page, u8 selected);
void RiftTracker_Check(void);
struct MapHeader;
bool32 RiftTracker_BlockWarp(const struct MapHeader *map, u32 warpId);
#endif
