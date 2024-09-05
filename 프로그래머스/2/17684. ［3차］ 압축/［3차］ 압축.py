def solution(msg):
    answer = []
    d = dict()
    
    idx = 1
    for i in range(65, 91):
        d[chr(i)] = idx
        idx += 1
    
    l = len(msg)
    while l:
        for i in range(len(msg), 0, -1):
            w = msg[:i]
            if w in d:
                answer.append(d[w])
                break
        if i < l:
            d[msg[:i + 1]] = idx
            idx += 1
        msg = msg[i:]
        l -= i
        
    return answer