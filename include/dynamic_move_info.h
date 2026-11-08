#ifndef GUARD_DYNAMIC_MOVE_INFO_H
#define GUARD_DYNAMIC_MOVE_INFO_H
#include "move.h"
struct MoveDescriptionPreview {
    u16 power, accuracy, basePower, baseAccuracy;
    enum Move displayMove;
    enum DamageCategory category;
};
void GetMoveDescriptionPreview(enum BattlerId battler, enum Move move, struct MoveDescriptionPreview *out);
#endif
