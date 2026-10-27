Unova_Nuvema_FullSheetTest_MapScripts::
	.byte 0

NuvemaTest_EnterLab::
	warp MAP_UNOVA_NUVEMA_TEST_LAB, 255, 3, 11
	waitstate
	end

NuvemaTest_EnterCenterHouse::
	warp MAP_UNOVA_NUVEMA_TEST_CENTERHOUSE, 255, 3, 4
	waitstate
	end

NuvemaTest_EnterWestHouse::
	warp MAP_UNOVA_NUVEMA_TEST_WESTHOUSE, 255, 4, 8
	waitstate
	end

NuvemaTest_EnterEastHouse::
	warp MAP_UNOVA_NUVEMA_TEST_EASTHOUSE, 255, 10, 4
	waitstate
	end
