/* Map-scoped inspected vertical routes; preserve source cell attributes. */
extern const u8 HyperSinnoh_VerticalClimb_0_NORTH[];
extern const u8 HyperSinnoh_VerticalClimb_0_SOUTH[];
extern const u8 HyperSinnoh_VerticalClimb_1_NORTH[];
extern const u8 HyperSinnoh_VerticalClimb_1_SOUTH[];
extern const u8 HyperSinnoh_VerticalClimb_2_NORTH[];
extern const u8 HyperSinnoh_VerticalClimb_2_SOUTH[];
extern const u8 HyperSinnoh_VerticalClimb_3_NORTH[];
extern const u8 HyperSinnoh_VerticalClimb_3_SOUTH[];
extern const u8 HyperSinnoh_VerticalClimb_4_NORTH[];
extern const u8 HyperSinnoh_VerticalClimb_4_SOUTH[];
extern const u8 HyperSinnoh_VerticalClimb_5_NORTH[];
extern const u8 HyperSinnoh_VerticalClimb_5_SOUTH[];
extern const u8 HyperSinnoh_VerticalClimb_6_NORTH[];
extern const u8 HyperSinnoh_VerticalClimb_6_SOUTH[];
extern const u8 HyperSinnoh_VerticalClimb_7_NORTH[];
extern const u8 HyperSinnoh_VerticalClimb_7_SOUTH[];
extern const u8 HyperSinnoh_VerticalClimb_8_NORTH[];
extern const u8 HyperSinnoh_VerticalClimb_8_SOUTH[];
extern const u8 HyperSinnoh_VerticalClimb_9_NORTH[];
extern const u8 HyperSinnoh_VerticalClimb_9_SOUTH[];
extern const u8 HyperSinnoh_VerticalClimb_10_NORTH[];
extern const u8 HyperSinnoh_VerticalClimb_10_SOUTH[];
extern const u8 HyperSinnoh_VerticalClimb_11_NORTH[];
extern const u8 HyperSinnoh_VerticalClimb_11_SOUTH[];
static const struct { u16 map; s16 x,y; u8 direction; const u8 *script; } sVerticalClimbRoutes[] = {
 {MAP_HYPERSINNOH_36_13_SUNYSHORE_CITY, 58, 37, DIR_NORTH, HyperSinnoh_VerticalClimb_0_NORTH},
 {MAP_HYPERSINNOH_36_13_SUNYSHORE_CITY, 58, 33, DIR_SOUTH, HyperSinnoh_VerticalClimb_0_SOUTH},
 {MAP_HYPERSINNOH_36_24_ROUTE_208, 15, 14, DIR_NORTH, HyperSinnoh_VerticalClimb_1_NORTH},
 {MAP_HYPERSINNOH_36_24_ROUTE_208, 15, 10, DIR_SOUTH, HyperSinnoh_VerticalClimb_1_SOUTH},
 {MAP_HYPERSINNOH_36_27_ROUTE_210, 19, 14, DIR_NORTH, HyperSinnoh_VerticalClimb_2_NORTH},
 {MAP_HYPERSINNOH_36_27_ROUTE_210, 19, 12, DIR_SOUTH, HyperSinnoh_VerticalClimb_2_SOUTH},
 {MAP_HYPERSINNOH_36_27_ROUTE_210, 19, 16, DIR_NORTH, HyperSinnoh_VerticalClimb_3_NORTH},
 {MAP_HYPERSINNOH_36_27_ROUTE_210, 19, 14, DIR_SOUTH, HyperSinnoh_VerticalClimb_3_SOUTH},
 {MAP_HYPERSINNOH_36_32_ROUTE_213, 11, 35, DIR_NORTH, HyperSinnoh_VerticalClimb_4_NORTH},
 {MAP_HYPERSINNOH_36_32_ROUTE_213, 11, 29, DIR_SOUTH, HyperSinnoh_VerticalClimb_4_SOUTH},
 {MAP_HYPERSINNOH_36_32_ROUTE_213, 38, 5, DIR_NORTH, HyperSinnoh_VerticalClimb_5_NORTH},
 {MAP_HYPERSINNOH_36_32_ROUTE_213, 38, 2, DIR_SOUTH, HyperSinnoh_VerticalClimb_5_SOUTH},
 {MAP_HYPERSINNOH_36_32_ROUTE_213, 39, 12, DIR_NORTH, HyperSinnoh_VerticalClimb_6_NORTH},
 {MAP_HYPERSINNOH_36_32_ROUTE_213, 39, 9, DIR_SOUTH, HyperSinnoh_VerticalClimb_6_SOUTH},
 {MAP_HYPERSINNOH_36_32_ROUTE_213, 44, 4, DIR_NORTH, HyperSinnoh_VerticalClimb_7_NORTH},
 {MAP_HYPERSINNOH_36_32_ROUTE_213, 44, 2, DIR_SOUTH, HyperSinnoh_VerticalClimb_7_SOUTH},
 {MAP_HYPERSINNOH_36_32_ROUTE_213, 45, 9, DIR_NORTH, HyperSinnoh_VerticalClimb_8_NORTH},
 {MAP_HYPERSINNOH_36_32_ROUTE_213, 45, 6, DIR_SOUTH, HyperSinnoh_VerticalClimb_8_SOUTH},
 {MAP_HYPERSINNOH_36_48_ACUITY_LAKEFRONT, 19, 39, DIR_NORTH, HyperSinnoh_VerticalClimb_9_NORTH},
 {MAP_HYPERSINNOH_36_48_ACUITY_LAKEFRONT, 19, 34, DIR_SOUTH, HyperSinnoh_VerticalClimb_9_SOUTH},
 {MAP_HYPERSINNOH_36_91_MT_CORONET, 40, 14, DIR_NORTH, HyperSinnoh_VerticalClimb_10_NORTH},
 {MAP_HYPERSINNOH_36_91_MT_CORONET, 40, 10, DIR_SOUTH, HyperSinnoh_VerticalClimb_10_SOUTH},
 {MAP_HYPERSINNOH_36_9_VEILSTONE_CITY, 14, 41, DIR_NORTH, HyperSinnoh_VerticalClimb_11_NORTH},
 {MAP_HYPERSINNOH_36_9_VEILSTONE_CITY, 14, 38, DIR_SOUTH, HyperSinnoh_VerticalClimb_11_SOUTH},
};
static const u8 *HyperSinnoh_GetVerticalClimbInteraction(s16 x, s16 y, u8 direction)
{
 u32 i;
 for (i=0;i<ARRAY_COUNT(sVerticalClimbRoutes);i++)
  if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(sVerticalClimbRoutes[i].map) && gSaveBlock1Ptr->location.mapNum == MAP_NUM(sVerticalClimbRoutes[i].map) && x == sVerticalClimbRoutes[i].x + MAP_OFFSET && y == sVerticalClimbRoutes[i].y + MAP_OFFSET && direction == sVerticalClimbRoutes[i].direction)
   return sVerticalClimbRoutes[i].script;
 return NULL;
}
