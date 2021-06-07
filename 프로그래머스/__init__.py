import copy
def testDef():
    llist = [1,2,3,4,5]
    tlist = copy.deepcopy(llist)
    clist = tlist.copy()

    print(tlist)
    print(clist)

    del clist[0]
    print(tlist)
    print(clist)
    return

print(testDef())