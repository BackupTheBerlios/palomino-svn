from atop import store
from learningObjects import *

sillyString = [\
        "this is a silly string about bananas!",
        "heydi ho, away we go, over the rainbow bridge.",
        "egg yokes, nice!",
        "elephants, elephants, balanced on a string.",
        "Theres a TROLL UNDER THAT BRIDGE!!?",
        "Snow, Snow, go away.",
        "Ladders have rungs and strings, yes, what stupid terms.",
        "Mog is a Moogle, did'nt you realise? Kupo!",
        "HUGE SHARP POINTY TEETH!",
        "Just keep swimming, Just keep swimming.",
        ]

def findKeywordMatches(pool, keyword):
    for k in pool.queryIndex(KeywordIndex, result=store.INDEX_AND_ITEM):
        print k


def makeAPoolAndStuff():
    p = store.Pool(st)
    # add indexes to the pool
    [p.addIndex(i) for i in LoIndexes]
    
    for s in sillyString:
        o = LoText(st, ['sillyStrings'])
        o.setText(s)
        p.addItem(o)
    
    findKeywordMatches(p,'foo')
    
st = store.Store('data/db', 'data/files')
st.transact(makeAPoolAndStuff)
st.close()
