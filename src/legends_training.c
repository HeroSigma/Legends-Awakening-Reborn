#include "global.h"
#include "pokemon.h"
#include "caps.h"
#include "event_data.h"
#include "script.h"
#include "script_menu.h"
#include "malloc.h"
#include "string_util.h"
#include "task.h"
#include "main.h"
#include "overworld.h"
#include "evolution_scene.h"
#include "constants/flags.h"

// Only transient script variables are used. No money, items or save fields.
static const u8 *const sServices[] = {COMPOUND_STRING("Inspect build"), COMPOUND_STRING("EV training"), COMPOUND_STRING("Reset all EVs"), COMPOUND_STRING("IV adjustment"), COMPOUND_STRING("Nature effects"), COMPOUND_STRING("Ability"), COMPOUND_STRING("Level catch-up"), COMPOUND_STRING("Done")};
static const u8 *const sStats[] = {COMPOUND_STRING("HP"), COMPOUND_STRING("Attack"), COMPOUND_STRING("Defense"), COMPOUND_STRING("Sp. Attack"), COMPOUND_STRING("Sp. Defense"), COMPOUND_STRING("Speed")};
static const u8 sEVFields[] = {MON_DATA_HP_EV,MON_DATA_ATK_EV,MON_DATA_DEF_EV,MON_DATA_SPATK_EV,MON_DATA_SPDEF_EV,MON_DATA_SPEED_EV};
static const u8 sIVFields[] = {MON_DATA_HP_IV,MON_DATA_ATK_IV,MON_DATA_DEF_IV,MON_DATA_SPATK_IV,MON_DATA_SPDEF_IV,MON_DATA_SPEED_IV};
static const u8 *const sEVChoices[] = {COMPOUND_STRING("Set to 252"),COMPOUND_STRING("Set to 4"),COMPOUND_STRING("Set to 0"),COMPOUND_STRING("Choose exact value"),COMPOUND_STRING("Back")};
static EWRAM_DATA u16 sEvolutionSpecies = SPECIES_NONE;

static struct Pokemon *SelectedMon(void)
{
    u32 slot=gSpecialVar_0x8009;
    if (slot>=gPartiesCount[B_TRAINER_PLAYER]) return NULL;
    struct Pokemon *mon=&gParties[B_TRAINER_PLAYER][slot];
    if (!GetMonData(mon,MON_DATA_SPECIES) || GetMonData(mon,MON_DATA_IS_EGG) || GetMonData(mon,MON_DATA_SANITY_IS_BAD_EGG)) return NULL;
    return mon;
}

u32 LegendsTraining_LevelCap(void)
{
    // Before the Dex milestone, do not bypass the introductory story with Lv100.
    return FlagGet(FLAG_LA_RED_DEX_GIFTS)?GetCurrentLevelCap():16;
}

static void ResumeTraining(u8 taskId);

static void MenuItem(struct ListMenuItem *items,u32 index,const u8 *name,u32 id)
{
    u8 *copy=Alloc(StringLength(name)+1);
    StringCopy(copy,name);
    items[index]=(struct ListMenuItem){copy,id};
}

void LegendsTraining_Menu(void)
{
    struct Pokemon *mon=SelectedMon();
    u32 kind=gSpecialVar_0x8005,count=0,current=0;
    struct ListMenuItem *items=AllocZeroed(sizeof(*items)*254);
    if (!items) {gSpecialVar_Result=127;CreateTask(ResumeTraining,0);return;}
    if (kind==0) {
        for (u32 i=0;i<ARRAY_COUNT(sServices);i++) MenuItem(items,count++,sServices[i],i);
    } else if (kind==1) {
        for (u32 i=0;i<6;i++) MenuItem(items,count++,sStats[i],i);
        MenuItem(items,count++,COMPOUND_STRING("Back"),255);
    } else if (kind==2) {
        for (u32 i=0;i<ARRAY_COUNT(sEVChoices);i++) MenuItem(items,count++,sEVChoices[i],i);
    } else if (kind==3) {
        for (u32 i=0;i<NUM_NATURES;i++) MenuItem(items,count++,gNaturesInfo[i].name,i);
        MenuItem(items,count++,COMPOUND_STRING("Back"),255);
    } else if (kind==4 && mon) {
        const struct SpeciesInfo *info=&gSpeciesInfo[GetMonData(mon,MON_DATA_SPECIES)];
        for (u32 i=0;i<NUM_ABILITY_SLOTS;i++) {
            u32 ability=info->abilities[i];
            if (!ability) continue;
            bool32 duplicate=FALSE;
            for (u32 j=0;j<i;j++) if (info->abilities[j]==ability) duplicate=TRUE;
            if (!duplicate) MenuItem(items,count++,gAbilitiesInfo[ability].name,i);
        }
        MenuItem(items,count++,COMPOUND_STRING("Back"),255);
    } else if (kind>=5 && kind<=7 && mon) {
        u32 stat=gSpecialVar_0x8006;
        if (stat>=6 && kind!=7) {Free(items);gSpecialVar_Result=127;CreateTask(ResumeTraining,0);return;}
        u32 lo=kind==7?GetMonData(mon,MON_DATA_LEVEL):0;
        u32 hi=kind==5?252:kind==6?31:LegendsTraining_LevelCap();
        if (lo>hi) hi=lo; // Existing over-cap specimens cannot gain another level.
        if (kind!=7) current=GetMonData(mon,kind==5?sEVFields[stat]:sIVFields[stat]);
        for (u32 value=lo;value<=hi;value++) {
            u8 text[12];ConvertIntToDecimalStringN(text,value,STR_CONV_MODE_LEFT_ALIGN,3);
            MenuItem(items,count++,text,256+value);
        }
    }
    if (!count) {Free(items);gSpecialVar_Result=127;CreateTask(ResumeTraining,0);return;}
    if (!ScriptMenu_MultichoiceDynamic(0,0,count,items,FALSE,6,current,0)) CreateTask(ResumeTraining,0);
}

static void AppendNumber(u8 *dst,u32 number)
{
    u8 text[12];ConvertIntToDecimalStringN(text,number,STR_CONV_MODE_LEFT_ALIGN,3);StringAppend(dst,text);
}

void LegendsTraining_Inspect(void)
{
    struct Pokemon *mon=SelectedMon();
    gSpecialVar_Result=mon?0:1;
    if (!mon) return;
    GetMonData(mon,MON_DATA_NICKNAME,gStringVar1);
    StringCopy(gStringVar4,gStringVar1);StringAppend(gStringVar4,COMPOUND_STRING("\nLevel: "));AppendNumber(gStringVar4,GetMonData(mon,MON_DATA_LEVEL));
    StringAppend(gStringVar4,COMPOUND_STRING("\pNature effects: "));StringAppend(gStringVar4,gNaturesInfo[GetMonData(mon,MON_DATA_HIDDEN_NATURE)].name);
    StringAppend(gStringVar4,COMPOUND_STRING("\nAbility: "));StringAppend(gStringVar4,gAbilitiesInfo[GetMonAbility(mon)].name);
    for (u32 kind=0;kind<2;kind++) {
        StringAppend(gStringVar4,kind?COMPOUND_STRING("\pIVs"):COMPOUND_STRING("\pEVs"));
        for (u32 i=0;i<6;i++) {
            StringAppend(gStringVar4,i%2==0?COMPOUND_STRING("\n"):COMPOUND_STRING(" / "));
            if (i==2 || i==4) {
                // New pages keep every pair within the two-line text box.
                u32 n=StringLength(gStringVar4);gStringVar4[n-1]=CHAR_PROMPT_CLEAR;
            }
            StringAppend(gStringVar4,sStats[i]);StringAppend(gStringVar4,COMPOUND_STRING(": "));
            AppendNumber(gStringVar4,GetMonData(mon,kind?sIVFields[i]:sEVFields[i]));
        }
    }
}

// Results: 0 ready, 1 invalid/egg, 2 total EV limit, 3 cap/illegal choice,
// 4 unchanged. A cancelled prompt never calls Commit.
void LegendsTraining_Prepare(void)
{
    struct Pokemon *mon=SelectedMon();
    u32 action=gSpecialVar_0x8008,stat=gSpecialVar_0x8006,value=gSpecialVar_0x8007,old=0;
    gSpecialVar_Result=1;
    if (!mon) return;
    gSpecialVar_Result=3;
    if (action==1 || action==3) {
        if (stat>=6 || value>(action==1?252:31)) return;
        old=GetMonData(mon,action==1?sEVFields[stat]:sIVFields[stat]);
        if (action==1) {
            u32 total=value;
            for (u32 i=0;i<6;i++) if (i!=stat) total+=GetMonData(mon,sEVFields[i]);
            if (total>510) {gSpecialVar_Result=2;return;}
        }
    } else if (action==2) {
        for (u32 i=0;i<6;i++) old+=GetMonData(mon,sEVFields[i]);
        value=0;
    } else if (action==4) {
        if (value>=NUM_NATURES) return;
        old=GetMonData(mon,MON_DATA_HIDDEN_NATURE);
    } else if (action==5) {
        if (value>=NUM_ABILITY_SLOTS || !gSpeciesInfo[GetMonData(mon,MON_DATA_SPECIES)].abilities[value]) return;
        old=GetMonData(mon,MON_DATA_ABILITY_NUM);
    } else if (action==6) {
        old=GetMonData(mon,MON_DATA_LEVEL);
        if (value<old || value>LegendsTraining_LevelCap()) return;
    } else return;
    if (old==value) {
        bool32 canStop=TRUE;
        if (action!=6 || GetEvolutionTargetSpecies(mon,EVO_MODE_NORMAL,ITEM_NONE,NULL,&canStop,CHECK_EVO)==SPECIES_NONE) {gSpecialVar_Result=4;return;}
    }
    GetMonData(mon,MON_DATA_NICKNAME,gStringVar1);
    StringCopy(gStringVar4,COMPOUND_STRING("For "));StringAppend(gStringVar4,gStringVar1);StringAppend(gStringVar4,COMPOUND_STRING(":\n"));
    if (action==1 || action==3) {
        StringAppend(gStringVar4,sStats[stat]);StringAppend(gStringVar4,action==1?COMPOUND_STRING(" EVs: "):COMPOUND_STRING(" IVs: "));
        AppendNumber(gStringVar4,old);StringAppend(gStringVar4,COMPOUND_STRING(" to "));AppendNumber(gStringVar4,value);
    } else if (action==2) StringAppend(gStringVar4,COMPOUND_STRING("Reset all EVs to zero."));
    else if (action==4) {StringAppend(gStringVar4,COMPOUND_STRING("Nature effects: "));StringAppend(gStringVar4,gNaturesInfo[value].name);}
    else if (action==5) {StringAppend(gStringVar4,COMPOUND_STRING("Ability: "));StringAppend(gStringVar4,gAbilitiesInfo[gSpeciesInfo[GetMonData(mon,MON_DATA_SPECIES)].abilities[value]].name);}
    else {StringAppend(gStringVar4,COMPOUND_STRING("Level "));AppendNumber(gStringVar4,old);StringAppend(gStringVar4,COMPOUND_STRING(" to "));AppendNumber(gStringVar4,value);}
    StringAppend(gStringVar4,COMPOUND_STRING("\pApply this change?\nAll training is free."));
    gSpecialVar_Result=0;
}

void LegendsTraining_Commit(void)
{
    LegendsTraining_Prepare();
    if (gSpecialVar_Result) return;
    struct Pokemon *mon=SelectedMon();
    u32 action=gSpecialVar_0x8008,stat=gSpecialVar_0x8006,value=gSpecialVar_0x8007;
    if (action==1 || action==3) SetMonData(mon,action==1?sEVFields[stat]:sIVFields[stat],&value);
    else if (action==2) {u32 zero=0;for (u32 i=0;i<6;i++) SetMonData(mon,sEVFields[i],&zero);}
    else if (action==4) SetMonData(mon,MON_DATA_HIDDEN_NATURE,&value);
    else if (action==5) SetMonData(mon,MON_DATA_ABILITY_NUM,&value);
    else if (action==6) {
        u32 exp=gExperienceTables[gSpeciesInfo[GetMonData(mon,MON_DATA_SPECIES)].growthRate][value];
        SetMonData(mon,MON_DATA_EXP,&exp);
    }
    CalculateMonStats(mon);
}

static void ResumeTraining(u8 taskId)
{
    DestroyTask(taskId);ScriptContext_Enable();
}
static void AfterTrainingEvolution(void);
static bool32 StartTrainingEvolution(void)
{
    struct Pokemon *mon=SelectedMon();
    if (!mon) return FALSE;
    bool32 canStop=TRUE;
    u32 target=GetEvolutionTargetSpecies(mon,EVO_MODE_NORMAL,ITEM_NONE,NULL,&canStop,CHECK_EVO);
    if (target==SPECIES_NONE) return FALSE;
    sEvolutionSpecies=GetMonData(mon,MON_DATA_SPECIES);
    GetEvolutionTargetSpecies(mon,EVO_MODE_NORMAL,ITEM_NONE,NULL,&canStop,DO_EVO);
    gCB2_AfterEvolution=AfterTrainingEvolution;
    BeginEvolutionScene(mon,target,canStop,gSpecialVar_0x8009);
    return TRUE;
}
static void AfterTrainingEvolution(void)
{
    struct Pokemon *mon=SelectedMon();
    if (mon && GetMonData(mon,MON_DATA_SPECIES)!=sEvolutionSpecies && StartTrainingEvolution()) return;
    SetMainCallback2(CB2_ReturnToFieldContinueScriptPlayMapMusic);
}
void LegendsTraining_Evolve(void)
{
    if (!StartTrainingEvolution()) CreateTask(ResumeTraining,0);
}
