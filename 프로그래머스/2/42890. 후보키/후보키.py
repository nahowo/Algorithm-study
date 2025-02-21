from itertools import combinations

def check(idx, relation):
    tpl = [[] for _ in range(n)]
    for i in range(n):
        for j in idx:
            tpl[i].append(relation[i][j])
    checkSet = set()
    for i in range(n):
        tmp = tuple(tpl[i])
        if tmp in checkSet:
            return False
        else:
            checkSet.add(tmp)
    return True

def solution(relation):
    global n
    answer = 0
    n = len(relation)
    m = len(relation[0])
    nCand = set(i for i in range(m))
    cand = []
    
    for i in range(m):
        if check([i], relation):
            nCand.remove(i)
            answer += 1
    
    for i in range(2, len(nCand) + 1):
        comb = combinations(nCand, i)
        for c in comb:
            if check(c, relation):
                cand.append(set(c))

    cand.sort(key = lambda x: len(x), reverse = True)
    for i in range(len(cand)):
        flag = True
        for j in range(i + 1, len(cand)):
            if cand[j].issubset(cand[i]):
                flag = False
                print(cand[i], cand[j])
                break
        if flag:
            answer += 1
    return answer