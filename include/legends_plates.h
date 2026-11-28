#ifndef GUARD_LEGENDS_PLATES_H
#define GUARD_LEGENDS_PLATES_H
#define LEGENDS_PLATE_COUNT 17
struct LegendsQuest;
u32 LegendsPlates_CountCompleted(void);
u32 LegendsPlates_QuestState(u32 quest);
const struct LegendsQuest *LegendsPlates_QuestMetadata(u32 quest);
bool32 LegendsPlates_Activate(u32 index);
bool32 LegendsPlates_GuardianWon(u32 index);
u32 LegendsPlates_ClaimGuardian(u32 index);
u32 LegendsPlates_StartResearch(void);
u32 LegendsPlates_TryAwaken(void);
void LegendsPlates_ActivateQuest(void);
void LegendsPlates_RecordGuardianResult(void);
void LegendsPlates_CollectResonance(void);
void LegendsPlates_PrepareBirch(void);
void LegendsPlates_BeginResearch(void);
void LegendsPlates_Awaken(void);
void ItemUseOutOfBattle_LegendsPlate(u8 taskId);
#endif
