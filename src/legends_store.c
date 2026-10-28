#include "global.h"
#include "legends_store.h"
#include "bag_categories.h"
#include "event_object_lock.h"
#include "field_player_avatar.h"
#include "main.h"
#include "menu.h"
#include "money.h"
#include "malloc.h"
#include "rtc.h"
#include "script.h"
#include "string_util.h"
#include "task.h"
#include "text.h"
#include "strings.h"
#include "window.h"

static const u8 sTitle[] = _("LEGENDS STORE");
static const u8 sSale[] = _("Sale: {STR_VAR_1} -20%");
static const u8 sMoney[] = _("Funds: {STR_VAR_1}");
static const u8 sRow[] = _("{STR_VAR_1}");
static const u8 sPrice[] = _("{STR_VAR_1}");
static const u8 sFooter[] = _("Left/Right: pocket  L/R: page");
static const u8 sBrowse[] = _("A: choose  B: exit");
static const u8 sConfirm[] = _("Qty {STR_VAR_1}  Total {STR_VAR_2}\nLeft/Right: qty  A: buy  B: back");
static const u8 sBought[] = _("Delivered to your Bag!");
static const u8 sPoor[] = _("You don't have enough money.");
static const u8 sOwned[] = _("You already own this reusable item.");
static const u8 sFull[] = _("No room for that quantity.");
static const u8 sEmpty[] = _("No items in this pocket.");
static const struct WindowTemplate sWindow = {
    .bg=0, .tilemapLeft=1, .tilemapTop=1, .width=28, .height=18,
    .paletteNum=15, .baseBlock=1,
};

bool32 __attribute__((noinline)) LegendsStore_ItemAllowed(enum Item item)
{
    return item > ITEM_NONE && item < ITEMS_COUNT
        && gItemsInfo[item].name != NULL
        && gItemsInfo[item].name != gQuestionMarksItemName
        && LegendsStore_CategoryAllowed(GetItemBagCategory(item));
}

u32 __attribute__((noinline)) LegendsStore_Price(enum Item item, u32 saleCategory)
{
    u32 base, category;
    if (!LegendsStore_ItemAllowed(item)) return 0;
    category = GetItemBagCategory(item);
    base = gItemsInfo[item].price;
    switch (item)
    {
    case ITEM_MASTER_BALL: base=150000; break;
    case ITEM_ABILITY_CAPSULE: base=15000; break;
    case ITEM_ABILITY_PATCH: base=30000; break;
    case ITEM_RARE_CANDY: base=5000; break;
    case ITEM_CHOICE_BAND:
    case ITEM_CHOICE_SPECS:
    case ITEM_CHOICE_SCARF:
    case ITEM_LIFE_ORB:
    case ITEM_LEFTOVERS:
    case ITEM_FOCUS_SASH:
    case ITEM_ASSAULT_VEST: base=12000; break;
    default:
        if (category == BAG_MEGA_STONES) base=25000;
        else if (category == BAG_Z_CRYSTALS) base=20000;
        else if (gItemsInfo[item].sortType == ITEM_TYPE_NATURE_MINT) base=8000;
        else if (base == 0)
        {
            switch (category)
            {
            case BAG_MACHINES: base=10000; break;
            case BAG_TRAINING: base=5000; break;
            case BAG_EVOLUTION: base=8000; break;
            case BAG_EQUIPMENT: base=6000; break;
            case BAG_BALLS: base=1500; break;
            case BAG_BERRIES: base=500; break;
            case BAG_MEDICINE: base=2000; break;
            case BAG_TREASURES: base=10000; break;
            default: base=1000; break;
            }
        }
        break;
    }
    // Token native prices should not make useful upgrades effectively free.
    if (category == BAG_EQUIPMENT)
    {
        u32 floor = (gItemsInfo[item].sortType == ITEM_TYPE_X_ITEM
            || gItemsInfo[item].sortType == ITEM_TYPE_BATTLE_ITEM) ? 500 : 4000;
        if (base < floor) base=floor;
    }
    if (category == BAG_TRAINING && base < 3000) base=3000;
    if (category == BAG_EVOLUTION && base < 4000) base=4000;
    if (category == BAG_BERRIES && base < 100) base=100;
    if (category == BAG_REGULAR && base < 500) base=500;
    return category == saleCategory ? base : (base * 5 + 3) / 4;
}

// Atomic purchase: validate everything before changing inventory or money.
// 0 success, 1 invalid selection, 2 insufficient funds, 3 no bag space.
u32 __attribute__((noinline)) LegendsStore_Buy(enum Item item, u32 quantity, u32 saleCategory)
{
    u32 price=LegendsStore_Price(item, saleCategory), total;
    if (!price || !quantity || quantity > 99) return 1;
    if ((GetItemImportance(item) || GetItemPocket(item) == POCKET_TM_HM)
        && (quantity != 1 || CheckBagHasItem(item, 1))) return 1;
    total=price*quantity;
    if (!IsEnoughMoney(&gSaveBlock1Ptr->money, total)) return 2;
    if (!AddBagItem(item, quantity)) return 3;
    RemoveMoney(&gSaveBlock1Ptr->money, total);
    return 0;
}

struct StoreCatalog
{
    u16 items[ITEMS_COUNT];
    u16 offsets[BAG_CATEGORIES_COUNT];
    u16 counts[BAG_CATEGORIES_COUNT];
};
EWRAM_DATA static struct StoreCatalog *sCatalog = NULL;
static u32 ItemCount(u32 category)
{
    return sCatalog->counts[category];
}
static enum Item ItemAt(u32 category,u32 index)
{
    return index < ItemCount(category) ? sCatalog->items[sCatalog->offsets[category]+index] : ITEM_NONE;
}
static void Print(u8 win,const u8 *text,u32 x,u32 y)
{
    AddTextPrinterParameterized(win,FONT_SMALL,text,x,y,TEXT_SKIP_DRAW,NULL);
}
static void Draw(u8 id)
{
    s16 *d=gTasks[id].data;
    u8 win=d[0], buf[160];
    FillWindowPixelBuffer(win,PIXEL_FILL(1));
    Print(win,sTitle,2,0);
    StringCopy(gStringVar1,gBagCategoryNames[d[4]]);
    StringExpandPlaceholders(buf,sSale); Print(win,buf,2,14);
    ConvertIntToDecimalStringN(gStringVar1,GetMoney(&gSaveBlock1Ptr->money),STR_CONV_MODE_LEFT_ALIGN,6);
    StringExpandPlaceholders(buf,sMoney); Print(win,buf,130,0);
    Print(win,gBagCategoryNames[d[1]],2,28);
    for (u32 row=0;row<5;row++)
    {
        u32 index=(d[2]/5)*5+row;
        enum Item item=ItemAt(d[1],index);
        if (!item) break;
        if (index==d[2]) Print(win,gText_SelectorArrow2,0,42+row*12);
        CopyItemName(item,gStringVar1); StringExpandPlaceholders(buf,sRow); Print(win,buf,10,42+row*12);
        ConvertIntToDecimalStringN(gStringVar1,LegendsStore_Price(item,d[4]),STR_CONV_MODE_RIGHT_ALIGN,6);
        StringExpandPlaceholders(buf,sPrice); Print(win,buf,175,42+row*12);
    }
    if (!ItemCount(d[1])) Print(win,sEmpty,2,42);
    if (d[3])
    {
        ConvertIntToDecimalStringN(gStringVar1,d[5],STR_CONV_MODE_LEFT_ALIGN,2);
        ConvertIntToDecimalStringN(gStringVar2,LegendsStore_Price(ItemAt(d[1],d[2]),d[4])*d[5],STR_CONV_MODE_LEFT_ALIGN,8);
        StringExpandPlaceholders(buf,sConfirm); Print(win,buf,2,108);
    }
    else if (d[6]) Print(win,d[6]==1?sBought:d[6]==2?sPoor:d[6]==4?sOwned:sFull,2,108);
    else {Print(win,sFooter,2,108); Print(win,sBrowse,2,122);}
    CopyWindowToVram(win,COPYWIN_FULL);
}
static void Task_LegendsStore(u8 id)
{
    s16 *d=gTasks[id].data;
    u32 count=ItemCount(d[1]);
    if (!JOY_NEW(A_BUTTON | B_BUTTON | START_BUTTON | DPAD_ANY | L_BUTTON | R_BUTTON)) return;
    if (JOY_NEW(B_BUTTON | START_BUTTON))
    {
        if (d[3]) {d[3]=0;Draw(id);return;}
        ClearStdWindowAndFrame(d[0],TRUE); RemoveWindow(d[0]); DestroyTask(id);
        Free(sCatalog); sCatalog=NULL;
        ScriptUnfreezeObjectEvents(); UnlockPlayerFieldControls(); return;
    }
    if (d[3])
    {
        if (JOY_NEW(DPAD_LEFT) && d[5]>1) d[5]--;
        if (JOY_NEW(DPAD_RIGHT) && d[5]<99
            && !GetItemImportance(ItemAt(d[1],d[2]))
            && GetItemPocket(ItemAt(d[1],d[2]))!=POCKET_TM_HM) d[5]++;
        if (JOY_NEW(A_BUTTON))
        {
            u32 result=LegendsStore_Buy(ItemAt(d[1],d[2]),d[5],d[4]);
            d[3]=0; d[6]=result==0?1:result==2?2:result==1?4:3;
        }
    }
    else
    {
        d[6]=0;
        if (JOY_NEW(DPAD_LEFT | DPAD_RIGHT))
        {
            do {d[1]=(d[1]+(JOY_NEW(DPAD_LEFT)?BAG_CATEGORIES_COUNT-1:1))%BAG_CATEGORIES_COUNT;}
            while (!LegendsStore_CategoryAllowed(d[1]));
            d[2]=0;
        }
        else if (count && JOY_NEW(DPAD_UP)) d[2]=(d[2]+count-1)%count;
        else if (count && JOY_NEW(DPAD_DOWN)) d[2]=(d[2]+1)%count;
        else if (count && JOY_NEW(L_BUTTON)) d[2]=d[2]>=5?d[2]-5:0;
        else if (count && JOY_NEW(R_BUTTON)) d[2]=(d[2]+5<count?d[2]+5:count-1);
        else if (count && JOY_NEW(A_BUTTON)) {d[3]=1;d[5]=1;}
        else return;
    }
    Draw(id);
}
void LegendsStore_Open(void)
{
    u8 win, id;
    u32 day, category;
    u16 offset=0;
    sCatalog=AllocZeroed(sizeof(*sCatalog));
    if (!sCatalog) {ScriptUnfreezeObjectEvents();UnlockPlayerFieldControls();return;}
    for (category=0;category<BAG_CATEGORIES_COUNT;category++)
    {
        sCatalog->offsets[category]=offset;
        if (!LegendsStore_CategoryAllowed(category)) continue;
        for (u32 item=1;item<ITEMS_COUNT;item++)
            if (LegendsStore_ItemAllowed(item) && GetItemBagCategory(item)==category)
            {
                sCatalog->items[offset++]=item;
                sCatalog->counts[category]++;
            }
    }
    win=AddWindow(&sWindow);
    if (win==WINDOW_NONE) {Free(sCatalog);sCatalog=NULL;ScriptUnfreezeObjectEvents();UnlockPlayerFieldControls();return;}
    RtcCalcLocalTime();day=RtcGetLocalDayCount()%11;
    for (category=0;category<BAG_CATEGORIES_COUNT;category++)
        if (LegendsStore_CategoryAllowed(category) && day--==0) break;
    id=CreateTask(Task_LegendsStore,0);
    gTasks[id].data[0]=win; gTasks[id].data[4]=category;
    DrawStdWindowFrame(win,FALSE);PutWindowTilemap(win);Draw(id);
}
