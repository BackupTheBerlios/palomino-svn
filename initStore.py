from atop import store

def makeAPoolAndStuff():
    p = store.Pool(st)
    p.addIndex(TitleIndex)
    p.addIndex(CategoryIndex)
    t = []
    t.append(LoText(st, 'test1', ['foo','bar']))
    t.append(LoText(st, 'test2', ['foo','baz']))
    t.append(LoText(st, 'test3', ['foo','bar']))
    t.append(LoText(st, 'test4', ['foo','bok']))
    t.append(LoText(st, 'test5', ['fro','bar']))
    t.append(LoText(st, 'test6', ['foo','bat']))
    [p.addItem(o) for o in t]
    print "By Title"
    for o in p.queryIndex(TitleIndex):
        print o.title
    print "By category 'bar'"
    for o in [o for o in p.queryIndex(CategoryIndex) if 'bar' in o.categories]:
        print o.title
    print "get ids"
    for o in [o for o in p.queryIndex(CategoryIndex, result=store.STORE_ID)]:
        print o


