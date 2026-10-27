"""Regenerate/check collection story spans after an intentional save ABI change.
Changing an ABI/record layout requires a save-version migration for released saves.
"""
from pathlib import Path
from audit_layout import audit, R

def render(x):
    spans=[]
    for block in ['SaveBlock1','SaveBlock2']:
        end=0
        for v in sorted([v for v in x['expanded_omissions'] if v['block']==block],key=lambda v:v['offset']):
            if v['offset']>end:spans.append((1 if block=='SaveBlock1' else 2,end,v['offset']-end))
            end=v['offset']+v['size']
        if end<x['sizes'][block]:spans.append((1 if block=='SaveBlock1' else 2,end,x['sizes'][block]-end))
    s='/* Generated against current save ABI by the compact-PC layout audit. */\n'
    s+='static const u8 sCollectionAbi[32] = {'+','.join(str(v) for v in bytes.fromhex(x['abi_sha256']))+'};\n'
    s+='static const struct CollectionSpan sCollectionSpans[] = {\n'+''.join(' {%d,%d,%d},\n'%v for v in spans)+'};\n'
    s+='#define COLLECTION_STORY_SIZE '+str(x['story_bytes'])+'\n#define COLLECTION_USED '+str(x['slot_used'])+'\n'
    for st in ['SaveBlock1','SaveBlock2','SaveBlock3','PokemonStorage']:s+='STATIC_ASSERT(sizeof(struct %s) == %d, Collection_%s_Size);\n'%(st,x['sizes'][st],st)
    for i,v in enumerate(x['expanded_omissions']):s+='STATIC_ASSERT(offsetof(struct %s, %s) == %d, CollectionField%d);\n'%(v['block'],v['field'],v['offset'],i)
    return s
if __name__=='__main__':
    import sys
    p=R/'src/data/la_collection_save_spans.h';value=render(audit())
    if '--check' in sys.argv:assert p.read_text()==value,'collection save spans/ABI require regeneration and an explicit migration review'
    else:p.write_text(value)
    print('Collection save spans match the current ABI')
