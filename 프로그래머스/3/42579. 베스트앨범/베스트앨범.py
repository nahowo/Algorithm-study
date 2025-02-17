def solution(genres, plays):
    n = len(genres)
    g = dict()
    gpp = dict()
    for i in range(n):
        gpp[genres[i]] = gpp.get(genres[i], 0) + plays[i]
    for i in range(n):
        if genres[i] not in g:
            g[genres[i]] = [[-gpp[genres[i]], -plays[i], i]]
        else:
            g[genres[i]].append([-gpp[genres[i]], -plays[i], i])
    
    order = []
    for k, v in g.items():
        tmp = sorted(v)
        for i in range(min(2, len(tmp))):
            order.append(tmp[i])
    order.sort()
    answer = []
    for i in order:
        answer.append(i[2])
    return answer