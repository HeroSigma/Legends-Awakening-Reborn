from probe import *
assert lib.boot(str(R/'pokeemerald.gba').encode());state('hns_shop_menu',True)
def tap(key=1,n=60):frames(1,key);frames(n)
def money():return rd(rd(symbols['gSaveBlock1Ptr'])+0x490)^rd(rd(symbols['gSaveBlock2Ptr'])+0xac)
tap();tap();before=money();assert before==3000
for i in range(12):tap()
after=money();assert after==before-200,(before,after);shot('hns_shop_purchase_pass')
tap(2,240);tap(2,240);shot('hns_shop_cancel_confirm');tap(1,120);p=pos();frames(24,128);frames(20);assert pos()!=p;shot('hns_shop_cancel_pass')
rows=[dict(test='native_shop_purchase',passed=True,details=dict(before_money=before,after_money=after,cost=200,item='Poke Ball')),dict(test='native_shop_cancel',passed=True,details=dict(before_position=p,after_position=pos(),control_returned=True))]
(HERE/'hns_shop_results.json').write_text(json.dumps(rows,indent=2)+chr(10));print('PASS native shop purchase and cancel',before,after)
