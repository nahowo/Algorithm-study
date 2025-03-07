import bisect

def solution(info, query):
    answer = [0] * len(query)
    n = len(info)
    # 분류 튜플 만들기
    info_type = dict()
    for l in ['cpp', 'java', 'python', '-']:
        for p in ['backend', 'frontend', '-']:
            for e in ['junior', 'senior', '-']:
                for f in ['chicken', 'pizza', '-']:
                    t = ' '.join([l, p, e, f])
                    info_type[t] = []
    
    for i in range(len(info)):
        l, p, e, f, s = info[i].split()

        for l1 in [l, '-']:
            for p1 in [p, '-']:
                for e1 in [e, '-']:
                    for f1 in [f, '-']:
                        t = ' '.join([l1, p1, e1, f1])
                        info_type[t].append(int(s))
    
    for k in info_type.keys():
        info_type[k] = sorted(info_type[k])
    
    # 컬럼별 분류
    for i in range(len(query)):
        l, p, e, f = query[i].split(' and ')
        f, s = f.split()
        s = int(s)
        t = ' '.join([l, p, e, f])
        answer[i] = len(info_type[t]) - bisect.bisect_left(info_type[t], s)
        
    return answer