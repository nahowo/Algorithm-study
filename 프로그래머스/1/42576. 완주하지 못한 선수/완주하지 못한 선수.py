def solution(participant, completion):
    answer = ''
    num=dict()
    for p in participant:
        num[p]=num.get(p,0)+1
    for c in completion:
        num[c]-=1
        if num[c]==0:
            del num[c]
    return list(num.keys()).pop()