/* NPC roles only: no player-avatar IDs and no donor gameplay. */
static const struct ObjectEventGraphicsInfo *GetLaNpcRosterGraphics(u16 graphicsId)
{
    switch (graphicsId)
    {
    case OBJ_EVENT_GFX_RED: return &gObjectEventGraphicsInfo_LaRosterRed;
    case OBJ_EVENT_GFX_HNS_RED_NORMAL_HNS: return &gObjectEventGraphicsInfo_LaRosterRed;
    case OBJ_EVENT_GFX_BLUE: return &gObjectEventGraphicsInfo_LaRosterBlue;
    case OBJ_EVENT_GFX_HNS_BLUE_HNS: return &gObjectEventGraphicsInfo_LaRosterBlue;
    case OBJ_EVENT_GFX_RIVAL_BRENDAN_NORMAL: return &gObjectEventGraphicsInfo_LaRosterBrendan;
    case OBJ_EVENT_GFX_RIVAL_MAY_NORMAL: return &gObjectEventGraphicsInfo_LaRosterMay;
    case OBJ_EVENT_GFX_PROF_BIRCH: return &gObjectEventGraphicsInfo_LaRosterBirch;
    case OBJ_EVENT_GFX_HNS_SILVER_HNS: return &gObjectEventGraphicsInfo_LaRosterSilver;
    case OBJ_EVENT_GFX_WALLY: return &gObjectEventGraphicsInfo_LaRosterWally;
    case OBJ_EVENT_GFX_HNS_KRIS_NORMAL_HNS: return &gObjectEventGraphicsInfo_LaRosterKris;
    case OBJ_EVENT_GFX_ARCHIE: return &gObjectEventGraphicsInfo_LaRosterArchie;
    case OBJ_EVENT_GFX_MAXIE: return &gObjectEventGraphicsInfo_LaRosterMaxie;
    case OBJ_EVENT_GFX_HNS_GOLD_NORMAL_HNS: return &gObjectEventGraphicsInfo_LaRosterEthan;
    case OBJ_EVENT_GFX_PROF_OAK: return &gObjectEventGraphicsInfo_LaRosterOak;
    case OBJ_EVENT_GFX_HNS_PROF_OAK_HNS: return &gObjectEventGraphicsInfo_LaRosterOak;
    default: return NULL;
    }
}
