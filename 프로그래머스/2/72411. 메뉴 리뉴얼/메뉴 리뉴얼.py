from itertools import combinations

def solution(orders, course):
    setDict = dict()
    setMenu = []
    for i in orders:
        tmpOrder = list(i)
        for j in course:
            tmpArr = list(combinations(tmpOrder, j))
            for t in tmpArr:
                t = sorted(list(t))
                tmp = ''.join(t)
                if tmp in setDict:
                    setDict[tmp] += 1
                else:
                    setDict[tmp] = 1
    
    maxSet = {i:0 for i in course}
    for k, v in setDict.items():
        t = len(k)
        maxSet[t] = max(maxSet[t], v)

    for k, v in setDict.items():
        if v == maxSet[len(k)] and v >= 2:
            setMenu.append(k)
    setMenu.sort()
            
    return setMenu