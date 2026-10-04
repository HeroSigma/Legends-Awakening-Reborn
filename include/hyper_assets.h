#ifndef GUARD_HYPER_ASSETS_H
#define GUARD_HYPER_ASSETS_H
struct ObjectEventGraphicsInfo;
/* Source IDs name visual assets only; they are never assigned to event gameplay IDs. */
const struct ObjectEventGraphicsInfo *HyperAssets_GetSourceObjectGraphicsInfo(u16 sourceId);
#endif
