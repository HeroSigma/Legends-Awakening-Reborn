#ifndef GUARD_LEGENDS_QUESTS_H
#define GUARD_LEGENDS_QUESTS_H
enum { QUEST_LOCKED, QUEST_ACTIVE, QUEST_REWARD_READY, QUEST_CLAIMED };
#define LA_QUEST_GYM_FIRST 10
#define LA_QUEST_RIFT_FIRST 20
#define LA_QUEST_COUNT 46
void LegendsQuests_Open(void);
u32 LegendsQuest_State(u32 id);
bool32 LegendsQuest_RiftAllowed(u32 site);
void LegendsQuest_SurveyRift(u32 site);
void LegendsQuest_Claim(void);
#endif
