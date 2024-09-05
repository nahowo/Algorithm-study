def splitQuery(s):
    tmp = s.split()
    q = ''
    score = int(tmp[-1])
    for i in range(0, len(tmp) - 1, 2):
        q += (tmp[i][0])
    
    return q, score

def binarySearch(query, score):
    n = classify[query][1]
    candidate = classify[query][0]
    key = n
    
    top = n - 1
    bot = 0
    while bot <= top:
        mid = (top + bot) // 2
        if candidate[mid] >= score:
            key = mid
            top = mid - 1
        else:
            bot = mid + 1
    
    return n - key

def solution(info, query):
    global classify
    answer = []
    classify = dict()
    
    for l in ['c', 'j', 'p', '-']:
        for p in ['b', 'f', '-']:
            for e in ['j', 's', '-']:
                for f in ['c', 'p', '-']:
                    tmp = l + p + e + f
                    classify[tmp] = [[], 0]
    
    for i in info:
        lang, pos, exp, food, score = i.split()
        for l in [lang, '-']:
            for p in [pos, '-']:
                for e in [exp, '-']:
                    for f in [food, '-']:
                        tmp = l[0] + p[0] + e[0] + f[0]
                        classify[tmp][0].append(int(score))
                        classify[tmp][1] += 1
    
    for i in classify:
        classify[i][0].sort()
        
    for s in query:
        tmpQ, tmpS = splitQuery(s)
        answer.append(binarySearch(tmpQ, tmpS))
    
    return answer