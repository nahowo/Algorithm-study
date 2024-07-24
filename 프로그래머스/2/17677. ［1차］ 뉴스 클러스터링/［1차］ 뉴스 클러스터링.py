def makeSet(s):
    result = dict()
    for i in range(len(s) - 1):
        tmp = s[i : i + 2]
        if verifyStr(tmp) == True:
            tmp = tmp.upper()
            result[tmp] = result.get(tmp, 0) + 1
    return result

def verifyStr(s):
    for i in s:
        if not i.isalpha():
            return False
    return True

def intersection(s1, s2):
    result = []
    for element, cnt in s1.items():
        for _ in range(cnt):
            if element in s2:
                result.append(element)
                s2[element] -= 1
                if s2[element] == 0:
                    del s2[element]
    return result

def union(s1, s2):
    result = []
    for element, cnt in s1.items():
        for _ in range(cnt):
            if element in s2:
                result.append(element)
                s2[element] -= 1
                if s2[element] == 0:
                    del s2[element]
            else:
                result.append(element)
    
    for element, cnt in s2.items():
        for _ in range(cnt):
            result.append(element)
    return result

def solution(str1, str2):
    s1 = makeSet(str1)
    s2 = makeSet(str2)
    if len(s1) == 0 and len(s2) == 0:
        return 65536
    
    its = intersection(s1.copy(), s2.copy())
    unn = union(s1.copy(), s2.copy())    
    
    jaccard = int(len(its) / len(unn) * 65536)
    
    return jaccard